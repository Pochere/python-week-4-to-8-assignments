# BASE CLASS: To represent general animal behavior

class Animal:
    def move(self):
        pass  # To be overridden by specific animal behavior


# SUBCLASSES: For common animals
class Dog(Animal):
    def move(self):
        return "The dog runs energetically across the field."


class Cat(Animal):
    def move(self):
        return "The cat stealthily prowls through the grass."


class Rabbit(Animal):
    def move(self):
        return "The rabbit hops quickly, looking for food."


class Bird(Animal):
    def move(self):
        return "The bird flies gracefully through the sky."


# Function to demonstrate polymorphism
def demonstrate_animal_movement(animals):
    for animal in animals:
        print(animal.move())


# Instantiate objects
dog = Dog()
cat = Cat()
rabbit = Rabbit()
bird = Bird()

# Create a list of animals
common_animals = [dog, cat, rabbit, bird]

# Polymorphism in action
for animal in [Dog(), Cat(), Rabbit(), Bird()]:
   print (animal.move())

