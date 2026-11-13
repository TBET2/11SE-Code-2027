name = input("What is your name? ")
print(f"Hello {name}")

words = str(input("Say something to Bob "))
yar = "r" * len(words)
if len(words) >= 5:
    print(f"Ya{yar}")
else:
    print("Yar")


