class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"My name is {self.name}")


person = Person("Brian")
person.talk()

bob = Person("Sarah Bell")
bob.talk()