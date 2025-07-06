import uuid
import random

def stream_users():
    """
    A generator function that simulates fetching rows one by one from a
    'user_data' table.

    It uses the 'yield' keyword to return each user dictionary,
    making it memory efficient for large datasets.
    """
    # Simulate a large user_data table. In a real application, this would
    # involve querying a database (e.g., using a database cursor).
    # We'll generate a fixed number of dummy users for demonstration.
    num_users = 1000  # Simulate a large number of users

    # A single loop to iterate and yield each user
    for i in range(num_users):
        user_id = str(uuid.uuid4())
        name = f"User Name {i}"
        email = f"user{i}@example.com"
        age = random.randint(18, 120) # Simulate age

        user_data = {
            'user_id': user_id,
            'name': name,
            'email': email,
            'age': age
        }
        yield user_data

# Example of how it would be used (as seen in main.py):
# from itertools import islice
#
# # Create the generator object
# user_generator = stream_users()
#
# # Iterate over the generator function and print only the first 6 rows
# for user in islice(user_generator, 6):
#     print(user)
