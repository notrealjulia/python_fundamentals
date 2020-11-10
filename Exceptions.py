# Python Exceptions - example

import os
import sys

def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)
    except OSError as e: #catching the specific excpetion
        print(e, file=sys.stderr)
        raise
    finally: #gets performed no matter what
        os.chdir(original_path)
        
"""
avoid catching Type errors
"""
