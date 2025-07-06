def main():
    x = float(input("what's x?"))
    y = float(input("what's y?"))
    print("the squares of your numbers are", square(x),"and",square(y))

    """b = int(input("what's b?"))
    if(is_even(b)):
        print("Even")
    else:
        print("Odd")"""       

def square(n):
    return int(n*n)

def is_even(i):
    return i % 2 == 0 

if __name__ == "__main__":
    main()