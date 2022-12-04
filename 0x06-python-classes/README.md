# Python - Classes


(mandatory) Using OOP to create a square out of hashes.

_____________________________________________________________________________________________
## Required Concepts:

	-What is OOP
	-“first-class everything”
	-What is a class
	-What is an object and an instance
	-What is the difference between a class and an object or instance
	-What is an attribute
	-What are and how to use public, protected and private attributes
	-What is self
	-What is a method
	-What is the special __init__ method and how to use it
	-What is Data Abstraction, Data Encapsulation, and Information Hiding
	-What is a property
	-What is the difference between an attribute and a property in Python
	-What is the Pythonic way to write getters and setters in Python
	-How to dynamically create arbitrary new attributes for existing instances of a class
	-How to bind attributes to object and classes
	-What is and what does contain __dict__ of a class and of an instance of a class
	-How does Python find the attributes of an object or class
	-How to use the getattr function


## General Requirements:

_______________________________________________________________________________________________
	-Allowed editors: vi, vim, emacs
	-All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
	-All your files should end with a new line
	-The first line of all your files should be exactly #!/usr/bin/python3
	-A README.md file, at the root of the folder of the project, is mandatory
	-Your code should use the PEP 8 style (version 1.7.*)
	-All your files must be executable
	-The length of your files will be tested using wc
	-All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	-All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
	-All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')


## Tasks:


### 0. My first square
_________________________________________________________________________
Write an empty class Square that defines a square:

	-You are not allowed to import any module

_________________________________________________________________________

### 1. Square with size
_________________________________________________________________________
Write a class Square that defines a square by: (based on 0-square.py)

	-Private instance attribute: size
	-Instantiation with size (no type/value verification)
	-You are not allowed to import any module

_________________________________________________________________________

### 2. Size validation
_________________________________________________________________________
Write a class Square that defines a square by: (based on 1-square.py)

	-Private instance attribute: size
	-Instantiation with optional size: def __init__(self, size=0):
	-size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	-if size is less than 0, raise a ValueError exception with the message size must be >= 0
	-You are not allowed to import any module

_________________________________________________________________________

### 3. Area of a square
_________________________________________________________________________
Write a class Square that defines a square by: (based on 2-square.py)

	-Private instance attribute: size
	-Instantiation with optional size: def __init__(self, size=0):
	-size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	-if size is less than 0, raise a ValueError exception with the message size must be >= 0
	-Public instance method: def area(self): that returns the current square area
	-You are not allowed to import any module
_________________________________________________________________________


### 4. Access and update private attribute
_________________________________________________________________________
Write a class Square that defines a square by: (based on 3-square.py)

	-Private instance attribute: size:
	-property def size(self): to retrieve it
	-property setter def size(self, value): to set it:
	-size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	-if size is less than 0, raise a ValueError exception with the message size must be >= 0
	-Instantiation with optional size: def __init__(self, size=0):
	-Public instance method: def area(self): that returns the current square area
	-You are not allowed to import any module
_________________________________________________________________________

### 5. Printing a square
_________________________________________________________________________
Write a class Square that defines a square by: (based on 4-square.py)

	-Private instance attribute: size:
	-property def size(self): to retrieve it
	-property setter def size(self, value): to set it:
	-size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	-if size is less than 0, raise a ValueError exception with the message size must be >= 0
	-Instantiation with optional size: def __init__(self, size=0):
	-Public instance method: def area(self): that returns the current square area
	-Public instance method: def my_print(self): that prints in stdout the square with the character #:
	-if size is equal to 0, print an empty line
	-You are not allowed to import any module


_________________________________________________________________________

### 6. Coordinates of a square
_________________________________________________________________________
Write a class Square that defines a square by: (based on 5-square.py)

	-Private instance attribute: size:
	-property def size(self): to retrieve it
	-property setter def size(self, value): to set it:
	-size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
	-if size is less than 0, raise a ValueError exception with the message size must be >= 0
	-Private instance attribute: position:
	-property def position(self): to retrieve it
	-property setter def position(self, value): to set it:
	-position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
	-Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
	-Public instance method: def area(self): that returns the current square area
	-Public instance method: def my_print(self): that prints in stdout the square with the character #:
	-if size is equal to 0, print an empty line
	-position should be use by using space - Don’t fill lines by spaces when position[1] > 0
	-You are not allowed to import any module

___________________________________________________________________________________________________
