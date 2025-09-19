from typing import List

class SelectionSort:

    def selectionSort(self, arr:List[int]) -> None:
        '''
        Sort in increasing order

        Definition: Selection Sort is a comparison-based sorting algorithm. It sorts an array by 
        repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. 
        This process continues until the entire array is sorted.

        @input: list of integer
        @return: None
        '''

        for i in range(len(arr)):
            idx = i
            for j in range(i, len(arr)):
                if arr[j] < arr[idx]:
                    idx = j
                    
            arr[i], arr[idx] = arr[idx], arr[i]
            print(arr)


if __name__ == '__main__':
    ss = SelectionSort()
    arr = [2,10,5,7,11]
    ss.selectionSort(arr)
    print(arr)