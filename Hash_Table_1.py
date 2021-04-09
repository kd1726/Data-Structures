#Hash table with adjancency list collision handling. I could have imported the linked list but I will not reinvent the wheel.
class HashTable:
    def __init__(self,size=10):
        self.size =size
        self.table = self._make_table(self.size)

    def _make_table(self,new_size):
        return [[] for i in range(new_size)]

    def set_val(self,key,val):
        hashkey = hash(key)%self.size
        bucket = self.table[hashkey]
        found_key = False
        for index,content in enumerate(bucket):
            record_key,record_value = content

            if record_key==key:
                found_key=True
                break

        if found_key:
            bucket[index] = (key,val)
        else:
            bucket.append((key,val))
        return

    def search(self,key):
        hashkey = hash(key)%self.size
        bucket = self.table[hashkey]
        found_key = False
        for index,content in enumerate(bucket):
            record_key,record_value = content

            if record_key==key:
                found_key=True
                break

        if found_key:
            return bucket[index]
        else:
            return "No result"

    def delete(self,key):
        hashkey = hash(key)%self.size
        bucket = self.table[hashkey]
        found_key = False
        for index,content in enumerate(bucket):
            record_key,record_value = content

            if record_key==key:
                found_key=True
                break

        if found_key:
            bucket[index].pop()
        else:
            return "No result"

    def show_table(self):
        disp=[]
        for i in range(self.size):
            disp.append(self.table[i])
        return disp
