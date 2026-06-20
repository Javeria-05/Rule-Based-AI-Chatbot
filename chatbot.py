responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I am fine.",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "bye": "Goodbye!",
    "thanks": "You're welcome!",
    "good morning": "Good Morning!",
    "good evening": "Good Evening!",
    "help": "I can answer simple questions.",
    "python": "Python is a programming language.",
    "ai": "AI stands for Artificial Intelligence.",
    "who made you": "I was created by Javeria.",
    "what can you do": "I can answer predefined questions.",
    "welcome": "Thank you!",
    "good night": "Good Night!",
    "computer": "A computer is an electronic device.",
    "coding": "Coding is the process of writing programs.",
    "programming": "Programming is creating software.",
    "student": "Students learn new skills every day.",
    "university": "A university provides higher education."
}

print("=" * 50)
print("🤖 RULE-BASED AI CHATBOT")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        print("Chatbot: Goodbye! Have a nice day!")
        break

    reply = responses.get(
        clean_input,
        "Sorry, I do not understand. Please try another question."
    )

    print("Chatbot:", reply)