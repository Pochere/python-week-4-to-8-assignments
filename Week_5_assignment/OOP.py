# MAIN CLASS: The base class representing the general laptop
class Laptop:

# ATTRIBUTES: These define the properties of the Laptop class.
    def __init__(self, brand, model, processor, ram, storage):

        self.brand = brand  # The brand of the laptop (e.g., Dell, HP)
        self.model = model  # The model name of the laptop (e.g., Inspiron, Pavilion)
        self.processor = processor # The processor type (e.g., Intel i7, AMD Ryzen)
        self.ram = ram  # RAM size in GB
        self.storage = storage  # Storage size in GB
        self.powered_on = False  # Tracks whether the laptop is on or off


# METHOD: A behavior the laptop can perform, in this case, powering on.

    def power_on(self):
        # Turns the laptop on if it's off.
        if not self.powered_on:
            self.powered_on = True
            return f"{self.brand} {self.model} is now powered on."
        else:
            return f"{self.brand} {self.model} is already on."

    def power_off(self):
        # Turns the laptop off if it's on.
        if self.powered_on:
        # Encapsulated attribute: managed through methods, not directly accessed
            self.powered_on = False
            return f"{self.brand} {self.model} is now powered off."
        else:
            return f"{self.brand} {self.model} is already off."


# SUBCLASS: This class extends the Laptop class, inheriting its attributes and methods.
class GamingLaptop(Laptop):

# INHERITANCE: GamingLaptop inherits from Laptop, adding extra functionality.  
    def __init__(self, brand, model, processor, ram, storage, graphics_card):
       # Initializes a gaming laptop, including all attributes from the general laptop plus a graphicsrd.
        super().__init__(brand, model, processor, ram, storage)
        self.graphics_card = graphics_card

# METHOD: A behavior unique to GamingLaptop
    def enable_gaming_mode(self):

       # POLYMORPHISM: GamingLaptop has additional functionality beyond the base class.
        return f"{self.brand} {self.model} is now in Gaming Mode with {self.graphics_card} graphics."


# Demonstrating the usage of the Laptop and GamingLaptop classes
if __name__ == "__main__":
    # Creating a regular laptop object
    my_laptop = Laptop("Dell", "XPS 15", "Intel i7", 16, 512)

    # Creating a gaming laptop object
    gaming_laptop = GamingLaptop("Alienware", "M15", "Intel i9", 32, 1000, "NVIDIA GTX 3080")

    # Using the methods for the regular laptop
    print(my_laptop.power_on())       # Turns on the laptop
    print(my_laptop.power_off())      # Turns off the laptop

    # Using the methods for the gaming laptop
    print(gaming_laptop.power_on())   # Turn on the gaming laptop
    print(gaming_laptop.enable_gaming_mode())  # Enable gaming mode
    print(gaming_laptop.power_off())  # Turn off the gaming laptop
