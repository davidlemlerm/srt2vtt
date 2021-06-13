# Imports
import os.path
import sys
import getopt

# Variables
inputfilename = None
outputfilename = None

# Functions
def getTransformedLine(line):
	if "-->" in line:
		return line.replace(",", ".")
	else:
		return line

# Argument processing
args, params = getopt.getopt(sys.argv[1:], "i:o:")
for arg, param in args:
	if arg == "-i":
		inputfilename = param
	elif arg == "-o":
		outputfilename = param

# If input file is not specified in arguments, request it from the user
if inputfilename == None:
	print("Please enter the name of the file to open:", end=" ")
	inputfilename = input()
done = False
while done == False:
	if os.path.isfile(inputfilename):
		done = True
	else:
		print("File not found, please enter the filename:", end=" ")
		inputfilename = input()

# Open the file
inputfile = open(inputfilename)

# If we're outputting to the console
if outputfilename == None:
	print("WEBVTT")
	print()
	for line in inputfile:
		print(getTransformedLine(line), end="")

# If we're outputting to a file
else:
	if os.path.isfile(outputfilename):
		print("The file \"{0}\" already exists. Overwrite?:".format(outputfilename), end=" ")
		if input().lower() != "true":
			print("Exiting.")
			exit()
	output = open(outputfilename, "w")
	output.write("WEBVTT")
	output.write("\n\n")
	for line in inputfile:
		output.write(getTransformedLine(line))
	# Close our output file
	output.close()
			
# Close our input file
inputfile.close()
