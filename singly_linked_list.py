class Node:
    def __init__(self, data,next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return f"{self.data} pointer {self.next}"


class list:
    def __init__(self):
        self.head = None
    def __str__(self):
        return f"{self.head}"

    def insert_begin(self, data):
        node = Node(data,self.head)
        self.head = node
    def insert_end(self,data):
        node = Node(data)
        if(self.head):
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = node
        else:
            self.head = node

    def len(self):
        count = 0
        cur = self.head
        while(cur):
            count+=1
            cur = cur.next
        print(count)

    def remove_index(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            cur.next = cur.next.next

    def insert_index(self,data,index):
        if index == 0:
            node = Node(data,self.head)
            self.head = node
        else:
            cur = self.head
            cur1 = cur.next
            for i in range(index-1):
                cur = cur.next
                cur1 = cur1.next
            cur.next = Node(data)
            cur.next.next = cur1
    def insert_by_val(self,data_after,data_insert):
        if data_after == self.head.data:
            cur1 = self.head.next
            cur = self.head
            cur.next = Node(data_insert)
            cur.next.next = cur1
    def remove_by_val(self,data):
        cur = self.head.next
        prev = self.head
        while(data!=cur.data):
            cur = cur.next
            prev = prev.next
        print("\n this", prev.data)
        prev.next = prev.next.next



    def disp(self):
        cur = self.head
        while (cur):
            print(cur.data, end="-->")
            cur = cur.next



list = list()
list.insert_begin(10)
list.insert_begin(11)
list.insert_end(12)
list.insert_end(5)
list.insert_begin(2)
list.insert_index("jack",2)
list.len()
list.disp()
# list.remove_index(3)
print("\n")
list.disp()
list.insert_by_val(2,"good")
print("\n")
list.disp()
list.remove_by_val(10)
print("\n")
list.disp()
