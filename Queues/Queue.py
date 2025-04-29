from Linked_List import LinkedList
from random import randint
from ctypes import py_object
class QueueWithLinkedList:
    def __init__(self):
        self.queue = LinkedList()
        
    def enqueue(self,element: int):
        self.queue.insert(element,0)
        return self.queue.show()
    
    def dequeue(self):
        self.queue.delete(self.queue.n-1)
        return self.queue.show()
    
    def front_enqueue(self,element):
        self.queue.append(element)
        return self.queue.show()
    
    def back_dequeue(self):
        self.queue.delete(0)
        return self.queue.show()
    
    def peek_front(self):
        return self.queue.get(0)
    
    def peek_back(self):
        return self.queue.get(self.queue.n-1)
    
    def is_empty(self):
        return self.n == 0

x =  QueueWithLinkedList()

x.enqueue(3)
x.enqueue(4)
x.back_dequeue()
x.front_enqueue(8)
x.enqueue(7)
print(x.queue.show())

class QueueWithNoArray:
    def __init__(self):
        self.n = 0
        self.size = 5
        self.queue = self.__make_queue(self.size)
    
    def front_enqueue(self,element):
        if self.__should_resize_queue(self.n+1):
            self.__resize_queue()
            return self.front_enqueue(element)
        self.queue[self.n] = element
        self.n+=1
        return self.show()
    
    def enqueue(self,element):
        if self.__should_resize_queue(self.n+1):
            self.__resize_queue()
            return self.enqueue(element)

        new_queue = self.__make_queue(self.size)
        new_queue[0] = element
        
        for i in range(self.n):
            new_queue[i+1] = self.queue[i]
        self.queue = new_queue
        self.n+=1
        return self.show()
    
    def dequeue(self):
        if self.n <= 0 :
            raise IndexError
        self.queue[self.n] = None
        self.n -=1
        return self.show()
    
    def back_dequeue(self):
        if self.n <= 0 :
            raise IndexError
            
        new_queue = self.__make_queue(self.size)
        
        for i in range(self.n):
            try:
                new_queue[i] = self.queue[i+1]
            except Exception:
                break
        self.queue = new_queue
        self.n-=1
        return self.show()
    
    def peek_front(self):
        return self.queue[self.n-1]
    
    def peek_back(self):
        return self.queue[0]
    
    def show(self):
        print_statement = ""
        for i in range(self.n):
            if i==0 and i == self.n-1:
                print_statement+= f"[{self.queue[i]}]"
                break
            if i == 0:
                print_statement+= f"[{self.queue[i]}, "
            elif i == self.n-1:
                print_statement+= f"{self.queue[i]}]"
            else:
                print_statement+= f"{self.queue[i]}, "
        return print_statement
    
    def __resize_queue(self):
        new_size = self.size*2
        new_queue = self.__make_queue(new_size)
        for i in range(self.n):
            new_queue[i] = self.queue[i]
        self.size = new_size
        self.queue = new_queue
                
    def __should_resize_queue(self, size):
        return size/self.size >= 0.8

    def __make_queue(self,size):
        return (py_object*size)()
  
y = QueueWithNoArray()
for i in range(randint(0,99)):
    y.front_enqueue(randint(0,99))
y.show()
y.enqueue(2)
y.back_dequeue()
print(y.show())