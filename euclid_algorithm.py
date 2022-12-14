print("This program will find the greatest common divisor of two whole positive integers.")
x = 0
y = 0

def euclid_algo(x,y):
    #x must be less than y for algorithm to work properly
    if (y<x):
        temp_1 = x
        temp_2 = y
        y = temp_1
        x = temp_2

    remainder = y % x 

    #algorithm to find GCD
    while (remainder != 0):
        y = x
        x = remainder
        remainder = y % x
    return x


# main program
try: # input validation, must be an integer
    x = int(input("Please enter a whole positive number for x.\n"))
except:
    print("not an integer, please try again.")

try:
    y = int(input("Please enter another whole positive number for y.\n"))
except:
    print("not an integer, please try again.")

gcd_result = euclid_algo(x,y)

print("GCD is: ", gcd_result)