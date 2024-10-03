class cell:
    row = []
    col = []
    square = []
    candidates = []
    is_set = False
    n = -1

    def __init__(self, n):
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.n = n

    def set(self, n):
        assert n in self.candidates
        self.candidates = [n]
        self._prune(n)
        self.is_set = True

    def _prune(self, n):
        for c in self.row:
            if n in c.candidates:
                c.candidates.remove(n)
        for c in self.col:
            if n in c.candidates:
                c.candidates.remove(n)
        for c in self.square:
            if n in c.candidates:
                c.candidates.remove(n)

