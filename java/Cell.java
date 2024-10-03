import java.util.BitSet;

public class Cell {
    private BitSet candidates = new BitSet(9);
    private Cell[] row;
    private Cell[] col;
    private Cell[] square;
    public final int pos;
    private int n_set;

    public Cell(int pos) {
        this.candidates.set(0, 9);
        this.n_set = 9;
        this.pos = pos;
    }

    public void finishInit(Cell[] row, Cell[] col, Cell[] square) {
        this.row = row;
        this.col = col;
        this.square = square;
    }

    public void set(int i) {
        this.candidates.clear(0, 9);
        this.candidates.set(i-1);
        this.n_set = 1;

        for (Cell cell: this.row) {
            cell.clear(i);
        }
        for (Cell cell: this.col) {
            cell.clear(i);
        }
        for (Cell cell: this.square) {
            cell.clear(i);
        }
    }

    public void clear(int i) {
        this.candidates.clear(i-1);
        this.n_set -= 1;
    }

    public boolean probe(int i) {
        return candidates.get(i-1);
    }

    public boolean getIsSet() {
        return this.n_set == 1;
    }
}

