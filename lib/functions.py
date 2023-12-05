#!/usr/bin/env python3

def greet_programmer():
     print("Hello, programmer!")

def greet(name):
     print(f"Hello, {name}!")
greet("Guido")
     


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("James")
def add(num1, num2):
    return num1 + num2

result = add(3, 5)
print(result)

def halve(number):
    return number/2
results=halve(3)
print(results)
