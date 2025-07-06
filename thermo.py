def main():
    #allow the user select conversion mode
    while True:
        print("1. Celsius to Fahrenheit: ")
        print("2. Fahrenheit to Celsius: ")
        print("3. Exit")

        choice = input("select an option(1, 2 or 3): ")
        if choice == "1":
            cel = float(input("enter a temperature in Celsius: "))
            fah = cel_2_far(cel)
            print(f"{cel} degree Celsius is equal to {fah} degree Fahrenheit")

        elif choice == "2":
            fah = float(input("enter a temperature in Fahrenheit: "))
            cel = far_2_cel(fah)
            print(f"{fah} degree Fahrenheit is equal to {cel:.2f} degree Celsius")
        
        elif choice == "3":
            print("Ciao!")
            break
            
        else:
            print("invalid choice, please try again")
    

def  cel_2_far(x):
    y = (x * 1.8) + 32
    return y 


def far_2_cel(a):
    b = (a - 32) * 5/9
    return b


if __name__ == "__main__":
    main()
