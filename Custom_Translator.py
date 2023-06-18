# Python program to translate from any dictionary. 

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the translator.

DICT = {'A':'b', 'B':'c',
		'C':'d', 'D':'e', 'E':'f',
		'F':'g', 'G':'h', 'H':'i',
		'I':'j', 'J':'k', 'K':'l',
		'L':'m', 'M':'n', 'N':'o',
		'O':'p', 'P':'q', 'Q':'r',
		'R':'s', 'S':'t', 'T':'u',
		'U':'v', 'V':'w', 'W':'x',
		'X':'y', 'Y':'z', 'Z':'a',
		'1':'2', '2':'3', '3':'4',
		'4':'5', '5':'6', '7':'8',
		'8':'9', '9':'0', '0':'1', 
		', ':'.', '.':',', '!':'?',
		'?':'!', '/':'|', '-':'_',
		'(':'[', ')':']'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			# Looks up the dictionary and adds the
			# corresponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

	# extra space added at the end to access the
	# last morse code
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(DICT.keys())[list(DICT.values()).index(citext)]
				citext = ''

	return decipher

# Hard-coded driver function to run the program
def main():
	message = "Hello World?"
	result = encrypt(message.upper())
	print (result)

	message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
	result = decrypt(message)
	print (result)

# Executes the main function
if __name__ == '__main__':
	main()
