"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
"""

def capitalize(string):
    # must keep whitespace intact
    # str.title() does not work because 12abc becomes 12Abc
    result = ""
    last_is_space = True
    
    for c in string:
        if last_is_space and c.isalpha():
            result += c.upper()
            last_is_space = False
        else:
            if c.isspace():
                last_is_space = True
            else:
                last_is_space = False
            result += c
    return result
