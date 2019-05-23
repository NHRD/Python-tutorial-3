### EXILE PRIDE ###

org_list = [2, 3, 1, 78, 9]
org_list2 = sorted(org_list)
org_list3 = org_list.sort()
org_list.sort(reverse=True)
org_list.reverse()

print(org_list, "/n", org_list2, "/n", org_list3)


from collections import deque

sample_que = deque([1, 2, 3, 4, 5])
sample_que.append(3)
sample_que.append(6)
sample_que.popleft()
sample_que.pop()

print(sample_que)
result = list(sample_que)
print(result)
