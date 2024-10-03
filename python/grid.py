from cell import *

class grid:
    cells = []
    rows = []
    cols = []
    squares = []

    def __init__(self):
        self.cells = [cell(n) for n in range(81)]

        for i in range(9):
            self.rows.append([_find_i(i, j) for j in range(9)])
            self.cols.append([_find_i(j, i) for j in range(9)])
            self.squares.append([_find_i((i//3)*3 +j, (i//3)*3 +k) for j in range(3) for k in range(3)])

        for i, c in enumerate(self.cells):
            i_row, i_col = _find_coords(i)

            row = [_find_i(i_row, j) for j in range(9)]
            col = [_find_i(j, i_col) for j in range(9)]
            square = [_find_i((i_row//3)*3 +j, (i_col//3)*3 +k) for j in range(3) for k in range(3)]

            row.remove(i)
            col.remove(i)
            square.remove(i)
            
            c.row = [self.cells[j] for j in row]
            c.col = [self.cells[j] for j in col]
            c.square = [self.cells[j] for j in square]

    def get_cell(self, i_row, i_col):
        return self.cells[_find_i(i_row, i_col)]

    def set_cells(self, *tuples):
        for t in tuples:
            a, b, n = t
            self.cells[_find_i(a, b)].set(n)

    def parse_string(s):
        assert len(s) == 81+8
        tuples = []
        lines = s.split('.')
        for i, line in enumerate(lines):
            assert len(line) == 9
            for j, char in enumerate(line):
                if char == " ":
                    pass
                elif char in "123456789":
                    tuples.append((i, j, int(char)))
                else:
                    print("incorrent string!")
                    exit(1)
        G = grid()
        G.set_cells(*tuples)
        return G

    def __repr__(self):
        row_str = "{}{}{} {}{}{} {}{}{} | {}{}{} {}{}{} {}{}{} | {}{}{} {}{}{} {}{}{}"
        format = lambda a, n: row_str.format(*[cell.candidates[i] if i < len(cell.candidates) else " " for cell in self.cells[9*a:9*(a+1)] for i in range(3*n,3*(n+1))])
        return "\n".join([
            format(0, 0), format(0, 1), format(0, 2),
            " "*12+"|"+" "*13+"|",
            format(1, 0), format(1, 1), format(1, 2),
            " "*12+"|"+" "*13+"|",
            format(2, 0), format(2, 1), format(2, 2),
            "-"*39,
            format(3, 0), format(3, 1), format(3, 2),
            " "*12+"|"+" "*13+"|",
            format(4, 0), format(4, 1), format(4, 2),
            " "*12+"|"+" "*13+"|",
            format(5, 0), format(5, 1), format(5, 2),
            "-"*39,
            format(6, 0), format(6, 1), format(6, 2),
            " "*12+"|"+" "*13+"|",
            format(7, 0), format(7, 1), format(7, 2),
            " "*12+"|"+" "*13+"|",
            format(8, 0), format(8, 1), format(8, 2),
            ""
        ])

def _find_coords(i):
    i_row = i//9
    i_col = i%9
    return i_row, i_col

def _find_i(i_row, i_col):
    return 9*i_row + i_col

