About the Project
This project introduces advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations. The tasks focus on leveraging Python’s yield keyword to implement generators that provide iterative access to data, promoting optimal resource utilization, and improving performance in data-driven applications.

Learning Objectives
By completing this project, you will:

Master Python Generators: Learn to create and utilize generators for iterative data processing, enabling memory-efficient operations.
Handle Large Datasets: Implement batch processing and lazy loading to work with extensive datasets without overloading memory.
Simulate Real-world Scenarios: Develop solutions to simulate live data updates and apply them to streaming contexts.
Optimize Performance: Use generators to calculate aggregate functions like averages on large datasets, minimizing memory consumption.
Apply SQL Knowledge: Use SQL queries to fetch data dynamically, integrating Python with databases for robust data management.
Requirements
Proficiency in Python 3.x.
Understanding of yield and Python’s generator functions.
Familiarity with SQL and database operations (MySQL and SQLite).
Basic knowledge of database schema design and data seeding.
Ability to use Git and GitHub for version control and submission.
0. Getting started with python generators
mandatory
Objective: create a generator that streams rows from an SQL database one by one.

Instructions:

Write a python script that seed.py:
1. generator that streams rows from an SQL database
mandatory
Objective: create a generator that streams rows from an SQL database one by one.

Instructions:

In 0-stream_users.py write a function that uses a generator to fetch rows one by one from the user_data table. You must use the Yield python generator

Prototype: def stream_users()
Your function should have no more than 1 loop

2. Batch processing Large Data
mandatory
Objective: Create a generator to fetch and process data in batches from the users database

Instructions:

Write a function stream_users_in_batches(batch_size) that fetches rows in batches

Write a function batch_processing() that processes each batch to filter users over the age of25`

You must use no more than 3 loops in your code. Your script must use the yield generator

Prototypes:

def stream_users_in_batches(batch_size)
def batch_processing(batch_size)
3. Lazy loading Paginated Data
mandatory
Objective: Simulte fetching paginated data from the users database using a generator to lazily load each page

Instructions:

Implement a generator function lazypaginate(pagesize) that implements the paginate_users(page_size, offset) that will only fetch the next page when needed at an offset of 0.

You must only use one loop
Include the paginate_users function in your code
You must use the yield generator
Prototype:
def lazy_paginate(page_size)
4. Memory-Efficient Aggregation with Generators
mandatory
Objective: to use a generator to compute a memory-efficient aggregate function i.e average age for a large dataset

Instruction:

Implement a generator stream_user_ages() that yields user ages one by one.

Use the generator in a different function to calculate the average age without loading the entire dataset into memory

Your script should print Average age of users: average age

You must use no more than two loops in your script

You are not allowed to use the SQL AVERAGE


