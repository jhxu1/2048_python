from screen import Screen
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--size", default=5, type=int, help="Windows size")
parser.add_argument("--init_num", default=3, type=int, help="Initial the number of '2'")


if __name__ == '__main__':
    args = parser.parse_args()
    screen = Screen(height=args.size, width=args.size, init_num=args.init_num)
    screen.show()
    while True:
        cmd = input("Please input w/a/s/d\n")
        screen.move(cmd)
        screen.show()
        screen.check()
