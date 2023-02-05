# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x_oke = 1     #int
y_oke = 2.5   #float
name = 'OguzKagan'  #str
is_oke = True  #bool

# Multiple Assignment

x_oke, y_oke, name, is_oke = (1, 2.5, 'OguzKagan', True )

# Basic math

a_oke = x_oke + y_oke

print(x_oke, y_oke, name, is_oke, a_oke)

#Casting
x_oke = str(x_oke)
y_oke = int(y_oke)
z_oke = float(y_oke)

print(type(y_oke), y_oke)

print (type(z_oke), z_oke)