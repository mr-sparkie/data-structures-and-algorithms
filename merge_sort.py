import pandas as pd
def merge_sort(arr):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    helper(left,right,arr)

def helper(a,b,arr):
    a_len = len(a)
    b_len = len(b)
    i = j = k =0
    while i< a_len and  j< b_len:
        if a[i]<=b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i<a_len:
        arr[k] = a[i]
        i+=1
        k+=1
    while j<b_len:
        arr[k] = b[j]
        j+=1
        k+=1

def merge_sort_1(arr,key,descending=False):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort_1(left, key,descending)
    merge_sort_1(right, key,descending)
    helper1(left,right,arr,key,descending)
def helper1(a,b,arr,key,desc):
    len_a = len(a)
    len_b = len(b)
    i = j = k=0
    if not desc:
        while i<len_a and j<len_b:
            if a[i][key]<=b[j][key]:
                arr[k] = a[i]
                i+=1
            else:
                arr[k] = b[j]
                j+=1
            k+=1
        while len_b>j:
            arr[k]=b[j]
            j+=1
            k+=1
        while len_a>i:
            arr[k]=a[i]
            i+=1
            k+=1
    else:
        while i<len_a and j<len_b:
            if a[i][key]>=b[j][key]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
            k+=1
        while i<len_a:
            arr[k]=a[i]
            i+=1
            k+=1
        while j<len_b:
            arr[k]=b[j]
            j+=1
            k+=1


arr = [1,5,9,6,2,8,3,4,13]
data = [{'name':'nami','age':20,'salary':10000},
        {'name':'luffy','age':21,'salary':75000},
        {'name':'sanji','age':22,'salary':35000},
        {'name':'zoro','age':23,'salary':40000}]

merge_sort(arr)
print(merge_sort_1(data, 'name'))
print(arr)
print(data)
index=['captain:','navigator:','cook:','vice captain:']
df = pd.DataFrame(data)
print(df)


