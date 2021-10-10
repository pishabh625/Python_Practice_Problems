'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print ("\n*****Program To Sort Marks Of Student Given By User*****\n")

mr1 = int(input("Enter The Marks of Student Number 1 : "))
mr2 = int(input("Enter The Marks of Student Number 2 : "))
mr3 = int(input("Enter The Marks of Student Number 3 : "))
mr4 = int(input("Enter The Marks of Student Number 4 : "))
mr5 = int(input("Enter The Marks of Student Number 5 : "))
mr6 = int(input("Enter The Marks of Student Number 6 : "))

StdMarks = [mr1, mr2, mr3, mr4, mr5, mr6]
StdMarks.sort()
print("\nThe Sorted Marks Of Students is : ",StdMarks)