#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    name = input("Please enter your name: ")
    date = input("Please enter the day of the week: ")
    
    # display the input back to the user.
    print("Hello " + name + "!" + " Happy " + date + "!") 
    
# this calls main using formate allows others to import my code
if __name__== "__main__":
    main()

