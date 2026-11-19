# Your own tests: write the body of each one (step 3 in the README). For you to finish.
# Each test sends a request with client.get, then checks the response's status_code and its .json(), the way
# test_books.py does. Run them with: pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_8_get_book_3_is_rain_over_copper_hill():
    """GET /books/3 answers with the status code 200, and the book's "title" is "Rain over Copper Hill"."""
    raise NotImplementedError("Not built yet: write this test.")


def test_9_get_book_99_answers_404_book_not_found():
    """GET /books/99 answers with the status code 404, and its JSON is {"detail": "Book not found"}."""
    raise NotImplementedError("Not built yet: write this test.")
