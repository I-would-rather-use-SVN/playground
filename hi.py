import sys

def hi(name):
    print(f"hi, {name}")

def main():
    argc = sys.argv[1:]
    hi(argc[0])

if __name__=="__main__":
    main()
