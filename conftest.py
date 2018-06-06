import pytest
import requests

# @pytest.fixture
# def fixt1():
#     print("\nInitialization of fixture")
#     fixture = "I am a fixture"
#     yield fixture
#     print("\nDestroying of fixture")
import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"



books = [
            {"title": "sdgfs", "author": "sdfds     "},
            {"title": "$%^&%&", "author": "sdfds"},
            {"title": "234234", "author": "243324"}
        ]


@pytest.fixture(params=books, ids=[str(b) for b in books])
def book(base_url, request):
    book_data = request.param
    yield book_data
    if "id" in book_data.keys():
        requests.delete(base_url + 'books/' + str(book_data["id"]))


def book_init(base_url):
    book_data = {"title": "$%^&%&", "author": "sdfds"}
    r = requests.post(base_url + 'books/', data=book_data)
    book_data = r.json()
    yield book_data
    if "id" in book_data.keys():
        requests.delete(base_url + 'books/' + str(book_data["id"]))



