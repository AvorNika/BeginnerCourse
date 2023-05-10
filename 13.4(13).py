# раздел 13.4 Функции с возвратом значения, задание 13 Merge lists 2
def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    return result


total_list = []
for i in range(int(input())):
    num = [int(c) for c in input().split()]
    total_list = quick_merge(total_list, num)
print(*total_list)
