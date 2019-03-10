import random
input_int = [random.randint(1,10) for i  in range(10) ]
print("random list : ", input_int)


result_min = input_int[0]

def find_the_min(min, n):
    if n == len(input_int):
        print(min)
        return 0
    if min > input_int[n]:
        return find_the_min(input_int, n+1)
    else:
        return find_the_min(min, n+1)

find_the_min(result_min, 1)
