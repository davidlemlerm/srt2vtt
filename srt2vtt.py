import os.path
print("Please enter the name of the file to open:", end=" ")
done = False
while done == False:
	if os.path.isfile(filename):
		done = True
	else:
		print("File not found, please enter the filename:", end=" ")
input = open(filename)
print("WEBVTT")
print()
for line in input:
	if "-->" in line:
		# We need to perform a substitution.
		newline = line.replace(",", ".")
		print(newline, end="")
	else:
		# We don't need to do anything special.
		print(line, end="")
