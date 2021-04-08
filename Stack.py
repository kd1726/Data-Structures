import ctypes
class Stack:
    def __init__(self):
        self.n=0
        self.size=1
        self.stack = self._make_stack(self.size)

    def peek_top(self):
        return self.stack[self.n-1]

    def peek_bottom(self):
        return self.stack[0]

    def isEmpty(self):
        if self.stack==[]:
            return True
        return False

    def push(self,element):
        if self.n==self.size:
            self._resize(2*self.size)
        self.stack[self.n]=element
        self.n+=1
        return


    def pop(self):
        self.stack[self.n]=None
        self.n-=1
        return self.display()

    def _resize(self,new_size):
        new_stack = self._make_stack(new_size)
        for i in range(self.n):
            new_stack[i]=self.stack[i]
        self.stack = new_stack
        self.size = new_size
        return

    def _make_stack(self,new_size):
        return (new_size*ctypes.py_object)()

    def display(self):
        for i in range(self.n):
            print(self.stack[i])
        return
