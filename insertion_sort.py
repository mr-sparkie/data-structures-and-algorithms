def insertion_sort(data):
    for i in range(1,len(data)):
        anchor = data[i]
        j = i-1
        while j>=0 and anchor<data[j]:
            data[j+1] = data[j]
            j-=1
        data[j+1] = anchor
    return data
def insertion_rev(data):
    for i in range(len(data),0,-1):
        anchor = data[i-1]
        j = i
        while j<len(data) and anchor>data[j]:
            data[j-1] = data[j]
            j+=1
        data[j-1] = anchor
    return data

print(insertion_sort([21, 38, 29, 17, 4, 25, 11, 32, 9]))
print(insertion_rev([2, 1, 5, 7, 2, 0, 5]))