import turtle as trtl
import random
trtl.Turtle()
#Rules
print(" Hello, welcome to my game")
print("In this game you have 5 chances to guess a random 5 letter word correctly")
print("Good luck!")
#game setup
#repeats the guesses until word is guessed
#makes the user enter a 5-letter word
word_list = ['jumpy', 'brick', 'adieu']
word = random.choice(word_list)

for i in range(5):
    guess = input("Guess word: ")
    while len(guess) != 5:
        print("That's not a 5 letter word!")
        guess = input("Enter a word: ")

if guess == word:
    print("Correct")
else:
    print("Incorrect")
wn = trtl.Screen()
wn.mainloop()
