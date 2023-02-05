# If/ Else conditions are used to decide to do something based on something being true or false

x_oke =11
y_oke =4





# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
#Simple if
if x_oke > y_oke:
    print(f'{x_oke} is greater than {y_oke}')

#If/else

if x_oke > y_oke:
    print(f'{x_oke} is greater than {y_oke}')

else:
    print(f'{y_oke} is greater than {x_oke}')

#elif

if x_oke > y_oke:
    print(f'{x_oke} is greater than {y_oke}')

elif x_oke == y_oke:
    print(f'{x_oke} equal to {y_oke}')

else: 
    print(f'{y_oke} is greater than {x_oke}')

#Nested if

if x_oke > 3:
    if x_oke<=9:
        print(f'{x_oke} is greater than 3 or less than or equal to 9')


# Logical operators (and, or, not) - Used to combine conditional statements


# and
if x_oke > 3 and x_oke <= 9:
    print(f'{x_oke} is greater than 3 and less than or equal to 9')

#or
if x_oke > 3 or x_oke <= 9:
    print(f'{x_oke} is greater than 3 or less than or equal to 9')

#not

if not(x_oke == y_oke):
    print(f'{x_oke} is not equal to {y_oke}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_oke = [1,2,3,4,5]

# in 
if x_oke in numbers_oke:
    print(x_oke in numbers_oke)

# not in
if x_oke not in numbers_oke:
    print(x_oke not in numbers_oke)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_oke is y_oke:
    print(x_oke is y_oke)
# is not
if x_oke is not y_oke:
    print(x_oke is not y_oke)