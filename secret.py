codenum = 212
guess = None

while guess != codenum:
    guess = int(input("guess the secret number: "))
    if guess < codenum:
        print("too low!")
    elif guess > codenum:
        print("too high!")
print("Wow, you got the number right")

