#Scenario: Presidents Offcial Pen
#Singleton design pattern
#why?
#only one class exsists
#prevents accidental duplication


class OfficialPen:
    __instance = None  # Private class variable that stores the single instance
    def __new__(cls):
        #__new__ is responsible for creating a new instance of a class.
        #It runs BEFORE __init__.
        #We override __new__ to control object creation and enforce Singleton behavior.


        # Check if an instance already exists
        if cls.__instance is None:
            print("Creating the President's Official Pen...")

            # Call the parent class (__new__ from object) to create the instance
            cls.__instance = super(OfficialPen, cls).__new__(cls)

            # Initialize attributes ONLY once
            cls.__instance.ink_color = "Black"
            cls.__instance.serial_number = "PRES-001"

        # If instance already exists, return the existing one
        return cls.__instance

    def sign_document(self, document_name):
        #Simulates signing an official document.
        #Parameters:
        #document_name (str): The name of the document being signed.

        print(
            f"Signing '{document_name}' with the official pen "
            f"(Serial: {self.serial_number})."
        )

# Usage
pen1 = OfficialPen()
pen2 = OfficialPen()

pen1.sign_document("Economic Reform Bill")
pen2.sign_document("International Treaty")

# Verify both variables reference the same instance
print(pen1 is pen2)

#Scenario: Car Manufacturing Plant
#Factory Method Pattern
#why?
#there are multiple car models
#each model has different features

from abc import ABC, abstractmethod

#Product Interface

class Car(ABC):
    #Abstract base class representing a generic Car.
    #All car models must implement the assemble() method.

    @abstractmethod
    def assemble(self):
        pass


#Concrete Products
class Sedan(Car):
    #Concrete implementation of a Sedan car.

    def assemble(self):
        print("Assembling Sedan: 4 doors, petrol engine, compact body.")


class SUV(Car):
    #Concrete implementation of an SUV car.

    def assemble(self):
        print("Assembling SUV: 5 doors, AWD system, high ground clearance.")


class ElectricCar(Car):
    #Concrete implementation of an Electric Car.

    def assemble(self):
        print("Assembling Electric Car: Battery pack, electric motor, zero emissions.")


#Creator (Factory)
class CarFactory(ABC):
    #Abstract Factory class.
    #Declares the factory method that subclasses must implement.


    @abstractmethod
    def create_car(self):
        pass

    def produce_car(self):
        #Centralized production process.
        #Client calls this method instead of directly creating cars.
        
        car = self.create_car()
        car.assemble()
        print("Car production completed.\n")
        return car


#Concrete Factories
class SedanFactory(CarFactory):
    #Factory responsible for creating Sedan cars.

    def create_car(self):
        return Sedan()


class SUVFactory(CarFactory):
    #Factory responsible for creating SUV cars.

    def create_car(self):
        return SUV()


class ElectricCarFactory(CarFactory):
    #Factory responsible for creating Electric Cars.
    
    def create_car(self):
        return ElectricCar()


#Client Code
if __name__ == "__main__":
    sedan_factory = SedanFactory()
    suv_factory = SUVFactory()
    electric_factory = ElectricCarFactory()

    sedan_factory.produce_car()
    suv_factory.produce_car()
    electric_factory.produce_car()
    
#Scenario: Drawing tool
#Prototype Pattern
#why?
#Users create shapes (Circle, Rectangle, etc.)
#Shapes have properties (color, size, position)
#Users want to duplicate an existing shape

import copy
from abc import ABC, abstractmethod

#Prototype Base Class

class Shape(ABC):
    # Base class for all shapes
    # Contains common properties and the clone method

    def __init__(self, color, x, y):
        self.color = color      # Shape color
        self.x = x              # X position
        self.y = y              # Y position

    @abstractmethod
    def draw(self):
        # Each shape must implement its own draw method
        pass

    def clone(self):
        # Creates a deep copy of the object
        # deepcopy ensures all attributes are copied properly
        return copy.deepcopy(self)


#Concrete Prototype: Circle

class Circle(Shape):
    def __init__(self, color, x, y, radius):
        super().__init__(color, x, y)
        self.radius = radius  # Circle-specific property

    def draw(self):
        print(f"Drawing Circle: Color={self.color}, "
              f"Position=({self.x},{self.y}), Radius={self.radius}")


#Concrete Prototype: Rectangle
class Rectangle(Shape):
    def __init__(self, color, x, y, width, height):
        super().__init__(color, x, y)
        self.width = width      # Rectangle-specific property
        self.height = height    # Rectangle-specific property

    def draw(self):
        print(f"Drawing Rectangle: Color={self.color}, "
              f"Position=({self.x},{self.y}), "
              f"Width={self.width}, Height={self.height}")

#Client Code
if __name__ == "__main__":

    # Create an original circle
    circle1 = Circle("Red", 10, 20, 15)
    circle1.draw()

    # Clone the circle using Prototype pattern
    circle2 = circle1.clone()

    # Modify the cloned object to show it's independent
    circle2.x = 50
    circle2.color = "Blue"

    circle2.draw()

    # Verify they are different objects in memory
    print("Are they the same object?", circle1 is circle2)
    
#Scenario: Global Counter
#Singleton design pattern
#why?
#You need only one counter
#It must be shared across different parts of the application
#All components must access the same instance
#The count must remain consistent everywhere

class GlobalCounter:
    # Private class variable to store the single instance
    __instance = None

    def __new__(cls):
        # __new__ controls object creation

        # If no instance exists, create one
        if cls.__instance is None:
            print("Creating Global Counter instance...")
            cls.__instance = super(GlobalCounter, cls).__new__(cls)

            # Initialize counter only once
            cls.__instance.count = 0

        # Return the existing instance
        return cls.__instance

    # Method to increase the counter
    def increment(self):
        self.count += 1

    # Method to get the current count
    def get_count(self):
        return self.count


# Simulating different parts of the application
if __name__ == "__main__":

    # First component
    counter1 = GlobalCounter()
    counter1.increment()
    counter1.increment()

    print("Counter from component 1:", counter1.get_count())

    # Second component
    counter2 = GlobalCounter()
    counter2.increment()

    print("Counter from component 2:", counter2.get_count())

    # Check if both references point to the same object
    print("Are both counters the same instance?", counter1 is counter2)
    
#Scenario: Global Counter
#Director pattern
#what is director pattern?
#
#why?
#You start with a basic card template.
#Users can add a custom message.
#Users can apply different themes

# Base Component
class GreetingCard:
    def generate(self):
        return "Greeting Card"


# Concrete Component (Template)
class BirthdayCard(GreetingCard):
    def generate(self):
        return "Happy Birthday Card"


# Decorator Base Class
class CardDecorator(GreetingCard):
    def __init__(self, card):
        self.card = card

    def generate(self):
        return self.card.generate()


# Concrete Decorator – Custom Message
class MessageDecorator(CardDecorator):
    def __init__(self, card, message):
        super().__init__(card)
        self.message = message

    def generate(self):
        return self.card.generate() + f"\nCustom Message: {self.message}"


# Concrete Decorator – Theme
class ThemeDecorator(CardDecorator):
    def __init__(self, card, theme):
        super().__init__(card)
        self.theme = theme

    def generate(self):
        return self.card.generate() + f"\nTheme Applied: {self.theme}"


# Client Code
if __name__ == "__main__":
    
    # Start with a basic birthday card template
    card = BirthdayCard()

    # Add a custom message
    card = MessageDecorator(card, "Wishing you all the best!")

    # Apply a theme
    card = ThemeDecorator(card, "Blue Floral Theme")

    # Generate final personalized card
    print(card.generate())
