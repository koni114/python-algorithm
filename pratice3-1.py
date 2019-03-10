'''
    n명 중 두 명을 뽑아 짝을 짓는다고 할 때, 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들어보자
'''
name_list = input("짝을 지을 사람을 입력하세요").split()
name_len = len(name_list)

for i in range(name_len):
    for j in range(i+1, name_len):
        print(name_list[i], "-", name_list[j])

