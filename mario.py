def main():
    x = int(input("choose a number: "))
    print_square(x)
    
def print_square(n):
    # for each row in square
    for i in range(n):
        # for each brick in row
        for j in range(n):
            #print brick spaced evenly(the " " * (n-1))
            print(" " * (n-1) + "#", end="") #code will run without the " "*n-1 block
        print()
        
if __name__ == "__main__":
    main()