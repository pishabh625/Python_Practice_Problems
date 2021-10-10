'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print ("\n*****Program to calculate the grade of a student from his marks*****\n")

# Taking Input From User 
Marks = int(input("Enter Your Marks : "))

if(Marks >= 90 and Marks <= 100):
    print("\nCongrats! Your Grade is : Excellent")
elif(Marks >= 80 and Marks <= 90):
    print("\nCongrats! Your Grade is : A")
elif(Marks >= 70 and Marks <= 80):
    print("\nCongrats! Your Grade is : B")
elif(Marks >= 60 and Marks <= 70):
    print("\nCongrats! Your Grade is : C")
elif(Marks >= 50 and Marks <= 60):
    print("\nCongrats! Your Grade is : D")
elif(Marks < 50):
    print("\nSorry! Your Grade is : Fail")
elif(Marks > 100):
    print("\nMarks Should Be less Then 100!")
    














