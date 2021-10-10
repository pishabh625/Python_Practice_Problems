'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print ("\n*****Program to Find The Greatest Number In 4 Numbers Entered By User*****\n")

# Taking Input From User 
sub1 = int(input("Enter The Marks of Subject 1 : "))
sub2 = int(input("Enter The Marks of Subject 2 : "))
sub3 = int(input("Enter The Marks of Subject 3 : "))

# Comparing 1st and 2nd Number
if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("\n*****You Are Fail!*****")

elif((sub1+sub2+sub3)/3 < 40):
    print("\n*****You Are Fail Due To Your Percentage Is Less Than 40%*****")
else:
    print("\n*****Congrats! You Are Passed*****")
    














