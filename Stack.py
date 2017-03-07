class Stack():
    
    def __init__(self):
        self.elems = []

    def push(self, elem):
        self.elems.append(elem)
    
    def pop(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)
        
    def isEmpty(self):
        return self.elems == []