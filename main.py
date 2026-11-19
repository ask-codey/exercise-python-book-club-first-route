# Chapter & Verse Book Club's API: the club's books, as JSON. For you to finish.
# Run it with: fastapi dev main.py   (then open http://127.0.0.1:8000/docs, and press Ctrl+C to stop it)
from fastapi import FastAPI, HTTPException

app = FastAPI()

# The club's books: the ones it has read, and the one it's reading now. Ready to use; don't change it.
BOOKS = [
    {"id": 1, "title": "The Lantern Keeper's Cat", "pages": 312, "status": "read"},
    {"id": 2, "title": "Twelve Bridges North", "pages": 284, "status": "read"},
    {"id": 3, "title": "Rain over Copper Hill", "pages": 356, "status": "read"},
    {"id": 4, "title": "The Orchard Ledger", "pages": 241, "status": "reading"},
]


def list_books():
    """Answer GET /books with every book in BOOKS, in the order they're listed.

    Tie this function to GET /books with a decorator line right above it.

    GET /books -> 200, a JSON list of all 4 books, The Lantern Keeper's Cat first
    """
    raise NotImplementedError("Not built yet.")


def get_book(book_id):
    """Answer GET /books/{book_id} with the one book whose "id" is book_id.

    Tie this function to GET /books/{book_id} with a decorator line right above it, and give
    book_id the type hint int, so FastAPI turns the "2" in the address into the number 2.
    When no book has that id, raise HTTPException with the status code 404 and the detail
    "Book not found".

    GET /books/2   -> 200, {"id": 2, "title": "Twelve Bridges North", "pages": 284, "status": "read"}
    GET /books/42  -> 404, {"detail": "Book not found"}
    GET /books/abc -> 422  (FastAPI answers this one for you, once book_id has its type hint)
    """
    raise NotImplementedError("Not built yet.")
