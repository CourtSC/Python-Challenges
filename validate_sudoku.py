"""Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""

from math import isqrt


class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        if not self.data:
            return False
        n = len(self.data)
        # each row must have length n
        if any(len(row) != n for row in self.data):
            return False
        block_size = isqrt(n)
        if block_size * block_size != n or n <= 0:
            return False

        row_sets = [set() for _ in range(n)]
        col_sets = [set() for _ in range(n)]
        block_sets = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                val = self.data[r][c]

                # validate type and range
                if not isinstance(val, int) or val < 1 or val > n:
                    return False

                # row check
                if val in row_sets[r]:
                    return False
                row_sets[r].add(val)

                # column check
                if val in col_sets[c]:
                    return False
                col_sets[c].add(val)

                # block check: compute block index and test it
                br = r // block_size
                bc = c // block_size
                block_index = br * block_size + bc
                if val in block_sets[block_index]:
                    return False
                block_sets[block_index].add(val)

        # all checks passed
        return True
