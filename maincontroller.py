import controller

def main():
    a = controller.controller1()

    if a.listening():
        a.playA()
        print("hello")
    else:
        print("noooo!!")

main()
