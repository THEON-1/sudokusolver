from grid import *
from copy import deepcopy

def solve(G):
    stack = [G]
    while len(stack) > 0:
        grid = stack.pop()
        ret = simplify(grid)
        if ret == 0:
            branch(grid, stack)
    print(G)
    printn("unsolvable!")

def simplify(G):
    sum = 1
    while sum > 0:
        sum = 0
        ret = check_rows(G)
        if ret < 0:
            return -1
        else:
            sum += ret
    
        ret = check_cols(G)
        if ret < 0:
            return -1
        else:
            sum += ret
    
        ret = check_squares(G)
        if ret < 0:
            return -1
        else:
            sum += ret
    
        ret = reduce(G)
        if ret < 0:
            return -1
        else:
            sum += ret
    return 0

def branch(G, stack):
    min_cell = None
    min_cell_size = 10
    for cell in G.cells:
        if cell.is_set == False and len(cell.candidates) < min_cell_size:
            min_cell = cell
            min_cell_size = len(cell.candidates)
    candidates = min_cell.candidates
    for candidate in candidates:
        copy = deepcopy(G)
        copy.cells[min_cell.n].set(candidate)
        stack.append(copy)

def reduce(G):
    n_steps = 0
    while True:
        val = reduce_step(G)
        if val == 0:
            print(G)
            print("done")
            exit(0)
        elif val == 1:
            return n_steps
        n_steps += 1

def reduce_step(G):
    all_set = True
    nochange = True
    for cell in G.cells:
        l = len(cell.candidates)
        if not cell.is_set:
            if l == 1:
                cell.set(cell.candidates[0])
                nochange = False
            else:
                all_set = False
    if all_set:
        return 0
    elif nochange:
        return 1
    else:
        return 2

def check_rows(G):
    res = 0
    for row in G.rows:
        finds = [0]*9
        to_set = []
        for cell in row:
            cell = G.cells[cell]
            for candidate in cell.candidates:
                finds[candidate-1] += 1
        for i, find in enumerate(finds):
            if find == 1:
                to_set.append(i+1)
            elif find == 0:
                return -1
        for cell in row:
            cell = G.cells[cell]
            for i in to_set:
                if i in cell.candidates and not cell.is_set:
                    cell.set(i)
                    res += 1
    return res

def check_cols(G):
    res = 0
    for col in G.cols:
        finds = [0]*9
        to_set = []
        for cell in col:
            cell = G.cells[cell]
            for candidate in cell.candidates:
                finds[candidate-1] += 1
        for i, find in enumerate(finds):
            if find == 1:
                to_set.append(i+1)
            elif find == 0:
                return -1
        for cell in col:
            cell = G.cells[cell]
            for i in to_set:
                if i in cell.candidates and not cell.is_set:
                    cell.set(i)
                    res += 1
    return res

def check_squares(G):
    res = 0
    for square in G.squares:
        finds = [0]*9
        to_set = []
        for cell in square:
            cell = G.cells[cell]
            for candidate in cell.candidates:
                finds[candidate-1] += 1
        for i, find in enumerate(finds):
            if find == 1:
                to_set.append(i+1)
            elif find == 0:
                return -1
        for cell in square:
            cell = G.cells[cell]
            for i in to_set:
                if i in cell.candidates and not cell.is_set:
                    cell.set(i)
                    res += 1
    return res

