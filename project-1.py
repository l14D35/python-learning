class Dog:
    def __init__(self, color):
        self.color = color

    @property
    def imie(self):
        return self.imie

    @imie.setter
    def imie(self, value):
        self.imie = value


sonia = Dog("reeeeeeeeee")
print(sonia.color)
