import openai

openai.api_key = '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'


def explain(target, context, max=150, temp=0.9, simplicity=2):
    if simplicity == 1:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Generate an simpler explanation about {target} from the following context: \n{context}\n",
            max_tokens=max,
            temperature=temp
        )
    elif simplicity == 2:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Generate an explanation about {target} from the following context: \n{context}\n",
            max_tokens=max,
            temperature=temp
        )
    elif(simplicity == 3):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Generate a more complex explanation about {target} from the following context: \n{context}\n",
            max_tokens=max,
            temperature=temp
        )
    x = response.choices[0]['text'].replace("\n", " ")
    return x


def makeSimpler(past_text):
    return


def main():
    target = input("Input an target: ")
    context = input("Input the context: ")
    print(explain(target, context))
    satisfied = input("Are you satisfied with your answer? Type Y/N")
    if satisfied == "Y":
        print("Great")
    elif satisfied == "N":
        change = input(f"What would you like to change?"
                       f"1. More creative"
                       f"2. Simpler answer"
                       f"3. Longer answer"
                       f"4. Shorter answer"
                       f"5. More complex answer")
        if change == 1:
            print(explain(target, context, max=150, temp=1.5, simplicity=2))
        elif change == 2:
            print(explain(target, context, max=150, temp=0.9, simplicity=1))
        elif change == 3:
            print(explain(target, context, max=300, temp=0.9, simplicity=2))
        elif change == 4:
            print(explain(target, context, max=75, temp=0.9, simplicity=2))
        elif change == 5:
            print(explain(target, context, max=150, temp=0.9, simplicity=2))


if __name__ == '__main__':
    main()