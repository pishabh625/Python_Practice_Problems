'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print ("\n*****Program to Find The Greatest Number In 4 Numbers Entered By User*****\n")

# Taking Input From User 
n1 = int(input("Enter The Number 1 : "))
n2 = int(input("Enter The Number 2 : "))
n3 = int(input("Enter The Number 3 : "))
n4 = int(input("Enter The Number 4 : "))

# Comparing 1st and 2nd Number
if(n1>n2):
    g1 = n1
else:
    g1 = n2

# Comparing 3rd and 4th Number
if(n3>n4):
    g2 = n3
else:
    g2 = n4

# Comparing g1 and g2
if(g1 > g2):
    print("\nThe Greatest Number Is : ",g1)
else:
    print("\nThe Greatest Number Is : ",g2)
    














