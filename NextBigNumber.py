def next_bigger(n):
    digits = list(map(int,n))
    pivot_i = -1
    for i in range(len(digits)-1,0,-1):
        if digits[i] > digits[i-1]:
            pivot_i = i-1
            break
    if pivot_i == -1:
        print(-1)
    else:
        temp = digits[pivot_i:]
        pivot = temp[0]
        print(pivot)
        print(temp)


next_bigger("12543")
