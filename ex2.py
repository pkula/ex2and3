import sys
import copy
import pycountry


def read(file_name):
    #this function read a file line by line and return list contain lines
    with open(file_name, "r") as file:
        passwords = file.readlines()
    return passwords