#! /usr/bin/env python


class MaxSizeList:
    
    def __init__(self, size):
        self.size = size
        self.bucket = []
        
    def push(self, item):
        
        
        if len(self.bucket) < (self.size):
            self.bucket.append(item)
        else:
            self.bucket.pop(0)
            self.bucket.append(item)
        
        return

    def get_list(self):
        return self.bucket


class CheckVarType:

    counter = 10

    def __init__(self, var):
        self.var = var
        CheckVarType.counter += 1

    def get_var(self):
        return self.var

    def get_counter(self):
        return CheckVarType.counter
    
    
def main():
    
    a = MaxSizeList(3)
    b = MaxSizeList(1)
    
    a.push("hey")
    a.push("ho")
    a.push("let's")
    a.push("go")
    
    b.push("hey")
    b.push("ho")
    b.push("let's")
    b.push("go")

    print(a.get_list())
    print(b.get_list())


    x = CheckVarType(4)
    y = CheckVarType(10)
    z = CheckVarType(20)


    for obj in [x, y, z]:
        print('Instance variable: ', obj.get_var())
        print('Class variable: ', obj.counter)

    x.counter = 30

    print("Let's see if this updates across all: ", y.counter, z.counter)

if __name__ == '__main__':
    main()