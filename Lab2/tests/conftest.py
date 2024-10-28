import pytest
import sqlite3
import os

DATABASE_PATH = os.getenv("DATABASE_PATH", "data/library.db")

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATABASE_PATH):
        conn = sqlite3.connect(DATABASE_PATH)
        with open("migrations.sql", "r") as f:
            conn.executescript(f.read())
        conn.close()

@pytest.fixture(autouse=True)
def clear_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM readers")
    cursor.execute("DELETE FROM books")
    cursor.execute("DELETE FROM subscriptions")
    conn.commit()
    conn.close()
