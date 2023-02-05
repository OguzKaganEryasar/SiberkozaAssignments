# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function

def sayHello_oke(name_oke= 'OguzKagan'):
    print(f'Hello {name_oke}')

sayHello_oke()

#Return values

def getSum_oke(num1_oke, num2_oke):
    total_oke = num1_oke + num2_oke
    return total_oke

num_oke = getSum_oke(3,4)
print(num_oke)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum_oke = lambda num1_oke, num2_oke: num1_oke + num2_oke

print (getSum_oke(11,4))