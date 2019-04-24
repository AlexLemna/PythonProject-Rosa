# ----------------------------------------
# rlRandomName.py
# ----------------------------------------
# A logic module for Alex's "Project Rosa" that contains functions for randomly generating names.
import os
import random
import sys

# Defining empty list. Explicit variable declaration isn't necessary in Python, but I like it.
contents = []

def CWD_home(): # Ensures that the current working directory is set to the home directory of the active script. From https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
    os.chdir (os.path.dirname (sys.argv[0]))

# target files is at \Data\SampleData.txt"
def SampleData ():
  if __name__ == "Logic.rlRandomName": # This is the normal module behavior - it's being run from somewhere else.
    CWD_home()
    os.chdir ( ".\Data" )
    with open('SampleData.txt', 'r') as fileData:
      contents = fileData.readlines()
      return ( random.choice(contents) )

  elif __name__ == "__main__": # Checks if this program is running as the main script (only happens for debugging purposes)
    CWD_home()
    os.chdir ("..")
    os.chdir ( ".\Data" )
    with open('SampleData.txt', 'r') as fileData:
      contents = fileData.readlines()
      print ( random.choice(contents) )
  
  elif __name__ == "rlRandomName": # Checks if this program is running as a module from another script inside its home directory (only happens for debugging purposes)
    CWD_home()
    os.chdir ("..")
    os.chdir ( ".\Data" )
    with open('SampleData.txt', 'r') as fileData:
      contents = fileData.readlines()
      return ( random.choice(contents) )

  else: # I'm honestly not sure what situation wouldn't fit into the statements above.
    from inspect import currentframe, getframeinfo
    frameinfo = getframeinfo ( currentframe())

    print ("")
    print ("A wild UNEXPECTED ERROR appeared!")
    print ( f"REF: The file location is {frameinfo.filename}." )
    print ( f"REF: This error message is around line {frameinfo.lineno} of that file.")
    print ( "   SUMMARY:")
    print ( "   This section of code has some 'if' and 'else if' statements that should")
    print ( "   cover every situation. This error is the 'else' statement, and it means")
    print ( "   a situation occured that I didn't forsee.")
    print ( "   SPECIFICS:")
    print ( "   The error occured in a file called 'rlRandomName.py'. The file behaves")
    print ( "   differently depending on if it is running by itself or as a 'module' being")
    print ( "   called by a different file. It can tell how it is being run by checking")
    print ( "   a variable called __name__ against some predetermined values. It expects")
    print ( "   __name__'s value to be 'rlRandomName', 'Logic.rlRandomName', or '__main__'.")
    print ( f"   Instead, the value is '{__name__}'.")
    print ( "   WHAT YOU SHOULD DO:")
    print ( "   Take a screenshot and contact Alex. Also, tell him to create some kind of")
    print ( "   error logging system so you don't have to manually ask him for help every")
    print ( "   time he messes up.")
    
    # import pdb
    # pdb.set_trace() # Creates a breakpoint.

SampleData()
# print ( f"{SampleData}" )
