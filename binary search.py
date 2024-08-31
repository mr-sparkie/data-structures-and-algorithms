class BinarySearch:
    def __init__(self,data):
        self.data = data
        self.index = [i for i in range(len(self.data))]
        self.lenn = len(data)
    def traverse(self,val,left,right):
        mid = (left+right)//2
        mid_val = self.data[mid]
        if mid >= len(self.data) or mid_val <0 or left>right:
            return -1
        if val == mid_val:
            return self.index[mid]
        if val > mid_val:
            left = mid + 1

        else:
            right = mid - 1
        return self.traverse(val,left,right)
data = [4,9,11,17,21,25,29,5,32,38]
n = BinarySearch(sorted(data))
print(n.traverse(5,0,len(data)-1))