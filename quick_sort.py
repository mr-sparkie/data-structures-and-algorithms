def swap(a,b,arr):
    # if a!=b:
    #     temp = arr[a]
    #     arr[a] = arr[b]
    #     arr[b] = temp
    arr[a],arr[b] = arr[b],arr[a]





def partition(data,start,end):
    pivot_index = start
    pivot = data[pivot_index]
    while start < end:
        while start<len(data) and data[start] <= pivot:
            start += 1
        while data[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, data)
    swap(pivot_index, end, data)
    return end

def quick_sort(data,start,end):
    if start<end:
        pivot = partition(data,start,end)
        quick_sort(data,start,pivot-1)
        quick_sort(data,pivot+1,end)
    return data

data = [11,55,6,8,3,2,4,9,77,5,2]

print(quick_sort(data,0,len(data)-1))
