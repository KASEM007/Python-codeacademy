class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("Hi I am", self.name, 'an I am', self.age, 'years old')

    def talk(self):
        print("Haww!")

        

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("Meow!")


tim = Dog("Bolt", 4)

fred = Dog("Sanbo", 3)

tim.speak()
tim.talk()
fred.speak()
fred.talk()
tim = Cat('Tim', 5, 'Black&White')
tim.speak()
tim.talk()














