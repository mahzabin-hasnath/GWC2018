correctAnswer = "bananas"
currentAnswer = ["_", "_", "_", "_", "_", "_", "_"]
guessedLetters = []
bodyParts = ["head", "torso", "leg", "leg", "hand", "hand"]

print("Welcome to Hangman! \n")
print(currentAnswer)

chances = 6
j = 0

while chances > 0:
    userGuess = input("\nGuess a letter. ")
    userGuess = userGuess.lower()

    if userGuess in guessedLetters:
        print("\nYou already guessed that letter! Try again.\n")
        print(currentAnswer)

    elif userGuess in correctAnswer:
        print("\nYou got a letter!\n")
        guessedLetters.append(userGuess)
        for i in range(len(correctAnswer)):
            if correctAnswer[i] == userGuess:
                currentAnswer[i] = userGuess
        print(currentAnswer)
    
    else:
        chances -= 1
        print("\nA %s is drawn. You have %s tries left.\n" %(bodyParts[j], chances))
        j += 1
        print(currentAnswer)
    
    if "_" not in currentAnswer:
        print("\nYou win!")
        break
        
if chances == 0:
    print("\nYou lose :(")
