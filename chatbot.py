# Simple AI Chatbot
print("🤖 AI Chatbot (Simulated)")

responses = {
    "hello": "Hi there! How can I help?",
    "what is rag": "RAG = Retrieval Augmented Generation",
    "bye": "Goodbye! Have a great day!"
}

while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        break
    response = responses.get(user_input, "I'm learning! Ask about hello, rag, or bye")
    print(f"Bot: {response}")
