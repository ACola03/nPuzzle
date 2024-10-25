"""
This file will calculate the
Second heuristic for the puzzle
Implementation. The heuristic
Is the Manhattan Distance 
As seen in the lecture slides.
To calculate the distance, numpy
Lists will be used as they support
Element-wise subtraction and summation.
"""

import numpy as np
from createPuzzle import createPuzzle

def manhattanDistance(puzzle):
    """
    1. We ignore the location of tile 0
    2. We create a temporary (temp) np array to store 
       the location of the current tile. 
    3. We lookup the correct position of the current 
       tile using correctPositions
    4. We then compare the two xy positions by 
       subtracting them to get the distance in 
       each direction. 
    5. Using abs() on a np array makes every
       index positive
    6. We then sum the x and y elements to 
       get the Manhattan Distance for the
       individual tile 
    """


    # the dimension of the puzzle to loop over
    dimension = len(puzzle)
    manDis = 0

    # define the correct positions
    correctPositions = {}

    for i in range(dimension**2-1):
      row = i // dimension
      column = i % dimension
      correctPositions[i+1] = np.array([row,column])

    for row in range(dimension):
        for column in range(dimension):
            
            if puzzle[row][column] != 0:

                temp = np.array([row, column])
                manDis = manDis + sum(abs(temp - correctPositions[(puzzle[row][column])]))

    return manDis

# Driver:
if __name__ == "__main__":
    puzzle = createPuzzle(5)    
    print(puzzle)

    md = manhattanDistance(puzzle)

    print(md)
