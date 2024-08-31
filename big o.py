def o_n(arr):
    sq = []
    for i in arr:
        sq.append(i*i)
    return sq
arr = range(2,1000000)
# print(o_n(arr))

def o_1(a,i):
    return a[i]
print(o_1(arr,1000))

