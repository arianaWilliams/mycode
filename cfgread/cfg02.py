#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

#count the lines
line_count = len(configlist)
print("Number of lines in the file: ", line_count)

## Always close your file
configfile.close()

