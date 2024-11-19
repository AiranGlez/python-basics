# 📌 Python Basics

> **Project description:** Learn and practice Python basics.

---

## 🗂️ Index

1. [Description](#description)
2. [Installation](#installation)
3. [Content](#content)
4. [License](#license)

---

## 📝 Description

- Basic syntax.
- Variables and Data Types
- Conditionals
- Loops
- Type casting
- Exceptions
- Lists, tuples, sets and dictionaries
- Functions and builtin functions
- Modules
- Lambdas
- Decorators
- Iterators
- Regular expressions

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AiranGlez/python-basics
   cd app_name
2. Execute python main file:
   ```bash
   python src/main.py
---

## 🚀 Content

Summary of basic fundamental concepts:

1. **Functions**
   - **1.1 Arbitrary arguments (\*args)**
   
   Arbitrary arguments are used when the number of arguments passed to the function are unknown. The args variable prefixed with "*" 
   stores all the values passed to it and becomes a tuple.

   - **1.2. Keyword arguments (\*\*kwargs)**

   Arbitrary keyword arguments are used when the number of arguments passed to the function are unknown. The kwargs variable prefixed with "**" becomes a dictionary of keyword:value pairs.

   - **1.3. Recursion**

   Python allows a function to call itself. This allows to loop through data to reach a result.

   - **1.4. Built-in functions**

      1. **`print()`**
         - **Description**: Prints the specified object to the console.
         - **Usage**: `print(object)`
   
      2. **`len()`**
         - **Description**: Returns the length (number of elements) of an iterable object.
         - **Usage**: `len(iterable)`
         
      3. **`type()`**
         - **Description**: Returns the type of an object.
         - **Usage**: `type(object)`
         
      4. **`int()`**
         - **Description**: Converts a value to an integer.
         - **Usage**: `int(value)`
         
      5. **`str()`**
         - **Description**: Converts a value to a string.
         - **Usage**: `str(value)`
         
      6. **`sum()`**
         - **Description**: Sums the elements of an iterable.
         - **Usage**: `sum(iterable, start=0)`
         
      7. **`max()`**
         - **Description**: Returns the maximum value of an iterable or between two or more values.
         - **Usage**: `max(iterable)` or `max(a, b, c)`
         
      8. **`min()`**
         - **Description**: Returns the minimum value of an iterable or between two or more values.
         - **Usage**: `min(iterable)` or `min(a, b, c)`
         
      9. **`abs()`**
         - **Description**: Returns the absolute value of a number.
         - **Usage**: `abs(number)`
         
      10. **`sorted()`**
         - **Description**: Returns a sorted list of the elements of an iterable.
         - **Usage**: `sorted(iterable, key=None, reverse=False)`
         
      11. **`input()`**
         - **Description**: Reads input from the user as a string.
         - **Usage**: `input(prompt)`
         
      12. **`range()`**
         - **Description**: Returns a sequence of numbers, commonly used in `for` loops.
         - **Usage**: `range(start, stop, step)`

2. **Modules**
   - Modules are files containing sets of functions and variables that can be included on other parts of the application.
   - You can use a module with the 'import' statement. 

   ```python
   import my_module as m

   m.module_function(argument)
   m.module_variable
   ```

   - There is a built-in function to list all the function or variable names in a module: dir()

   ```python
   import platform

   x = dir(platform)
   print(x)
   ```

   - When Python interpreter executes a module, the '__name__' variable sets to '__main__' if the module is the main app. If the module is being imported, '__name__' will be set to that module name. The following statement is used to run certain lines of code according to this condition: 

   ```python
   if __name__ == '__main__':
      print("Run this code if this is the main app")
   ```

3. **Lambda**

   - Lambda or anonymous functions does not require a name and are defined in one line. Lambda functions are used for simple tasks that are executed once.

   Basic syntax:
   ```python
   lambda argument: expression
   ```

   Sample:
   ```python
   square = lambda x: x ** 2
   print(square(5))
---

## 📄 License

This project is under the MIT License. This means you are free to use, modify, and distribute the code, as long as you include a copy of the license in any distribution or modification of the code.

### Terms:

Permission is granted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.
The code is provided "as is," without any warranty of any kind, express or implied, including but not limited to warranties of merchantability or fitness for a particular purpose.

### Purpose:

This code is provided for educational and training purposes. You may use it to learn, modify, and share it, but it should not be used for commercial purposes without additional authorization.

For more information, refer to the LICENSE file for the full details of the MIT License.