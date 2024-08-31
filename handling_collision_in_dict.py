class hashmap:

    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    def key(self,key):
        h1 = 0
        for i in key:
            h1 += ord(i)
        return h1 % self.max
    def table(self,key,val):
        h = self.key(key)
        self.arr[h] = val
    def get(self,key):
        h = self.key(key)
        return self.arr[h]
    def __setitem__(self, key, val):
        h = self.key(key)
        flag = True
        for index,value in enumerate(self.arr[h]):
            if len(value) ==2 and value[0]==key:
                self.arr[h][index] = (key, val)
                flag = False
                break
        if flag:
            self.arr[h].append((key,val))
    def __getitem__(self, key):
        h = self.key(key)
        for i in self.arr[h]:
            if i[0] == key:
                return i[1]
    def __delitem__(self, key):
        h = self.key(key)
        for idx,val in enumerate(self.arr[h]):
            if val[0]==key:
                del self.arr[h][idx]
    def disp(self):
        return self.arr
h1 = hashmap()
# h1.table("march 6",67)
h1['march 6'] = 178
print(h1.key('march 19'))
h1['march 17'] = 324
print(h1.disp())
print(h1["march 6"])