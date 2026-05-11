class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for row in board:
            hashset = set()
            for digit in row:
                if digit == '.':
                    continue
                if digit in hashset:
                    return False
                hashset.add(digit)

        # column check
        for col in range(9):
            hashset = set()
            for row in range(9):
                digit = board[row][col]
                if digit == '.':
                    continue
                if digit in hashset:
                    return False
                hashset.add(digit)

        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                hashset = set()
                for r in range(3):
                    for c in range(3):
                        digit = board[boxRow + r][boxCol + c]
                        if digit == '.':
                            continue
                        if digit in hashset:
                            return False
                        hashset.add(digit)
        return True