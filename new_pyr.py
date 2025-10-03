def print_pyr(symbol, height):
    for i in range(1, height + 1):
        # Print spaces
        for _ in range(height - i):
            print(" ", end="")
        # Print symbols
        for _ in range(2 * i - 1):
            print(symbol, end="")
        print()  # Move to the next line

def main():
    symbol = input("enter a symbol: ")
    height = int(input("enter the height of the pyramid: "))
    print_pyr(symbol, height)

main()