from random import randint
rand_sort = [randint(0,10) for i in range(10)]

def insert_sort(rand_sort):
    print("rand_sort :", rand_sort)
    sort_len = len(rand_sort)
    for i in range(1, sort_len):
        for j in range(i):
            if rand_sort[i] < rand_sort[j]:
                tmp = rand_sort[i]
                del rand_sort[i]
                rand_sort.insert(j, tmp)
                break
    return rand_sort

print("sorted sort :", insert_sort(rand_sort))