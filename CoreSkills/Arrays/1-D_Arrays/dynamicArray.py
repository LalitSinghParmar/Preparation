from typing import Optional

class DynamicArray:

    def __init__(self, capacity:int):
        '''
        Initialize empty array of initial capacity as capacity and initial size 0
        '''
        self.array = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        '''
        return element present at index i if index i is valid
        else raise IndexError
        '''
        if i>=0 and i < self.size:
            return self.array[i]
        else:
            raise IndexError(f"Index- {i}, is out of range-{self.size}")

    def set(self, i: int, n: int) -> None:
        '''
        set element at index i of an array
        '''
        if i>=0 and i < self.capacity:
            self.array[i] = n
            self.size = i+1
        else:
            raise IndexError(f"Index- {i}, is beyond capacity- {self.capacity} range")

    def pushback(self, n: int) -> None:
        '''
        add element to an array in the end if array size is less than it's capacity
        else it increase the array capacity and then add
        '''
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        '''
        If array is non empty then pop out element from back
        '''
        if self.size > 0:
            ret_val = self.array[self.size-1]
            self.array[self.size-1] = None
            self.size -= 1
            return ret_val
        else:
            raise "Error: Empty array"

    def resize(self) -> None:
        '''
        Double the size of an array
        '''
        self.array = self.array + [None]*self.capacity
        self.capacity += self.capacity

    def getSize(self) -> int:
        '''
        Return the current size of an array
        '''
        return self.size     
    
    def getCapacity(self) -> int:
        '''
        Return current allowed capacity of an array
        '''
        return self.capacity
    

if __name__ == '__main__':
    # test = ["Array", 1, "getSize", "getCapacity"]
    test = ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
    # test = ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
    result = []
    dynamicArr = DynamicArray(test[1])
    result.append(None)
    i = 2
    while i<len(test):
        if test[i] == "getSize":
            result.append(dynamicArr.getSize())
        elif test[i] == "getCapacity":
            result.append(dynamicArr.getCapacity())
        elif test[i] == "pushback":
            i += 1
            result.append(dynamicArr.pushback(test[i]))
        elif test[i] == "get":
            i += 1
            result.append(dynamicArr.get(test[i]))
        elif test[i] == "set":
            val = test[i+1]
            idx = test[i+2]
            i += 2
            result.append(dynamicArr.set(val, idx))
        elif test[i] == "popback":
            result.append(dynamicArr.popback())
        i += 1
    print(dynamicArr.array)
    print(result)
        




