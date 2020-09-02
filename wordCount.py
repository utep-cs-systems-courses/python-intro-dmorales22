#Author: David Morales 
#Course: CS 4375 Theory of Operating Systems
#Instructor: Dr. Eric Freudenthal
#T.A: David Pruitt 
#Assignment: Lab 1
#Last Modification: 09/01/2020
#Purpose: To count words in a input file

import sys
import re

def main(): 
	print("Welcome to word counter!")
	dict = word_counter(sys.argv[1]) #Takes first argument (input file)
	file_writer(dict, sys.argv[2]) #Takes dictionary and second argument (output file) and writes contents of dictionary

def word_counter(filename): #Counts every instance of word from an input file by parsing.
	dict = {}
	with open(filename, encoding='windows-1252') as textFile:  
		for line in textFile:
			line = line.rstrip("\n") #Removes new lines 
			line = line.replace("'", " ") 
			line = line.replace("-", " ") #Removes dashed lines to separate words 
			line = line.lower() #Makes string lower case 
			string = line.split() #Tokenizes the string. 

			for i in range(len(string)): 
				word = word_parser(string[i])

				if word in dict: #Checks if word is in dictionary and adds one to count 
					value = dict.get(word) + 1
					dict.update({word : value})

				else:
					dict[word] = 1 #Adds word to dictionary if doesn't exist

	return dict

def word_parser(word_u): #Parses each tokenized word to removed capitalized letters and unwanted characters
	word = str(word_u) #Makes sure word is a string
	word = word.replace(",", "")
	word = word.replace(".", "")
	word = word.replace(";", "")
	word = word.replace("?", "")
	word = word.replace('"', "")
	word = word.replace(":", "")

	return word

def file_writer(dict, output): #Get dictionary and writes its contents to output file
	file = open(output, "w") #Overrides existing contents 

	for i in sorted(dict.keys()): #Writes out dictionary in order. 
		line = str(i) + " " + str(dict[i])
		file.write(line + "\n")
		print(i, dict[i]) #Prints out on command line too

	file.close()

if __name__ == "__main__":
	main()