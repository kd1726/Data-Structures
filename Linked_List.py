class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class Linked_List:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev =cur_node
        return self.display()

    # I could import on of my array dat strcutres but again I will ot reinvent the wheel
    def display(self):
        disp = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            disp.append(cur_node.data)
        return disp

    def length(self):
        cur_node = self.head
        idx=0
        while cur_node.next!=None:
            cur_node = cur_node.next
            idx+=1
        return idx

    def get_item(self,index):
        if index>self.length():
            raise IndexError("Index out of range")
        cur_node = self.head
        if index==0:
            return self.head.data
        else:
            idx = 0
            while cur_node.next!=None:
                cur_node = cur_node.next
                if index==idx:
                    return cur_node.data
                idx+=1
            return

    def delete(self,index):
        if index>self.length():
            raise IndexError("Index out of range")
        cur_node = self.head
        if index==0:
            self.head = cur_node.next
            cur_node.prev = None
            return self.display()
        else:
            idx=0
            while cur_node.next!=None:
                last_node = cur_node
                cur_node = cur_node.next
                if idx==index:
                    last_node.next = cur_node.next
                    cur_node.next.prev = last_node
                    return self.display()
                idx+=1
            return

    def insert(self,index,data):
        cur_node=self.head
        new_node = Node(data)
        if index>self.length():
            raise IndexError("Index out of range!")
        if index==0:
            self.head = new_node
            new_node.next = cur_node
            cur_node.prev = new_node
        else:
            idx = 0
            while cur_node.next!=None:
                last_node = cur_node
                cur_node = cur_node.next
                if idx==index:
                    last_node.next = new_node
                    new_node.next =  cur_node
                    new_node.prev = last_node
                    return self.display()
                idx+=1
        return
