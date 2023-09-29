#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
        return

    print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
    for i, arg in enumerate(argv):
        print(f"{i+1}: {arg}")

if __name__ == "__main__":
    args = sys.argv[1:]
    print_arguments(args)
