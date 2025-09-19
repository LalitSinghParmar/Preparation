from typing import List


class BinarySearch:

    def binarySearch(self, arr:List[int], val:int) -> int:
        '''
        Search an element in an sorted array
        Input: List of an array, val to be search
        Return index of element if found else -1
        '''
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    

if __name__ == '__main__':
    bs = BinarySearch()
    print(bs.binarySearch([1,2,3,4,5],3)) #2
    print(bs.binarySearch([1,2,3,4,5],5)) #4
    print(bs.binarySearch([1,2,3,4,5],4)) #3
    print(bs.binarySearch([1,2,3,4,5],2)) #1
    print(bs.binarySearch([1,2,3,4,5],1)) #0
    print(bs.binarySearch([1,2,3,4,5],7)) #-1
    print(bs.binarySearch([1],3)) #-1
    print(bs.binarySearch([1],1)) #0
    print(bs.binarySearch([1,2],2)) #1
    print(bs.binarySearch([1,2],3)) #-1
