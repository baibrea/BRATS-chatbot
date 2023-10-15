import openai

openai.api_key = ''

# List that acts like a dynamic array
# stores past user inputs
past_messages = []


# Helper method for explain()
def createPrompt(request, simplicity):
    prompt = f"Answer the following request like a Verizon employee would: {request}."
    if simplicity == 1:
        prompt += "Make the answer simple enough for a senior citizen to understand."
    elif simplicity == 2:
        prompt += ""
    elif simplicity == 3:
        prompt += "Make the answer more in-depth."
    prompt += "Make the answer simple enough so anyone can understand." \
              "Search through the Verizon website for additional accurate information if necessary." \
              "Don't mention that you are an employee and don't tell them to go to the website." \
              "Answer in less than 100 words."
    return prompt


# Generates OpenAI responses
def explain(target, context="", max=100, temp=1, simplicity=2):
    newPrompt = createPrompt(target, simplicity)
    past_messages.append({"role": "user", "content": newPrompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=past_messages,
        max_tokens=max,
        temperature=temp,
    )
    past_messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
    explanation = response["choices"][0]["message"].content
    return explanation


# Testing only (only runs if you run this file)
def main():
    target = input("Input a target: ")
    print(explain(target))


if __name__ == '__main__':
    main()