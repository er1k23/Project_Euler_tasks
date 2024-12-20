sum = 0
prev_num = 0
prev_of_prev_num = 0
num = 1

while num <= 4000000:
    prev_prev_num = prev_num
    prev_num = num
    num = prev_prev_num + prev_num
    if num % 2 == 0:
        sum += num
print(sum)