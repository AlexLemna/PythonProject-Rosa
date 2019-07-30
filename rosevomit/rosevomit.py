# --------------------
# ROSEVOMIT.PY
# --------------------
# The main file for Alex's "Project ROSEVOMIT", a random name generator  and random timeline generator written in Python.

print ()
print ("Starting ROSEVOMIT.")
# *** SOME SETUP STUFF ***
# MODULES FROM PYTHON'S STANDARD LIBRARY
print ("Getting some modules from the standard library... ", end="")
import os
import sys
print ("done.")

# MODULES FROM PYPI (the Python community)
# none

# INTERNAL MODULES
print ("Proceeding to get local modules... ", end="")
from core import Startup
from programlogic import LogicController
from programcli import DialogExit, TextStuff, WorseCLI
print ("done.")


# SOME FUNCTIONS
def show_main_menu():
    """Contains display instructions for the main menu."""
    print ()
    print (10 * "-", "Rosevomit.py Main Menu", 10 * "-")
    print ("What would you like to generate?")
    print ("     1. Random names")
    print ("     2. A random timeline")
    print ("X or 0. Exit program")
    print ()


def ask_for_input():
    """Asks for user input and processes it. Contains logic for the main menu."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.rstrip()  # Strips whitespaces at the end.

    if menuchoice == "1":
        WorseCLI.submenu_name_show()
        WorseCLI.submenu_name_input()
        show_main_menu()
    elif menuchoice == "2":
        WorseCLI.submenu_timeline_show()
        WorseCLI.submenu_timeline_input()
        show_main_menu()
    elif menuchoice == '0' or menuchoice == 'X' or menuchoice == "x" or menuchoice == "exit":
        do_we_exit = DialogExit.exit()  # DialogExit.exit() should either return False or close the program itself
        if do_we_exit is False:
            show_main_menu()
    elif menuchoice == "help" or menuchoice == "'help'" or menuchoice == "h" or menuchoice == "H" or menuchoice == "helf":
        show_main_menu()
    elif menuchoice == "":
        ask_for_input()
    else:
        print (f"{menuchoice} is not a recognized command.")


# **********************************************
# ********** MAIN PROGRAM STARTS HERE **********
# **********************************************
Startup.main_setup()

print ()
print (69 * "-")
print (27 * "-", "ROSEVOMIT.PY", 28 * "-")
print (69 * "-")
print ()

# After setup, rosevomit.py will display the main menu and will carry out instructions based on user input. This is an infinite loop - if rosevomit.py ever has no more instructions to carry out, it displays the main menu again and awaits further instructions. This is based on the 'see_rosa_run' variable. This variable should never change. If it does, the program exits and gives the system an error code.
see_rosa_run = True
show_main_menu()
while see_rosa_run is True:
    ask_for_input()
else:
    sys.exit(1)