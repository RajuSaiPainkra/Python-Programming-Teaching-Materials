# Python Exceptions
# Exception Handling in Python

# Exception Related to Execution and Getting Error during the # execution of the code

# Most Common Exception in Python
# ZeroDivisionError - Occurs when dividing by zero
# SyntaxError - Occurs when there is a syntax error in the code
# TypeError - Occurs when an operation or function is applied to an object of inappropriate type
# IndentationError - Occurs when there is an indentation error in the code
# NameError - Occurs when a local or global name is not found



## SyntaxError : does'n follow the Syntax Rules of Python
        # with Opening or Closing Parenthesis, Brackets, or Quotes
        # String Literal without Closing Quotes
        # structure of the code is not correct

# Example of SyntaxError
# print("Hello, World!" # Missing closing parenthesis
# print("Hello, world!) # Missing closing quote
# print("Hello, 
# World!") # Missing closing quote and parenthesis




## NameError : Occurs when a local or global name is not found

# Example of NameError:
# print(Hello, Echo) # Hello and Echo are not defined variables or functions
# print(x)


## IndentationError : Occurs when there is an indentation error in the code

# Example of IndentationError:
# def my_function():
# print("Hello, World!") # Missing indentation
# def my_function():
#     print("Hello, World!") # Correct indentation



## TypeError : Occurs when an operation or function is applied to an object of inappropriate type
# Example of TypeError:
# print("Hello" + 5) # Cannot concatenate str and int
# print("Hello" + str(5)) # Correct way to concatenate str and int
# print("Hello" + str(5)) # Correct way to concatenate str and int
# print(5 + "Hello") # Cannot add int and str
# print(5 + str("Hello")) # Correct way to concatenate int and str
# print(5 + str("Hello")) # Correct way to concatenate int and str