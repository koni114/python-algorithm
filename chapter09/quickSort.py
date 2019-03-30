import random as ran
arr = [ran.randint(0, 10) for _ in range(10)]
print("before arr : " , arr)

def partition(left, right, mid):
    arr[left], arr[mid] = arr[mid], arr[left]
    i, j        = left, right
    pivot_value = arr[left]
    while i < j:
        while(arr[j] > pivot_value): j -= 1
        while(arr[i] <= pivot_value and i < j): i += 1
        if i < j: arr[i],arr[j] = arr[j],arr[i]
    arr[left], arr[i] = arr[i], arr[left]
    return i


def quickSort(left, right):
    if left >= right: return 0
    mid = (left + right) // 2
    i = partition(left, right, mid)
    quickSort(left, i-1)
    quickSort(i+1, right)


quickSort(0, 9)
print("after arr :", arr)