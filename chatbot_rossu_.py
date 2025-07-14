import nltk
from nltk.chat.util import Chat, reflections

# Optional: Set the nltk data path if needed
nltk.data.path.append('D:/nltk_data')  # <-- change if your folder is elsewhere

# --- Smarter Pairs ---
pairs = [
    [r"(hi|hello|hey)", ["Hi there! How can I help you today? 😊"]],
    [r"my name is (.*)", ["Hello %1, nice to meet you!"]],
    [r"who created you", ["I was created by Rossu 💫 as part of an AI project."]],
    [r"what is your name", ["My name is RossuBot 💖"]],
    [r"what can you do", ["I can answer simple questions and help with basic tasks!"]],
    [r"what is the time", ["I don’t have a watch, but you can check your device clock ⏰."]],
    [r"what is the date", ["I don’t have a calendar, but your system has today’s date 📅."]],
    [r"what is python", ["Python is a powerful programming language used for AI, web, and more!"]],
    [r"what is your favourite language", ["Of course, Python! 🐍"]],
    [r"(bye|exit|quit)", ["Goodbye Rossu! 👋 Take care 💖"]],
    [r"what is AI",["AI stands for Artificial Intelligence.It enables to think and learn"]],
    [r"what is python", ["Python is a powerful programming language used for AI, web, data, and more! 🐍"]],
    [r"who created python", ["Python was created by Guido van Rossum in the late 1980s. 🧠"]],
    [r"what is a variable", ["A variable is used to store information that can be reused and changed."]],
    [r"what is a list", ["A list is a collection of items in a particular order in Python, like [1, 2, 3]. 📋"]],
    [r"what is a function", ["A function is a block of code which performs a specific task."]],
    [r"what is (a)? loop", ["A loop lets you repeat actions — like using 'for' or 'while' loops. 🔁"]],
    [r"what is an if statement", ["An 'if' statement runs code only if a condition is true."]],
    [r"what is print", ["'print()' is a function that displays text or results on the screen. 🖨"]],
    [r"what is input", ["'input()' lets the user enter data from the keyboard."]],
    [r"what is int", ["'int' is a data type used for whole numbers in Python."]],
    [r"what is str", ["'str' means a string — a sequence of characters, like text."]],
    [r"what is float", ["'float' is a number with a decimal point, like 3.14."]],
    [r"how to install python", ["Go to python.org and download Python from there. 🔽"]],
    [r"what is pip", ["'pip' is a tool to install Python packages like numpy, pandas, etc. 📦"]],
    [r"what is a module", ["A module is a file with Python code that you can import into your programs."]],
    [r"what is import", ["'import' brings external code (modules/libraries) into your script."]],
    [r"what is a dictionary", ["A dictionary stores data in key-value pairs, like {'name': 'Rossu'}."]],
    [r"what is class", ["A class is a blueprint for creating objects in object-oriented programming."]],
    [r"what is exception", ["An exception is an error that can be caught and handled."]],
    [r"what is try except", ["Used to catch and handle errors gracefully in Python."]],
    [r"what is machine learning", ["Machine learning is a way computers learn from data without being explicitly programmed."]],
    [r"tell me a joke", ["Why did the developer go broke? Because he used up all his cache! 😂"]],
    [r"what is your hobby", ["I love chatting with you and learning new things! 😄"]],
    [r"are you real", ["I exist in code, but I'm real in spirit! 💻✨"]],
    [r"thank you", ["You're welcome! 🫶"]],
    [r"(.*)", ["Sorry, I didn’t understand that. Can you try saying it differently? 🤔"]],
]
# --- Start Chatbot ---
print("🤖 Hello! I’m RossuBot – your AI assistant. Type 'exit' to quit.")
chat = Chat(pairs, reflections)

while True:
    user_input = input("You: ").lower().strip()
    if user_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye Rossu! 👋")
        break
    response = chat.respond(user_input)
    print("Bot:", response)