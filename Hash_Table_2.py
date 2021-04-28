# I thought that maybe having the number of times an addition needed to rehash as well as mapping that number to the actual data
#would make it easier to do the search. I'm still figuring that part out.
class Hash:
    def __init__(self,size=10):
        self.size = size
        self.n = 0
        self.table = self._make_hash_table(self.size)
        self.iterations = self._make_hash_table(self.size)

    def _make_hash_table(self,new_size):
        return [[] for i in range(new_size)]

    def _filter_empty_spots(self,table):
        full_list = []
        for i in table:
            if i!=[]:
                full_list.append(i)

        return full_list

    def _resize(self,new_size,table):
        items = self._filter_empty_spots(table)
        new_hash_table = self._make_hash_table(new_size)
        new_iterations = self._make_hash_table(new_size)
        for i,content in enumerate(items):
            keys = content[0][0]
            vals = content[0][1]
            self._resizinghash(keys,vals,new_hash_table,new_iterations,iterations = 0)
            print(keys,vals)
        self.table = new_hash_table
        self.size = new_size
        self.iterations = new_iterations
        return

    def hash_key(self,key):
        return hash(key)%self.size

    def _probing_function(self,hash_key):
        return (hash_key+1)%self.size

    def set_val(self,key,val):
        hash_key = self.hash_key(key)
        bucket = self.table[hash_key]
        iters = self.iterations[hash_key]
        iterations = 0
        load_factor = self.n/self.size
        found_key = False
        for idx,content in enumerate(bucket):
            record_key,record_val = content

            if record_key==key:
                found_key = True
                break;
        if found_key:
            bucket[idx] = (key,val)
        else:
            if load_factor > 0.67:
                self._resize(2*self.size,self.table)
            if bucket!=[]:
                iterations+=1
                return self._rehash(key,val,hash_key,iterations)
            else:
                bucket.append((key,val))
                iters.append(1)
                self.n+=1
                return

    def _rehash(self,key,val,hash_key,iterations):
        new_key = self._probing_function(hash_key)
        bucket = self.table[new_key]
        iters = self.iterations[new_key]
        for idx,content in enumerate(bucket):
            record_key,record_val = content

        if bucket!=[]:
            iterations+=1
            return self._rehash(key,val,new_key,iterations)
        else:
            bucket.append((key,val))
            iters.append(iterations)
            self.n+=1
            return

    def _resizinghash(self,key,val,table,iterations_table,iterations):
        hash_key = self.hash_key(key)
        bucket = table[hash_key]
        iters = iterations_table[hash_key]
        for idx,content in enumerate(bucket):
            record_key,record_val = content
        if bucket==[]:
            bucket.append((key,val))
            iters.append(iterations)
            return
        else:
            iterations+=1
            return self._resizingrehash(key,val,hash_key,table,iterations_table,iterations)

    def _resizingrehash(self,key,val,hash_key,table,iterations_table,iterations):
        new_key = self._probing_function(hash_key)
        bucket = table[new_key]
        iters = iterations_table[new_key]
        for idx,content in enumerate(bucket):
            record_key,record_val = content

        if bucket!=[]:
            iterations+=1
            return self._resizingrehash(key,val,new_key,table,iterations_table,iterations)
        else:
            bucket.append((key,val))
            iters.append(iterations)
            self.n+=1
            return

    def search(self,key):
        hash_key = self.hash_key(key)
        bucket = self.table[hash_key]
        num_of_rehash = self.iterations[hash_key]
        found_key = False
        for idx,content in enumerate(bucket):
            record_key,record_val = content

            if record_key==key:
                found_key = True
                break;

        if found_key:
            return bucket[idx]
        else:
            iteration = 1
            return self._searchagain(key,hash_key,iteration)

    def _searchagain(self,key,hash_key,iterations):
        new_key = self._probing_function(hash_key)
        bucket = self.table[new_key]
        num_of_rehash = self.iterations[new_key]
        found_key=False
        for idx,content in enumerate(num_of_rehash):
            record_key,record_val = content

            if record_key==key:
                found_key = True
                break;

        if found_key:
            for i in range(num_of_rehashp[idx]-iterations):
                the_key = self._probing_function(new_key)
            return bucket[the_key]
        else:
            return "No result"

    def print_table(self):
        disp = []
        for i in range(self.size):
            disp.append(self.table[i])
        return disp

    def print_itertable(self):
        disp = []
        for i in range(self.size):
            disp.append(self.iterations[i])
        return disp

    def delete(self,key):
        hash_key = self.hash_key(key)
        bucket = self.table[hash_key]
        found_key = False
        for idx,content in enumerate(bucket):
            record_key,record_val = content

            if record_key==key:
                found_key = True
                break;
        if found_key:
            bucket.pop()
        else:
            return "Nothing to delete"
