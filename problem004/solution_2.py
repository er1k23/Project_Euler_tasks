def solution():
    lst = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if str(i * j) == str(i * j)[::-1]:
                lst.append(i * j)
            else:
                continue
    return max(lst)

print(solution())