#hash table that resizes based on load factor
class Hash:
    def __init__(self,size=10):
        self.size=10
        self.n =0
        self.hash_table = self._make_hash_table(size)

    def _make_hash_table(self,new_size):
        return [[] for i in range(new_size)]

    def _full_list(self,table):
        full_list =[]
        for i in self.hash_table:
            if i!=[]:
                full_list.append(i)
        return full_list

    def _resize(self,new_size):
        full_list = self._full_list(self.hash_table)
        new_hash_table = self._make_hash_table(new_size)
        for index,value in enumerate(full_list):
            self._set_rehash(value[0][0],value[0][1],new_hash_table)
        self.hash_table = new_hash_table
        self.size=new_size
        return


    def _set_rehash(self,key,value,table):
        hashkey = self._hash_key(key)
        bucket = table[hashkey]
        found_key = False
        if bucket!=[]:
            self._set_resize_prob_value(key,value,hashkey,table)
        elif bucket==[]:
            bucket.append((key,value))
        return

    def _set_resize_prob_value(self,key,value,hashkey,table):
        new_key = self._probe_key(hashkey)
        bucket = table[new_key]
        if bucket!=[]:
            self._set_resize_prob_value(key,value,new_key,table)
        else:
            bucket.append((key,value))
            self.n+=1
        return

    def _hash_key(self,key):
        return hash(key)%self.size

    def _probe_key(self,hash_key):
        return ((hash_key)+1)%self.size

    def set_val(self,key,val):
        hashkey = self._hash_key(key)
        bucket = self.hash_table[hashkey]
        load_factor = float(self.n/self.size)
        found_key = False
        for index,content in enumerate(bucket):
            record_key,record_value = content

            if record_key==key:
                found_key=True
                break

        if found_key:
            bucket[index] = (key,val)
        else:
            if load_factor>0.67:
                self._resize(2*self.size)
            if bucket!=[]:
                self._set_prob_value(key,val,hashkey)
            elif bucket==[]:
                self.n+=1
                bucket.append((key,val))
        return

    def _set_prob_value(self,key,value,hashkey):
        new_key = self._probe_key(hashkey)
        bucket = self.hash_table[new_key]
        if bucket!=[]:
            self._set_prob_value(key,value,new_key)
        else:
            bucket.append((key,value))
            self.n+=1
        return

    def search(self,key):
        hashkey = self._hash_key(key)
        bucket = self.hash_table[hashkey]
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

#I have to adjust the delete function as when the rehas function is at play the key and the rehashed key do not have the same value. As a result it will not be able to delete since it doesn't know the values hash key.
    def delete(self,key):
        hashkey = self._hash_key(key)
        bucket = self.hash_table[hashkey]
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
            disp.append(self.hash_table[i])
        return disp
