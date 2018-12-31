import numpy as np


class Printer:

    def printBoard(self, list1, list2):
        board = np.zeros((15, 15), dtype=np.int)
        for piece in list1:
            board.itemset((piece.getX(), piece.getY()), 1)
        for piece in list2:
            board.itemset((piece.getX(), piece.getY()), 2)
        for i in range(0, 15):
            for j in range(0, 15):
                print(str(board.item((i, j))) + " ", end="")
            print()
