import requests


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}



url = 'https://5ka.ru/api/v2/special_offers/'
response = requests.get(url, headers=headers)

with open('5ka.html', 'w', encoding='UTF-8') as file:
    file.write(response.text)