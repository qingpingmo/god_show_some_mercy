import functools
import asyncio
from typing import List, Dict, Optional, TypeVar, Generic
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from collections import defaultdict
from contextlib import contextmanager
from functools import reduce

print("fuck!")
import concurrent.futures

# Type variables for generics
T = TypeVar('T')
U = TypeVar('U')

# Decorator examples
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Class decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

# Abstract base class
class Animal(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def make_sound(self) -> str:
        pass
    
    @property
    def species(self) -> str:
        return self.__class__.__name__

# Inheritance example
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self) -> str:
        return "Woof!"
    
    def __str__(self) -> str:
        return f"{self.name} is a {self.breed} dog"

# Multiple inheritance
class Pet:
    def __init__(self, owner: str):
        self.owner = owner
    
    def get_owner(self) -> str:
        return f"Owned by {self.owner}"

class DomesticDog(Dog, Pet):
    def __init__(self, name: str, breed: str, owner: str):
        Dog.__init__(self, name, breed)
        Pet.__init__(self, owner)
    
    def __str__(self) -> str:
        return f"{super().__str__()} {self.get_owner()}"

# Dataclass example
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

# Generic class
class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> Optional[T]:
        if not self.items:
            return None
        return self.items.pop()
    
    def __iter__(self):
        return iter(reversed(self.items))

# Context manager
@contextmanager
def managed_resource(name: str):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")

# Async functions
async def fetch_data(delay: int) -> str:
    await asyncio.sleep(delay)
    return f"Data after {delay} seconds"

async def process_data():
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    return results

# Using comprehensions, lambdas
def demo_features():
    # List comprehension
    squares = [x**2 for x in range(10) if x % 2 == 0]
    
    # Dict comprehension
    name_to_length = {name: len(name) for name in ["Alice", "Bob", "Charlie"]}
    
    # Generator expression
    sum_of_cubes = sum(x**3 for x in range(5))
    
    # Lambda function with map and filter
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    
    # Functional programming with reduce
    product = reduce(lambda x, y: x * y, numbers, 1)
    
    return {
        "squares": squares,
        "name_lengths": name_to_length,
        "sum_of_cubes": sum_of_cubes,
        "doubled": doubled,
        "evens": evens,
        "product": product
    }

# Using all the features
@singleton
class Application:
    def __init__(self):
        self.data = defaultdict(list)
    
    @logger
    def run(self):
        # Create objects
        fido = DomesticDog("Fido", "Golden Retriever", "John")
        point = Point(3.0, 4.0)
        
        # Use generic class
        number_stack = Stack[int]()
        for i in range(5):
            number_stack.push(i)
        
        # Use context manager
        with managed_resource("database") as db:
            print(f"Working with {db}")
        
        # Run async code
        async_results = asyncio.run(process_data())
        
        # Use multi-threading
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(lambda: [i**2 for i in range(10)])
            thread_results = future.result()
        
        # Call other functions
        feature_results = demo_features()
        
        return {
            "dog": str(fido),
            "point_distance": point.distance_from_origin(),
            "stack_contents": [item for item in number_stack],
            "async_results": async_results,
            "thread_results": thread_results,
            "feature_results": feature_results
        }

# Run the application
app = Application()
result = app.run()
print("Final results:", result)