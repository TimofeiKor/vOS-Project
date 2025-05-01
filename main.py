import utils.calc as calc
import utils.time_util as timeapp
import os
import time
from colorama import init, Fore

init(autoreset=True)

def clear():
    os.system('cls')

def boot():
    clear()
    print(Fore.YELLOW + "config files [py]...")
    time.sleep(1)
    print(Fore.GREEN + "opening files [py]...")
    time.sleep(0.5)
    print(Fore.BLUE + "re-config files [py]...")
    time.sleep(0.5)
    print(Fore.CYAN + "booting py...")
    time.sleep(3)
    clear()

    print(Fore.LIGHTGREEN_EX + "config files [vos]...")
    time.sleep(1)
    print(Fore.LIGHTYELLOW_EX + "opening files [vos]...")
    time.sleep(0.5)
    print(Fore.LIGHTCYAN_EX + "re-config files [vos]...")
    time.sleep(0.5)
    print(Fore.LIGHTMAGENTA_EX + "installing vos...")
    time.sleep(2)
    os.system('cls')
boot()

commands = ["vos", "info"]
apps = ["calc", "time"]
cmd = input("root/py/> ")

def infoLong():
    print("vOS build 40")
    print("Powered by Python")
    print("Author: @TimofeiKor(GitHub)")

def infoShort():
    print(Fore.LIGHTBLUE_EX + "vOS build 40")

def againcmd():
    global cmd
    while cmd != commands[0]:
        print("for opening vos, input 'vos'")
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
        print(apps[1])
        print("========================")
        cmd = input("root/py/vos/> ")

        if cmd == commands[1]:
            infoLong()
        cmd = input("root/py/vos/> ")
        if cmd == apps[0]:
            calc.question()
        helpMenu()
        cmd = input("root/py/vos/> ")
        if cmd == apps[1]:
            timeapp.cTime()
        


helpMenu()
