import random

word = "kaktus"
lives = 5

wordupper = word.upper()

wordlist = list(wordupper)
wordlistcopy = list(wordupper)
usedletters = set()

for i in range(len(word)):
    wordlist[i] = "-"

while True:
    t = 0
    t2 = 0

    print(f"Lives: {lives}")
    print(wordlist)

    answer = input("What is this word?: ")
    if answer == word:
        print(f"Winner! You corretly guessed word {word}!")
        break
    else:
        guess = input("Write your letter: ").upper()

        if guess in usedletters:
            lives = lives - 1

            usedletters.add(guess)
            print(len(usedletters))

        for i in range(len(word)):
            if guess == wordupper[i]:
                wordlist[i] = guess

        for i in range(len(word)):
            if guess != wordupper[i]:
                t = t + 1

        if t == len(word):
            lives = lives - 1

        if lives == 0:
            print("You lose! Try again!")
            break
