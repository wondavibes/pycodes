def main():
    #remove whitespace
    names = new_list()
    for name in sorted(names):
        print(hello(name))

def hello(to):
    return f"hola, {to}"

def new_list():
    ur_list = []
    while True:
        ur_input = input("enter a name to add (or '!!' to finish):")
        if ur_input == '!!':
            break
        ur_list.append(ur_input)
    return ur_list

if __name__ == "__main__":
    main()














#first, last = name.split(" ")
#chat = "we're good"
#print(last,chat)