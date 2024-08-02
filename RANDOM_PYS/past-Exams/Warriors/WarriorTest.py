import pytest
from Warrior import Warrior  

# Creating a Warrior instance with a name and skill
def test_create_warrior_instance():
    warrior = Warrior(name="Arthur", skill="Sword")
    assert warrior.name == "Arthur"
    assert "sword" in warrior.skills
    assert warrior.battles == []
    assert warrior.wins == 0
    assert not warrior.dead
    assert warrior.active

# Defeating a Warrior with no battles
def test_defeat_warrior_no_battles():
    warrior1 = Warrior(name="Arthur", skill="Sword")
    warrior2 = Warrior(name="Lancelot", skill="Shield")
    warrior1.defeat(warrior2)
    assert warrior2.dead
    assert not warrior2.active
    assert len(warrior1.battles) == 1
    assert "shield" in warrior1.skills

# Adding a skill to a Warrior instance
def test_add_skill_to_warrior_instance():
    warrior = Warrior(name="Lancelot", skill="Lance")
    warrior.skills.add("shield")
    assert "lance" in warrior.skills
    assert "shield" in warrior.skills

