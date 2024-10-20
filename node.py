"""
This file defines the structure for 
Each puzzle node in the search algorithm.
As per the lecture slides, they will contain
The parent, current state, action, and 
Path-cost. On top of this, it will also
Include the location of the blank tile
So subsequent actions are easier to 
Determine.
"""

class node:

    def __init__(self, parent, puzzle, blank, action, gn, hn):
        """
        parent: previous state (np array)
        puzzle: current state (np array)
        blank: location of blank square
        action: movement from parent to current state
        gn: total moves so far
        hn: estimated cost to goal
        """

        # on the fence about whether to make the blank location 2d
        # as [x,y] in a matrix or 1d as x in a flattened list
        # right now its 2d

        self.parent = parent
        self.puzzle = puzzle
        self.blank = blank
        self.action = action
        self.gn = gn
        self.hn = hn
        self.fn = self.gn + self.hn

    # In order to compare priority of nodes
    # We check their fn costs
    def __lt__(self, nxt):
        return self.fn < nxt.fn

