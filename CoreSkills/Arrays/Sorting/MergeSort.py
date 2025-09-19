from typing import List, Optional

class MergeSort:

    def merge(self, arr1, arr2):
        temp = []
        i, j = 0, 0
        while i<len(arr1) and j <len(arr2):
            if arr1[i] < arr2[j]:
                temp.append(arr1[i])
                i += 1
            else:
                temp.append(arr2[j])
                j += 1
        if i < len(arr1):
            temp.extend(arr1[i:])
        if j < len(arr2):
            temp.extend(arr2[j:])
        return temp

    def divide(self, arr:List[int], left:int, right:int) -> Optional[int]:
        if left >= right:
            return arr[left:right+1]
        mid = (left + right)//2
        left_arr = self.divide(arr, left, mid)
        right_arr = self.divide(arr, mid+1, right)
        return self.merge(left_arr, right_arr)

    def mergeSort(self, arr:List[int]) -> None:
        arr = self.divide(arr, 0, len(arr)-1)
        print(arr)


if __name__ == '__main__':
    arr1 = [3,3,2,4,1]
    arr2 = [1]
    arr3 = [1,2]
    arr4 = [2,1]
    arr5 = [1,1]
    arr6 = [1,2,3,4]
    arr7 = [4,2,1,3]
    arr8 = [4,3,2,1]
    arr9 = [3,1,2]
    ms = MergeSort()
    ms.mergeSort(arr1)
    ms.mergeSort(arr2)
    ms.mergeSort(arr3)
    ms.mergeSort(arr4)
    ms.mergeSort(arr5)
    ms.mergeSort(arr6)
    ms.mergeSort(arr7)
    ms.mergeSort(arr8)
    ms.mergeSort(arr9)
