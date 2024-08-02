from random import randint

class Warrior:
    def __init__(self, name, skill):
        self.name = name
        self.skills = set()
        self.skills.add(skill.lower())
        self.battles = []
        self.wins = 0
        self.dead = False
        self.active = True

    def defeat(self, warrior):
        assert self.active, "Dead player cannot defeat others"
        assert not self.__eq__(warrior), "A player must defeat a different player"
        assert warrior.active, "The other player must be alive to be defeated"
        
        self.battles.append(warrior)
        self.wins += 1
        warrior.dead = True
        warrior.active = False
        
        new_skills = warrior.skills - self.skills
        self.skills = self.skills.union(new_skills)

    def __eq__(self, other_warrior) -> bool:
        if not isinstance(other_warrior, self.__class__):
            return False
        return self.name == other_warrior.name

    def __repr__(self) -> str:
        status = "alive" if self.active else "dead"
        skills = "No weapons" if not self.skills else f"Weapons: {', '.join(self.skills)}"
        return f"{self.name} is {status}\nDefeats: {self.wins}\n{skills}"

class Duel:
    def __init__(self, player1, player2):
        assert player1.active and player2.active, "Both players in a duel must be alive"
        self.player1 = player1
        self.player2 = player2

    def fight(self):
        winner = self.player1 if randint(1, 2) == 1 else self.player2
        loser = self.player2 if winner == self.player1 else self.player1
        winner.defeat(loser)