import os

def clear():
    os.system('cls')

def question():
    clear()
    char = input("input char: ")
    if char == '+':
        plus()
    elif char == '-':
        minus()
    elif char == '*':
        multiply()
    elif char == '/':
        divide()

def plus():
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x + y
    print("result: ", res)
    cmd = input("input 'exit' for closing app... ")

def minus():
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x - y
    print("result: ", res)
    cmd = input("input 'exit' for closing app... ")

def divide():
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x / y
    print("result: ", res)
    cmd = input("input 'exit' for closing app... ")

def multiply():
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x * y
    print("result: ", res)
    cmd = input("input 'exit' for closing app... ")