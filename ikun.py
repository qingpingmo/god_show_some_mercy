import sys

print("i am ikun!")
# Decorator definition
def simple_decorator(func):
    """A simple decorator that prints messages before and after function execution."""
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' finished.")
        return result
    return wrapper

# Base class
class Vehicle:
    """A base class for vehicles."""
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        return self._brand

    def start_engine(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Derived class inheriting from Vehicle
class Car(Vehicle):
    """A car class that inherits from Vehicle."""
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        self.__mileage = 0  # Private attribute

    @simple_decorator
    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is running.")

    def drive(self, distance):
        self.__mileage += distance
        print(f"Drove {distance} km. Total mileage: {self.__mileage} km.")

    @staticmethod
    def get_type():
        return "This is a land vehicle."

# A function demonstrating various features
def process_data(data):
    """Processes a list of numbers using list comprehension and lambda."""
    # List comprehension to get squares of even numbers
    squares = [x**2 for x in data if x % 2 == 0]
    
    # Using map with a lambda function
    cubes = list(map(lambda x: x**3, data))
    
    print(f"Original data: {data}")
    print(f"Squares of even numbers: {squares}")
    print(f"Cubes of all numbers: {cubes}")

# Generator function
def fibonacci_generator(n):
    """Generates Fibonacci numbers up to n."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Main execution block
if __name__ == "__main__":
    # Class instantiation and method calls
    my_car = Car("Tesla", "Model S")
    print(my_car.get_type())
    my_car.start_engine()
    my_car.drive(100)

    # Function call
    numbers = [1, 2, 3, 4, 5, 6]
    process_data(numbers)

    # Using the generator
    print("Fibonacci sequence up to 50:")
    fib_gen = fibonacci_generator(50)
    for num in fib_gen:
        print(num, end=" ")
    print()

    # Exception handling
    try:
        print("Attempting to divide by zero...")
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")
    finally:
        print("This 'finally' block always executes.")

    # Using a dictionary and a set
    my_dict = {"name": "ikun", "skill": "sing, dance, rap, basketball"}
    my_set = {1, 2, 2, 3, 4, 4, 5}
    print(f"Dictionary: {my_dict}")
    print(f"Set (duplicates removed): {my_set}")