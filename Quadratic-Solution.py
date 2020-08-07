# Solving the quadratic equation ax**2 + bx + c = 0.
print ('Quadratic equations are of form : [ax**2 + bx + c = 0] ')

# import complex math module.
import cmath
print ('Enter value of a:')
a = int(input())
print ('Enter value of b:')
b = int(input())
print ('Enter value of b:')
c = int(input())

# Calculating the discriminant (d):
d = (b**2) - (4*a*c)

# Finding two solutions:
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
