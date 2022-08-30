class Dog:
    species = "Cans familiars"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


golden = GoldenRetriever('golden', 8)
g = golden.speak(sound='Bark')
print(g)
