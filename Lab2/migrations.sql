-- migrations.sql

CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    pages INTEGER NOT NULL,
    reader_id INTEGER,
    FOREIGN KEY(reader_id) REFERENCES readers(id)
);

CREATE TABLE IF NOT EXISTS subscriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reader_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    max_pages INTEGER,
    FOREIGN KEY(reader_id) REFERENCES readers(id)
);
