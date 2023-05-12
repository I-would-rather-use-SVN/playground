import sys

def hi(name):
    print(f"hi, {name}")

def main():
    argc = sys.argv[1:]
    hi(argc)