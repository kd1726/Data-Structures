#Since a priportiy queue is simply data abstrction of a heap, we will create the heap data structure
#Iterative min heap
class Heap:
    def __init__(self,array):
        self.heap = array
        self.size = len(array)
        self.Heapify()

    def length(self):
        return len(self.heap)

    def append(self,data):
        self.heap.append(data)
        index = self.size-1
        self.BubbleUp(index)
        self.size+=1
        return self.display()

    def BubbleUp(self,index):
        parentIdx = (index-1)//2
        while index>0 and self.heap[index]<self.heap[parentIdx]:
            self.heap[index],self.heap[parentIdx] = self.heap[parentIdx],self.heap[index]
            index = parentIdx
            parentIdx = (index-1)//2
        return

    def pop(self):
        last = self.heap[self.size-1]
        self.heap[0]= last
        self.heap.pop()
        self.size-=1
        self.BubbleDown()
        return

    def BubbleDown(self,i=0):
        element = self.heap[i]
        left_child = 2*i+1
        right_child = 2*i+2
        children = self.getChildren(left_child,right_child)
        smaller,smalleridx = self.getSmaller(children)
        if children and self.heap[i]>smaller:
            self.heap[i],self.heap[smalleridx]=self.heap[smalleridx],self.heap[i]
            i  = smalleridx
            left_child = 2*i+1
            right_child = 2*i+2
            children = self.getChildren(left_child,right_child)
            smaller,smalleridx = self.getSmaller(children)
        return

    def getChildren(self,left,right):
        children = []
        if left<self.size:
            children.append((self.heap[left],left))
        if right<self.size:
            children.append((self.heap[right],right))
        return children

    def getSmaller(self,children):
        if len(children)==0:
            return float('inf'),None
        if len(children)==1:
            return children[0]
        if len(children)==2:
            childA,idxA = children[0]
            childB,idxB = children[1]
            return children[0] if childA<childB else children[1]

    def Heapify(self):
        i = (self.size-1)//2
        while i>=0:
            self.BubbleDown(i)
            i-=1
        return

    def display(self):
        disp =[]
        for i in range(self.size):
            disp.append(self.heap[i])
        self.Heapify()
        return disp
