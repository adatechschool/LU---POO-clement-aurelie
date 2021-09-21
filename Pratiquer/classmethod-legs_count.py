class Pet:
    def __init__(self, name, greeting = "Hello"):
        self.name = name
        self.greeting = greeting
        
        
    def say_hi(self):
        print(f"{self.greeting}, I'm {self.name}!")
        
    @classmethod
    def legs_count(cls, legs):
     cls.legs = legs
     return(f" I have {cls.legs} legs !")

#my_pet = Pet("Gaston")
#my_pet.say_hi()

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Meow")

cat = Cat("Felix")
cat.say_hi()
print(Cat.legs_count("4"))



class Parrot(Pet):
    def __init__(self, name):
        super().__init__(name, "Cui-cui")

    def say_hi(self):
        print(f"{self.greeting}, My name is {self.name}!")

my_parrot = Parrot("Robert")
my_parrot.say_hi()
print(Parrot.legs_count("2"))