# shop-costumer-support
it is what it is....bishnoi gang for the win


# No-Wait Customer Support Bot

A simple, multi-shop customer support chatbot for local businesses.  
Shop owners paste their FAQ once and instantly get a **shareable chat link** that answers customer questions with zero wait.

---

## Problem

Small local shops (barbers, cafés, salons, hardware stores) repeatedly answer the same questions every day:
- Opening hours
- Pricing
- Parking
- Shop policies

This wastes staff time and creates unnecessary wait for customers.

---

## Solution

This project provides a lightweight web application where:
1. A shop owner pastes their FAQ text.
2. The system generates a **shop-specific chat link**.
3. Customers use that link to ask questions.
4. The chatbot answers **only from that shop’s FAQ**.
5. If the answer is not present, it safely responds:
   > “I don’t have that information.”

Each shop’s data is isolated to prevent cross-shop answers.

---

## How It Works

- One platform supports **multiple shops**
- Each shop has its own FAQ-based knowledge store
- User questions are matched against that shop’s data only
- The most relevant FAQ entry is returned
- No hallucinations or external data usage

This follows a **RAG-lite architecture**:
- FAQ ingestion
- Data chunking (sentences)
- Retrieval based on relevance
- Context-limited answers

---

## Tech Stack

- **Language:** Python  
- **Backend:** Flask  
- **Frontend:** Server-rendered HTML  
- **Storage:** In-memory (demo-focused)


