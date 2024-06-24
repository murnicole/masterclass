#!/bin/bash

''' Simple calculator '''

def add (a, b):
    return a + b:

def substract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by Zero"

# List of operations
operList = ["Add", "Substract", "Multiply", "Divide"]

# Dictionary of Functions
operDict = {
        1: add,
        2: substract,
        3: multiply,
        4: divide
}



