import ctypes
class DynamicArray:
    def __init__(self):
        self.n = 0
        self.size = 10
        self.array = self.__make_array(self.size)
    
    def length(self):
        return self.n
    
    def get(self,index):
        if (index > self.n or index < 0):
            raise IndexError("This is index if out of range") 
        else:
            return self.array[index]
        
    def find(self,element):
        i = 0
        while i < self.length():
            if self.array[i] == element:
                return self.array[i]
            i+=1
        return "Element not found"
    
    def get_index_of(self,element):
        i = 0
        while i < self.length():
            if self.array[i] == element:
                return i
            i+=1
        return "Element not found"
    
    def pop(self):
        self.array[self.n-1] = None
        self.n-=1
        return self.__display()
    
    def append(self,element):
        if (self.n+1/self.size > 0.7):
            self.__resize()
        self.array[self.n] = element
        self.n+=1
        return self.__display()
            
    def __resize(self):
        new_size = self.size*2
        new_array = self.__make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.size = new_size
        self.array = new_array
        return
    
    def __make_array(self,size):
        return (ctypes.py_object*size)()
    
    def __display(self):
        for i in range(self.n):
            print(self.array[i])
        return