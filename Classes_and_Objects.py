class Robot:
    
    #Constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

#r1 & r2 are 'Attributes'
        
        #NOTE : once we start to use the constructor in our class the default constructor is gonna be gone
            # is this case the default constructor is : def __init__(self):
                #and the default is the one that is below eg. r1 = Robot()


#r1 = Robot()
#r1.name = "Tom"
#r1.color = "green"
#r1.weight = 30 
        
#///This is the much cleaner way to do it instead of the one above

r1 = Robot("Tom", "green", 30)        
r1.introduce_self()  

#Quick Explanation : the "r1.introduce_self() " is gonna got back to the "print("My name is " + self.name)"
# and the "self.name" is gonna go back to the "r1.name = "Tom" " and the "Tom" is gonna go back to the "print("My name is " + self.name)"

#r2 = Robot()
#r2.name = "Jerry"   
#r2.color = "blue"
#r2.weight = 40

#///This is the much cleaner way to do it instead of the one above
r2 = Robot("Jerry", "blue", 40)
r2.introduce_self()

#Quick Explanation : the "r2.introduce_self() " is gonna got back to the "print("My name is " + self.name)"
