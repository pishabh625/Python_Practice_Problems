'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print ("\n*****Program to greet all the person names stored in a list L1 and which starts with S*****\n")

n = int(input("Enter The Number : "))
isPrime = True
for i in range(2, n):
    if(n%i == 0):
        isPrime = False
        break

if(isPrime == True):
    print("\n*****This Number Is Prime Number*****")
else:
    print("\n*****This Number Is Not Prime Number*****")













