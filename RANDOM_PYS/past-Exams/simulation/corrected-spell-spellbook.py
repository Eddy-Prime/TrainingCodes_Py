class Spell:
    def __init__(self, name: str, element: str, power_level: int):
        self.name = name
        self.element = element
        self.power_level = power_level  # This will use the setter

    @property
    def power_level(self):
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        if not isinstance(value, int) or not (1 <= value <= 100):
            raise ValueError("Power level must be an integer between 1 and 100!")
        self._power_level = value

    def cast(self):
        return f"Casting {self.name}, a level {self.power_level} {self.element} spell!"

    def __str__(self):
        return f"Spell: {self.name} (Element: {self.element}, Power: {self.power_level})"

class Spellbook:
    def __init__(self, title: str):
        self.title = title
        self._spells = []

    @property
    def spells(self):
        return self._spells

    def add_spell(self, spell):
        if not any(s.name.lower() == spell.name.lower() for s in self._spells):
            self._spells.append(spell)

    def remove_spell(self, name):
        self._spells = [s for s in self._spells if s.name.lower() != name.lower()]

    def get_spells_by_element(self, element):
        return [s for s in self._spells if s.element.lower() == element.lower()]

    def __str__(self):
        spell_list = "\n".join(str(spell) for spell in self._spells)
        return f"Spellbook: {self.title}\nSpells:\n{spell_list}"
