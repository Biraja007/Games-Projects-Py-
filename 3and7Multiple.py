#check if number is multiple of 3
#6%3=0;10%3=2
print('Enter a number')
number=int (input())
if number % 3 == 0:
    print('Number is a multiple of 3')
    if number % 7 == 0:
        print('Number is multiple of 7')
    else:
        print('Number is multiple of 3,but not of 7')
else:
    print ("Number is neither a multiple of 3 nor a multiple of 7")
