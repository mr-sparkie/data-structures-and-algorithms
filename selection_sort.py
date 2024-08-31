def selection_sort(data):
    for i in range(len(data)-1):
        anchor=i
        for j in range(anchor + 1, len(data)):
            if data[anchor]>data[j]:
                anchor = j
        if i!=anchor:
            data[i],data[anchor] = data[anchor],data[i]
data = [9,4,5,3,2,66,7,3]
selection_sort(data)
print(data)