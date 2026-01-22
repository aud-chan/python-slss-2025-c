# Variables, Data, Input and Output

16 September 2025

## Designing Algorithms

> A step by step procedure for solving a problem or accomplishing some end.
> Merriam-Webster

An algorithm is like a recipe. if you follow the steps, you should be able to solve the problem. 

## Variables 

We use variables to *store* values.
Variables have two parts: a **name** and a **value**.

Example: 
```python
greeting = "Hello. I am a chabot."
```

`greeting` is the **name**
`"Hello..."` is the **value**

**Get the type:** 
 `type()` - to get the data type

 
Can allow you to get the type of data of the variable 
`str` is the sequence of characters
* Enclosed in single ('') or double quotes ("")
* used for text
*   `int` -  represents numbers, can be + or - but no decimal points

  **Case Sensititve**
  ```
a = 4
A = "sally"
A will not overwrite A
```
Different sized letters (capaital or not) will represent different variables 

**Variable Names**
>* A variable name must start with a letter or an underscore character
>* A variable name cannot start with a number
>* A variable name only contain alphabets, numbers, and underscores
>* Variable names are case sensitive - AGE, Age, and age are 3 different variables
>* A variable name cannot be a Python Keyword

acceptable names: 
```
my_var="john"
_my_var="john"
MYVAR2-"john"
```
not accepted names:
```
2MYVAR="john"
my-var="john"
my var="john"
```

if number with decimal is embedded in quotation marks ("") - string
if no quotation - float
if just number no decimal - integer

three quotation marks inlcudes the "" when you run the code

`print(int(23))` - will print the number 3 when you run the code
`print(type(str(123.45)))` - prints = <class 'str'>
` print( int(53.785) )` - will print as 53 bc the int function removes all values after the integer value

```day = "Thursday"
day = 32.5
day = 19
print(day)
```
- Will print day as 19 bc it is the last value assigned to it

## Data

So far, we've used two **types of data**.

`"Mr. Ubial"` is an example of a **string**.

`32` is an example of a **integer**

`32.2` is a number, but more specifically it's an example of a **float**


### F-String
This only exists in Puthon. The F in F-string stands for **format**. To create an f-string you put an `f` in front of the opening quotation.
```python
name = f"Mr Ubial"
friends_name = "bro"
print(f"Hey {friends_name}!")
```
You can use `{}` inside of an f-string to evaluate an expression

## Input and Output
Whenever we want to get information from the user, we can use the `input()` function. 
```python
# prompt the user for their name
# store their name in a variable
print("What's your name?")
user_name = input()
```