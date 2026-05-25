class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_sets = [set() for _ in range(9)]
        cols_sets = [set() for _ in range(9)]
        boxes_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == ".":
                    continue

                k = i//3*3 + j//3
                print(f"i: {i} j: {j} k: {k} current: {current}")
                if current in rows_sets[i] or current in cols_sets[j] or current in boxes_sets[k]:
                    return False

                rows_sets[i].add(current)
                cols_sets[j].add(current)
                boxes_sets[k].add(current)

        return True