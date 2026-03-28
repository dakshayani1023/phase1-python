# Flow control

# if statement
name = 'Addison'
if name == 'Addison':
    print('Hello, Addison!')

name = 'Addison'
if name == 'Alex':
    print('Hello, Addison!') # This will not print anything because the condition is not met and the claue is skipped.

# else statement
name = 'Emma'
if name == 'Emma':
   print('Hi, Emma')
else:
   print('Hello, stranger')

name = 'Emma'
if name == 'Sarah':
   print('Hi, Emma')
else:
   print('Hello, stranger') # This will print 'Hello, stranger' because the condition is not met and the else clause is executed.

# elif statement
name = 'Liam'   
if name == 'Liam':
    print('Hi, Liam')
elif name == 'Olivia':
    print('Hi, Olivia')
elif name == 'Noah':
    print('Hi, Noah')
else:
    print('Hello, stranger') # This will print 'Hi, Liam' because the first condition is met and the corresponding clause is executed. The other conditions are not checked because the first condition was already satisfied.

name = 'Liam'
if name == 'Mason':
    print('Hi, Mason')
elif name == 'Liam':
    print('Hi, Liam')
elif name == 'Ethan':
    print('Hi, Ethan')
else:
    print('Hello, stranger') # This will print 'Hi, Liam' because the second condition is met and the corresponding clause is executed. The first condition is not met, so it is skipped. The third condition is not checked because the second condition was already satisfied.

# EXAMPLE - Using if, elif, and else statements to determine the type of a triangle based on the lengths of its sides.
side1 = 5
side2 = 5
side3 = 5
if side1 == side2 == side3:
    print('The triangle is equilateral.')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('The triangle is isosceles.')
else:
    print('The triangle is scalene.') # This will print 'The triangle is equilateral.' because all three sides are equal, satisfying the first condition. The other conditions are not checked because the first condition was already satisfied.

