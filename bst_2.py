class btree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if self.data == data:
            return
        if self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = btree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = btree(data)
    def in_order(self):
        n = []
        if self.left:
            n += self.left.in_order()
        n.append(self.data)
        if self.right:
            n+= self.right.in_order()
        return n
    def minn(self):
        if self.left:
           return self.left.minn()
        return self.data
    def maxx(self):
        if self.right:
            return self.right.maxx()
        return self.data

    def delete_right(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_right(val)
        elif val> self.data:
            if self.right:
                self.right = self.right.delete_right(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min1 = self.right.minn()
            self.data = min1
            self.right = self.right.delete_right(min1)
        return self
    def delete_left(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_left(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_left(val)
        else:
            if not self.left and not self.right:
                return None
            if not self.right:
                return self.left
            if not self.left:
                return self.left
            maxx = self.left.maxx()
            self.data = maxx
            self.left = self.left.delete_left(maxx)
        return self



root = btree(17)
for i in [4,1,20,9,23,18,34] :
    root.add_child(i)
print(root.in_order())
# root.delete_right(17)
# print(root.in_order())
root.delete_left(17)
print(root.in_order())
#[1, 4, 9, 18, 20, 23, 34]