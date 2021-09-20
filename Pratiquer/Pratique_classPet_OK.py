class Pet:
    def __init__(self, name, legs, greeting = "Hello"):
        self.name = name
        self.greeting = greeting
        self.legs = legs
        
    def say_hi(self):
        print(f"{self.greeting}, I'm {self.name}!")

    def legs_count(self):
        print(f"I have {self.legs} legs !")

#my_pet = Pet("Gaston")
#my_pet.say_hi()


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, 4, "Meow")

cat = Cat("Felix")
cat.say_hi()
cat.legs_count()


class Parrot(Pet):
    def __init__(self, name):
        super().__init__(name, 2, "Cui-cui")

    def say_hi(self):
        print(f"{self.greeting}, My name is {self.name}!")

my_parrot = Parrot("Robert")
my_parrot.say_hi()
my_parrot.legs_count()