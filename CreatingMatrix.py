"""
    File: CreatingMatrix.py
    Author: Caeden Motley
    Purpose: This program is the FIRST to be executed within the SetTheory
    program and will intake a users set and create a corresponding matrix.
    Both of these will then be written into a text file 'MySet'.
"""

def SetFindr():
    ''' takes user input and formats the set into a list'''
    setlist = input('input your set in format of (a,b)(b,a): ')[1:-1].split(")(")
    return setlist

def Orgset(setlist):
    ''' Takes the set and returns the universe in ascending order

    :param setlist: the users set in list format
    :return: a list of all potential numbers
    '''
    numset =[]
    for set in setlist:
        set = set.split(',')
        if set[0] not in numset and set[0] != set[1]:
            numset.append(set[0])
        if set[1] not in numset:
            numset.append(set[1])
    numset.sort()
    return numset

def create_matrix(orgnums):
    ''' Creates an empty list of lists which represents a matrix.

    :param orgnums: The ordered Universe of numbers (ascending order)
    :return: An empty matrix WITH THE UNIVERSAL VALUES LABELED
    '''
    # Determine the dimensions of the grid
    num_rows = len(orgnums) + 1
    num_cols = len(orgnums) + 1
    # Create the grid filled with zeros
    grid = [[0] * num_cols for _ in range(num_rows)]
    # Assign the numbers to the top row and left column
    for i in range(1,num_rows):
        grid[0][i] = int(orgnums[i-1])
        grid[i][0] = int(orgnums[i-1])

    return grid

def fillmatrix(matrix,setlist):
    ''' fills the matrix with either 1's representing a pair which occurs
    within the set, and 0's meaning it does not occur

    :param matrix: An empty set of sets representing a Matrix
    :param setlist: The users desired set represented as a list
    :return: The printed version of the matrix
    '''
    for set in setlist:
        set = set.split(',')
        matrix[int(set[1]) ][int(set[0])] = 1
    return matrix

def save_set(setlist,matrix):
    ''' Writes the set and matrix
    to a text file which will be used in later processes'''
    MySet = open("MySet","w")
    MySet.write('Your Set:'+'\n' + str(setlist) + '\n\n')
    MySet.close()
    MySet = open("MySet", "a")
    MySet.write('Your sets matrix representation:' + '\n')
    for row in matrix:
        MySet.write(str(row) + '\n')
    MySet.write('\n')
    MySet.close
    return

def main():
    setlist = SetFindr()
    orgnums = Orgset(setlist)
    matrix = create_matrix(orgnums)
    filledmatrix = fillmatrix(matrix,setlist)
    save_set(setlist,filledmatrix)

main()
