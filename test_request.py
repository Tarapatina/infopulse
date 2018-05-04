import requests

url = 'http://httpbin.org/get'
payload = {'key1': 'value1'}
r = requests.get(url, params=payload)
print(r.text)

to_dict = r.json()
print(type(to_dict))
print(to_dict['headers'])
print(to_dict['headers']['User-Agent'])