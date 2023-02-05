# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
# from camelcase  import CamelCase

# Import custom module
import validator
from validator import validate_email

# today_oke = datetime.date.today()
today_oke = date.today()
timestamp_oke = time()

#c_oke = CamelCase()
# print(c_oke.hump('hello there world'))

email_oke = '210201016@ostimteknik.edu.tr'
if validate_email(email_oke):
  print('Email is valid')
else:
  print('Email is bad')