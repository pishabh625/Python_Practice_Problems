'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print ("\n*****Program to Check Whether The Given Text Is Spam Or Not*****\n")

# Taking Input From User 
text = input("Enter The comment : ")
isSpam = False


if("buy now" in text):
    isSpam = True
elif("make a lot of money" in text):
    isSpam = True
elif("subscribe this" in text):
    isSpam = True
elif("click this" in text):
    isSpam = True

if(isSpam == True):
    print("\n*****This Is An Spam comment !!!*****")
else:
    print("\n*****This Is Not An Spam comment*****")
    














