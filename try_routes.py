# Sends four requests to your app, the way a member's phone would, and prints what each one answers. Ready to use.
# Run it with: python try_routes.py   (no server needed: TestClient hands each request straight to your app)
from fastapi.testclient import TestClient

from main import app

client = TestClient(app, raise_server_exceptions=False)

print("Chapter & Verse: what the app answers")
for path in ["/books", "/books/2", "/books/42", "/books/abc"]:
    response = client.get(path)
    print()
    print("GET", path, "->", response.status_code)
    print(response.text)
