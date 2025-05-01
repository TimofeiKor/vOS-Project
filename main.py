import calc

commands = ["help", "info"]
apps = ["calc"]
cmd = input("root/py/> ")

def info():
    print("vOS build 17")

def againcmd():
    global cmd
    while cmd != commands[0]:
        print("for opening vos, input 'vos'")
        cmd = input("root/py/> ")
againcmd()

def helpOpen():
    global cmd
    if cmd == commands[0]:
        print("==========MENU==========")
        print(commands[1])
        print(apps[0])
        print(apps[1])
        print("========================")
        cmd = input("root/py/vos/> ")

        if cmd == commands[1]:
            info()
        elif cmd == apps[0]:
            calc.question()
        cmd = input("root/py/> ")
        againcmd()


helpMenu()
