23 September

##  `if`
Branching is a concept in computer science that allows us to write code that has *two or more different outcomes*. 

This is the "grammar" of the `if` expression. 
```python
if <statement>:
<code block - line 1> 
<...>
<code block - line n>
```

Example: 
```python
user_name = "Mr Ubial"
if user_name == "Mr Ubial"
	print("Access granted.")
	print("You can see all the secret information.")



````


## `elif and else`
`elif` and `else` are keywords we can use to extend our `if` statements. 
If we want to add *more8 branches to our statement, we can 

`elif` stands for 'else if'

```python
user_name = "Mr Ubial"
if user_name == "Mr Ubial"
	print("Access granted.")
	print("You can see all the secret information.")
elif user_name == "Spongebob":
	print("Who lives in a pineappple under the sea?")
	print("Spongebob Squarepants.")
elif user_name == "Abraham Lincoln":
	print("Abe Lincoln? I heard you're a good wrestler.")
else:
	print("I don't have any secrets for you.")
```

## Booleans

>Asking my computer science friends
>"Do you want piza OR burgers to eat for dinner"
>All of them replied:
>"YES"

**Booleans** are a type of data in Python. Booleans are binary and are either `True` or `False`.

```python
is_sunny = True

if is_sunny:
	print("You should probably wear sunscreen.")
else: 
	print("Maybe you should bring a sweater.")
```

### `or`

`or` can be used to join tqo or more statements together.
`or` is true if and only if at least one statement is True. 
```python
food_to_eat_one = "pizza"
foood_to_eat_two = "burgers"


if food_to_eat_one == "pizza" or food_to_eat_two == "burgers":
	print("We're going to eat pizza or burgers.")
else:
	print("We're not going to eat pizza or burgers.")
````


### `and`
`and` is true if and only if **both** statements are True.

```python
x = "cats"
y = "dogs"

if x == "cats" and y == "dogs":
	print("It's raining cats AND dogs.")
else
	print("We have either a cat or a dog or neither.")
```

```python
want_cookies = True
want_chips = True
if want_cookies and want_chips:
	print("You get both!")     	# This will print
else:
	print("You get none.")
```



```python
time.sleep(x seconds)
```