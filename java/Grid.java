
public class Grid {
    private Cell[] cells = new Cell[81];
    private Cell[][] rows = new Cell[9][9];
    private Cell[][] squares = new Cell[9][9];

    public Grid() {
        initializeCells();
    }

    public Grid(String repr) {
        initializeCells();
        parseRepr(repr);
    }

    private void initializeCells() {
        for (int i = 0; i < 81; i++) {
            this.cells[i] = new Cell(i);
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                Cell cell = this.cells[9*i +j];

                this.rows[i][j] = cell;
                this.squares[3*(i/3) +(j/3)][3*(i%3) +(j%3)] = cell;
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                Cell cell = this.cells[9*i +j];
                int curr_square = 3*(i%3) + (j%3);

                Cell[] row = new Cell[8];
                Cell[] col = new Cell[8];
                Cell[] square = new Cell[8];

                int offset_row = 0;
                int offset_col = 0;
                int offset_square = 0;
                for (int k = 0; k < 8; k++) {
                    if (k == j) {
                        offset_row = 1;
                    }
                    if (k == i) {
                        offset_col = 1;
                    }
                    if (k == curr_square) {
                        offset_square = 1;
                    }

                    row[k] = this.rows[i][k+offset_row];
                    col[k] = this.rows[k+offset_col][j];
                    square[k] = this.squares[3*(i/3) +(j/3)][k+offset_square];
                }

                cell.finishInit(row, col, square);
            }
        }
    }

    @Deprecated
    public void setCell(int n, int v) {
        this.cells[n].set(v);
    }

    private void parseRepr(String repr) {
        String[] rows = repr.split("\\.");
        assert rows.length == 9;
        for (int i = 0; i < rows.length; i++) {
            String line = rows[i];
            assert line.length() == 9;

            for (int j = 0; j < 9; j++) {
                char c = line.charAt(j);
                if (c != ' ') {
                    int val = c - '0';
                    this.cells[9*i +j].set(val);
                }
            }
        }
    }

    @Override
    public String toString() {
        Character[][] values = new Character[27][27];
        for (int i = 0; i < 27; i++) {
            for (int j = 0; j < 27; j++) {
                int value = 3*(i%3) +(j%3) +1;
                values[i][j] = this.rows[i/3][j/3].probe(value)
                    ? (char)('0'+value)
                    : ' ';
            }
        }
        String formatString = "%c%c%c %c%c%c %c%c%c | %c%c%c %c%c%c %c%c%c | %c%c%c %c%c%c %c%c%c\n";
        String delim1 = "            |             |\n";
        String delim2 = "---------------------------------------\n";
        return 
            String.format(formatString, (Object [])values[0])+
            String.format(formatString, (Object [])values[1])+
            String.format(formatString, (Object [])values[2])+
            delim1+
            String.format(formatString, (Object [])values[3])+
            String.format(formatString, (Object [])values[4])+
            String.format(formatString, (Object [])values[5])+
            delim1+
            String.format(formatString, (Object [])values[6])+
            String.format(formatString, (Object [])values[7])+
            String.format(formatString, (Object [])values[8])+
            delim2+
            String.format(formatString, (Object [])values[9])+
            String.format(formatString, (Object [])values[10])+
            String.format(formatString, (Object [])values[11])+
            delim1+
            String.format(formatString, (Object [])values[12])+
            String.format(formatString, (Object [])values[13])+
            String.format(formatString, (Object [])values[14])+
            delim1+
            String.format(formatString, (Object [])values[15])+
            String.format(formatString, (Object [])values[16])+
            String.format(formatString, (Object [])values[17])+
            delim2+
            String.format(formatString, (Object [])values[18])+
            String.format(formatString, (Object [])values[19])+
            String.format(formatString, (Object [])values[20])+
            delim1+
            String.format(formatString, (Object [])values[21])+
            String.format(formatString, (Object [])values[22])+
            String.format(formatString, (Object [])values[23])+
            delim1+
            String.format(formatString, (Object [])values[24])+
            String.format(formatString, (Object [])values[25])+
            String.format(formatString, (Object [])values[26]);
    }
}

