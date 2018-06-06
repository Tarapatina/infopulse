
# import requests
#
# def test_create_book_positive(base_url,book):
#         response = requests.post(base_url + "books/", data=book)
#         assert response.status_code==201
#         body = response.json()
#         for key in book:
#             assert book[key].strip()== body[key]
#         book['id'] = body['id']
#         # TODO GET запросы
#         response2=requests.get(base_url+ "books/"+ str(body['id']))
#         assert response2.status_code==200
import requests


def test_create_book_positive(base_url, book):
    response = requests.post(base_url + "books/", data=book)
    assert response.status_code == 201
    body = response.json()
    for key in book:
        assert book[key].strip() == body[key]
    book["id"] = body["id"]
    response2 = requests.get(base_url + 'books/' + str(body["id"]))
    assert response2.status_code == 200

    # TODO GET запрос все книги

def test_update_book(base_url, book):
    pass