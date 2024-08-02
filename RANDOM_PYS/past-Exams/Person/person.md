# Python Class Tasks

## Task 1: Person Class

Create a `Person` class with properties for `name`, `age`, and `email`. Implement appropriate validation for each property.

### Requirements
- The `name` should be a non-empty string.
- The `age` should be a positive integer.
- The `email` should be a non-empty string containing "@".
- Implement getter and setter methods for each property with the necessary validation.

### Example
```python
p = Person("John Doe", 30, "john.doe@example.com")
print(p.name)  # Output: John Doe
print(p.age)   # Output: 30
print(p.email) # Output: john.doe@example.com
```

## Task 2: Movie Class
Create a `Movie` class with properties for `title`, `director`, and `release_year`. Implement a method that returns a formatted string with the movie’s details.

### Requirements
- The `title` and `director` should be non-empty strings.
- The `release_year` should be a positive integer.
- Implement getter and setter methods for each property with the necessary validation.
- Implement a `get_details` method that returns a string in the format: "Title directed by Director, released in Year".

## Task 3: Playlist Class
Create a `Playlist` class that manages a list of `Song` objects. Implement methods to add, remove, and list songs, ensuring no duplicate songs (based on title and artist) are added.

### Requirements
- Create a `Song` class with properties `title` and `artist`, both of which should be non-empty strings.
- In the `Playlist` class, implement methods:
    - `add_song(song)`: Adds a song to the playlist if it is not already present (based on title and artist).
    - `remove_song(title, artist)`: Removes a song from the playlist based on the given title and artist.
    - `list_songs()`: Returns a list of strings with each song’s details in the format "Title by Artist".
