# TARUN-R-D-111925CB01056
# Week-2: Factorial Program

## Problem
Write a Python program to find the factorial of a given number.

## Input
Enter a number: 5

## Output
Factorial of 5 = 120

## Description
This Python program calculates the factorial of a given number using a `for` loop.

The factorial of a number is the product of all positive integers from 1 to that number.

Example:

5! = 5 × 4 × 3 × 2 × 1 = 120

## Python Program

```python
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "=", factorial) 

##Sample Output:
Enter a number: 5
Factorial of 5 = 120

##Files:
factorial.py – Python program
README.md – Project documentation
output.png – Screenshot of the program output

### Your GitHub folder should finally contain:

```text
Week-2/
├── factorial.py
├── README.md
└── output.png 
