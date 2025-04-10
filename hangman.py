import random

words = ["gazebo", "galaxy", "jigsaw", "queue", "larynx"]
correct_word = random.choice(words)
display = ["_" for _ in correct_word]
guessed_letters = []
attempts = 5

print("Guess the word:", " ".join(display))

while "_" in display and attempts > 0:
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)

        if guess in correct_word:
            print("the letter is in the word.")
            for i, letter in enumerate(correct_word):
                if letter == guess:
                    display[i] = guess
        else:
            attempts -= 1
            print("The letteris not in the word")

        print("Current word:", " ".join(display))
    

if "_" not in display:
    print("You guessed the word!")
else:
    print(f"You have lost the game. The word was '{correct_word}'.")
