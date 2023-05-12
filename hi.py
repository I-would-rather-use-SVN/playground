import sys

def hi(name):
    print(f"hi, {name}!")

def main():
    hi(sys.argv[1])

if __name__=="__main__":
    main()
