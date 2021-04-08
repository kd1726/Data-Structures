import ctypes
class StaticList:
    def __init__(self,size=10):
        self.n = 0
        self.size=size
        self.array = self._make_array(self.size)

    def length(self):
        return self.n

    def get_item(self,index):
        if not 0<index<self.size:
            return "IndexError(Index is out of range)"
        return self.array[index]

    def append(self,element):
        if self.n==self.size:
            return "This list is at max capacity"
        self.array[self.n]=element
        self.n+=1
        return

    def pop(self):
        self.array[self.n]=None
        self.n-=1
        return self.display()

    def _make_array(self,new_size):
        return (new_size*ctypes.py_object)()

    def display(self):
        for i in range(self.n):
            print(self.array[i])
        return
