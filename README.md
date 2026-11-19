# Exercise: Book Club's First Route

Exercise code for the lesson **Exercise: Book Club's First Route** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

Chapter & Verse, a book club, wants an app that shows its books. You'll write the API behind it with FastAPI: one route that answers with every book, and one that answers with a single book by its number, or a 404 when there's no such book. Then you'll write two tests of your own that prove it.

## What's here

- `main.py`: the app, with the club's four books in `BOOKS` and two functions, `list_books` and `get_book`. Each one stops with `NotImplementedError: Not built yet.` for now, and neither is tied to an address yet. The docstring under each says what it should answer, with examples. For you to finish.
- `tests/test_books.py`: seven tests that send requests to your app and check what comes back. You don't need to change this file.
- `tests/test_your_tests.py`: two tests for you to write. Each one's docstring says what it checks. For you to finish.
- `try_routes.py`: sends four requests to your app and prints each answer, so you can see it at work. Ready to use.
- `requirements.txt`: the packages the app and the tests need, at exact versions: FastAPI with its standard extras (including the Uvicorn server, the `fastapi` command and httpx2, which TestClient uses), httpx and pytest. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `main.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The app and the tests need packages, and they go in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it. FastAPI brings a few packages of its own, so it takes a minute.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because neither function is tied to an address yet, and your two tests aren't written. A failing test in `test_books.py` says what it asked for, what it expected and what came back, for example *GET /books (status code) should answer 200, but it answered 404.*

To see your app's answers, run:

```bash
python try_routes.py
```

To try it in your browser, start the app with `fastapi dev main.py`, open `http://127.0.0.1:8000/docs`, and use **Try it out** on each route. Press **Ctrl+C** in the terminal to stop the app.

## The rules

- `GET /books` answers with every book in `BOOKS`, in the order they're listed.
- `GET /books/{book_id}` answers with the one book whose `"id"` is `book_id`. `book_id` has the type hint `int`.
- A `book_id` that no book has gets the status code 404 and the JSON `{"detail": "Book not found"}`, from `HTTPException`.
- Keep the function names, `BOOKS` and the addresses as they are. Don't change `test_books.py` or `try_routes.py`.
- Each of your two tests sends its request with `client.get` and checks both the status code and the JSON, as its docstring says.

## Tips

- A route is a decorator line right above a function: `@app.get("/books")` ties the function below it to GET requests for `/books`.
- The function returns the data, and FastAPI turns it into JSON. A list of dictionaries is fine as it is.
- In `/books/{book_id}`, the name in the braces must match the function's parameter name.
- Without the type hint, `book_id` arrives as the text `"2"`, which never equals the number `2`.
- A loop over `BOOKS` can return the book as soon as its `"id"` matches. If the loop ends without a match, raise the `HTTPException`.
- Your tests look like the tests in `test_books.py`: send the request, then `assert` the status code and the JSON.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
