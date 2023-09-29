#!/usr/bin/python3
import sys

def infinite_add(a, b, c):
    while True:
        a = a + b + c

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 3-infinite_add.py <a> <b> <c>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3]))

    infinite_add(a, b, c)
    