import random
def main():
    symbol = input("enter a symbol: ")
    height = int(input("enter the height of the pyramid: "))
    print_pyr(symbol, height)


def print_pyr(symbol, height):
    for i in range(1, height + 1):
        print(" " * (height - i) + symbol * (2 * i - 1))

main()