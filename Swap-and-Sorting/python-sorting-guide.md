# Python Sorting Guide

This guide demonstrates how to sort different data structures in Python using `.sort()` and `sorted()` methods.

## Sorting Lists

```python
fruits = ["banana", "orange", "apple", "coconut"]

# Sort in ascending order
# fruits.sort()

# Sort in descending order
# fruits.sort(reverse=True)

print(fruits)
```

## Sorting Tuples

```python
fruits = ("banana", "orange", "apple", "coconut")

# Sort in ascending order
# fruits = tuple(sorted(fruits))

# Sort in descending order
# fruits = tuple(sorted(fruits, reverse=True))

print(fruits)
```

## Sorting Dictionaries

```python
fruits = {
   "banana": 105,
   "apple": 72,
   "orange": 73,
   "coconut": 354
}

# Sort by keys in ascending order
# fruits = dict(sorted(fruits.items()))

# Sort by keys in descending order
# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))

# Sort by values in ascending order
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))

# Sort by values in descending order
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

print(fruits)
```

## Sorting Objects

```python
class Fruit:
   def __init__(self, name, calories):
       self.name = name
       self.calories = calories

   def __repr__(self):
       return f"{self.name}: {self.calories}"

fruits = [
    Fruit("banana", 105),
    Fruit("apple", 72),
    Fruit("orange", 73),
    Fruit("coconut", 354)
]

# Sort by name in ascending order
# fruits = sorted(fruits, key=lambda fruit: fruit.name)

# Sort by name in descending order
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)

# Sort by calories in ascending order
# fruits = sorted(fruits, key=lambda fruit: fruit.calories)

# Sort by calories in descending order
# fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)
```

Note: Uncomment the desired sorting method in each section to see it in action.
