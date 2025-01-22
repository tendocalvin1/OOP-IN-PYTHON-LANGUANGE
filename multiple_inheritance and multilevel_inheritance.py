#multiple inheritance = Inherit from more than one parent class
#                       C(A,B)
# multilevel inheritance = Inherit from a parent which inherits from another parent
#                           c(B) < --B(A) <--A

class Prey:
    def flee(self):
        print("This animal is fleeing.")
    

class Predator:
    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

class Hawk(Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()