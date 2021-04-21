import requests


class ProductConfig:
    url = "http://192.168.101.34:8080"


class HTTPConfig:
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6',
    }
    S = requests.Session()
    S.headers = headers


class EnvConfig:
    pass
