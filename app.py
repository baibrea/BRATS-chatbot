from flask import Flask, render_template, request, jsonify
from echo import explain
import random

app = Flask(__name__)

past_inputs = []

hello_input = ["hello", "good day","greetings","salutations","hi there","hello there"]
hello_output = ["Hi hi!", "Hello :D", "Hi, nice to meet you :)"]

help_input=["help","help me","i need help","i want help"]
help_output=["Please type in a topic you would like to learn more about"]

thanks_input=["thank you","thanks"]
thanks_output=["No problem!","Happy to help!","Of course!"]

howareyou_input=["how are you","whats up","what's up","what is up",]
howareyou_output=["I am doing well thank you. Is there anything I can help you with?"]

selfname_input=['what is your name',"what are you called","what are you","what is this","who are you"]
selfname_output=["My name is Korok. I am an AI chat assistant."]

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # check if text is valid
    if any(hello_input in text.lower() for hello_input in hello_input):
        message = {"answer": random.choice(hello_output)}
        return jsonify(message)
    elif text.lower() == "hi" or text.lower() == "hey":
        message = {"answer": random.choice(hello_output)}
        return jsonify(message)
    elif any(help_input in text.lower() for help_input in help_input):
        message = {"answer": random.choice(help_output)}
        return jsonify(message)
    elif any(thanks_input in text.lower() for thanks_input in thanks_input):
        message = {"answer": random.choice(thanks_output)}
        return jsonify(message)
    elif any(howareyou_input in text.lower() for howareyou_input in howareyou_input):
        message = {"answer": random.choice(howareyou_output)}
        return jsonify(message)
    elif any(selfname_input in text.lower() for selfname_input in selfname_input):
        message = {"answer": random.choice(selfname_output)}
        return jsonify(message)
    response = explain(target=text)
    past_inputs.append(response)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)