📚 Library Management System (Python)

A simple Library Management Program built in Python that uses text files for storage.
This project allows you to manage books easily from the terminal/console without any database.

✨ Features

➕ Add Book – Add new books with author names.

📖 View Books – Display all available books in the library.

🔍 Search Book – Find books by title.

📤 Issue Book – Issue a book (moves it from bookshelf to issued list).

📥 Return Book – Return a previously issued book.

❌ Delete Book – Remove unwanted books from the library.

🚫 Error Handling – Gracefully handles wrong inputs & empty files.


🛠 How It Works

bookshelf.txt → Stores all available books.

issued.txt → Stores all issued books.

Data is saved in plain text (no database required).


📌 Requirements

Python 3.10+ (uses match-case syntax)

Works on Windows, Linux, macOS


▶️ Usage

Run the program in your terminal:

python library.py

📈 Future Improvements

Prevent duplicate entries.

Fuzzy search for typos (e.g., "harry poter" → "harry potter").

Track users who issue books.
