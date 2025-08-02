def main():
    s = input("enter an alphanumeric string: ")
    print(sort(s))

def sort(s):
    if not s:
        return "Invalid input, please enter alphanumeric characters only."
    lowers = []
    uppers = []
    odds = []
    evens = []
    zero = []
    for i in s:
        if i.islower():
            lowers.append(i)
        elif i.isupper():
            uppers.append(i)
        elif i.isdigit():
            if int(i) % 2 == 1:
                odds.append(i)
            elif int(i) == 0:
                zero.append(i)
            else:
                evens.append(i)
    return ''.join(sorted(lowers) + sorted(uppers) + odds + zero + evens)
        


if __name__ == "__main__":
    main()