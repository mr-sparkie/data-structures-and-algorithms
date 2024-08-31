class hashmap:

    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
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
        self.arr[h] = val
    def __getitem__(self, key):
        h = self.key(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.key(key)
        self.arr[h]= None
    def disp(self):
        return self.arr
h1 = hashmap()
h1.table('march 6',340)
print(h1.arr[9])
print(h1.get('march 6'))
h1['march 8'] = 390
h1['march 11'] = 980
h1['march 13'] = 90
print(h1['march 13'])
del h1['march 8']
print(h1.disp())