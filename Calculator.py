# A simple calculator program:

# add function adds two numbers.
def add (x,y):
    return x + y

# subtract function gives difference of two numbers.
def subtract (x,y):
    return x - y

# multiplication function gives product of two numbers.
def multiplication (x,y):
    return x * y

# divide function is used to divide two numbers.
def divide (x,y):
    return x / y

print ("Select operation.")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")

while True:
    # Take input from the user.
    choice = input ("Enter choice(1/2/3/4):")

    # Check if choice is among the options given.
    if choice in ('1','2','3','4'):
        num1 = float (input ("Enter first number: ") )
        num2 = float (input ("Enter second number: ") )

        if choice == '1':
            print (num1 , "+" , num2, "=" , add(num1,num2))
        elif choice == '2':
            print (num1 , "-" , num2, "=" , subtract(num1,num2))
        elif choice == '3':
            print (num1 , "*" , num2, "=" , multiplication(num1,num2))
        elif choice == '4':
            print (num1 , "/" , num2, "=" , divide(num1,num2))
        break
    else:
        print ("Invalid Input")
