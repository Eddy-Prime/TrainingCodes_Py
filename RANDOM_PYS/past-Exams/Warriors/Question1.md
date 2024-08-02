# Exercise: Warrior Class

## Warrior Class
Create a class `Warrior`. A warrior has a `name` and a list of `skills` (a skill in this model is a string). A warrior can only have one of each type of skill in their list. For example, "archery" and "Archery" are considered the same skill. We also keep track of the number of `battles` a warrior has won and whether the warrior is `active`.

The constructor of the `Warrior` class is given a `name` and one initial `skill`. Provide a method to give a string representation of a warrior based on the following example:

Alex is active
Battles won: 5
Skills: 'archery', 'swordsmanship', 'stealth'

Provide a method called `defeat` that performs the following actions on another active warrior:

1. The number of battles won by this warrior increases by 1.
2. The other warrior is now inactive.
3. This warrior acquires the other warrior's skills unless this warrior already has those skills.

**Notes:**

- An inactive warrior cannot defeat others.
- You can't defeat a warrior who is already inactive.
- The other warrior must be different from the warrior performing the defeat.
- Always provide an assert with an appropriate message.
- Warriors are considered the same if they have the same name.

## Duel Class
Create a class `Duel`. The constructor of this class takes two different active warriors as parameters. In this class, provide a method `fight` in which one warrior defeats the other warrior. Who defeats whom is determined at random.
