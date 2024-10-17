import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Commit the changes
conn.commit()

# Function to create a new user
def create_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

# Function to read all users
def read_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Function to update a user
def update_user(user_id, name, age):
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
    conn.commit()

# Function to delete a user
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

# Example usage
if __name__ == '__main__':
    # Create users
    create_user('Alice', 30)
    create_user('Bob', 25)

    # Read users
    print("Users:")
    for user in read_users():
        print(user)

    # Update a user
    update_user(1, 'Alice Smith', 31)

    # Read users after update
    print("\nUsers after update:")
    for user in read_users():
        print(user)

    # Delete a user
    delete_user(2)

    # Read users after deletion
    print("\nUsers after deletion:")
    for user in read_users():
        print(user)

# Close the connection
conn.close()
