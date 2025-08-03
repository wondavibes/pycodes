def main():
    s = input("enter an alphanumeric string: ")
    print(sort(s))

def sort(s):
    if not s or s == "" or not s.isalnum():
        return "Invalid input, please enter alphanumeric characters only."
    lowers = sorted([i for i in s if i.islower()])
    uppers = sorted([i for i in s if i.isupper()])
    odds = sorted([i for i in s if i.isdigit() and int(i) % 2 != 0])
    evens = sorted([i for i in s if i.isdigit() and int(i) % 2 == 0])
    
    return ''.join(sorted(lowers) + sorted(uppers) + odds + evens)
        


if __name__ == "__main__":
    main()