# Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "How man bones are in the human body?: ",
             "How many planets are in the solar system?: ")

options = (("A. 116", "B. 117", "C. 118 ", "D. 119"), 
           ("A. Bald Eagle", "B. Crocodile", "C. Platapus", "D. Ostrich"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"), 
           ("A. 5", "B. 7", "C. 8", "D. 9"))

answers = ("C", "D", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else: 
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1 #

print("------------------------------")
print("          RESULTS             ")
print("------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")