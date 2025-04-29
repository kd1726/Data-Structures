from . Linked_List import LinkedList
import ctypes
# stacks are exactly as they sound. They are data strutctures that only allow you to see the top element.
# The methods are pop, push and peek
class StackWithLinkedList:
    
    def __init__(self):
        self.stack = LinkedList()
        self.n = 0
        
    def peek(self):
        return self.stack.get(self.n-1)
    
    def peek_bottom(self):
        return self.stack.get(0)
    
    def push(self,element):
        self.stack.append(element)
        self.n+=1
        return self.show()
    
    def pop(self):
        self.stack.delete(index=self.n-1)
        self.n-=1
        return self.show()
        
    def show(self):
        return self.stack.show()

class StackWithNoLinkedList:
     def __init__(self):
        self.size = 5
        self.n = 0
        self.stack = self.__make_stack(self.size)
        
     def push(self,element):
        if self.__should_resize_stack():
            self.__resize_stack()
            return self.push(element)
        self.stack[self.n] = element
        self.n+=1
        return self.show()
    
     def pop(self):
        self.stack[self.n] = None
        self.n-=1
        return self.show()
    
     def peek_top(self):
        return self.stack[self.n-1]
        
     def peek_bottom(self):
        return self.stack[0]
    
     def show(self):
        print_statement = ""
        for i in range(self.n):
            if i==0 and i == self.n-1:
                print_statement+= f"[{self.stack[i]}]"
                break
            if i == 0:
                print_statement+= f"[{self.stack[i]}, "
            elif i == self.n-1:
                print_statement+= f"{self.stack[i]}]"
            else:
                print_statement+= f"{self.stack[i]}, "
        return print_statement
    
     def __resize_stack(self):
        new_size = self.size*2
        new_stack = self.__make_stack(new_size)
        
        for i in range(self.n):
            new_stack[i] = self.stack[i]
            
        self.stack = new_stack
        self.size = new_size
        
     def __should_resize_stack(self):
        return self.n/self.size >= 0.7
    
     def __make_stack(self,size):
        return (py_object*size)()