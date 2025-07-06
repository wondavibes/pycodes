
#you can use _ for a counting variable

"""for _ in range(5):
    print("oof")"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
         n = int(input("pick a number: "))
         if n > 0:
             break
    return n

def meow(n):       
    for _ in range(n):print("oof")  
      
if __name__ == "__main__":
    main()
