# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create tuple

fruits_oke = ('Apples', 'Oranges', 'Grapes')
fruits2_oke = tuple(('Apple', 'Orange', 'Grapes'))

print(fruits2_oke, type(fruits2_oke))

# Single value needs trailing comma
fruits2_oke = ('Apples',)

# Get value

print(fruits_oke[1])

# Can't change value

#print fruits_oke[0] ='Pears'  Won't work

# Delete tuple

del fruits2_oke


# Get length

print (len(fruits_oke))

# Create set

fruits_set_oke = {'Apples', 'Oranges', 'Mango'}

# Check if in set

print('Apples' in fruits_set_oke)

# Add to set

fruits_set_oke.add('Grape')

# Remove from set

fruits_set_oke.remove ('Grape')

# Add duplicate

fruits_set_oke.add ('Apples')

# Clear set

fruits_set_oke.clear()

# Delete

del fruits_set_oke


# A Set is a collection which is unordered and unindexed. No duplicate members.
