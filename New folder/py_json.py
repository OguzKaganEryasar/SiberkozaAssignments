# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

#  Sample JSON
userJSON_oke = '{"first_name": "Oguz Kagan", "last_name": "Eryasar", "age": 19}'

# Parse to dict
userJSON_oke = json.loads(userJSON_oke)

# print(user_oke)
# print(user_oke['first_name'])

car_oke = {'make': 'Volkswagen', 'model': 'Golf', 'year': 2011}

car_okeJSON = json.dumps(car_oke)

print(car_okeJSON)