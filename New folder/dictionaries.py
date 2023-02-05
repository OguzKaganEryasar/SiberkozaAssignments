# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#Create dict

person_oke = {
    'first_name_oke': 'OguzKagan',
    'last_name_oke': 'Eryasar',
    'age_oke': 19
}
print(person_oke, type(person_oke))


#Use constructor

#person2_oke = dict(first_name_oke= 'OguzKagan', last_name_oke='Eryasar')

# Get value

print(person_oke['first_name_oke'])
print(person_oke.get('last_name_oke'))

#Add key/value

person_oke['phone'] = '0505 050 50 50'

# Get dict keys

print(person_oke.keys())

# Get dict items

print(person_oke.items())

#Copy dict

person2_oke = person_oke.copy()

person2_oke['city'] = 'Ankara'

print(person2_oke)

#Remove item

del(person_oke['age_oke'])
person_oke.pop('phone')

print(person_oke)

#Clear

person_oke.clear()

#Get length

print(len(person2_oke))

print(person_oke)

#List of dict

people_oke =[
    {'name_oke': 'OguzKagan', 'age_oke': 19},
    {'name_oke': 'Ulas', 'age_oke':19}
]

print(people_oke[1] ['name_oke'])