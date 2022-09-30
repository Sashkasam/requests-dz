
import yadisk
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

# Вариант решения № 1 только с помощью библиотеки requests
class Yandexloader:
    def __init__(self,token : str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def uploader_file(self, file_path : str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        filename = file_path.split("/")[-1]
        headers = self.get_headers()
        params = {"path": filename, "overwrite": "true"}
        _response = requests.get(url, headers=headers, params=params).json()
        href = _response.get("href", "")
        response = requests.put(href, data=open(file_path, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл успешно загружен")


# Вариант решения № 2 с помощью библиотеки yadisk
user_token = input("Введите свой токен от яндекс диска: ")
path_to_file = "C:/Users/boss/Desktop/my photo/family.JPG"
file_name = path_to_file.split('/')[-1]
my_disk = yadisk.YaDisk(token = user_token)
with open(path_to_file, "rb") as file:
    my_disk.upload(file,file_name)

# Задача № 3
def question_tag_python():
    url = "https://api.stackexchange.com/2.3/questions?fromdate=1664323200&order=desc&max=1664496000&order=desc&sort=activity&tagged=Python&site=stackoverflow"
    response = requests.get(url)
    response.raise_for_status()
    result = response.json()
    pprint(result)

if __name__ == '__main__':
    path_to_file = "C:/Users/boss/Desktop/my photo/family.JPG"
    token = input("Введите свой токен от яндекс-диска: ")
    uploader = Yandexloader(token)
    result = uploader.uploader_file(path_to_file)
    print(result)
    question_tag_python()



















   

