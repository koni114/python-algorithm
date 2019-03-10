from random import randint
rand_sort = [randint(0,10) for i in range(10) ]

def bubble_sort(rand_sort):
    sort_len = len(rand_sort)
    print("rand_sort", rand_sort)
    for i in range(sort_len-1, 0, -1):
        count = 0
        for j in range(0, i):
            if rand_sort[j] > rand_sort[j+1]:
                rand_sort[j], rand_sort[j+1] = rand_sort[j+1], rand_sort[j]
            else:
                count += 1
        if count == i: break
    return rand_sort

print("sorted_sort :", list(bubble_sort(rand_sort)))

