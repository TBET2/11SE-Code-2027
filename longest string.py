import time
a = input("first string? ")
b = input("second string? ")
c = input("third string? ")

longest = ""
while True:

    if len(a) >= len(longest):
        longest = a
    if len(b) > len(longest):
        longest = b
    if len(c) > len(longest):
        longest = c
    print(f"The longest line was {longest}")
    counter = 0
    while counter != 5:
        counter += 1
        time.sleep(1)
    retry = input("Ya got 5 seconds(i lie) to make a choice, Try Again? YES/NO ")
    if counter == 5:
        print("Ya spent too long")
        break
    if retry.upper() == "YES":
        pass
    elif retry.upper() == "NO":
        break
    else:
        print("lol didn't even say anything")
    a = input("first string? ")
    b = input("second string? ")
    c = input("third string? ")

    longest = ""
print("Bye Bye")
