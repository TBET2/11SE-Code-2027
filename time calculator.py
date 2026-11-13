import math
bps = float(input("How many bytes were downloaded in the past second? "))
btg = float(input("How many bytes still to go? "))
sl = math.floor(btg/bps)
print(sl)
while True:
    if sl > 1:
        print(f"The download will take approximately {sl} seconds")
    elif sl == 1:
        print(f"The download will take approximately {sl} second")
    elif sl == 0:
        print("Dude your stuff is done")
    else:
        print("Put an positive number next time brodie")
    bps = float(input("How many bytes were downloaded in the past second? "))
    btg = float(input("How many bytes still to go? "))
    sl = math.floor(btg/bps)


