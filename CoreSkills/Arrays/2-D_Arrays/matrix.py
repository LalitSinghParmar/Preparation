from typing import List, Optional

class Matrix:

    def __init__(self, row:int, col:int):
        self.row = row
        self.col = col
        self.arr = []*row
        
    def rowwise_traversal(self) -> None:
        '''
        Traverse matrix row by row, for each row all col and then next row and going on till end
        '''
        print('Rowwise traversal')
        for i in range(self.row):
            for j in range(self.col):
                print(self.arr[i][j], sep=' ', end='')
            print()

    def colwise_traversal(self) -> None:
        '''
        Traverse matrix col by col, for each col all row and then next col and going on till end
        '''
        print('Colwise Traversal')
        for i in range(self.col):
            for j in range(self.row):
                print(self.arr[j][i], sep=' ', end='')
            print()
    
    def initialise(self, vals:list[int]) -> None:
        '''
        Creating a 2-d array/matrix from list of integer
        '''
        i, j = 0, 0
        temp = []
        for val in vals:
            temp.append(val)
            j += 1
            if j >= self.col:
                self.arr.append(temp)
                temp = []
                j = 0
                i += 1
            

if __name__ == '__main__':
    mat1 = Matrix(2,3)
    mat2 = Matrix(3,2)
    mat3 = Matrix(3,3)
    mat4 = Matrix(1,1)

    mat1.initialise([1,2,3,4,5,6])
    print(mat1.arr)
    mat1.colwise_traversal()
    mat1.rowwise_traversal()

    mat2.initialise([1,2,3,4,5,6])
    mat2.colwise_traversal()
    mat2.rowwise_traversal()

    mat3.initialise([1,2,3,4,5,6,7,8,9])
    mat3.colwise_traversal()
    mat3.rowwise_traversal()

    mat4.initialise([1])
    mat4.colwise_traversal()
    mat4.rowwise_traversal()
        
