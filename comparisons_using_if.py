#My response to HackerRank for Python Practice exercise number 3

#Task 
#Given an integer, , perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#Input Format
#A single line containing a positive integer, .
#Constraints
#Output Format
#Print Weird if the number is weird; otherwise, print Not Weird.


#!/bin/python3

N = int(input())
if N % 2 == 1:
    print("Weird")
elif N % 2 == 0 and 2 <= N <= 5:
    print("Not Weird")
elif N % 2 == 0 and 6 <= N <= 20:
    print("Weird")
else:
    print("Not Weird")
