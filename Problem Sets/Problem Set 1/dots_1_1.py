#!/use/bin/env python

"""
Title: Ask for an integer from the terminal and print out that many periods on a single line followed by the newline character, and then stop.

Solution to Problem Set 1, Problem 1
~ Arsh R. Nadkarni

To run:
python dots_1_1.py

"""
def dots():
    dots = int(input("Enter an Integer: ")) # input integer variable
    for foo in range(0,dots): # for loop to print out periods in the given integer range
        print(".", end="") # print the periods to the terminal
dots() # call the function

print() # print a new line