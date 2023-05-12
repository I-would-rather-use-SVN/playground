import sys

def hello(name):
    print(f"Hello {name}")

def main():
    hello(sys.argv[1])

if __name__=="__main__":
    main()
