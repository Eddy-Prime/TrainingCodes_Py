# Adding and Removing Items in Python Data Structures

## Lists

**Add Item**
- Use `append(item)` to add an item to the end of the list.
- Use `insert(index, item)` to add an item at a specific index.

**Remove Item**
- Use `remove(item)` to remove the first occurrence of an item.
- Use `pop(index)` to remove an item at a specific index and return it.

### Example

```python
my_list = [1, 2, 3]

# Add items
my_list.append(4)  # Adds 4 to the end
my_list.insert(1, 5)  # Inserts 5 at index 1

# Remove items
my_list.remove(2)  # Removes the first occurrence of 2
item = my_list.pop(1)  # Removes the item at index 1 and returns it


Dictionaries

**Add Item**

Assign a value to a new key or update an existing key using `my_dict[key] = value`.

**Remove Item**

Use `pop(key)` to remove an item by key and get its value.
Use `del my_dict[key]` to remove an item by key without returning the value.

### Example
```python
my_dict = {'a': 1, 'b': 2}

# Add item
my_dict['c'] = 3  # Adds or updates the key 'c' with value 3

# Remove items
value = my_dict.pop('b')  # Removes the item with key 'b' and returns its value
del my_dict['a']  # Removes the item with key 'a'
```

## Sets 

**Add Item**

Use `add(item)` to add an item to the set.

**Remove Item**

Use `remove(item)` to remove an item from the set (raises KeyError if the item is not found).
Use `discard(item)` to remove an item from the set (does nothing if the item is not found).

### Example
```python
my_set = {1, 2, 3}


# Add item
my_set.add(4)  # Adds 4 to the set

# Remove items
my_set.remove(2)  # Removes 2 from the set (raises KeyError if not found)
my_set.discard(5)  # Removes 5 from the set (does nothing if 5 is not found)
```


