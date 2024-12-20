def solution():
    sum_sq_num = (sum([i for i in range(1,101)]) ** 2)
    sq_num = sum([i**2 for i in range(1,101)])
    return sum_sq_num - sq_num
print(solution())