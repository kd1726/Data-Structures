import ctypes
class DynamicList:
    def __init__(self):
        self.n = 0
        self.size=1
        self.array = self._make_array(self.size)

    def length(self):
        return self.n

    def get_item(self,index):
        if not 0>index>self.size:
            return "IndexError(Index is out of range)"
        return self.array[index]

    def append(self,element):
        if self.n==self.size:
            self._resize(2*self.size)
        self.array[self.n]=element
        self.n+=1
        return
    def pop():
        self.array[self.n]=None
        self.n-=1
        return display()
        
    def _resize(self,new_size):
        new_arr = self._make_array(new_size)
        for i in range(self.n):
            new_arr[i]=self.array[i]
        self.array = new_arr
        self.size = new_size
        return

    def _make_array(self,new_size):
        return (new_size*ctypes.py_object)()

    def display(self):
        for i in range(self.n):
            print(self.array[i])
        return
