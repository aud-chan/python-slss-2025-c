# Functions *Friends*

8 October 2025

```python
print("Hello")
print("2.1")
```

Print is a **function** that outputs values to the consoles. 

```python
user_information = input("Some prompt: ")
```

Input is a **function** that waits for a user to give some information, then it *returns* their input. 

## What is a Function?
> A function is a **block of usable code** with a **name*

## `def`ining your own Function

```python
def <function_name>(<operational params>): 
	<code block>
```

1. Use the `def` keyword
2. Give the unction a *good* **name**
       - convention - use lowercase characters and underscores
3. write your code in an **indented code block**

## Calling a **Function**

When we use a function, we say that we **call** it. 
We call a function by using its name followed byparentheses. If there are any values that the function **needs**. we put those values inside the parentheses.

```python
<function_name?(<optional arguments>)
```

## Practical Example
We can **normalize input** so that our programs can be more robust

```python
weather_reply = input("What's the weather like?").lower().strip(",.?! ")
	print	
```

To optimize the code above, we can use **functions**

```python
def normailized_input():
	# get input from the user
	output = input()
	# .strip and .lower the input
	output = output.strip(",?! ").lower()
	# return the ouput
	return output 

# Ask the user for the weather 
print("What's the weather like?")
weather_reply = normalized_input()

if weather_reply == "rainy":
	print("You should bring an umbrealla.")
```

## Parameters
**Parameters** are the **inputs** of the function

```python
# Create a function that represents f(x) = x^2
def squared(num: float):
	output = num ** 2
	print(output)

def power(num: float, exp: float):
	"""Raise a number to a power."""
	
squared(2) #4 
squared)6.5) #6.5 * 6.5
power(2, 2) #4

````
## `return` values

The **return** keyword iis used to give the the function an **output** value. 
In a function, the `return` keywoord will stop the excution of the rest of the function. 
```python
def some_fun():
	print("hello!")

def some_fun_return() -> str:
	print("hello!")
	return "hello"

return_val = some_fun()

print(return_val) # what's the difference?

return_val = some_fun_return()

print(return_val) # what's the difference?
```

## Default Arguments

**Parameters** are the *inputs* to a function.

**Arguments** are the *values* given as inputs.
```python
# our example from notes-3-functions.py
# default name -> "Tiger"
def say_hello_personal(name="Tiger" str):
	print(f"hello {name}") 

say_hello_personal("David") # David is the argument
say_hello_personal()
```

