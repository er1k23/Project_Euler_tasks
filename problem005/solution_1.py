def solution():
    ans = 2520
    while True:
        for i in range(20,10,-1):
            if ans % i != 0:
                break
            elif i == 11:
                return ans
            else:
                continue
        ans += 2520
print(solution())