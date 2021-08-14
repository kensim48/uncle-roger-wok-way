import requests
import json
import random

url = "http://localhost:8000/auth/jwt/create/"

payload = "{\r\n    \"username\":\"admin\",\r\n    \"password\":\"password\"\r\n}"
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)

access_token = json.loads(response.text)["access"]

item_names = ["Beef Kway Teow", "Beef noodle soup", "Mee pok", "Banmian", "Char kway teow", "Crab been hoon", "Fish soup bee hoon", "Hokkien mee", "Kwetiau goreng", "Shredded chicken noodles", "Vegetarian bee hoon", "Mee rebus", "Mee siam", "Mee soto", "Katong Laksa", "Mee goreng", "Satay bee hoon", "Name", "Hainanese Curry Rice", "Bak kut teh", "Chai tow kway", "Drunken prawn", "Char siu", "Duck rice", "Har Cheong Gai", "Pig's brain soup",
              "Pig fallopian tubes", "Pig's organ soup", "Sliced fish soup", "Teochew Porridge", "Turtle soup", "Assam pedas", "Ayam penyet", "Dendeng paru", "Gudeg Putih", "Gulai daun ubi", "Lemak siput", "Nasi goreng", "Satay", "Sayur lodeh", "Soto", "Soto ayam", "Soup kambing", "Soup tulang", "Fish head curry", "Kari lemak ayam", "Kari debal", "Cereal prawns", "Black pepper crab", "Chilli crab", "Oyster omelette", "Hainanese chicken rice"]

url = "http://localhost:8000/api/item_modify/"

for item_name in item_names:
    payload = json.dumps({
        "name": item_name,
        "price": random.uniform(1, 20),
        "serial_id": str(random.random())
    })
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
