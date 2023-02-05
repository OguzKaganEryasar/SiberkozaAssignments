# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object



# Create class
class User_oke:
  # Constructor
  def __init__(self_oke, name_oke, email_oke, age_oke):
    self_oke.name_oke = name_oke
    self_oke.email_oke = email_oke
    self_oke.age_oke = age_oke

  def greeting_oke(self_oke ):
    return f'My name is {self_oke.name_oke} and I am {self_oke.age_oke}'

  def has_birthday_oke(self_oke):
    self_oke.age_oke += 1


# Extend class
class Customer_oke(User_oke):
  # Constructor
  def __init__(self_oke, name_oke, email_oke, age_oke):
    self_oke.name = name_oke
    self_oke.email = email_oke
    self_oke.age = age_oke
    self_oke.balance_oke = 0

  def set_balance(self_oke, balance_oke):
    self_oke.balance_oke = balance_oke

  def greeting(self_oke):
    return f'My name is {self_oke.name_oke} and I am {self_oke.age_oke} and my balance is {self_oke.balance_oke}'

#  Init user object
OguzKagan =  User_oke('Oguz Kagan Eryasar', '210201016@ostimteknik.edu.tr', 19)
# Init customer object
Ulas = Customer_oke('Ulas Sivelek', '55555555@hotmail.com', 19)

Ulas.set_balance_oke(500)
print(Ulas.greeting_oke())

OguzKagan.has_birthday_oke()
print(OguzKagan.greeting_oke())