#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer

Enter a number: 2.4
2.4 is not a positive integer

Enter a number: 5
5 is a positive integer

Enter a number: 4.0
4.0 is a positive integer
"""

a = input("enter a number")
a = float(a)

a2 = round(a, 0)

if a < 0:
    print(f"{a} is not a positive interger")
elif a - a2 !=0:
    print(f"{a} is not a positive interger")
else:
    print(f"{a} is a positive interger.")