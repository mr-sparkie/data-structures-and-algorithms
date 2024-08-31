def swap(a,b,arr):
    arr[a],arr[b] = arr[b],arr[a]
def partition(data,p_index,i=0):
    pivot = len(data)-1
    pivot_val = data[pivot]
    while data[p_index] != pivot_val:
        while p_index<pivot_val:
            p_index+=1
            i +=p_index
        i +=1
        while i>pivot_val:
             i+=1
        if p_index<i:
            swap(p_index,i,data)
    swap(pivot_val,p_index,data)

def quicksort(data,p_index,i):
    partition(data,p_index,i)
    return data
quicksort([11,9,29,7,2,15,28],0,0)







