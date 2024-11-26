```

Connection Successful
Database cleared.
Database initialized with constraints.
Processing File: code.php

Extracting data: 100%|████████████████████████████| 1/1 [00:10<00:00, 10.04s/it]
Building [done]: 100%|████████████████████████████| 7/7 [00:01<00:00,  6.63it/s]
Successfully inserted content from code.php.
Querying for nodes...
Raw Node Response (Full):
Entities and their types:

1. FORM - Form element for user input.
2. TODO - Variable containing the formatted todo item.
3. DESIGN - Object instance or design configuration.
4. FILETODO - Resource handle for file opened for appending.
5. GET - HTTP method used for form submission.
6. FILE - Variable to store the filename (initially 'todo.txt').
7. B - HTML bold tag used in the todo item.
8. CHECKBOX - HTML checkbox element in the todo item.
9. WRITE - Function to write the todo item to the file.
10. READ - Function to read the contents of the file.
11. INPUT - HTML input element for user interaction.
Node response is not JSON formatted. Attempting plain-text parsing.
Querying for edges...
Raw Edge Response (Full):
The relevant relationships between entities with filename, line number, user input functions, potential vulnerabilities, and nodes are as follows:

1. **Filename**: `code.php`
   - **Function**: `WRITE`
   - **Source**: `FILETODO`
   - **Target**: `TODO`
   - **Description**: The 'write' method appends data to the 'fileTodo' object, which handles user input.
   - **Vulnerability**: This function is vulnerable to code injection attacks through user input without proper sanitization.

2. **Filename**: `code.php`
   - **Function**: `READ`
   - **Source**: `FILE`
   - **Target**: `FILETODO`
   - **Description**: The 'read' method retrieves the contents of the 'file' variable, allowing user input output.
   - **Vulnerability**: Retrieving file contents could be exploited with malicious input if file handling is not secured.
Edge response is not JSON formatted. Attempting plain-text parsing.
Final Nodes: [{'id': '1', 'type': 'FORM', 'category': 'Form element for user input.', 'linenumber': 3, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '2', 'type': 'TODO', 'category': 'Variable containing the formatted todo item.', 'linenumber': 4, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '3', 'type': 'DESIGN', 'category': 'Object instance or design configuration.', 'linenumber': 5, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '4', 'type': 'FILETODO', 'category': 'Resource handle for file opened for appending.', 'linenumber': 6, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '5', 'type': 'GET', 'category': 'HTTP method used for form submission.', 'linenumber': 7, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '6', 'type': 'FILE', 'category': "Variable to store the filename (initially 'todo.txt').", 'linenumber': 8, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '7', 'type': 'B', 'category': 'HTML bold tag used in the todo item.', 'linenumber': 9, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '8', 'type': 'CHECKBOX', 'category': 'HTML checkbox element in the todo item.', 'linenumber': 10, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '9', 'type': 'WRITE', 'category': 'Function to write the todo item to the file.', 'linenumber': 11, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '10', 'type': 'READ', 'category': 'Function to read the contents of the file.', 'linenumber': 12, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}, {'id': '11', 'type': 'INPUT', 'category': 'HTML input element for user interaction.', 'linenumber': 13, 'filename': 'code.php', 'Linenumber': 'Unknown', 'Filename': 'Unknown'}]
Final Edges: []
Graph data successfully pushed to Neo4j.

```
