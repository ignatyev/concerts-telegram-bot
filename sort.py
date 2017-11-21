lst = [6, 3, 2, 8, 4, 0]

swapped = True
while swapped:
    i = 0
    swapped = False
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            tmp = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = tmp
            swapped = True
        i = i + 1


print(lst)