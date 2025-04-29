#Since a priportiy queue is simply data abstrction of a heap, we will create the heap data structure
#recursive min heap
from typing import List
from random import randint
class MinHeapWithArrRecursive:
    def __init__(self,arr):
        self.heap = arr
        self.size = len(self.heap)
        self.__heapify()
    
    def append(self,element):
        if type(element) != int:
            raise TypeError("element must be an integer")
        self.heap.append(element)
        self.__bubbleUp(self.size)
        self.size +=1
        return print(self.heap)
    
    def remove(self,index):
        if index > self.size-1:
            raise IndexError("index if greater than size of heap")
        element = self.heap[index]
        self.heap.remove(element)
        self.size-=1
        self.__heapify()
        return print(self.heap)
            
    def __bubbleUp(self,index):
        element = self.heap[index]
        parent_idx = index//2
        parent = self.heap[parent_idx]
        return self.__handleBubbleUp(parent,parent_idx,element,index)
        
    def __handleBubbleUp(self,parent,parent_idx,element,element_idx):
        if parent > element:
            self.heap[parent_idx], self.heap[element_idx] = self.heap[element_idx],self.heap[parent_idx]
            element_idx = parent_idx
            parent_idx = element_idx//2
            element = self.heap[element_idx]
            parent = self.heap[parent_idx]
            return self.__handleBubbleUp(parent,parent_idx,element,element_idx)
        return
    
    def __bubbleDown(self,index):
        parent = self.heap[index]
        left, right = self.__getChildren(index)
        left_child,left_child_idx = left
        right_child,right_child_idx = right
        smaller = self.__getSmaller(self.__getChildren(index))
        return self.__handleBubbleDown(index,parent,left_child,right_child,left_child_idx,right_child_idx,smaller)
    
    def __handleBubbleDown(self,index,parent,left_child,right_child,left_child_idx,right_child_idx,smaller):
        if not smaller:
            return print("Next iteration")
        if smaller[0] < parent:
            self.heap[smaller[1]], self.heap[index] = self.heap[index], self.heap[smaller[1]]
            index = smaller[1]
            parent = self.heap[index]
            left, right = self.__getChildren(index)
            left_child,left_child_idx = left
            right_child,right_child_idx = right
            smaller = self.__getSmaller(self.__getChildren(index))
            return self.__handleBubbleDown(index,parent,left_child,right_child,left_child_idx,right_child_idx,smaller)
        return
            
        
        
    def __getChildren(self,index):
        left_child = 2*index+1
        right_child = 2*index+2

        left_child = self.heap[left_child] if left_child < self.size else None
        right_child = self.heap[right_child] if right_child < self.size else None

        return [(left_child,2*index+1),(right_child,2*index+2)]
    
    def __getSmaller(self,children):
        if type(children) != list:
            raise TypeError("children must be a list")

        if not self.__is_int(children[0][0]) and not self.__is_int(children[1][0]):
            return None
        if self.__is_int(children[0][0]) and not self.__is_int(children[1][0]):
            return children[0]
        if self.__is_int(children[1][0]) and not self.__is_int(children[0][0]):
            return children[1]
        if self.__is_int(children[0][0]) and self.__is_int(children[1][0]):
            return children[0] if children[0][0] < children[1][0] else children[1]
    
    def __is_int(self,element):
        return type(element) == int
    
    def __heapify(self):
        index = self.size // 2
        while index>=0:
            self.__bubbleDown(index)
            index-=1
        return print(self.heap)
y= []
for i in range(0,10):
  y.append(randint(1,123))
print(y)
x = MinHeapWithArrRecursive(y)
x.append(0)