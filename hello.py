import sys

def hello(name):
    print(f"Hello {name}")

def main():
    args = sys.argv[1:]
    hello(args[0])

if __name__ == "__main__":
    main()