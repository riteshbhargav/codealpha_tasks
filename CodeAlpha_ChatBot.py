def get_response(user_input):
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"

    elif "internship" in user_input:
        return "We offer internships in Python, AI, Web Development, and Data Science."

    elif "duration" in user_input or "time period" in user_input:
        return "The internship duration is usually 1 month."

    elif "certificate" in user_input:
        return "Yes, a certificate is provided after successful task completion."

    elif "contact" in user_input or "website" in user_input:
        return "You can visit our official website for more details."

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day 👋"

    else:
        return "Sorry, I didn't understand that. Please try again."


def chatbot():
    print("🤖 Basic Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        user = input("You: ").lower()

        response = get_response(user)
        print("Bot:", response)

        if user in ["bye", "goodbye", "exit"]:
            break


# Run the chatbot
chatbot()
