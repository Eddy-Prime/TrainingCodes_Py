# Python Exam Simulation and Practice Tasks

## Exam Simulation (19/08/2024)

**Total Points:** 20  
**Time:** 60 minutes

### Question 1: Spell Class (10 points)

Create a class called `Spell`. A spell has a `name`, `element` (e.g., fire, water, earth, air), and `power_level` (an integer). Implement the following:

a) Constructor that takes `name`, `element`, and `power_level` as parameters.
b) A property for `power_level` with a setter that ensures the power level is between 1 and 100. If an invalid value is provided, raise a ValueError.
c) A method called `cast()` that returns a string in the format "Casting [name], a level [power_level] [element] spell!"
d) A string representation method that returns the spell's information in the format "Spell: [name] (Element: [element], Power: [power_level])".

### Question 2: Spellbook Class (10 points)

Create a class called `Spellbook`. A spellbook has a `title` and contains a collection of `Spell` objects. Implement the following:

a) Constructor that takes a `title` parameter and initializes an empty list to store spells.
b) A method called `add_spell(spell)` that adds a `Spell` to the spellbook. Ensure that no two spells with the same name can be added (case-insensitive).
c) A method called `remove_spell(name)` that removes a spell from the spellbook based on its name (case-insensitive).
d) A method called `get_spells_by_element(element)` that returns a list of all spells in the spellbook of the given element.
e) A string representation method that returns the spellbook's information, including its title and a list of all spells it contains.

## Additional Practice Tasks

To improve your Python skills, complete the following tasks:

1. **Property and Setter Practice**
   - Create a class `Potion` with properties for `name` and `potency`.
   - The `potency` should be a float between 0.0 and 1.0.
   - Implement a setter that enforces this range.

2. **List Comprehension and Filtering**
   - Add a method to the `Spellbook` class called `get_powerful_spells(threshold)`.
   - This method should return a list of all spells with a power level above the given threshold.

3. **String Representation**
   - Create a class `MagicWand` with attributes for `wood_type` and `core`.
   - Implement both `__str__()` and `__repr__()` methods for this class.

4. **Method Implementation**
   - Add a method to the `Spellbook` class called `merge_spellbook(other_spellbook)`.
   - This method should add all non-duplicate spells from `other_spellbook` to this spellbook.

5. **Reading and Implementing Requirements**
   - Create a class `MagicAcademy` that has a name, a list of students (strings), and a `Spellbook`.
   - Implement methods to add/remove students, assign a spellbook, and get a string representation of the academy.
   - The string representation should include its name, number of students, and a summary of its spellbook.

Good luck with your practice!
