import openai

openai.api_key = ''


def createPrompt(request, simplicity):
    prompt = f"Answer the following request like a Verizon employee would: {request}."
    if simplicity == 1:
        prompt += "Make the answer simple enough for a senior citizen to understand."
    elif simplicity == 2:
        prompt += ""
    elif simplicity == 3:
        prompt += "Make the answer more in-depth."
    return prompt


def explain(target, context="", max=150, temp=1, simplicity=2):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=createPrompt(target, simplicity),
        max_tokens=max,
        temperature=temp
    )
    explanation = response.choices[0]['text'].replace("\n", " ")
    return explanation


def main():
    target = input("Input a target: ")
    print(explain(target))


if __name__ == '__main__':
    main()