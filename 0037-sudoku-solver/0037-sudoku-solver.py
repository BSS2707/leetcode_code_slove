class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def get_candidates(r, c):
            box = (r // 3) * 3 + (c // 3)
            return [ch for ch in "123456789"
                    if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box]]

        def backtrack():
            if not empties:
                return True

            # Choose the cell with the fewest candidates
            empties.sort(key=lambda pos: len(get_candidates(pos[0], pos[1])))
            r, c = empties.pop(0)
            box = (r // 3) * 3 + (c // 3)

            for ch in get_candidates(r, c):
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box].add(ch)

                if backtrack():
                    return True

                # Undo choice
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[box].remove(ch)

            empties.insert(0, (r, c))
            return False

        backtrack()
