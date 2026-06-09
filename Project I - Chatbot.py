print("=" * 50)
print("        PROJECT I - AI CHATBOT")
print("=" * 50)
print("Hello! I am Oreo, a Rule-Based AI Chatbot. I am here to assist you with simple conversations. You can ask me about my name, how I'm doing, or just say hi! I will do my best to respond appropriately. Let's chat!\n")
print("Here are some commands you can try:")
print("- 'hello', 'hi', 'hey' to greet me.")
print("- 'how are you' to ask about my well-being.")
print("- 'what is your name' to know my name.")
print("- 'who created you' to know my creator.")
print("- 'good morning' or 'good evening' for greetings.")
print("- 'thanks' or 'thank you' to express gratitude.")
print("- 'help' to see this list again.")
print("or\n")
print("Type 'bye' to exit.\n")

responses = {
    "hello": "Hello! Nice to meet you.",
    "hi": "Hi there!",
    "hey": "Hey! How can I help you?",
    "how are you": "I am doing great. Thanks for asking!",
    "what is your name": "I am Oreo, a Rule-Based AI Chatbot.",
    "who created you": "I was created by Hiral Goyal. She is a DecodeLabs AI Intern.",
    "what can you do?": "I can have simple conversations with you. Try asking me about my name, how I'm doing, or just say hi!",
    "good morning": "Good Morning! Have a wonderful day.",
    "good evening": "Good Evening!",
    "good afternoon": "Good Afternoon!",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "help": "Try saying hello, asking my name, or typing bye.",
    "bye": "Goodbye! Have a nice day."
}

while True:

    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Oreo:", responses["bye"])
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that command."
    )

    print("Oreo:", reply)

print("\nChatbot closed successfully.")