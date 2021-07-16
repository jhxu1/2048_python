from screen import Screen

if __name__ == '__main__':
    screen = Screen()
    screen.show()
    while True:
        cmd = input("Please input w/a/s/d\n")
        screen.move(cmd)
        screen.show()
        screen.check()
