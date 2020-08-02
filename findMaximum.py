def findMax(firstNumber,secondNumber):
    if firstNumber > secondNumber:
        print('First Number is greater')
        return firstNumber
    elif secondNumber>firstNumber:
        print('Second Number is greater')
        return secondNumber
    else:
        print('Both numbers are equal')
        return firstNumber

print('Enter the first number:')
firstNumber=int (input())
print('Enter the second number:')
secondNumber= int (input())
MaxNumber= findMax(firstNumber,secondNumber)
print('Maximun number = {}'.format(MaxNumber))
