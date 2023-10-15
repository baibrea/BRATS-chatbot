from flask import Flask, render_template, request, jsonify
from echo import explain
import random

# Runs flask
app = Flask(__name__)

# List that acts like a dynamic array
# stores past user inputs
past_inputs = []




# Presets for user inputs and user outputs

# "Hello" user inputs / ChatiGator outputs
hello_input = ["hello", "good day", "greetings", "salutations", "hi there", "hello there", "hi chatigator", "hey chatigator"]
hello_output = ["Hi!", "Hello :D", "Hi, nice to meet you :)"]

# "Help" user inputs / ChatiGator outputs
help_input = ["help", "help me", "i need help", "i want help"]
help_output = ["Please type in a topic you would like to learn more about!"]

# "Thanks" user inputs / ChatiGator outputs
thanks_input = ["thank you", "thanks", "thank"]
thanks_output = ["No problem!", "Happy to help!", "Of course!"]

# "How are you" user inputs / ChatiGator outputs
howareyou_input = ["how are you", "whats up", "what's up", "what is up",
                   "how's it going", "how is it going", "how are you doing"]
howareyou_output = ["I'm doing well, thank you. Is there anything I can help you with?",
                    "I'm doing great today. What do you need help with?",
                    "Today has been wonderful so far. How may I help you?"]

# "Self name" user inputs / ChatiGator outputs
selfname_input = ["what is your name", "what are you called", "what are you", "what is this", "who are you",
                  "whomst are you", "what's your name", "whats your name"]
selfname_output = ["My name is ChatiGator. I am an AI chat assistant.",
                   "I am ChatiGator, an AI assistant meant to help you with any questions about Verizon you may have."]

# "Goodbye" user inputs / ChatiGator outputs
goodbye_input = ["goodbye", "cya", "see ya", "nice talking to ya", "nice talking to you", "bye", "deuces",
                 "talk to ya later", "talk to you later", "speak with you later", "speak with ya later"]
goodbye_output = ["Bye! It was nice chatting with you :)",
                  "See you later! Please return with any other questions you have!"]

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # check if text is valid
    if (any(hello_input in text.lower() for hello_input in hello_input)) or text.lower() == "hi" or text.lower() == "hey":
        response = random.choice(hello_output)
    elif any(help_input in text.lower() for help_input in help_input):
        response = random.choice(help_output)
    elif any(thanks_input in text.lower() for thanks_input in thanks_input):
        response = random.choice(thanks_output)
    elif any(howareyou_input in text.lower() for howareyou_input in howareyou_input):
        response = random.choice(howareyou_output)
    elif any(selfname_input in text.lower() for selfname_input in selfname_input):
        response = random.choice(selfname_output)
    elif any(goodbye_input in text.lower() for goodbye_input in goodbye_input):
        response = random.choice(goodbye_output)
    else:
        response = explain(target=text)
    past_inputs.append(response)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)