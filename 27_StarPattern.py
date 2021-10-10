'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print ("\n*****Program to print the sum of first n natural numbers using while loop*****\n")

num = int(input("Enter The Number : "))

for i in  range(num):
    print(" " * (num - i - 1), end = "")
    print("* " * (i+1), end = "")
    print(" " * (num - i - 1))














