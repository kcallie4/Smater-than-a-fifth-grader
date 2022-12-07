# -------------------------

print("Welcome to are you smarter than a fifth Grader? The game show to test your elementary education! What is your name player?")
print("enter your name: ")
x=input()
print("Hello " +x,"you will be tested on a series of different curriculum from the fifth grade. Are you ready..set..go!")


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "What is the captial of New York?: ": "A",
 "In the intials of the federal agency known as NASA, what does the first 'A' stand for?: ": "B",
 "What number does the Roman Numeral representation XXXVIII represent?: ": "C",
 "What is the first item in the periodic table of elements?": "C",
 "In the term 'PEMDAS', what does the 'S' stand for?: ": "A",
 "The first day of the 20th century was...":"B"
 }

options = [["A. Albany", "B. New York", "C. Brooklyn", "D. Rochester "],
          ["A. Astronaut", "B. Aeronautics", "C. Awsome", "D. Administration"],
          ["A. 14", "B. 35", "C. 38", "D. 59"],
          ["A. Sodium", "B. Helium", "C. Hydrogen", "D. Nitrogen"],
          ["A. Aunt Sally","B. Aunt Sarah", "C. Uncle Sean", "D. Grandpa Sheldon"],
          ["A. January 1st 1900","B. January 1st,1901", "C. January 1st, 2000", "D. January 1st, 2001"]]

new_game()

while play_again():
    new_game()

print("See you later 5th grader!")

# -------------------------












