```python3.12 test_viz37.py
Connection Successful
Database cleared.
Database initialized with constraints.
index.php
Extracting data: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:08<00:00,  8.01s/it]
Building [done]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:01<00:00,  3.76it/s]
Querying for nodes...
Raw Node Response (Full):
Entities and their types:

1. USER::LOGIN - Method to validate user credentials.
2. USER - User class to handle user-related operations.
3. POST - The HTTP method used to submit form data.
4. FORM - An HTML form to collect user input.
5. LOGIN SUCCESSFUL - Response indicating successful login.
6. LOGIN FAILED - Response indicating failed login.
7. DATABASE - Database class to manage database connections.
8. DATABASE::GETCONNECTION - Method to establish a connection to the database.
9. USERNAME - User input for the username.
10. PASSWORD - User input for the password.
11. INDEX.PHP - The file that processes the login form submission.
12. LOGIN - Method to perform login operation.
Node response is not JSON formatted. Attempting plain-text parsing.
Cleaned Nodes: [{'id': '286d186a-8636-456d-bc4d-d852d392d3c4', 'type': 'USER::LOGIN', 'category': 'Method to validate user credentials.', 'linenumber': 3, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '670f5baf-214b-4307-aa60-f5f316506c7a', 'type': 'USER', 'category': 'User class to handle user-related operations.', 'linenumber': 4, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '434c73b1-2161-476b-ac0e-8ac7ca3295f6', 'type': 'POST', 'category': 'The HTTP method used to submit form data.', 'linenumber': 5, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'af23c3c0-7859-4c54-a748-d5dcad67b144', 'type': 'FORM', 'category': 'An HTML form to collect user input.', 'linenumber': 6, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'a5afbd2c-4f2a-4a3e-89ae-13e7e9d3629b', 'type': 'LOGIN SUCCESSFUL', 'category': 'Response indicating successful login.', 'linenumber': 7, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '24c35cd7-4837-4cf8-8349-9877c3e39f04', 'type': 'LOGIN FAILED', 'category': 'Response indicating failed login.', 'linenumber': 8, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '33b84fd6-24ca-445d-ad4d-cbbe45f16411', 'type': 'DATABASE', 'category': 'Database class to manage database connections.', 'linenumber': 9, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'f0e535e1-1b2d-458b-a88d-720c11d46eb2', 'type': 'DATABASE::GETCONNECTION', 'category': 'Method to establish a connection to the database.', 'linenumber': 10, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '03d20137-9e71-4d8a-b2e3-d4e60a5273d4', 'type': 'USERNAME', 'category': 'User input for the username.', 'linenumber': 11, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '171f2574-7f9b-46d3-8ee4-c1a5f2705927', 'type': 'PASSWORD', 'category': 'User input for the password.', 'linenumber': 12, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'dd0eab44-d05a-4246-b282-8fa88eb5d48a', 'type': 'INDEX', 'category': 'The file that processes the login form submission.', 'linenumber': 13, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '90afbcef-ccc1-4cc5-a6c8-33d0d33add87', 'type': 'LOGIN', 'category': 'Method to perform login operation.', 'linenumber': 14, 'filename': 'index.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}]
Querying for edges...
Raw Edge Response (Full):
Error querying GraphRAG: name 'edge_response' is not defined
Final Nodes: []
Final Edges: []
Graph data successfully pushed to Neo4j.
Database.php
Extracting data: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:05<00:00,  5.60s/it]
Building [done]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:02<00:00,  2.47it/s]
Querying for nodes...
Raw Node Response (Full):
Entities and their types:

1. GETCONNECTION - Method
2. DATABASE - Class
3. USER - Class
4. TEST - Database
5. USER::LOGIN - Method
6. DATABASE::GETCONNECTION - Method
7. PDO - Extension
8. FORM - HTML Form
9. LOGIN SUCCESSFUL - Response
10. MYSQL - Database Management System
11. PDOEXCEPTION - Exception Class
12. LOCALHOST - Host Name
13. ROOT - Username
14. POST - HTTP Method
15. LOGIN FAILED - Response
16. PASSWORD - User Input
17. USERNAME - User Input
18. INDEX.PHP - File
Node response is not JSON formatted. Attempting plain-text parsing.
Cleaned Nodes: [{'id': '4fc4e4ec-8d6b-4add-9741-ca0a206c0d72', 'type': 'GETCONNECTION', 'category': 'Method', 'linenumber': 3, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '49584ccd-166d-49a0-a2fc-1beae6161b37', 'type': 'DATABASE', 'category': 'Class', 'linenumber': 4, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '9f6b6db2-23a5-41b4-9924-aa9ff32d5f02', 'type': 'USER', 'category': 'Class', 'linenumber': 5, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'f30faf38-682a-41c1-854a-320befa82a72', 'type': 'TEST', 'category': 'Database', 'linenumber': 6, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '63f62860-5af9-4bdd-8628-89801be5ccac', 'type': 'USER::LOGIN', 'category': 'Method', 'linenumber': 7, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'a14ce9df-ab2b-4a7a-902a-c83b302115fd', 'type': 'DATABASE::GETCONNECTION', 'category': 'Method', 'linenumber': 8, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '14cafad9-bcaf-48d4-9d7c-4f5b861c279d', 'type': 'PDO', 'category': 'Extension', 'linenumber': 9, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '7f0de04d-878c-4121-a3df-0ac4a960d40b', 'type': 'FORM', 'category': 'HTML Form', 'linenumber': 10, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '78c79a22-784a-46a6-865d-5c7de8b83e2d', 'type': 'LOGIN SUCCESSFUL', 'category': 'Response', 'linenumber': 11, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'f7278e9c-83fa-44d5-980a-811cd147adbc', 'type': 'MYSQL', 'category': 'Database Management System', 'linenumber': 12, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'f77f7325-7c0c-46a2-9e74-9d7907618ddd', 'type': 'PDOEXCEPTION', 'category': 'Exception Class', 'linenumber': 13, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'a59ff2d5-c0a8-4ae5-ae48-276708026141', 'type': 'LOCALHOST', 'category': 'Host Name', 'linenumber': 14, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '9bfb2888-6326-4fc2-b1bc-091c5570309e', 'type': 'ROOT', 'category': 'Username', 'linenumber': 15, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '062de3b0-12f7-42a7-b091-9c3fabefc881', 'type': 'POST', 'category': 'HTTP Method', 'linenumber': 16, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '3096298b-8419-4340-8375-0bf4b5f77caf', 'type': 'LOGIN FAILED', 'category': 'Response', 'linenumber': 17, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '04f8cb09-b985-40dc-ba1a-d36c043333c9', 'type': 'PASSWORD', 'category': 'User Input', 'linenumber': 18, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '88ee82f3-7b89-4d49-a4f2-31475dd946c6', 'type': 'USERNAME', 'category': 'User Input', 'linenumber': 19, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'db79be95-b1e4-488f-8214-d366798ad134', 'type': 'INDEX', 'category': 'File', 'linenumber': 20, 'filename': 'Database.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}]
Querying for edges...
Raw Edge Response (Full):
Error querying GraphRAG: name 'edge_response' is not defined
Final Nodes: []
Final Edges: []
Graph data successfully pushed to Neo4j.
User.php
Extracting data: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:05<00:00,  5.52s/it]
Building [done]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:01<00:00,  5.04it/s]
Querying for nodes...
Raw Node Response (Full):
Entities and their types:

1. LOGIN - Method
2. USERS - Table
3. GETCONNECTION - Method
4. SQL INJECTION - Vulnerability
5. USER - Class
6. DATABASE - Class
7. FORM - HTML Form
8. USER::LOGIN - Method
9. USERNAME - Input Parameter
10. PASSWORD - Input Parameter
11. DATABASE.PHP - File
12. DATABASE::GETCONNECTION - Method
13. PDO - PHP Extension
14. POST - HTTP Method
15. FALSE - Return Value
16. LOGIN SUCCESSFUL - Response
17. LOGIN FAILED - Response
18. TRUE - Return Value
19. MYSQL - Database Management System
20. TEST - Database
21. PDOEXCEPTION - Exception Class
22. LOCALHOST - Host Name
23. INDEX.PHP - File
24. ROOT - Username
Node response is not JSON formatted. Attempting plain-text parsing.
Cleaned Nodes: [{'id': 'a714540c-8803-4ba3-ab9b-80391e0091ed', 'type': 'LOGIN', 'category': 'Method', 'linenumber': 3, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '702b7659-bf3d-4339-853b-1dbfb3071570', 'type': 'USERS', 'category': 'Table', 'linenumber': 4, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '6ea98a6e-ed81-430e-aafb-2cb1a0a360bc', 'type': 'GETCONNECTION', 'category': 'Method', 'linenumber': 5, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '489e7ba9-536a-40f2-b2e4-ef5d5c87aa94', 'type': 'SQL INJECTION', 'category': 'Vulnerability', 'linenumber': 6, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'edf528b4-8304-4e41-a44e-07270618fc9f', 'type': 'USER', 'category': 'Class', 'linenumber': 7, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '254572a6-a2a5-45e8-95d8-82d394c221ac', 'type': 'DATABASE', 'category': 'Class', 'linenumber': 8, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'df21b51d-e13c-4461-ae9d-20c312eba88e', 'type': 'FORM', 'category': 'HTML Form', 'linenumber': 9, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '0c000151-9f4b-4109-b929-6318c98607db', 'type': 'USER::LOGIN', 'category': 'Method', 'linenumber': 10, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'a902d0cb-47ce-4cb1-8e78-60aaf17d25ac', 'type': 'USERNAME', 'category': 'Input Parameter', 'linenumber': 11, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '1b53129b-7c7a-47a1-af72-ef4ade35cfe0', 'type': 'PASSWORD', 'category': 'Input Parameter', 'linenumber': 12, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '271a5c26-d9a5-487e-9f6f-aca153b3b068', 'type': 'DATABASE', 'category': 'File', 'linenumber': 13, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'a1bea93d-286a-45bd-bb00-168531e8f91f', 'type': 'DATABASE::GETCONNECTION', 'category': 'Method', 'linenumber': 14, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'c3c484de-8595-4a8d-9863-8029a36aa2db', 'type': 'PDO', 'category': 'PHP Extension', 'linenumber': 15, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '1ff7d494-ea29-44b0-87b4-fb90c3e27356', 'type': 'POST', 'category': 'HTTP Method', 'linenumber': 16, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '786f2384-1b50-469e-9adb-645e447d7a4b', 'type': 'FALSE', 'category': 'Return Value', 'linenumber': 17, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '30122234-4f43-4bb7-8471-608325853469', 'type': 'LOGIN SUCCESSFUL', 'category': 'Response', 'linenumber': 18, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '6cab2603-9f4d-449d-89d6-ffe62cc58a67', 'type': 'LOGIN FAILED', 'category': 'Response', 'linenumber': 19, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '9b3fd920-469b-4029-a230-f03c6cef8efe', 'type': 'TRUE', 'category': 'Return Value', 'linenumber': 20, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'a3d98b73-c6f2-4b09-a4ee-b9c1b58ff977', 'type': 'MYSQL', 'category': 'Database Management System', 'linenumber': 21, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'ece7e232-f0ab-4b0c-90a8-c6090dc6f349', 'type': 'TEST', 'category': 'Database', 'linenumber': 22, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '33066ef8-2df8-4bc0-b5f1-10f0d23867b4', 'type': 'PDOEXCEPTION', 'category': 'Exception Class', 'linenumber': 23, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '75b1d750-529a-4a25-a8e5-cf82683d881c', 'type': 'LOCALHOST', 'category': 'Host Name', 'linenumber': 24, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': 'c628828e-e0fc-471d-b42e-c13a97232e07', 'type': 'INDEX', 'category': 'File', 'linenumber': 25, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '83a5ca7b-3a75-4cb4-bb53-102bd4915db0', 'type': 'ROOT', 'category': 'Username', 'linenumber': 26, 'filename': 'User.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}]
Querying for edges...
Raw Edge Response (Full):
Error querying GraphRAG: name 'edge_response' is not defined
Final Nodes: []
Final Edges: []
Graph data successfully pushed to Neo4j.
1. **User Class - login Method**
   - **Function:** login
   - **Input:** username, password
   - **Vulnerability:** Potential SQL Injection risk due to untrusted input in the SQL query.
   - **File Name:** User.php
   - **Line Number:** Query inside the login method is vulnerable, specific line number not provided in the source.

2. **Form - Collects User Input**
   - **Inputs:** username, password
   - **Vulnerability:** Data passed directly to the database query, allowing for potential SQL Injection.
   - **File Name:** index.php
   - **Line Number:** Specific line number not provided; however, the form code appears in the provided source code.
```
