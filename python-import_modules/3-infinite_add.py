#!/usr/bin/python3
import sys

def infinite_add(*args):
    result = sum(map(int, args))
    print(result)

if __name__ == "__main__":
    args = sys.argv[1:]
    infinite_add(*args)
