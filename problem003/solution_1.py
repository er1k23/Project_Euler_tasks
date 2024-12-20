import math

def solution():
    n = math.isqrt(600851475143)+1
    i = 2
    for i in range(3,n):
        if i >= n:
            return n
        elif n % i == 0: 
            n = n // i

print(solution())