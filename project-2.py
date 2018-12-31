class Dog:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color

sonia = Dog("czarny")
print(sonia.get_color())
