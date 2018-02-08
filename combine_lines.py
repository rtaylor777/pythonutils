#!/usr/bin/python
# Author: Robert L. Taylor
# Date: Feb 8, 2018
# Purpose: This file combines lines from 2 files. The idea is if you have
# 2 wordlists you can combine every word from one file together with every
# word from a 2nd file. For example if you want to combine a list of months
# together with a list of years.
import sys
import os.path
# prnt is a function to print stuff without outputting a terminating
# line feed or space.
def prnt(stuff):
	sys.stdout.write(stuff)

if (len(sys.argv) < 3):
	prnt("Combine every line of a second file with every line from the first.\n")
	prnt("Produces (number of lines in file 1) * (number of lines in file 2) to STDOUT\n")
	prnt("Please pass the 2 filenames on the commandline...\n\n")
	sys.exit()
file1=sys.argv[1]
file2=sys.argv[2]
#prnt("File1 is: " + file1 + "\n")
#prnt("File2 is: " + file2 + "\n")
file1exist = os.path.isfile(file1)
file2exist = os.path.isfile(file2)
if (file1exist):
	#prnt("File: " + file1 + "exists\n")
	pass # in python means do nothing
else:
	prnt("File: " + file1 + " does not exist\n")
if (file2exist):
	#prnt("File: " + file2 + "exists\n")
	pass # in python means do nothing
else:
	prnt("File: " + file2 + " does not exist\n")
if (not file1exist) or (not file2exist):
	prnt("At least one of the files specified does not exist, exiting...\n\n")
	sys.exit()
#prnt("Yay both files exist\n\n")
try:
	f = open(file1, 'r')
except Exception, err:
	print(err)
	sys.exit()

try:
	f2 = open(file2, 'r')
except Exception, err:
	print(err)
	f.close() # supposedly file1 was successfully opened
	sys.exit()
def prepend_word_to_lines(word,filehandle):
	"""Reads through every line in file referenced by filehandle and
	   prepends the word passed to it. Output is to STDOUT.
	   I avoided stripping the lines from this file so they still include
	   the charriage return or newline characters when output.
	"""
	filehandle.seek(0)
	for line in filehandle:
		prnt(word + line)
		
def main():
	"""Reads through every line in a file referenced by filehandle f and calls
		prepend_word_to_lines passing that line and a handle to f2.
		If the file referenced by filehandle f has leading or trailing
		spaces in the words they are left intact. Only carriage return and
		new line characters are stripped from the end of the line.
	"""
	for line in f:
		line = line.rstrip('\r\n')
		prepend_word_to_lines(line,f2)
	f.close()
	f2.close()
		
# Standard boilerplate to call the main() function to begin
# the program. Helps to avoid calling main if this file is imported to another program.
if __name__ == '__main__':
	main()

