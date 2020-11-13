#core function for opening files, text vs. binary files, read and write files, close files explicitly,
#context managers -  python suppoer for managing resources and with keyword 
# list of encodings https://docs.python.org/3/library/codecs.html#standard-encodings

"""
open() Modes
'r' - read
'w' - write
'a' - append
combined with 
't' - text
'b' - binary
"""

f = open('file.txt', mode='wt', encoding='utf-8')
