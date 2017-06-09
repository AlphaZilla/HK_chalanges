# Wrap evrey line from preInput.txt with ""

# open file for read and write input
preInputFile = open("pre-input.txt", "rt")  # read text
inputFile = open("input-file.txt", "wt")  # write text

# create a list with all the lines from file
textFile = preInputFile.readlines()


# ad "" to every line
for line in textFile:
    if line[-1] == "\n":
        newFormat = "\"" + line[:-1] + "\"" + "\n"
        inputFile.write(newFormat)
    else:
        newFormat = "\"" + line + "\""
        inputFile.write(newFormat)

# close all the opened files
preInputFile.close()
inputFile.close()
