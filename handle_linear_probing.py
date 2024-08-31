class hashmap:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]
    def get_hash(self,key):
        h = 0
        for i in key:
            h+=ord(i)
        return h% self.max
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h]:
            if self.arr[h][0]==key:
                self.arr[h] = (key,value)
            else:
                i = h+1
                print("intial i",i)
                if i>=len(self.arr):
                    i = 0
                    print("change i", i)

                while(self.arr[i]!=None):
                    print(self.arr[i])
                    if i >= len(self.arr):
                        i = 0
                    if self.arr[i]==None:
                        break
                    i+=1
                print(i)
                self.arr[i] = (key,value)
        else:
            self.arr[h]= (key,value)
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key:
            return self.arr[h][1]


h1 = hashmap()
print(h1.get_hash("march 16"))#25
h1["march 7"] = 123
h1["march 8"] = 456

h1["march 25"] = 1923
h1["march 16"]=198
print(h1.arr)
h1["march 25"] = 32

print(h1["march 16"])
print(h1.arr)

