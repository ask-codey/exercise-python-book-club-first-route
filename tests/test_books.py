# Tests for main.py's two routes. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test sends one request to your app with TestClient (no server needed) and checks the status code or the JSON
# that comes back. A failing test says what it asked for, what it expected and what came back.
# You don't need to change this file.
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def check(request, got, expected):
    """Fails with a message that says what the request answered and what it should answer."""
    assert got == expected, f"{request} should answer {expected!r}, but it answered {got!r}."


def test_1_get_books_answers_200():
    response = client.get("/books")
    check("GET /books (status code)", response.status_code, 200)


def test_2_get_books_answers_all_4_books():
    response = client.get("/books")
    check("GET /books (how many books)", len(response.json()), 4)


def test_3_get_books_lists_the_lantern_keepers_cat_first():
    response = client.get("/books")
    check("GET /books (the first book)", response.json()[0],
          {"id": 1, "title": "The Lantern Keeper's Cat", "pages": 312, "status": "read"})


def test_4_get_book_2_answers_200_with_twelve_bridges_north():
    response = client.get("/books/2")
    check("GET /books/2 (status code)", response.status_code, 200)
    check("GET /books/2", response.json(),
          {"id": 2, "title": "Twelve Bridges North", "pages": 284, "status": "read"})


def test_5_get_book_4_is_the_orchard_ledger_being_read_now():
    response = client.get("/books/4")
    check("GET /books/4 (status code)", response.status_code, 200)
    check("GET /books/4", response.json(),
          {"id": 4, "title": "The Orchard Ledger", "pages": 241, "status": "reading"})


def test_6_get_book_42_answers_404_book_not_found():
    response = client.get("/books/42")
    check("GET /books/42 (status code)", response.status_code, 404)
    check("GET /books/42", response.json(), {"detail": "Book not found"})


def test_7_get_book_abc_answers_422():
    response = client.get("/books/abc")
    check("GET /books/abc (status code)", response.status_code, 422)
