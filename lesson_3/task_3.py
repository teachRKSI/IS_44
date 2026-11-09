class Dog:
    def sound(self):
        return "Гав"


class Cat:
    def sound(self):
        return "Мяу"


class Cow:
    def sound(self):
        return "Му"


def chorus(animals):
    for animal in animals:
        print(f"{animal.sound()}!")


animals = [Dog(), Cat(), Cow()]
print("Хор животных:")
chorus(animals)


class Robot:
    def sound(self):
        return "Beep"


animals.append(Robot())

print("\nХор с роботом:")
chorus(animals)