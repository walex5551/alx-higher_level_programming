#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))
    if length >= 1:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1
