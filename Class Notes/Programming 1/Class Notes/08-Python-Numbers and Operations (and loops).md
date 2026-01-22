# Numbers and Operations

5 November 2025

## Data types so far

| Data type	   | Name	|  Example		 |
|  ----		   | ---	| ---			 |
| String	   | `str`	| `"Mr. Ubial"`	 |
| Boolean	   | `bool` |`True` `False`  |
| **integers** |`int`   | `1` `2` `-100` |
| **float**	   | `float`| `1.0` `-2.3`   |
| Dictionary   |`dict`  | `{"key": "val",}`|
| Array		   | ``

## Numbers, Variables, and Operations

## Operators that work on Numbers

### Addition and Subtraction
```python
sum = 1 + 1 			# 2
diff = 10 - 8 			# 2 
another_sum = 1 + 1.0	# 2.0
```

### Multiplication and Division
```python
product = 8 * 8 		# 64
answer = 10 / 2			# 5.0
```

### Order of Operations
```python
# BEDMAS - brackets, exponents, div/mult, add/sub
answer = (2 + 3) * 4 + 2 / 3
```
### Cool Other Operations
```python
# Exponents
ans = 3 ** 2	# 9
# Floor Division
ans = 10 // 3	# 3 - answer to floor division will always be an int
# Modulo
ans = 2 % 2 	# r0
ans = 3 % 2 	# r1
ans = 4 % 2 	# r0
ans = 5 % 2  	# r1
# Increment, decrement, mult-rement, divide-rement
# Update the value of a variable
egg_count =  1
egg_count += 1		# Raises the value of egg-count
egg_count -= 1		# decreases the value of egg-count
egg_count *= 5		# multiplies the value of egg-count
egg_count /= 2		# halves the value of egg-count



```

## Loops Again
Recall: 
```python
# Repeat something 10 times
for _ in range(10):
	print("This will be printed 10 times.")
```

Iterate over a *sequence*.

```python
grocery_list = [
	"cucumbers",
	"eggs",
	"hot wheels",
	"tea"
]

# Print out a pretty version of the list 
for item in grocery_list:
	# Create a bulleted list and print it out
	bulleted_tem = "* " + item
	separator = "-------"
	print(bulleted_item)
	print(separator)
```

Output
```python
* cucumbers 
-------
* eggs 
-------
* hot wheels 
-------
* tea
-------
