from model import ask_ai
# import random

print("Welcome to Trivia Game")
print("Enter n to display result")

scores = 0
decide = "y"
while decide == 'y':
    question = ask_ai("Generate a simple addition question in mathematics, in one line", "user")
    options = ask_ai(f"{question}. Generate options to this question the option should be in this format [2,3,4,10]", "assistant")
    answer = int(ask_ai(f"{question}. Return the answer in integer", "assistant"))

    # options = [random.randint(1,5) for _ in range(4)]
    
    # options = []
    # for _ in range(5):
    #     numbers = random.randint(1,5)
    #     if numbers not in options:
    #         options.append(numbers)

    # if answer not in options: 
    #     options.append(answer)
   

    print(question)
    try: 
        choice = int(input(f"Choose options {options}: "))
    except ValueError:
        print("Invalid option, try again")
        choice = int(input(f"Choose options {options}: "))

    # while choice not in options:
    #     print("Invalid options, try again")
    #     choice = int(input(f"Choose options {options}: "))

    if choice == "n":
        decide = 'n'

    if answer == choice:
        scores += 1
        print("Correct!!!, here's the next question\n")

    else:
        print("Wrong!!!, here's the next question\n")
    

    decide = input("Do you want to continue. y/n: ")
    if decide == 'n':
        print(f"Total score is {scores}")