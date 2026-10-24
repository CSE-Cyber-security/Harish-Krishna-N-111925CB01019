# Harish-Krishna-N-111925CB01019
# Week-3:Fibonacci Series in Python
# Aim:

To write a Python program to print the Fibonacci series for "n" terms.

# Problem Statement

# Write a Python program to print the Fibonacci series for the given number of terms.

Input

Enter the number of terms: 7

Output

Fibonacci Series:
0 1 1 2 3 5 8

# Python Program

n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Algorithm

1. Start the program.
2. Read the number of terms "n".
3. Initialize "a = 0" and "b = 1".
4. Repeat the loop "n" times.
5. Print the current value of "a".
6. Update "a" and "b" to generate the next Fibonacci number.
7. Stop the program.

Result

The Python program successfully prints the Fibonacci series for the given number of terms.
