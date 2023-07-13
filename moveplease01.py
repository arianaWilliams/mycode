#!/usr/bin/env python3
""" A simple script to move two files into ceph_storage/ 
    Alta3 Research | rzfeeser@alta3.com"""

# standard library imports
import shutil # shell utilities will be used to move files
import os # provides access to low level os operations

def main():
    """called at runtime"""
    #force start in the home directory
    os.chdir('/home/student/mycode/')
    # move the file
    shutil.move('raynor.obj', 'ceph_storage/')
    # prompt for new file name
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

# call to main
if __name__ == "__main__":
    main()
