class Dog:
    species = "Cans familiars"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} barks: {sound}'

    def coat_color(self, coat_color):
        return f'{self.name} is {self.age}, {self.speak("gbo gbo")}, philo\'s coat is {coat_color}'


class JackRusselTerrier(Dog):
    def speak(self, sound='Arf'):
        return super().speak(sound)


class Bulldog(Dog):
    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9, "Jack Russell Terrier")
miles = Dog("Miles", 4, "Dachshund")
philo = Dog("Philos", 5, "Bulldog")
jack = JackRusselTerrier("Jim", 5, "Bulldog")
j = jack.speak('Arf')
print(j)

jim = Bulldog("Jim", 5, 'bulldog')
i = jim.speak('woof')
print(i)


# for dog in (buddy, miles, philo):
#     print(f'The {dog.name} is {dog.age} years old')


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        return f'The {self.color} has {self.mileage} miles.'

    def drive(self, gear):
        return f'{gear} + {self.mileage}'


red_car = Car(color='blue', mileage=20_000)
blue_car = Car(color='red car', mileage=30_000)
for car in (blue_car, red_car):
    print(f"{car.color} car has {car.mileage:,} miles")
