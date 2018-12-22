'''
Sample solution of a hangman game between two players: one player chooses the word and the other player has to guess it
'''

print("Welcome to Hangman! \n")

while True:
    word = input("Please enter a word for someone to guess: ")
    word = word.lower()

    # check if input is valid
    if word.isalpha() == False:
        print("That is not a valid input. Try again.")
    else:
        break

currentAnswer = []
guessedLetters = []
bodyParts = ["head", "torso", "leg", "leg", "hand", "hand"]
chances = 6
fails = 0

for letter in word:
    currentAnswer.append("_")

print(currentAnswer)

while chances > 0:
    userGuess = input("\nGuess a letter. ")
    userGuess = userGuess.lower()

    if userGuess in guessedLetters:
        print("\nYou already guessed that letter! Try again.\n")
        print(currentAnswer)

    elif userGuess in word:
        print("\nYou got a letter!\n")
        guessedLetters.append(userGuess)
        for i in range(len(word)):
            if word[i] == userGuess:
                currentAnswer[i] = userGuess
        print(currentAnswer)
    else:
        chances -= 1
        print("\nA %s is drawn. You have %s tries left.\n" %(bodyParts[j], chances))
        fails += 1
        print(currentAnswer)

    if "_" not in currentAnswer:
        print("\nYou win!")
        break

if chances == 0:
    print("\nYou lose :(")

