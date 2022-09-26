
import requests
from pprint import pprint

# Задача № 1 Кто самый умный супергерой?

response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json").json()

heroes_list = ["Hulk", "Captain America", "Thanos"]
new_dict = {}
for all_heroes in response:
    if all_heroes['name'] in heroes_list:
        new_dict[all_heroes['name']] = all_heroes['powerstats']['intelligence']



print(f'Самый умный это {max(new_dict.keys())} у него {max(new_dict.values())}  интеллекта')


# Задача № 2 