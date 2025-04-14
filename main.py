import calc
import os

commands = ["help", "info"]
apps = ["calc"]
cmd = input("root/py/> ")

def clear():
    os.system('cls')

def infoLong():
    print("vOS build 17")
    print("Powered by Python")
    print("Author: @TimofeiKor(GitHub)")

def infoShort():
    print("vOS build 17")

def againcmd():
    global cmd
    while cmd != commands[0]:
        cmd = input("root/py/> ")
againcmd()

def helpOpen():
    global cmd
    if cmd == commands[0]:
        helpMenu()

def helpMenu():
        clear()
        infoShort()
        print("==========MENU==========")
        print(commands[1])
        print(apps[0])
        print("========================")
        cmd = input("root/py/vos/> ")

        if cmd == commands[1]:
            infoLong()
        cmd = input("root/py/vos/> ")
        if cmd == apps[0]:
            calc.question()
        helpMenu()
        cmd = input("root/py/vos/> ")


helpMenu()
againcmd()