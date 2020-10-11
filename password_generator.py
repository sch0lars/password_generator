from random import randint

class Password:
	def __init__(self):
		self.password = Password.generate_password()
		
	def __str__(self):
		return self.password
		
	def generate_password():
		word1 = words[randint(0, 10000)].strip()
		word2 = words[randint(0, 10000)].strip()
		
		password = word1 + " " + word2
		password = password.replace('a', '@')
		password = password.replace('e', '3')
		password = password.replace('i', '!')
		password = password.replace('o', '0')
		password = password.replace('l', '1')
		password = password.replace('s', '$')
		password = password.replace(' ', '_')
		
		return password
		
words = open("wordlist.txt").readlines()



print("Press enter to generate a new password. Press 'q' to quit")

i = input()
while i != 'q':
        print(Password.generate_password())
        i = input()
