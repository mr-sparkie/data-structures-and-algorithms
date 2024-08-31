def bubble_sort(list):
    for i in range(len(list)-1):
        flag = False
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1]=temp
                flag = True
        if not flag:
            break
    return list
def bubble_key(data,key):
    for i in range(len(data) - 1):
        flag = False
        for j in range(len(data) - 1 - i):
            if data[j][key] > data[j + 1][key]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j+1] = temp
                flag = True
        if not flag:
            print("yes")
            break
    return data

data = [{'name':'mary','age':27,'salary':10000},
        {'name':'luffy','age':21,'salary':50000},
        {'name':'zoro','age':23,'salary':30000}]
print(bubble_sort([1,2,4,5,68,9,4]))
print(bubble_key(data, 'name'))
print(data)