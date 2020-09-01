#Written by David Morales
import sys
import re

def main(): 
	print("Welcome to word counter!")
	dict = word_counter(sys.argv[1])
	file_writer(dict, sys.argv[2])

def word_counter(filename):
	dict = {}
	with open(filename, encoding='windows-1252') as textFile:  
		for line in textFile:
			line = line.rstrip("\n")
			string = line.split()

			for i in range(len(string)):
				word = word_parser(string[i])

				if word in dict:
					value = dict.get(word) + 1
					dict.update({word : value})

				else:
					dict[word] = 1

	return dict

def word_parser(word_u):
	word = str(word_u)
	word = word.replace(",", "")
	word = word.replace(".", "")
	word = word.replace(";", "")
	word = word.replace("?", "")
	word = word.replace('"', "")
	word = word.replace(":", "")
	word = word.replace("-", "")

	char_strs = ""
	for i in range(len(word)):
		char = caps_detector(word[i])
		char_strs += char

	return char_strs

def caps_detector(char): #Checks if a letter is capitalized, then returns the lower case equivalent if the letter is capitalized.  
	cap_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
	
	lower_char = '' 
	for i in range(len(cap_list)): 
		if (char == cap_list[i]): 
			lower_char = lower_list[i] 
			return lower_char
			
	return char 

def file_writer(dict, output):
	file = open(output, "w")

	for i in sorted(dict.keys()):
		line = str(i) + " " + str(dict[i])
		file.write(line + "\n")
		print(i, dict[i])

	file.close()

main()