"""x = int(input("what is x?"))
y = int(input("what is y?"))

if x != y:
    print("x is not equal to y")    
else:
    print("x is equal to y")"""

name = input("what's your name? ")

match name:
    case "Harry" | "Hermione" | "Draco":
        print("Gryffindor")   
    case "Pelumi":
        print("Beggie Beggie")
    case "Testimony" :
        print("Baby of the house")
    case "Khalid" :
        print("Trouble in sneakers and pencil jeans")
    case "David":
        print("Mummy's Pet")
    case "Akwaugo":
        print("Egg roll")
    case "Adeola":
        print("The boss lady")
    case _:
        print("Who?")    
