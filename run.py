# welcome texts

print("welcome to Animal Ques Game!")
name = input("Whats you name?: ")
player = input("Hi " + name + ". Do you want to play? Yes or No: ")

if player.lower() != "yes":
    print ("Come back when you feel like playing. Take care.")
    quit()
else:
    print ("Let's play, good luck " + name + "!")


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print(" ")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, or C ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key), guess)
        question_num += 1
        print(f'Your Score Is {correct_guesses}')


# print(correct_guesses)

# Check answer see if is correct or wrong.

def check_answer(answer, guess):

    if answer == guess:
        print("Correct, good job!")
        return 1
    else:
        print("Wrong answer.")
        return 0

question = {
   "How long is the gestation period of an African elephant?:": "A",
   "What’s the scientific name of a wolf?:": "C",
   "What is a female donkey called?:": "B",
   "Which mammal has no vocal cords?:": "B",
   "What’s the fastest land animal in the world?:": "A",
   "How many eyes does a bee have?:": "C",
   "Which animal symbolizes good luck in Europe?:": "B",
   "What name is used to refer to a group of frogs?:": "C",
   "How many hearts does an octopus have?:": "A",
   "How many compartments are in a cow's stomach:": "B",
}

options = [["A. 22 month", "B. 24 month", "C. 18 month"],
           ["A. Candiz Lupra", "B. Cardo Lapo", "C. Canis Lupus"],
           ["A. A Sendra", "B. A Jenny", "C. A Sara"],
           ["A. Tiger", "B. Giraffe", "C. Cat"],
           ["A. The cheetah ", "The lion", "C. The horse"],
           ["A. Four", "B. Six", "C. Five"],
           ["A. Bee", "B. Ladybug", "C. Butterfly"],
           ["A. A family", "B. A stuff", "C. An army"],
           ["A. Three", "B. Five", "C. One"],
           ["A. Two", "B. Four", "C. Six"]]

new_game()