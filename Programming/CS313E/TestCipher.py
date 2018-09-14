#  File: TestCipher.py

#  Description: A program to apply different cyphers to text

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 3/30/16

#  Date Last Modified: 3/30/16

# /////////////////////////////////////////////////////////////////////////////////

def substitution_encode (st):

	cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 
		't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']

	st = st.lower()

	code = ""

	# encrypting loop
	for i in range (len(st)):

		# checks for spaces and non-letters
		if (st[i] == " "):
			code += " "
			continue
		if (ord(st[i]) < 97) or (ord(st[i]) > 122):
			code += st[i]
			continue

		# finds index of cipher list and adds said element to code	
		idx = ord(st[i]) - ord("a")
		code += cipher[idx]

	return code

# /////////////////////////////////////////////////////////////////////////////////

def substitution_decode (code):

	cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 
		't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']

	code = code.lower()
	st = ""

	# decryption loop
	for i in range (len(code)):

		# checks for spaces and non-letters
		if (code[i] == " "):
			st += " "
			continue
		if (ord(code[i]) < 97) or (ord(code[i]) > 122):
			st += code[i]
			continue
		idx = cipher.index(code[i]) + ord('a')
		st += chr(idx)

	return (st)

# /////////////////////////////////////////////////////////////////////////////////

def vigenere_encode (st, pword):

	p_phrase = ""

	# loop to make pass-phrase
	# fix aids the process when a space throws the index off
	fix = 0
	for i in range (len(st)):
		if (st[i] == " "):
			p_phrase += " "
			fix -= 1
			continue
		idx = i % (len(pword)) + fix
		p_phrase += pword[idx]

	code = ""

	# encryption loop
	for i in range (len(st)):

		# checks for spaces and non-letters
		if (st[i] == " "):
			code += " "
			continue
		if (ord(st[i]) < 97) or (ord(st[i]) > 122):
			code += st[i]
			continue

		# used this nifty rule from the matrix to find the appropriate letter
		idx = ord(p_phrase[i]) + ord(st[i]) - ord('a')

		# sometimes the idx was too big, but always a multiple of 26 away
		while (idx > 122):
			idx -= 26
		code += chr(idx)
	
	return code

# /////////////////////////////////////////////////////////////////////////////////

def vigenere_decode (code, pword):

	# basically the same as encypting, but working backwards
	p_phrase = ""

	fix = 0
	for i in range (len(code)):
		if (code[i] == " "):
			p_phrase += " "
			fix -= 1
			continue
		idx = i % (len(pword)) + fix
		p_phrase += pword[idx]

	st = ""
	for i in range (len(code)):
		if (code[i] == " "):
			st += " "
			continue
		if (ord(code[i]) < 97) or (ord(code[i]) > 122):
			st += code[i]
			continue
		idx = ord(code[i]) - ord(p_phrase[i]) + ord('a')
		while (idx < 97):
			idx += 26
		st += chr(idx)

	return st

# /////////////////////////////////////////////////////////////////////////////////

def main():

	in_file = open("./cipher.txt", "r")

	# print header for substitution cipher
	print ("\nSubstitution Cipher\n")

	# read line to be encoded
	line = in_file.readline()
	line = line.strip()

	# encode using substituion cipher
	encoded_str = substitution_encode (line)

	# print result
	print ("Plain Text to be Encoded: {}".format(line))
	print ("Encoded Text: {}\n".format(encoded_str))

	# read line to be decoded
	line = in_file.readline()
	line = line.strip()

	# decode using substitution cipher
	decoded_str = substitution_decode (line)

	# print result
	print ("Encoded Text to be Decoded: {}".format(line))
	print ("Decoded Plain Text: {}\n".format(decoded_str))

	# print header for vigenere cipher
	print("Vigenere Cipher\n")

	# read line to be encoded and pass phrase
	line = in_file.readline()
	line = line.strip()
	pword = in_file.readline()
	pword = pword.strip()

	# encode using vigenere cipher
	encoded_str = vigenere_encode(line, pword)

	# print result
	print ("Plain Text to be Encoded: {}".format(line))
	print ("Pass Phrase (no spaces allowed): {}".format(pword))
	print ("Encoded Text: {}\n".format(encoded_str))

	# read line to be decoded and pass phrase
	line = in_file.readline()
	line = line.strip()
	pword = in_file.readline()
	pword = pword.strip()

	# decode using vigenere cipher
	decoded_str = vigenere_decode(line, pword)

	# print result
	print("Encoded Text to be Decoded: {}".format(line))
	print("Pass Phrase (no spaces allowed): {}".format(pword))
	print("Decoded Plain Text: {}\n".format(decoded_str))

	# close file
	in_file.close()

main()