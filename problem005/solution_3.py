def solution():
    ans = 2520
    while True:
        flag = all(ans%x==0 for x in range(20, 10, -1))
        if flag:
            return ans
        else:
            ans += 2520
print(solution())