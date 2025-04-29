# Linked list works like an array. The nodes can be used for graph implementations. You can also insert nodes at any point as well as remove them
# It consists of a head and a current_node or tail. The default time complexity is O(n) time.
# methods: append, insert, delete, print, get, and length
#Technically all arrays are a derivative of linked lists.

from random import randint
class Node:
    def __init__(self, data=None):
        self.data : int | None = data
        self.next : self | None= None
        
    def __repr__(self):
        return f"{self.data},{self.next}"
        
class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.n = 0
        self.cur_node: Node = None
        
    def append(self, element:int):
        node = Node(element)
        if self.n == 0:
            self.head = node
            self.cur_node = self.head
            self.n+=1
        else:
            current_node = self.head
            while True:
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    current_node.next = node
                    self.cur_node = current_node.next
                    self.n+=1
                    break
        return self.show()
                    
    def insert(self, element: int, index: int):
        if index-1 > self.n:
            raise IndexError("Index out of range")

        node = Node(element)
        idx = 0
        current_node = self.head
        prev_node = None
        
        if self.n ==0:
            self.head = node
            self.n+=1
            return self.show()

        while idx < self.n:
            if index == 0:
                self.head = node
                self.head.next = current_node
                self.n+=1
                return self.show()
            elif idx == index:
                prev_node.next = node
                node.next = current_node
                self.n+=1
                break
            else:
                idx+=1
                prev_node = current_node
                current_node = current_node.next
    
    def delete(self, index=None, element=None):
        if index is not None:
            if type(index) != type(2):
                raise TypeError("Index must be an integer")
            return self.__index_delete(index)
        elif element is not None:
            if type(element) != type(2):
                raise TypeError("Index must be an integer")
            return self.__element_delete(element)
        else:
            raise AttributeError("element or index is required")
    
    def get(self, index=None, element=None):
        if index is not None:
            if type(index) != type(2):
                raise TypeError("Index must be an integer")
            return self.__index_get(index)
        elif element is not None:
            if type(element) != type(2):
                raise TypeError("Index must be an integer")
            return self.__element_get(element)
        else:
            raise AttributeError("element or index is required")
    
    def length(self):
        return self.n
    
    def show(self):
        idx = 0
        print_statement = ""
        current_node = self.head
        while True:
            if idx == 0:
                append_statement = f"[ {current_node.data} ->"
            else:
                append_statement = f" {current_node.data} ->"
            
            print_statement+=append_statement
              
            if current_node.next:
                idx+=1
                current_node = current_node.next
            else:
                print_statement+="]"
                break
            
        return print_statement
                
    def __index_delete(self, index: int):
        if index-1 > self.n:
                raise IndexError("Index out of range")
        idx = 0
        current_node = self.head
        prev_node = None
        
        while idx < self.n:
            if index == 0:
                self.head = self.head.next
                self.n -=1
                return self.show()
            elif index == idx:
                prev_node.next = current_node.next
                self.n -=1
                return self.show()
            else:
                idx +=1
                prev_node = current_node
                current_node = current_node.next
    
    def __element_delete(self, element: int):
        current_node = self.head
        prev_node = None
        
        if self.head.data == element:
            self.head = self.head.next
            self.n -=1
            return self.show()
        while current_node.next:
            if current_node.data == element:
                prev_node.next = current_node.next
                self.n-=1
                return self.show()
            else:
                prev_node = current_node
                current_node = current_node.next
        return print("Element Not Found")

    def __index_get(self, index: int):
        if index-1 > self.n:
            raise IndexError("Index out of range") 
        idx = 0
        current_node = self.head
        
        while idx < self.n:
            if index == 0:
                return self.head.data
            elif idx == index:
                return current_node.data
            else:
                idx+= 1
                current_node = current_node.next
        return print("Element Not Found")
        
    def __element_get(self, element: int):
        current_node = self.head
        if self.head.data == element:
            return print(self.head.data)
        while current_node.next:
            if current_node.data == element:
                return print(current_node.data)
            else:
                current_node = current_node.next
        return print("Element Not Found")
                
                
# lis = LinkedList()
# for i in range(randint(0,99)):
#   lis.append(randint(0,1934))

# print(lis.show())
# print(lis.delete(0))