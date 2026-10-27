# LoginSystem-Python
This is a Python-based authentication system that allows users to register and log in through a command-line interface. The project uses Flask to build a backend API, MySQL to store user information, and secure password hashing to protect stored credentials. 


# Features

User Registration: Creates new user accounts and prevents duplicate usernames.

User Login: Verifies user credentials against records stored in the database.

Password Hashing: Uses Werkzeug's password-hashing utilities to store password hashes instead of plaintext passwords.

REST-Style API: Uses Flask to handle HTTP POST requests and exchange JSON data between the client and server.

MySQL Integration: Stores and retrieves user information using SQL queries.

Parameterized Queries: Uses parameterized SQL statements to help prevent SQL injection.

JSON Responses: Returns structured success and error messages for authentication operations.

Command-Line Interface: Provides a simple interactive menu for registration, login, and exit.

# Learning Objectives

This project explores client-server architecture, backend API development, relational database integration, HTTP communication, password hashing, and basic authentication security practices.
