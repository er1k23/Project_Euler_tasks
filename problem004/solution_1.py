def solution():
    lst = []
    for i in range(100,1000):
        for j in range(100,1000):
            num = i*j
            rev_num = 0
            tmp = 0
            while num != 0:
                tmp = num % 10
                num //= 10
                rev_num = rev_num * 10 + tmp
            if rev_num == i*j:
                lst.append(rev_num)
            else:
                continue
    return max(lst)
print(solution())