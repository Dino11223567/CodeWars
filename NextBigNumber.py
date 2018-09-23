def next_bigger(n):
    digits = list(map(int,n))
    pivot_i = -1
    for i in range(len(digits)-1,0,-1):
        if digits[i] > digits[i-1]:
            pivot_i = i-1
            break
    if pivot_i == -1:
        return(-1)
    else:
        left = digits[:pivot_i]
        pivot = digits[pivot_i]
        right = digits[pivot_i+1:]
        temp = min(i for i in right if i > pivot)

        right.insert(right.index(temp),pivot)
        right.remove(3)
        left.append(temp)
        left += right
        return(''.join(map(str,left)))



print(next_bigger("1254332"))
