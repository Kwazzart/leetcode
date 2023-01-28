from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_counters = [[0 for i in range(9)] for i in range(9)]
        column_counters = [[0 for i in range(9)] for i in range(9)]
        square_counters = [[[0 for k in range(9)] for j in range(3)] for i in range(3)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j]) - 1

                row_counters[i][value] += 1
                column_counters[j][value] += 1

                x_square = i//3
                y_square = j//3
                square_counters[x_square][y_square][value] += 1

                if 2 in [row_counters[i][value],
                        column_counters[j][value],
                        square_counters[x_square][y_square][value]]:
                    return False
        return True
