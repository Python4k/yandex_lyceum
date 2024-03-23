class SparseArray:
    def __init__(self):
        self.storage = {}
        
    def __setitem__(self, key, value):
        if value == 0 and key in self.storage:
            del self.storage.get(key, 0)
        else:
            self.storage[key] = value
        
    def __getitem__(self, key):
        return self.storage.get(key, 0)
    
    
arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))  