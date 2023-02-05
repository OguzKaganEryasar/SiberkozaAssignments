# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers_oke = [1, 2, 3, 4, 5]
fruits_oke = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Use a constructor
numbers2_oke = list((1,2,3,4,5))

print(numbers_oke, numbers2_oke)
 
 # Get a value
print(fruits_oke[1])

 #get length
print(len(fruits_oke))

# Append to list
fruits_oke.append('Mangos')

print(fruits_oke)

# Remove from list

fruits_oke.remove('Grapes')

#Insert into position

fruits_oke.insert(2, 'Strawberries')

# Remove with pop
fruits_oke.pop(2)

# Reverse list
fruits_oke.reverse()

# Sort list
fruits_oke.sort()

# Reverse sort

fruits_oke.sort(reverse=True)

# Change value
fruits_oke[0] = 'Blueberries'

print(fruits_oke)

