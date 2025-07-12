import os
import sys
import time
import functools
import threading
import dataclasses
from typing import List, Dict, Any, Optional, Callable, TypeVar, Generic
from contextlib import contextmanager
from abc import ABC, abstractmethod

print("shit!")
# Type variables for generics
T = TypeVar('T')
S = TypeVar('S')

# Decorators
def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"{func.__name__} took {elapsed:.3f} seconds to run")
        return result
    return wrapper

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator

# Context manager
@contextmanager
def changed_directory(directory):
    original_dir = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(original_dir)

# Abstract base class
class Animal(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def make_sound(self) -> str:
        pass
    
    def introduce(self):
        return f"I am {self.name} and I {self.make_sound()}"

# Inheritance
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self) -> str:
        return "bark"
    
    def __str__(self):
        return f"{self.name} ({self.breed})"

# Multiple inheritance
class Pet:
    def __init__(self, owner: str):
        self.owner = owner
    
    def get_owner(self):
        return self.owner

class PetDog(Dog, Pet):
    def __init__(self, name: str, breed: str, owner: str):
        Dog.__init__(self, name, breed)
        Pet.__init__(self, owner)

# Data class
@dataclasses.dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Generic class
class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)

# Property and property setter
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (value - 32) * 5/9

# List comprehension and generator expression
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers if x % 2 == 0]
sum_of_cubes = sum(x**3 for x in numbers)

# Lambda function and high-order functions
multiply = lambda x, y: x * y
result = list(map(lambda x: x*2, filter(lambda x: x > 5, numbers)))

# Multithreading
def worker(name):
    print(f"Worker {name} started")
    time.sleep(2)
    print(f"Worker {name} finished")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for thread in threads:
    thread.start()

# Example usage
@timing_decorator
@retry(max_attempts=2)
def complex_function(a, b):
    print(f"Executing complex function with {a} and {b}")
    return a + b

if __name__ == "__main__":
    # Use the classes and functions
    fido = PetDog("Fido", "Labrador", "John")
    print(fido.introduce())
    
    temp = Temperature(25)
    print(f"Celsius: {temp.celsius}, Fahrenheit: {temp.fahrenheit}")
    temp.fahrenheit = 100
    print(f"After conversion - Celsius: {temp.celsius:.2f}")
    
    point = Point(3, 4)
    print(f"Distance from origin: {point.distance_from_origin()}")
    
    string_stack = Stack[str]()
    string_stack.push("Hello")
    string_stack.push("World")
    print(f"Popped: {string_stack.pop()}")
    
    with changed_directory("/tmp"):
        print(f"Current directory: {os.getcwd()}")
    
    result = complex_function(10, 20)
    print(f"Result: {result}")
    
    for thread in threads:
        thread.join()
    
    print("All tasks completed!")