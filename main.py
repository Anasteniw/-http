
# Задача№1

import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
heroes = resp.json()
intelligence_list = ['Hulk', 'Captain America', 'Thanos']
heroes_dict ={hero['name']:hero['powerstats']['intelligence'] for hero in heroes}
dict_filter = {}
for name, intellige in heroes_dict.items():
    if name in intelligence_list:
        dict_filter[name] = intellige
best_hero =max(dict_filter, key=dict_filter.get)
print(best_hero)


# Задача №2

TOKEN = '......'
token =TOKEN
class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite":"true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload_file_to_disk (self, disk_file_path, filename):
        result =self._get_upload_link(disk_file_path=disk_file_path)
        href = result.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    ya = YandexDisk(token)
    ya.upload_file_to_disk("netology", "archery.jpg")


