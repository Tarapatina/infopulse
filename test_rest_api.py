import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'
# role_dict ={
#     'name': "Mimi",
#     'type': "classic",
#     'level': 8,
#     'book': 3
# }

resp = requests.put(base_url+'roles/10')#, data=role_dict)

req_dict = resp.json()
print (req_dict)
#print ( req_dict['id'],req_dict['name'])
