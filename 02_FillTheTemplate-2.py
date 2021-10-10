'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
UserName = input("Enter the Name: ")
Date = input("Enter the Date: ")

letter = '''\nDear <|NAME|>
You Are Selected!
Date - <|DATE|>
'''
letter = letter.replace("<|NAME|>", UserName)
letter = letter.replace("<|DATE|>", Date)
print(letter)
