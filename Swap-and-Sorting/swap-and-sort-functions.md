# Swap and Sort Functions in Python

## Swap Function

A swap function is used to exchange the values of two variables. In Python, you don't typically need a separate function for this, as you can use tuple unpacking.

### Basic Swap

```python
def swap(a, b):
    return b, a

# Usage
x = 5
y = 10
x, y = swap(x, y)
print(f"After swap: x = {x}, y = {y}")
```

### In-Place Swap

In Python, you can swap values without a function:

```python
a = 5
b = 10
a, b = b, a
print(f"After swap: a = {a}, b = {b}")
```

### Swapping Elements in a List

```python
def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]

# Usage
my_list = [1, 2, 3, 4, 5]
swap_elements(my_list, 1, 3)
print(f"After swap: {my_list}")
```

## Sort Function

Sorting is the process of arranging data in a particular order, typically ascending or descending.

### Built-in sort() Method

Python lists have a built-in sort() method:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(f"Sorted numbers: {numbers}")

# Descending order
numbers.sort(reverse=True)
print(f"Sorted numbers (descending): {numbers}")
```

### sorted() Function

The sorted() function returns a new sorted list:

```python
original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(original)
print(f"Original: {original}")
print(f"Sorted: {sorted_numbers}")
```

### Custom Sort

You can sort with a key function:

```python
words = ["apple", "banana", "cherry", "date"]
sorted_by_length = sorted(words, key=len)
print(f"Sorted by length: {sorted_by_length}")
```

### Implementing Bubble Sort

As an example of a custom sort algorithm:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Usage
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(unsorted)
print(f"Sorted array: {sorted_arr}")
```

Remember, while implementing custom sort algorithms is great for learning, Python's built-in sorting functions are typically faster and more efficient for real-world use.
