# This Program will return whether a integer is odd of even based on the user's input


# Test 1:
#Input: 5
# Output: This is an odd number

#Test 2:
#Input: 10
#Ouput: This is an even number.

#Test 3:
#Input: 0
#Ouput: This is an even number.

#Test 4:
#Input: 1.3
#Ouput: This is not an integer, try again.

number = 0
number = float(input("Enter an integer: "))

while number < 10:
    if number % 2 == 1:
        print("This is an odd number")
    elif number % 2 == 0:
        print("This is an even number")
    else:
        print("This is not an integer, try again!")
    number = float(input("Try again: "))
print("Ya finished.")
