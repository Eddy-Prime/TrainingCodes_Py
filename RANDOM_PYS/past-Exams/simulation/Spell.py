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

    def get_powerful_spells(self,threshold):
        return [s for s in self._spells if s.threshold.lower() == threshold.lower()]

    #not sure if this code is correct
    def merge_spellbook(self,other_spellbook):
        if not any(s.name == other_spellbook.name for s in self._spells):
            self._spells = other_spellbook

class Potion:
    def __init__(self,name :str , potency):
         self.name = name
         self.potency = potency

    @property
    def potency(self):
        return self._potency

    @potency.setter
    def potency(self,value):
        if not isinstance(value, float) or not (0.0 <= value <= 1.0):
            raise ValueError("Must be a float!")
        self._potency = value


class MagicWand:
    def __init__(self, wood_type : str, core):
        self.wood_type = wood_type
        self.core = core

    def __str__(self) -> str:
        wood_type = "\n".join(str(wood) for wood in self.wood_type)
    
    def __repr__(self) -> str:
        core = "\n".join(str(core) for core in self.core)

class MagicAcademy:
    def __init__(self, name: str, spellbook):
        self.name = name
        self.students = []
        self.spellbook = spellbook
    
    def add_student(self, student):
        if not any(s.name.lower() == student.name.lower() for s in self.students):
            self.students.append(student)
        else:
            raise ValueError(f"Student with name {student.name} already exists.")

    def remove_student(self, student_name):
        self.students = [s for s in self.students if s.name.lower() != student_name.lower()]

    def assign_spellbook(self, student_name, spellbook):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                student.spellbook = spellbook
                return
        raise ValueError(f"Student with name {student_name} not found.")
               
    def __str__(self):
        student_rep = "\n".join(str(student) for student in self.students)
        spellbook_summary = ", ".join(spell.name for spell in self.spellbook.spells)
        return (f"Name: {self.name}\n"
                f"Number of students: {len(self.students)}\n"
                f"Students:\n{student_rep}\n"
                f"Spellbook Summary: {spellbook_summary}")
    