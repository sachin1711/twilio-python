import sys

res = int(sys.argv[1]) + int(sys.argv[2])

if res<=0:
    print("You have chosen the path of destitution.")
elif 1<=res<=100:
    print("You have chosen the path of plenty.")
else:
    print("You have chosen the path of excess.")
