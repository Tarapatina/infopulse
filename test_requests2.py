import requests
r = requests.get('https://api.github.com/events')
c = r.content #выводит HTML страницы
print(c)