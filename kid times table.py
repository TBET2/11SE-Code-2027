import time
stop = ""
while stop.lower != "stop":
    counter = 0
    num = int(input("Whats up kid, can you please put a number that you wanna see the times table of? "))
    limit = int(input("Whats up again kiddo, can you please put how much of the times table you wanna see? "))
    speed = float(input("How much seconds do you wanna have to read it? "))
    if num == 0 or limit == 0:
        print("So kid, did you know that 0 x anything is 0?")
        print("Why not do this again?")
        break
    else:
        while counter != limit:
            counter += 1
            print(f"Hey Kid, {num} x {counter} is {num*counter}")
            time.sleep(speed)

    stop = input("Do you want to stop or continue? If you do, type stop :) ")

print("Bye Bye, Have Fun :)")
