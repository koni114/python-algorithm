# stack
a = [1,2,3,4,5]
# push
a.append(10)
a.append(20)
# pop
b = a.pop()
print(b)

word      = input("input a word : ")
word_list = list(word)
print(word_list)

result = []

for i in range(len(word_list)):
    result.append(word_list.pop())

print(result)
print(word[::-1])

# queue
a = [1,2,3,4,5]
a.append(10)
a.append(20)
a.pop(0)
a.pop(0)

# set
s = set([1,2,3,1,2,3])  # 1, 2, 3만 출력 됨
s.add(1)                # 추가되지 않음
s.remove(1)             # 1 삭제
s.update([1,2,3,4,5])   # 있는 것은 추가가 되지 않고, 없는 것만 추가
s.discard(5)            # 5 삭제
s.clear()

