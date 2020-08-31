#Written by David Morales
import sys
import re

def main(): 
	print("Welcome to word counter!")
	word_counter(sys.argv)

def word_counter(textFile):
	with open(filename, encoding='windows-1252') as textFile:  
		for line in textFile:
			string = line.split()
			word = str(string)


	print("wip")