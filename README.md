```
(venv) ➜  test python3.12 test_viz36.py
Connection Successful
Database cleared.
Database initialized with constraints.
index.php
Extracting data: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 2839.75it/s]
Querying for nodes...
Node response is not JSON formatted. Attempting plain-text parsing.
Error querying GraphRAG: name 'edge_response' is not defined
Final Nodes: []
Final Edges: []
Graph data successfully pushed to Neo4j.
Database.php
Extracting data: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 6413.31it/s]
Querying for nodes...
Node response is not JSON formatted. Attempting plain-text parsing.
Error parsing line: - PDO: A PHP Data Object for database interaction., Error: list index out of range
Error parsing line: - PDOEXCEPTION: Exception class for PDO errors., Error: list index out of range
Error parsing line: - LOGIN: A method to authenticate user login., Error: list index out of range
Error parsing line: - QUERY: SQL query to select user information., Error: list index out of range
Error parsing line: - DATABASE: A class that represents a database connection., Error: list index out of range
Error parsing line: - USER: A class responsible for user operations., Error: list index out of range
Error parsing line: - USERS: The table name in the database., Error: list index out of range
Error parsing line: - STMT: Prepared statement object., Error: list index out of range
Error parsing line: - PASSWORD: The password input by the user., Error: list index out of range
Error parsing line: - USERNAME: The username input by the user., Error: list index out of range
Error parsing line: - POST: The type of HTTP request method used to submit the form., Error: list index out of range
Error parsing line: - INDEX.PHP: The filename where the form data is submitted., Error: list index out of range
Error parsing line: - TEST: The name of the database., Error: list index out of range
Error parsing line: - CONNECTION: Method that establishes a connection to the database., Error: list index out of range
Error parsing line: - EMPTY STRING: The password for database access., Error: list index out of range
Error parsing line: - LOCALHOST: The hostname for the local server., Error: list index out of range
Error parsing line: - CONN: Database connection object., Error: list index out of range
Error parsing line: - ROOT: The username for database access., Error: list index out of range
Error querying GraphRAG: name 'edge_response' is not defined
Final Nodes: []
Final Edges: []
Graph data successfully pushed to Neo4j.
User.php
Extracting data: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 8422.30it/s]
Querying for nodes...
Node response is not JSON formatted. Attempting plain-text parsing.
Error querying GraphRAG: name 'edge_response' is not defined
Final Nodes: []
Final Edges: []
Graph data successfully pushed to Neo4j.
The relationships involving functions that get input from users and are vulnerable to attacks are as follows:

1. Relationship: USER -> LOGIN
   - File Name: index.php
   - Line Number: The login method in the User class is vulnerable due to SQL injection risk when handling user input (username and password).

2. Relationship: PASSWORD -> LOGIN
   - File Name: index.php
   - Line Number: The login method takes the password input as an argument.

3. Relationship: USERNAME -> LOGIN
   - File Name: index.php
   - Line Number: The login method takes the username input as an argument.

The login function has a known vulnerability to SQL injection due to the construction of the SQL query directly from user inputs without proper sanitization.
```
