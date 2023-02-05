# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_oke= 'OguzKagan'
age_oke= 19

# Concatenate
print ('Hello, my name is ' + name_oke + 'and I am ' + str(age_oke))

# String Formatting


#Arguments by position
print('My name is {name_oke} and I am {age_oke}'.format(name_oke =name_oke, age_oke = age_oke))

#F-Strings
print(f'Hello, my name is {name_oke} and I am {age_oke}')
# String Methods

s_oke = 'hello world'

# Capitalize string

print(s_oke.capitalize())

# Make all lower
print(s_oke.lower())

# Swap case
print(s_oke.swapcase())

# Get length
print(len(s_oke))

# Replace
print(s_oke.replace('world', 'everyone'))

# Count
sub_oke ='h'
print(s_oke.count(sub_oke))

# Starts with
print(s_oke.startswith('hello'))

# Ends with
print(s_oke.endswith('d'))

# Split into a list

print(s_oke.split())

# Find position

print(s_oke.find('r'))

# Is all alphanumeric

print(s_oke.isalnum())

# Is all alphabetic

print(s_oke.isalpha())

# Is all numeric
print (s_oke.isnumeric())