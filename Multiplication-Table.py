# Multiplication table using Python:
num = int(input("Enter number for desired Multiplication Table: "))
# It takes input from the user.

print ("The table of", num , "is:")
print()

# Iterate 10 times from i = 1 to 10
for a in range(1, 11):
   print(num, '*', a, '=', num*a)
