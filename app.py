from flask import Flask, request, redirect

app = Flask(__name__)

shops = {}

def process_faq(text):
    text = text.replace("?", ".").replace("!", ".")
    return [s.strip() for s in text.split(".") if s.strip()]

def answer_question(shop_id, question):
    faq = shops.get(shop_id, [])
    q_words = question.lower().split()

    best_score = 0
    best_answer = ""

    for sentence in faq:
        score = 0
        s_words = sentence.lower().split()
        for w in q_words:
            if w in s_words:
                score += 1
        if score > best_score:
            best_score = score
            best_answer = sentence

    if best_score == 0:
        return "I don't have that information."
    return best_answer

@app.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        faq_text = request.form["faq"]
        shop_id = str(len(shops) + 1)
        shops[shop_id] = process_faq(faq_text)
        return redirect(f"/chat/{shop_id}")

    return """
    <html>
    <head><title>No-Wait Support Bot</title></head>
    <body>
        <h1>No-Wait Customer Support Bot</h1>
        <h3>Create Shop FAQ Bot</h3>
        <form method="post">
            <textarea name="faq" rows="10" cols="70"
            placeholder="Paste shop FAQ here"></textarea><br><br>
            <button type="submit">Generate Chat Link</button>
        </form>
    </body>
    </html>
    """

@app.route("/chat/<shop_id>", methods=["GET", "POST"])
def chat(shop_id):
    if shop_id not in shops:
        return "Invalid shop link"

    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = answer_question(shop_id, question)

    return f"""
    <html>
    <head><title>Shop Chat</title></head>
    <body>
        <h2>Shop Support Chat</h2>
        <form method="post">
            <input type="text" name="question" size="60"
            placeholder="Ask a question" required>
            <button type="submit">Ask</button>
        </form>
        <p><strong>{answer}</strong></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
