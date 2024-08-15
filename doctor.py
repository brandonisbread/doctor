"""
doctor.py
Chapter 5 example
8/2/24

An application that simulates an interactive session of nondirective psycho therapy.
"""

import random

# Global variables of various lists of data that all functions can share
hedges = ("Please, tell me more.", "Many of the patients tell me the same thing.", "Please continue.", "Go on, go on...", "You don't say...")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "I'm":"you're", "us":"you", "mine":"yours", "am":"are", "you":"I"}

# Definition of the reply() function
def reply(sentence):
	probability = random.randint(1, 4)
	if probability == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + changePerson(sentence)


# DEfinition of the changePerson() function
def changePerson(sentence):
	"""Replaces first-person pronounds with second-person pronouns"""
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)

# Definition of the main() function
def main():
	"""Handles the interaction between user and doctor."""
	print("Good day, I hope you are well today.")
	print("What can I do for you?")
	while True:
		sentence = input("\nType your response or QUIT to exit >> ")
		if sentence.upper() == "QUIT":
			input("Have a great day! Press ENTER to exit the program >> ")
			break
		print(reply(sentence))

main()

#Global call to main() for program execution
if _name_ == _main_:
	main()