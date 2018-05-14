import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'
role_dict = {
    'name': "Mimi",
    'type': "classicc",
    'level': 1,
    'book': 2
}

resp = requests.post(base_url+'roles/', data = role_dict)

req_dict = resp.json()
print (req_dict)
print ( req_dict['id'],req_dict['name'])
