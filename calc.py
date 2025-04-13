def question():
    char = input("input char: ")
    if char == '+':
        plus()

def plus():
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x + y
    print("result: ", res)
    cmd = input("input 'exit' for closing app... ")