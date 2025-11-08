# Lab 10 - Get Divisors
# 202135573 장동준

import sys

number = int(sys.argv[1])
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
print()
