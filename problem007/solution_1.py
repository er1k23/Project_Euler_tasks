import math
def solution():
    counter = 0
    res = 1
    while True:
        res += 1
        prime_is = all([res % i != 0 for i in range(2,math.isqrt(res)+1)])
        if prime_is:
            counter += 1
        elif counter == 10001:
            return res - 1
print(solution())