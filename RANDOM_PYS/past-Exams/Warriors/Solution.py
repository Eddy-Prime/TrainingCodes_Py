#write your code here, Happy coding (:
from random import randint
class Warrior:
    def __init__(self,name,skill):
        self.name = name
        self.skills = set()
        self.skills.add(skill.lower())
        self.battles = []
        self.wins = 0
        self.dead = False
        self.active = True

    def defeat(self,warrior) :
        assert not self.battles, "dode speler kan niet moorden"
        assert not self.__eq__(warrior), "speler moet andere speler doden"
        assert not warrior.active, "andere speler moet levend zijn"
        self.battles += 1
        warrior.dead = True
        d = self.skills.intersection(warrior.skill)
        self.skills = self.skills.union(warrior.skill)
        warrior.skill = d   

    def __eq__(self, other_warrior) -> bool:
        if not isinstance(other_warrior,self.__class__):
            return False
        return self.name == other_warrior.name

    def __repr__(self) -> str:
        sActive = ("levend" if not self.dead else "dood")
        sKills = ""
        if len(self.skills) == 0:
            sSkills = "Heeft geen wapens"
        else:
            sSkills = str(self.skills)
            sSkills = "Wapens: " + sSkills[1:len(sSkills) - 1]
        return self.name + " is " + sActive + "\naantal vermoord " + str(self.wins) + "\n" + sKills
    

class Duel:
    def __init__(self,player1,player2):
        assert not player1.dead and not player2.dead, "speler in gevecht moet levend zijn"
        self.player1 = player1
        self.player2 = player2
    def fight(self):
        i = randint(1,2)
        if i == 1:
            self.player1.dead(self.player2)
        else:
            self.player2.dead(self.player1)

