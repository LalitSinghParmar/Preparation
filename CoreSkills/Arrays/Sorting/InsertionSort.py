from typing import List

class InsertionSort:

    def insertionSort(self, arr:List[int]) -> None:
        '''
        Sort in increasing order

        Definition: Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list 
        into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. 
        You split the cards into two groups: the sorted cards and the unsorted cards. T
        hen, you pick a card from the unsorted group and put it in the right place in the sorted group
        
        @input: list of integer
        @return: None
        '''
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            print(arr)

if __name__ == '__main__':
    ins = InsertionSort()
    arr = [10,5,2,7,11]
    ins.insertionSort(arr)
    print(arr)
