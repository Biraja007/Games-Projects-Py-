import random

# A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program: {chr() is used for ASCII code}
Uppercase=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
LowerCase=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
Number=chr(random.randint(48,57)) #Generate a random Number (based on ASCII code)
Symbols=chr(random.randint(33,64)) #Generate a random Symbols(based on ASCII code)

#Generating the password  in random order:
password = Uppercase + LowerCase + Number + Symbols # + ....
password = shuffle(password)

# For Printing Ouput:
print(password)
