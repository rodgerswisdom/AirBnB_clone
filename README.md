# 0x00. AirBnB clone - The console

## Group Project
This project is part of the curriculum at [Holberton School](https://www.holbertonschool.com/), and it's being developed by a team consisting of Karanja Karanja and RODGERS WISDOM.

## Overview
This project aims to create a command-line interface (CLI) for managing objects within an AirBnB clone. The CLI will allow users to create, retrieve, update, and delete various objects such as users, states, cities, and places. It serves as the first step towards building a full web application for the AirBnB clone.

## Authors
- Guillaume

## Project Details
- **Start Date:** March 18, 2024, 6:00 AM
- **End Date:** March 25, 2024, 6:00 AM
- **Checker Release Date:** March 23, 2024, 12:00 PM
- **Weight:** 5

## Concepts
In this project, we will focus on the following concepts:
- Python packages
- AirBnB clone

## Background Context
Welcome to the AirBnB clone project! Before starting, please read the AirBnB concept page.

The first step involves writing a command interpreter to manage AirBnB objects. This step is crucial as it lays the foundation for subsequent tasks such as HTML/CSS templating, database storage, API integration, and front-end development.

## Learning Objectives
By the end of this project, participants are expected to understand and be able to explain the following concepts without external assistance:
- Creating a Python package
- Developing a command interpreter using the cmd module in Python
- Implementing unit testing in a large project
- Serializing and deserializing classes
- Working with JSON files
- Managing datetime in Python
- Understanding UUID
- Utilizing *args and **kwargs in Python functions

## Requirements
### Python Scripts
- **Allowed Editors:** vi, vim, emacs
- **Interpreter:** python3 (version 3.8.5)
- **Line Endings:** All files should end with a new line
- **Shebang:** The first line of all files should be `#!/usr/bin/python3`
- **README.md:** Mandatory at the root of the project folder
- **Coding Style:** Pycodestyle (version 2.8.*) should be adhered to
- **Execution:** All files must be executable
- **Documentation:** Modules, classes, and functions should be documented appropriately
- **Length Check:** The length of files will be tested using `wc`

### Python Unit Tests
- **Allowed Editors:** vi, vim, emacs
- **Line Endings:** All files should end with a new line
- **Folder Structure:** All test files should be inside a folder named `tests`
- **Test Framework:** Unittest module should be used
- **File Extensions:** Test files should have a `.py` extension
- **Test Naming:** Test files and folders should start with `test_`
- **Execution:** Tests should be executed using `python3 -m unittest discover tests`

## Execution
The shell should support both interactive and non-interactive modes, similar to the following examples:

### Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should pass in both interactive and non-interactive modes.

## Resources
- [cmd module](https://docs.python.org/3/library/cmd.html)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [Python Test Cheatsheet](https://www.pythoncheatsheet.org/#Python-Testing)
- [cmd module Wiki Page](https://en.wikipedia.org/wiki/Cmd_(command))
- [Python Unittest](https://docs.python.org/3/library/unittest.html)

## Copyright - Plagiarism
Participants are expected to complete the tasks themselves without copying or plagiarizing from external sources. Any form of plagiarism is strictly prohibited and may result in removal from the program.

## More Info
For further details about the project, refer to the project instructions and guidelines provided by Holberton School.
