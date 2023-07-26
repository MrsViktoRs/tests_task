import requests


def check_folder(name_folder):
    token = r'тут наш токен'
    url = r'https://cloud-api.yandex.net'
    headers = {"Content-Type": "application/json",
               "Authorization": token}
    params = {'path': name_folder}
    spell_url = r'/v1/disk/resources'
    method_url = url + spell_url
    res = requests.get(method_url, params=params, headers=headers)
    return res.status_code


def create_folder(name_folder):
    url = r'https://cloud-api.yandex.net'
    token = r'тут наш токен'
    headers = {"Content-Type": "application/json",
                "Authorization": token}
    params = {'path': name_folder}
    spell_url = r'/v1/disk/resources'
    method_url = url + spell_url
    res = requests.put(method_url, params=params, headers=headers)
    return res.status_code