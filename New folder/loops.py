# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_oke = ['OguzKagan', 'Ulas', 'Caka', 'Fuat']

# Simple for loop
for person_oke in people_oke:
  print(f'Current Person: {person_oke}')

# Break
for person_oke in people_oke:
  if person_oke == 'Caka':
    break
  print(f'Current Person: {person_oke}')

# Continue
for person in people_oke:
  if person == 'Caka':
    continue
  print(f'Current Person: {person_oke}')

# range
for i in range(len(people_oke)):
  print(people_oke[i])

for i in range(0, 7):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_oke = 0
while count_oke < 7:
  print(f'Count: {count_oke}')
  count_oke += 1