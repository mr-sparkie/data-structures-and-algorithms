class binarySerachTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binarySerachTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarySerachTree(data)

    def inorder_traversal(self):
        ele = []
        if self.left:
            ele += self.left.inorder_traversal()
        ele.append(self.data)
        if self.right:
            ele += self.right.inorder_traversal()
        return ele

    def pre_order(self):
        ele = []
        ele.append(self.data)
        if self.left:
            ele += self.left.pre_order()
        if self.right:
            ele += self.right.pre_order()
        return ele
    def post_order(self):
        ele = []
        if self.left:
            ele += self.left.post_order()
        if self.right:
            ele += self.right.post_order()
        ele.append(self.data)
        return ele
    def oper(self,what):
        ele = []
        if self.left:
            ele += self.left.post_order()
        if self.right:
            ele += self.right.post_order()
        ele.append(self.data)
        if what == 'min':
            return min(ele)
        elif what == 'max':
            return max(ele)
        else:
            return sum(ele)


def tree(ele):
    root = binarySerachTree(ele[0])
    for i in range(1,len(ele)):
        root.add_child(ele[i])
    return root
num = tree([15,12,7,14,20,23,88,27])
print(num.inorder_traversal())
print(num.pre_order())
print(num.post_order())
print(num.oper('sum'))

