# [3, 0, 6, 1, 5]	3

test = [3,4,2]
sorted(test, reverse= True)

def solution(citations):
    sort_list = sorted(citations, reverse = True)
    # print(sort_list)
    sort_max = sort_list[0]
    sort_min = sort_list[-1]
    sort_len = len(sort_list)
    if(sort_min > sort_len): return sort_len

    for i in range(sort_max, 0, -1): # i : h편 이상 인용된 논문 개수
        # print("i :", i)
        for j in range(sort_len):    # j : 논문 h편 개수
            if i > sort_list[j]:
                # print(" j :", j)
                if j >= i:
                    answer = i
                    return answer
                else: break

solution([1, 2, 3, 3, 3, 3, 4, 4, 5,  6, 7, 7, 8, 8, 9, 9, 10, 10, 10])
solution([3, 0, 6, 1, 5])
solution([42, 22])