import random

class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapons = [weapon]
        self.killed = 0
        self.alive = True

    def __str__(self):
        status = "alive" if self.alive else "dead"
        return f"{self.name} is {status}\nNumber killed: {self.killed}\nWeapons: {', '.join(self.weapons)}"

    def assassinate(self, other):
        assert self.alive, "A dead player cannot kill."
        assert other.alive, "You can't kill a player who is already dead."
        assert self != other, "The other player must be different from the player committing the murder."
        self.killed += 1
        other.alive = False
        self.weapons += [weapon for weapon in other.weapons if weapon not in self.weapons]

    def __eq__(self, other):
        return self.name == other.name

class Battle:
    def __init__(self, player1, player2):
        self.players = [player1, player2]

    def fight(self):
        killer, victim = random.sample(self.players, 2)
        killer.assassinate(victim)

# Create two different players
player1 = Player("John", "spear")
player2 = Player("Jane", "rifle")

# Have them fight each other in a battle
battle = Battle(player1, player2)
battle.fight()

# Print the players
print(player1)
print(player2)
