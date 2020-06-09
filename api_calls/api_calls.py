# https://restcountries.eu/#api-endpoints-all

import requests

r = requqests.get('https://restcountries.eu/#api-endpoints-all')

#Use json decoder to decode the response
resp = r.json()

for item in resp:
  print(f"Country: {item['name']})
  print(f"Country: {item['region']})
  print(f"Country: {item['capital']})
  print(20 * '-')
  
#Listcomp used to filter out specific records 
[item for item in resp if item['name'] == 'Poland'] 
  
  
