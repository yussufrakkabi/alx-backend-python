import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # Open the connection
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor  # So you can use it directly in the with-block

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit if no exception, then close
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            self.connection.close()


with DatabaseConnection("example.db") as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO users (name) VALUES ('Bob')")

# Run the SELECT query using the context manager
with DatabaseConnection("example.db") as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print("Users:")
    for row in results:
        print(row)
