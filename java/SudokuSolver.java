
public class SudokuSolver {
    public static final String hard = " 5  1   6.3  5 8 9 .     7 4 .       2 . 9   31  .     1  9. 8 36 9 5.92       .6   7  8 ";
    public static final String extreme = "  1   7  .    1 485.84 6   3 .5  19    .  35    6.      5  . 593  64 .18 72   3.3        ";
    public static void main(String[] args) {
        Grid G = new Grid(SudokuSolver.hard);
        System.out.println(G);
    }
}

