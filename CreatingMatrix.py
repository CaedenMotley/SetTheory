def SetFindr():
    setlist = input('input your set in format of (a,b)(b,a): ')[1:-1].split(")(")
    return setlist
def Orgset(setlist):
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
    for set in setlist:
        set = set.split(',')
        matrix[int(set[1]) ][int(set[0])] = 1
    for row in matrix:
        print(row)


def main():
    setlist = SetFindr()
    orgnums = Orgset(setlist)
    matrix = create_matrix(orgnums)
    fillmatrix(matrix,setlist)
main()
