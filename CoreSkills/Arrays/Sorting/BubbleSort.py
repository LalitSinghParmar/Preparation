from typing import List

class BubbleSort:

    def bubbleSort(self, arr:List[int]) -> None:
        '''
        Sort array in increasing order
        Definition: Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 
        args: list of integer
        return: None (sort the arr in-place)
        '''
        i, j = 0, 0
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                if arr[j-1] > arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
            print(arr)


if __name__ == '__main__':
    arr = [10,5,2,7,11]
    bs = BubbleSort()
    bs.bubbleSort(arr)
    print(arr)

        
