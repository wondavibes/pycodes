import random
def main():
    symbol = input("enter a symbol: ")
    height = random.randint(1,10)
    print_pyr(symbol, height)


def print_pyr(symbol, height):
    for i in range(1, height + 1):
        print(" " * (height - 1) + symbol * i)

main()