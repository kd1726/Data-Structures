from random import randint

class MinHeapWithArrIterative:
    def __init__(self,arr):
        self.heap = arr
        self.size = len(self.heap)
        self.__heapify()
        
    def append(self, element):
        self.heap.append(element)
        self.size +=1
        self.__bubbleUp(self.size-1)
        return print(self.heap)
        
    
    def remove(self, index):
        if index >= self.size:
            raise IndexError("index value is greater than total size of heap")
        self.heap.remove(self.heap[index])
        self.size-=1
        self.__heapify()
        return print(self.heap)
    
    def __bubbleUp(self, index):
        idx = index
        parent_idx = index //2 -1
        parent = self.heap[parent_idx]
        element = self.heap[idx]
        
        while parent > element:
            self.heap[parent_idx], self.heap[idx] =  self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
            parent_idx = idx //2
            parent = self.heap[parent_idx]
            element = self.heap[idx]
        return
    
    def __bubbleDown(self,idx):
        index = idx
        reheapify = True
        while index >= 0:
            if index==0 and reheapify:
                reheapify = False
                index = idx
                
            element = self.heap[index]
            left_child,right_child = self.__getChildren(index)
            smaller = self.__getSmaller(self.__getChildren(index))

            if not hasattr(smaller, '__iter__'):
                print("next iteration")
                index-=1
                continue
            elif smaller[1] < element :
                self.heap[smaller[0]],self.heap[index] = self.heap[index],self.heap[smaller[0]]
                index = smaller[0]//2 
            else:
                index-=1
            
        
    def __getChildren(self,idx):
        left_child_idx = 2*idx +1
        right_child_idx = 2*idx +2
        left_child = None if left_child_idx >= self.size else self.heap[left_child_idx]
        right_child = None if right_child_idx >= self.size else self.heap[right_child_idx]
        return [(left_child_idx,left_child),(right_child_idx,right_child)]
    
    def __getSmaller(self,children):
        left_child = children[0][1]
        right_child = children[1][1]
        
        if left_child and not right_child:
            return left_child
        if right_child and not left_child:
            return right_child
        if right_child and left_child:
            return children[0] if left_child < right_child else children[1]
        
    def __heapify(self):
        idx =  self.size//2
        self.__bubbleDown(idx)
        return print(self.heap)

y = [randint(1,122) for i in range(0,11)]

x = MinHeapWithArrIterative(y)

print(y)

x.append(2)
x.append(12)
x.remove(8)