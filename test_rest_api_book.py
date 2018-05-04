import requests

base_url = 'http://pulse-rest-testing.herokuapp.com/'


role_dict ={
    'title': 'Python',
    'author': 'me'
}
resp = requests.get(base_url+ 'books/', data = role_dict)

req_dict = resp.json()
print (req_dict)
#print (req_dict['id'],req_dict['title'])