import random
import time
cChoices = ["Arizona","Racecar", "Tower"]
name = input("Whats your name? ")
print("Hello " +name, ",Welcome to Hangman!!")

mysteryWord = random.choice(cChoices)
print(mysteryWord)
Guesslist = []

for letter in mysteryWord:
	Guesslist.append("_")

print(Guesslist)

misses = 0
while True:
	guess = input("Guess a letter: ")
	if guess in mysteryWord:
		print("Letter in word")
	else:
		misses = misses + 1
		print("Misses: " + str(misses))

#How to replace a certain index


count = 0
Guesslist = list(mysteryWord)
for letter in Guesslist:
	if letter == guess:
		print(count)
		count += 1