class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def get_lvl(self):
        lvl = 0
        p = self.parent
        while p:
            lvl += 1
            p = p.parent
        return lvl
    def prnt(self):
        sap = " "*self.get_lvl()*3
        sap = sap + " " if self.parent else ' '
        if self.parent:
            sap = sap + "|-->" if self.parent.parent else sap
        print(sap+''+self.data)
        if self.children:
            for i in self.children:
                i.prnt()
        return root
    def prnt_level(self,lvl):
        sap = " "*self.get_lvl()*3
        sap = sap + " " if self.parent else ' '
        if self.parent:
            sap = sap + "|-->" if self.parent.parent else sap
        print(sap+''+self.data)
        if self.children:
            p = self.parent
            print(p)
            for i in self.children:

                if self.get_lvl()==lvl:
                    break
                else:
                    i.prnt()
        return root



root = TreeNode("Electronics")

laptops = TreeNode("laptops")

laptops.add_child(TreeNode("macbook"))
laptops.add_child(TreeNode("asus"))
laptops.add_child(TreeNode("dell"))

tv = TreeNode("Television")

tv.add_child(TreeNode("LG"))
tv.add_child(TreeNode("Vu"))
tv.add_child(TreeNode("sony"))

mobile = TreeNode("mobile")

mobile.add_child(TreeNode("samsung"))
mobile.add_child(TreeNode("poco"))
mobile.add_child(TreeNode("oneplus"))

root.add_child(laptops)
root.add_child(tv)
root.add_child(mobile)
root.prnt()
root.prnt_level(2)
