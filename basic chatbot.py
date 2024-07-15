import nltk
from nltk.chat.util import Chat, reflections

# Define some pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good.\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am (.*) good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon.", "It was nice talking to you. Bye.",]
    ],
]

def chatbot():
    print("Hi! I am a chatbot created by you. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
