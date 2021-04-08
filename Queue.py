#I figured that I could use a linked list as an abstract data ctypes
#for this data structure. However, I decided to not reinvent the wheel and just use the
# python list object notation
class Queue:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.queue = []

    def length(self):
        return self.size

    def peek_front(self):
        return self.queue[self.n-1]

    def peek_back(self):
        return self.queue[0]

    def isEmpty(self):
        if self.queue!=[]:
            return False
        return True

    def back_enqueue(self,element):
        self.queue.append(element)
        self.n +=1
        self.size+=1
        return self.display()

    def front_enqueue(self,element):
        self.queue.insert(0,element)
        self.n +=1
        self.size+=1
        return self.display()
#I didn't design this to support mass deletion. As a result it would be pendantic to delete
#all of the elements as you would need to say where you would like to delete for each iteration.
    def dequeue(self):
        ask = input("Are you dequeing from the tail(T) or the head (H)?").upper()
        if ask=="H":
            self.queue.pop()
            self.n-=1
            self.size-=1
        elif ask=="T":
            self.queue.remove(self.queue[0])
            self.n-=1
            self.size-=1
        return self.display()

    def display(self):
        return self.queue
