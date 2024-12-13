import nltk

# Download the punkt tokenizer
nltk.download('punkt')


import nltk
from nltk.chat.util import Chat, reflections

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')

# Define pairs of patterns and responses for the chatbot
faq_pairs = [
    (r"Hi|Hello", ["Hello! How can I assist you with your fitness questions?"]),
    (r"(.*) exercise (.*)", ["Exercise is essential for staying healthy. What kind of exercise are you looking for?"]),
    (r"(.*) weight (.*)", ["A combination of exercise and a balanced diet can help you lose weight."]),
    (r"(.*) diet (.*)", ["A healthy diet with plenty of vegetables and lean proteins is key to fitness."]),
    (r"(.*) muscle (.*)", ["Strength training is the best way to build muscle."]),
    (r"How can I lose weight?", ["A good combination of exercise and a balanced diet can help you lose weight."]),
    (r"How often should I exercise?", ["It is recommended to exercise at least 3-5 times a week for a healthy lifestyle."]),
    (r"(.*) cardio (.*)", ["Cardiovascular exercise, like running or cycling, is great for heart health and burning fat."]),
    (r"(.*) strength training (.*)", ["Strength training helps build muscle mass and increases metabolism."]),
    (r"(.*) protein (.*)", ["Protein is essential for muscle repair and growth. Ensure you get enough in your diet."]),
    (r"quit", ["Goodbye! Stay fit and healthy."]),
]

# Initialize the chatbot using NLTK's Chat utility
fitness_chatbot = Chat(faq_pairs, reflections)

# Function to interact with the chatbot
def fitness_chat():
    print("Fitness FAQ Chatbot (type 'quit' to exit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot: Goodbye! Stay fit and healthy.")
            break
        response = fitness_chatbot.respond(user_input)
        print(f"Bot: {response}")

# Run the chatbot
if __name__ == "__main__":
    fitness_chat()

