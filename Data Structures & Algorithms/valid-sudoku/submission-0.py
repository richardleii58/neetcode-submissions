class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowh = [set() for _ in range(9)]
        colh = [set() for _ in range(9)]
        sqh = [set() for _ in range(9)]

        for row in range(len(board)):
            for num in range(len(board[row])):
                print(colh[num])

                # row check
                if board[row][num] != ".":
                    if board[row][num] in rowh[row]:
                        return False
                    else:
                        rowh[row].add(board[row][num])

                    # column check
                    if board[row][num] in colh[num]:
                        return False
                    else: 
                        colh[num].add(board[row][num])

                    # square check
                    square_index = (row // 3) * 3 + (num // 3)
                    if board[row][num] in sqh[square_index]:
                        return False
                    else:
                        sqh[square_index].add(board[row][num])

        return True
