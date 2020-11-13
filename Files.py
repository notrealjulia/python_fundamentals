#core function for opening files, text vs. binary files, read and write files, close files explicitly,
#context managers -  python suppoer for managing resources and with keyword 
# list of encodings https://docs.python.org/3/library/codecs.html#standard-encodings
#can call help() on instances too
#to remember to close the files it can be incorporated into try: finally: file.close() structure
"""
open() Modes
'r' - read
'w' - write
'a' - append
combined with 
't' - text
'b' - binary
"""

#writing files
f = open('file.txt', mode='wt', encoding='utf-8')
f.write('this is a string to be written into the file')
f.close() #remember this if opening files in this format

#reading files
g = open('file.txt', mode='rt', encoding='utf-8')
g.read()
g.seek(0) #moves the reader back to the beginning of the file
g.readline() #reads one line at a time
g.readlines() #reads all lines into a list
g.close()

#appending files
h = open('file.txt', mode='at', encoding='utf-8')
h.writelines('add more text to the existing file')
h.close()

#itteration over files and reading the whole file in the terminal
#sys.argv[1] takes the name of the file passed in the terminal when running the .py file with the following:
import sys
f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
    print(line)
    #or use the follwing to avoid extra spaces and lines
    #sys.stdout.write(line) 
f.close()

#using WITH-blocks
#can be used with any object that supports the context-manager protocol
def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]

#sugary syntax
