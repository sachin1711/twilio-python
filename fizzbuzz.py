import sys

# Set up a list for our code to work with that omits the first CLI argument, 
# which is the name of our script (fizzbuzz.py)
inputs = sys.argv
inputs.pop(0)

for i in inputs:
    num = int(i)
    if num%3 == 0 and num%5 == 0:
        print("fizzbuzz")
    elif num%3 == 0:
        print("fizz")
    elif num%5 == 0:
        print("buzz")
    else:
        print(num)
        
