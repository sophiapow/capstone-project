import random
words = ["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
         "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"]

word = random.choice(words)

guessed_letters = ["_" for letter in word]
print(guessed_letters)

guesses_left = 6
previous_guesses = []

while "_" in guessed_letters and guesses_left > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter")
        continue

    if guess in previous_guesses:
        print(f"You've already guessed {guess}")
        continue
    else:
        previous_guesses.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
    else:
        print("Incorrect, try again")
        guesses_left -= 1
        print(f"You have {guesses_left} guesses remaining")

    print(guessed_letters)

if "_" not in guessed_letters:
    print("Well done, you have guessed the word!")
else:
    print(f"Unlucky! The word was {word}")
