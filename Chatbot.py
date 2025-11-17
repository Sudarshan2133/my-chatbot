# chatbot.py

import random
import warnings
import nltk
import requests

from config import API_URL     # Ensure file name is config.py (NOT Config.py)
from config import API_KEY
from config import MODEL

warnings.filterwarnings("ignore")

# Download NLTK data silently
nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)

# ----------------------------
# Load chatbot corpus
# ----------------------------
def load_corpus(file_path="chatbot_corpus.txt"):
    """Load chatbot knowledge from text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return """Artificial Intelligence is the simulation of human intelligence in machines.
        Machine learning is a subset of AI that learns from data.
        Chatbots are AI applications that can converse with humans.
        Python is a popular language for building AI systems.
        """

chatbot_corpus = load_corpus()
sent_tokens = nltk.sent_tokenize(chatbot_corpus)

# ----------------------------
# Greetings
# ----------------------------
GREETING_INPUTS = ("hello", "hi", "hey", "greetings", "sup", "yo")
GREETING_RESPONSES = [
    "Hello there!",
    "Hey! How are you today?",
    "Hi! Great to see you!",
    "Greetings! 😊"
]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

# ----------------------------
# Custom replies
# ----------------------------
def custom_reply(user_input):
    user_input = user_input.lower()

    if "your name" in user_input:
        return "I'm PyBot 🤖 — your friendly AI assistant!"

    elif "help" in user_input:
        return "Sure! You can ask me about AI, ML, Python, or chatbots."

    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to therapy? Because it had a hard drive 😂",
            "I told my AI friend a joke... now it keeps repeating it in loops! 🤖",
            "I'm reading a book on anti-gravity — it's impossible to put down!"
        ]
        return random.choice(jokes)

    elif "thank" in user_input:
        return "You're most welcome! 😊"

    elif "bye" in user_input:
        return "Goodbye! Take care and keep learning 🚀"

    return None

# ----------------------------
# OpenRouter API function
# ----------------------------
def response(user_response, context):
    """Get LLM response from OpenRouter API"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",         # REQUIRED
        "HTTP-Referer": "http://localhost",            # REQUIRED
        "X-Title": "PyBot-Chatbot"                     # Any custom title
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are PyBot, a friendly and helpful AI assistant."},
            {"role": "user", "content": f"Context: {context}\nUser: {user_response}"}
        ]
    }

    try:
        api_response = requests.post(API_URL, headers=headers, json=payload)
        api_response.raise_for_status()
        data = api_response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"

# ----------------------------
# Chatbot loop
# ----------------------------
def chatbot():
    print("BOT: Hello! I’m PyBot 🤖. Type 'bye' to exit.\n")

    conversation_history = []

    while True:
        user_response = input("You: ").strip()
        if not user_response:
            continue

        if user_response.lower() in ["bye", "exit", "quit"]:
            print("BOT: Goodbye! Take care 😊")
            break

        conversation_history.append(user_response)
        if len(conversation_history) > 5:
            conversation_history.pop(0)

        greet = greeting(user_response)
        if greet:
            print("BOT:", greet)
            continue

        custom = custom_reply(user_response)
        if custom:
            print("BOT:", custom)
            if "bye" in user_response.lower():
                break
            continue

        context = " ".join(conversation_history)
        bot_reply = response(user_response, context)
        print("BOT:", bot_reply)

if __name__ == "__main__":
    chatbot()
