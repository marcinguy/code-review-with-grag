```

python3.12 test_viz34.py
Connection Successful
Database cleared.
Database initialized with constraints.
Processing File: pyproject.toml

Extracting data: 100%|████████████████████████████| 1/1 [00:09<00:00,  9.90s/it]
Building [done]: 100%|████████████████████████████| 7/7 [00:01<00:00,  4.86it/s]
Successfully inserted content from pyproject.toml.
Querying for nodes...
Raw Node Response (Full):
Entities and their types:

1. **PROGRAM** - A software application or code.
2. **LEGAL ENTITY** - An entity that has legal rights and obligations.
3. **TYPE** - A classification that denotes the nature of entries.
4. **LICENSE** - A legal document granting permissions regarding a covered work.
5. **COPYRIGHT** - A legal right that grants the creator of original work exclusive rights to its use and distribution.
6. **LIBRARY** - A collection of precompiled routines that a program can use.
7. **FUNCTION** - A routine or method that performs a specific task.
8. **WORK** - The entire creation or compilation that is being licensed.
9. **GNU GENERAL PUBLIC LICENSE** - A widely recognized copyleft license that ensures software freedom.
10. **LICENSE STEWARD** - Entity that holds the rights to modify the license.
11. **FREE SOFTWARE FOUNDATION** - An organization that promotes software freedom.
12. **OBJECT** - An instance of a class that contains data.
13. **SOFTWARE** - Refers to the software as a product.
14. **OBJECT CODE** - Executable code generated from source code.
15. **YOU** - The individual or entity agreeing to the terms of the License.
16. **PACKAGES** - List of packages to install.
17. **INPUT** - The data that is received by functions or methods.
18. **FILENAME** - The name of the file where code is located.
19. **GNU AFFERO GENERAL PUBLIC LICENSE** - A license allowing software to be freely used, modified, and distributed.
20. **CONTRIBUTOR** - An individual or entity providing contributions to the software.
21. **LICENSEE** - An individual or organization granted the right to use the software under its license.
22. **USERS** - Individuals who use software programs.
23. **CATEGORY** - A grouping that defines the type of category.
24. **USER COMMANDS** - Commands or options list presented in an interface.
25. **SOURCE CODE** - Human-readable instructions that make up a program.
26. **ENTITY TRANSACTION** - A transaction that transfers control of an organization or its assets.
27. **AUTHOR** - The individual who creates or writes the program.
28. **LEGAL NOTICES** - Notices that convey legal information.
29. **MODIFICATION** - The action or process of altering software from its original state.
30. **USER INTERFACES** - Interactive interfaces that display legal notices.
31. **METHOD** - A function associated with an object.
32. **TAINTED** - Data that can potentially be insecure if not handled properly.
33. **DATA TABLE** - A structured set of data that can be used by functions in the library.
34. **COMBINED LIBRARIES** - Libraries that are combined and conveyed together.
35. **COMBINED WORK** - A work that combines multiple elements, usually involving a library and an application.
36. **COVERED SOFTWARE** - Software that is covered under this license.
37. **COPYRIGHT HOLDER** - An individual or organization that holds the copyright to a work.
38. **MODIFIED VERSION** - A work that has been altered from its original form.
39. **OBJECT FORM** - Any form resulting from the transformation of a Source form.
40. **RECIPIENT** - An individual or organization that receives the software.
41. **YOUR** - Includes any entity under common control with You.
42. **GNU LESSER GENERAL PUBLIC LICENSE** - A free software license permitting use, modification, and redistribution.
43. **CORRESPONDING SOURCE** - The source code that must accompany object code.
44. **COVERED WORK** - A work that is under a patent license.
45. **MOZILLA FOUNDATION** - The steward of the license.
46. **GENERAL PUBLIC LICENSE** - A widely used free software license.
47. **CHECKMATE5** - A specific software project version.
48. **LINENUMBER** - The line number within the file.
49. **DEV-PACKAGES** - Development related packages.
50. **SINK** - A point in the code where data is used, potentially leading to security issues.
51. **FREEDOM** - The ability to share and change works.
52. **MESSAGE** - Explanation of the error.
Node response is not JSON formatted. Attempting plain-text parsing.
Querying for edges...
Raw Edge Response (Full):
To address the query regarding the relationships between entities that involve functions, filenames, line numbers, input from users, and vulnerabilities to attacks, the relevant details extracted from the provided data are as follows:

### Identified Relationships:
1. **Functions and Input**:
   - Functions can take input data from users.
   - Functions receive input as parameters.

2. **Functions and Vulnerabilities**:
   - Functions must handle tainted input properly.
   - Functions should sanitize tainted data before usage.
   - Tainted inputs can lead to security vulnerabilities at sinks in the code.
   - Sinks can be vulnerable if they process tainted data.

3. **Function Architecture**:
   - Functions are defined within specific files (filenames) and located at specific lines (line numbers) within those files which correlates to the need for proper input management and vulnerability handling.

### Summary of Vulnerable Functions:
- Functions that take user input and are associated with tainted data may face security issues when processing that input without proper sanitization. These functions are critical points in the code (sinks) where vulnerabilities could be exploited.
Edge response is not JSON formatted. Attempting plain-text parsing.
Processing File: MANIFEST.in

Extracting data: 100%|██████████████████████████| 1/1 [00:00<00:00, 5518.82it/s]
Successfully inserted content from MANIFEST.in.
Querying for nodes...
Raw Node Response (Full):
The entities and their types are as follows:

1. **PROGRAM** - Type: Software Application
2. **LEGAL ENTITY** - Type: Entity with Legal Rights and Obligations
3. **TYPE** - Type: Classification
4. **LICENSE** - Type: Legal Document
5. **COPYRIGHT** - Type: Legal Right
6. **LIBRARY** - Type: Software Library
7. **FUNCTION** - Type: Routine or Method
8. **WORK** - Type: Compilation or Creation
9. **GNU GENERAL PUBLIC LICENSE** - Type: Software License
10. **LICENSE STEWARD** - Type: Entity
11. **FREE SOFTWARE FOUNDATION** - Type: Organization
12. **OBJECT** - Type: Instance of a Class
13. **SOFTWARE** - Type: Product
14. **OBJECT CODE** - Type: Executable Code
15. **YOU** - Type: Individual or Entity
16. **PACKAGES** - Type: List
17. **INPUT** - Type: Data
18. **FILENAME** - Type: File Name
19. **GNU AFFERO GENERAL PUBLIC LICENSE** - Type: Software License
20. **CONTRIBUTOR** - Type: Individual or Organization
21. **LICENSEE** - Type: Individual or Organization
22. **USERS** - Type: Individuals
23. **CATEGORY** - Type: Grouping
24. **USER COMMANDS** - Type: Commands List
25. **SOURCE CODE** - Type: Programming Instructions
26. **ENTITY TRANSACTION** - Type: Transactional Action
27. **AUTHOR** - Type: Individual
28. **LEGAL NOTICES** - Type: Notices
29. **MODIFICATION** - Type: Process
30. **USER INTERFACES** - Type: Interface
31. **METHOD** - Type: Function Related to Object
32. **TAINTED** - Type: Data
33. **DATA TABLE** - Type: Structured Data
34. **COMBINED LIBRARIES** - Type: Library Combination
35. **COMBINED WORK** - Type: Work Combining Elements
36. **COVERED SOFTWARE** - Type: Software under License
37. **COPYRIGHT HOLDER** - Type: Entity Holding Copyright
38. **MODIFIED VERSION** - Type: Altered Work
39. **OBJECT FORM** - Type: Transformed Form
40. **RECIPIENT** - Type: Individual or Organization
41. **YOUR** - Type: Entity Related to You
42. **GNU LESSER GENERAL PUBLIC LICENSE** - Type: Modified Software License
43. **CORRESPONDING SOURCE** - Type: Required Source Code
44. **COVERED WORK** - Type: Work under License
45. **MOZILLA FOUNDATION** - Type: License Steward
46. **GENERAL PUBLIC LICENSE** - Type: Free Software License
47. **CHECKMATE5** - Type: Software Project
48. **LINENUMBER** - Type: Reference Number
49. **DEV-PACKAGES** - Type: Development Related Packages
50. **SINK** - Type: Point in Code
51. **FREEDOM** - Type: Concept
52. **MESSAGE** - Type: Explanation
Node response is not JSON formatted. Attempting plain-text parsing.
Querying for edges...
Raw Edge Response (Full):
No relevant information was found.
Edge response is not JSON formatted. Attempting plain-text parsing.
Processing File: README.md

Extracting data: 100%|██████████████████████████| 1/1 [00:00<00:00, 7810.62it/s]
Successfully inserted content from README.md.
Querying for nodes...
Raw Node Response (Full):
1. **PROGRAM** - A software application or code.
2. **LEGAL ENTITY** - An entity that has legal rights and obligations.
3. **TYPE** - A classification that denotes the nature of entries.
4. **LICENSE** - A legal document granting permissions regarding a covered work.
5. **COPYRIGHT** - A legal right that grants the creator of original work exclusive rights to its use and distribution.
6. **LIBRARY** - A collection of precompiled routines that a program can use.
7. **FUNCTION** - A routine or method that performs a specific task.
8. **WORK** - The entire creation or compilation that is being licensed.
9. **GNU GENERAL PUBLIC LICENSE** - A widely recognized copyleft license that ensures end users the freedom to run, study, share, modify, and distribute software.
10. **LICENSE STEWARD** - Entity that holds the rights to modify the license.
11. **FREE SOFTWARE FOUNDATION** - An organization that promotes software freedom.
12. **OBJECT** - An instance of a class that contains data.
13. **SOFTWARE** - Refers to the software as a product.
14. **OBJECT CODE** - Executable code generated from source code by a compiler.
15. **YOU** - The individual or entity agreeing to the terms of the License.
16. **PACKAGES** - List of packages to install.
17. **INPUT** - The data that is received by functions or methods.
18. **FILENAME** - The name of the file where code is located.
19. **GNU AFFERO GENERAL PUBLIC LICENSE** - A license under which the program may be combined with other works.
20. **CONTRIBUTOR** - An individual or organization providing contributions toward software development.
21. **LICENSEE** - An individual or organization that is granted the right to use the software under its license.
22. **USERS** - Individuals who use software programs.
23. **CATEGORY** - A grouping that defines the type of category.
24. **USER COMMANDS** - Commands or options list presented in an interface.
25. **SOURCE CODE** - Human-readable instructions that make up a program.
26. **ENTITY TRANSACTION** - A transaction that transfers control of an organization or its assets.
27. **AUTHOR** - The individual who creates or writes the program.
28. **LEGAL NOTICES** - Notices that convey legal information.
29. **MODIFICATION** - The action or process of altering a software from its original state.
30. **USER INTERFACES** - Interactive interfaces that display legal notices.
31. **METHOD** - A function that is associated with an object.
32. **TAINTED** - Data that can potentially be insecure if not handled properly.
33. **DATA TABLE** - A structured set of data that can be used by functions in the library.
34. **COMBINED LIBRARIES** - Libraries that are combined and conveyed together.
35. **COMBINED WORK** - A work that combines multiple elements, usually involving a library and an application.
36. **COVERED SOFTWARE** - Software that is covered under this license.
37. **COPYRIGHT HOLDER** - An individual or organization that holds the copyright to a work.
38. **MODIFIED VERSION** - A work that has been altered from its original form.
39. **OBJECT FORM** - Any form resulting from transformation of a Source form.
40. **RECIPIENT** - An individual or organization that receives the software.
41. **YOUR** - Includes any entity that controls, is controlled by, or is under common control with You.
42. **GNU LESSER GENERAL PUBLIC LICENSE** - A free software license that permits the use, modification, and redistribution of software.
43. **CORRESPONDING SOURCE** - The source code required to generate, install, and modify the object code.
44. **COVERED WORK** - A covered work is subject to the terms of the patent license.
45. **MOZILLA FOUNDATION** - The steward of the license.
46. **GENERAL PUBLIC LICENSE** - A widely used free software license.
47. **CHECKMATE5** - A software project version 4.0.98.
48. **LINENUMBER** - The line number within the file.
49. **DEV-PACKAGES** - Development related packages.
50. **SINK** - A point in the code where data is used.
51. **FREEDOM** - The ability to share and change works.
52. **MESSAGE** - Explanation of the error.
Node response is not JSON formatted. Attempting plain-text parsing.
Querying for edges...
Raw Edge Response (Full):
The relevant relationships are:

- **Filename** is associated with **Function** (A filename typically contains functions defined within it).
- **LineNumber** is associated with **Function** (Each function can be located at a specific line number in the code).
- **Input** is associated with **Function** (Function can receive input as parameters, indicating functions take input data).
- **Function** is associated with **Tainted** (Functions must handle tainted input properly, implying a vulnerability if not managed correctly).
- **Function** is associated with **Sink** (Sinks can be vulnerable if they process tainted data, further suggesting potential vulnerabilities in these functions).

Thus, the functions that get input, are linked to filenames and line numbers, and are potentially vulnerable to attacks are characterized by their handling of tainted inputs leading to security issues at sinks.
Edge response is not JSON formatted. Attempting plain-text parsing.
Processing File: Pipfile

Extracting data: 100%|██████████████████████████| 1/1 [00:00<00:00, 7463.17it/s]
Successfully inserted content from Pipfile.
Querying for nodes...
Raw Node Response (Full):
- PACKAGES: TYPE
- PROGRAM: TYPE
- LEGAL ENTITY: LEGAL ENTITY
- TYPE: TYPE
- LICENSE: LICENSE
- DEV-PACKAGES: DEV-PACKAGES
- COPYRIGHT: COPYRIGHT
- LIBRARY: LIBRARY
- CHECKMATE5: PROGRAM
- FUNCTION: FUNCTION
- WORK: WORK
- LICENSE STEWARD: LEGAL ENTITY
- OBJECT: OBJECT
- GNU GENERAL PUBLIC LICENSE: LICENSE
- SOFTWARE: SOFTWARE
- FREE SOFTWARE FOUNDATION: LEGAL ENTITY
- YOU: LEGAL ENTITY
- OBJECT CODE: OBJECT
- FILENAME: FILENAME
- INPUT: INPUT
- SQLALCHEMY: DEV-PACKAGES
- USERS: LEGAL ENTITY
- PYYAML: DEV-PACKAGES
- BLITZDB5: DEV-PACKAGES
- CATEGORY: TYPE
- CONTRIBUTOR: LEGAL ENTITY
- USER COMMANDS: FUNCTION
- GNU AFFERO GENERAL PUBLIC LICENSE: LICENSE
- LICENSEE: LEGAL ENTITY
- ENTITY TRANSACTION: ENTITY TRANSACTION
- REQUESTS: DEV-PACKAGES
- LEGAL NOTICES: FUNCTION
- SOURCE CODE: OBJECT
- METHOD: FUNCTION
- USER INTERFACES: FUNCTION
- TAINTED: TYPE
- DATA TABLE: FUNCTION
- COMBINED LIBRARIES: TYPE
- CHARDET: DEV-PACKAGES
- NAME: TYPE
- PYFLAKES: DEV-PACKAGES
- PYLINT: DEV-PACKAGES
- PEP8: DEV-PACKAGES
- PSYCOPG2-BINARY: DEV-PACKAGES
- CFFI: DEV-PACKAGES
- TQDM: DEV-PACKAGES
- MODIFICATION: TYPE
- COMBINED WORK: TYPE
- MODIFIED VERSION: TYPE
- AUTHOR: LEGAL ENTITY
- OBJECT FORM: TYPE
- COPYRIGHT HOLDER: LEGAL ENTITY
- YOUR: LEGAL ENTITY
- COVERED SOFTWARE: SOFTWARE
- GNU LESSER GENERAL PUBLIC LICENSE: LICENSE
- MOZILLA FOUNDATION: LEGAL ENTITY
- LINENUMBER: TYPE
- SINK: TYPE
- GENERAL PUBLIC LICENSE: LICENSE
- RECIPIENT: LEGAL ENTITY
Node response is not JSON formatted. Attempting plain-text parsing.
Error parsing line: - PACKAGES: TYPE, Error: list index out of range
Error parsing line: - PROGRAM: TYPE, Error: list index out of range
Error parsing line: - LEGAL ENTITY: LEGAL ENTITY, Error: list index out of range
Error parsing line: - TYPE: TYPE, Error: list index out of range
Error parsing line: - LICENSE: LICENSE, Error: list index out of range
Error parsing line: - DEV-PACKAGES: DEV-PACKAGES, Error: list index out of range
Error parsing line: - COPYRIGHT: COPYRIGHT, Error: list index out of range
Error parsing line: - LIBRARY: LIBRARY, Error: list index out of range
Error parsing line: - CHECKMATE5: PROGRAM, Error: list index out of range
Error parsing line: - FUNCTION: FUNCTION, Error: list index out of range
Error parsing line: - WORK: WORK, Error: list index out of range
Error parsing line: - LICENSE STEWARD: LEGAL ENTITY, Error: list index out of range
Error parsing line: - OBJECT: OBJECT, Error: list index out of range
Error parsing line: - GNU GENERAL PUBLIC LICENSE: LICENSE, Error: list index out of range
Error parsing line: - SOFTWARE: SOFTWARE, Error: list index out of range
Error parsing line: - FREE SOFTWARE FOUNDATION: LEGAL ENTITY, Error: list index out of range
Error parsing line: - YOU: LEGAL ENTITY, Error: list index out of range
Error parsing line: - OBJECT CODE: OBJECT, Error: list index out of range
Error parsing line: - FILENAME: FILENAME, Error: list index out of range
Error parsing line: - INPUT: INPUT, Error: list index out of range
Error parsing line: - SQLALCHEMY: DEV-PACKAGES, Error: list index out of range
Error parsing line: - USERS: LEGAL ENTITY, Error: list index out of range
Error parsing line: - PYYAML: DEV-PACKAGES, Error: list index out of range
Error parsing line: - BLITZDB5: DEV-PACKAGES, Error: list index out of range
Error parsing line: - CATEGORY: TYPE, Error: list index out of range
Error parsing line: - CONTRIBUTOR: LEGAL ENTITY, Error: list index out of range
Error parsing line: - USER COMMANDS: FUNCTION, Error: list index out of range
Error parsing line: - GNU AFFERO GENERAL PUBLIC LICENSE: LICENSE, Error: list index out of range
Error parsing line: - LICENSEE: LEGAL ENTITY, Error: list index out of range
Error parsing line: - ENTITY TRANSACTION: ENTITY TRANSACTION, Error: list index out of range
Error parsing line: - REQUESTS: DEV-PACKAGES, Error: list index out of range
Error parsing line: - LEGAL NOTICES: FUNCTION, Error: list index out of range
Error parsing line: - SOURCE CODE: OBJECT, Error: list index out of range
Error parsing line: - METHOD: FUNCTION, Error: list index out of range
Error parsing line: - USER INTERFACES: FUNCTION, Error: list index out of range
Error parsing line: - TAINTED: TYPE, Error: list index out of range
Error parsing line: - DATA TABLE: FUNCTION, Error: list index out of range
Error parsing line: - COMBINED LIBRARIES: TYPE, Error: list index out of range
Error parsing line: - CHARDET: DEV-PACKAGES, Error: list index out of range
Error parsing line: - NAME: TYPE, Error: list index out of range
Error parsing line: - PYFLAKES: DEV-PACKAGES, Error: list index out of range
Error parsing line: - PYLINT: DEV-PACKAGES, Error: list index out of range
Error parsing line: - PEP8: DEV-PACKAGES, Error: list index out of range
Error parsing line: - PSYCOPG2-BINARY: DEV-PACKAGES, Error: list index out of range
Error parsing line: - CFFI: DEV-PACKAGES, Error: list index out of range
Error parsing line: - TQDM: DEV-PACKAGES, Error: list index out of range
Error parsing line: - MODIFICATION: TYPE, Error: list index out of range
Error parsing line: - COMBINED WORK: TYPE, Error: list index out of range
Error parsing line: - MODIFIED VERSION: TYPE, Error: list index out of range
Error parsing line: - AUTHOR: LEGAL ENTITY, Error: list index out of range
Error parsing line: - OBJECT FORM: TYPE, Error: list index out of range
Error parsing line: - COPYRIGHT HOLDER: LEGAL ENTITY, Error: list index out of range
Error parsing line: - YOUR: LEGAL ENTITY, Error: list index out of range
Error parsing line: - COVERED SOFTWARE: SOFTWARE, Error: list index out of range
Error parsing line: - GNU LESSER GENERAL PUBLIC LICENSE: LICENSE, Error: list index out of range
Error parsing line: - MOZILLA FOUNDATION: LEGAL ENTITY, Error: list index out of range
Error parsing line: - LINENUMBER: TYPE, Error: list index out of range
Error parsing line: - SINK: TYPE, Error: list index out of range
Error parsing line: - GENERAL PUBLIC LICENSE: LICENSE, Error: list index out of range
Error parsing line: - RECIPIENT: LEGAL ENTITY, Error: list index out of range
Querying for edges...
Raw Edge Response (Full):
The relationships between entities with `FILENAME` and `LINENUMBER` related to `FUNCTION`, which take `INPUT` from the user and are vulnerable to attacks (i.e., handling `TAINTED` data), include the following:

1. **FILENAME -> FUNCTION**: A filename typically contains functions defined within it.
2. **LINENUMBER -> FUNCTION**: Each function can be located at a specific line number in the code.
3. **FUNCTION -> INPUT**: Functions can receive input as parameters.
4. **FUNCTION -> TAINTED**: Functions must handle tainted input properly.
5. **FUNCTION -> SINK**: The function may output or use data that can lead to security vulnerabilities (sinks can be vulnerable if they process tainted data).

In summary, the interconnected elements include filenames and line number references that define functions handling user input, with potential vulnerabilities related to tainted data.
Edge response is not JSON formatted. Attempting plain-text parsing.
Processing File: setup.py

Extracting data: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:05<00:00,  5.94s/it]
Building [done]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:01<00:00,  6.42it/s]
Successfully inserted content from setup.py.
Querying for nodes...


```
