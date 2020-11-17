"""
Modularization - modules can be either run as scripts from an OS shell or imported into the
module - single source file, packages contain other modules - a way to ehirarchicly organize modules
"""

#Main Block Concept
#if __name__ == '__main__' then the program executes the function
#if not then it knows that it is being imported into another module, so it only defines the dunction without executing it
def function():
    four = 2 + 2
    returns four

if __name__ == '__main__':
    function()

    
#Setting paths for custom directories
import urllib
urllib.__path__ #returns the place where the package is saved
urllib.requests.__path__ #throws an Attribution Error
#to locate the modules Python uses sys.path which leads to the list of directories

#Method 1
import sys
sys.path
#this returns a list, and we can append it with Diretories (folders) that we want Python to search
sys.path.append('name_of_new_directory')

#Method 2
#Windows shell
set PYTHONPATH=name_of_new_directory;path2;path3
#Linux/macOS shelss
export PYTHONPATH=name_of_new_directory:path2:path3

        
#Creating a Package 
#1. create __init__.py in the root directory indicates that this is a package - can be left empty, not necessary for 3.3+
#2. after the __init__.py was create the directory can be imported as a module
#3. can create other modules including classes and other directories example: name_of_subdirectory (also add __init__.py)
"""
name_of_new_directory
|---__init__.py
|---module.py
|---name_of_subdirectory
    |---__init__.py
    |---sub_module_1.py
    |---sub_module_2.py
"""
import name_of_new_directory.name_of_subdirectory

#modules can also be imported with relative paths when importing with the 'from package import module' form
"""
||Relative||                                ||Absolute||
from . import name                          from name_of_new_directory.name_of_subdirectory import name
from .. import name                         from name_of_new_directory import name
from ..name_of_subdirectory import name     from name_of_new_directory.name_of_subdirectory import name
"""
