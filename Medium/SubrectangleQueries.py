# Solution author: Alexadre de Rosso Crestani
# Problem picked from Leet Code website: https://leetcode.com/

# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
# Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).

# 2. getValue(int row, int col)
# Returns the current value of the coordinate (row,col) from the rectangle.
 

# Example 1:
# Input
# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
# [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
# Output
# [null,1,null,5,5,null,10,5]
# Explanation
# SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
# // The initial rectangle (4x3) looks like:
# // 1 2 1
# // 4 3 4
# // 3 2 1
# // 1 1 1
# subrectangleQueries.getValue(0, 2); // return 1
# subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
# // After this update the rectangle looks like:
# // 5 5 5
# // 5 5 5
# // 5 5 5
# // 5 5 5 
# subrectangleQueries.getValue(0, 2); // return 5
# subrectangleQueries.getValue(3, 1); // return 5
# subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
# // After this update the rectangle looks like:
# // 5   5   5
# // 5   5   5
# // 5   5   5
# // 10  10  10 
# subrectangleQueries.getValue(3, 1); // return 10
# subrectangleQueries.getValue(0, 2); // return 5

# Example 2:
# Input
# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
# [[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
# Output
# [null,1,null,100,100,null,20]
# Explanation
# SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
# subrectangleQueries.getValue(0, 0); // return 1
# subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
# subrectangleQueries.getValue(0, 0); // return 100
# subrectangleQueries.getValue(2, 2); // return 100
# subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
# subrectangleQueries.getValue(2, 2); // return 20

class SubrectangleQueries:

    # initialize an SubrecltangleQuerie object
    def __init__(self, rectangle: list[list[int]]):
            self.rectangle = rectangle

    # update all spots in the subrectangle limited by row1,col1 and row2,col2
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:

        # for each line, from line dictated by row1 until the line by row2, in...
        # until row2+1 because the iteration go only until one before the given parameter
        for i in range(row1, row2+1):

            # ...in each colum, from colum dictated by col1 until by col2, do
            for j in range(col1, col2+1):

                # overwrite that spor with the newValue
                self.rectangle[i][j] = newValue

    # get the value of one spot
    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]




# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
# [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
# Output
# [null,1,null,5,5,null,10,5]




# Tests:
SubrectangleQuerie = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])

print()
print(f"given rectangle:   {SubrectangleQuerie.rectangle}\n")

print(f"getValue at 0,2:   {SubrectangleQuerie.getValue(0, 2)}\n")

print(f"update 0,0 3,2 5:  {SubrectangleQuerie.updateSubrectangle(0, 0, 3, 2, 5)}")
print(f"given rectangle:   {SubrectangleQuerie.rectangle}\n")

print(f"getValue at 0,2:   {SubrectangleQuerie.getValue(0, 2)}")
print(f"getValue at 3,1:   {SubrectangleQuerie.getValue(3, 1)}\n")

print(f"update 3,0 3,2 10: {SubrectangleQuerie.updateSubrectangle(3, 0, 3, 2, 10)}")
print(f"given rectangle:   {SubrectangleQuerie.rectangle}\n")

print(f"getValue at 0,2:   {SubrectangleQuerie.getValue(0, 2)}")
print(f"getValue at 3,1:   {SubrectangleQuerie.getValue(3, 1)}")