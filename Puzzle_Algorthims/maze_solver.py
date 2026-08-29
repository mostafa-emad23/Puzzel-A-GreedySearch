import tkinter as tk
from queue import PriorityQueue

# harder starting state
start = (7,2,4,5,0,6,8,3,1)
goal  = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in moves:
        r, c = row+dr, col+dc
        if 0 <= r < 3 and 0 <= c < 3:
            new = list(state)
            new_zero = r*3 + c
            new[zero], new[new_zero] = new[new_zero], new[zero]
            neighbors.append(tuple(new))
    return neighbors

# ---------- A* with path ----------
def solve_astar():
    pq = PriorityQueue()
    pq.put((0, start))
    parent = {}
    g = {start: 0}

    while not pq.empty():
        _, state = pq.get()

        if state == goal:
            return reconstruct_path(parent, state)

        for n in get_neighbors(state):
            temp_g = g[state] + 1
            if n not in g or temp_g < g[n]:
                g[n] = temp_g
                f = temp_g + heuristic(n)
                parent[n] = state
                pq.put((f, n))

# ---------- Greedy with path ----------
def solve_greedy():
    pq = PriorityQueue()
    pq.put((0, start))
    parent = {}
    visited = set()

    while not pq.empty():
        _, state = pq.get()

        if state == goal:
            return reconstruct_path(parent, state)

        visited.add(state)

        for n in get_neighbors(state):
            if n not in visited:
                parent[n] = state
                pq.put((heuristic(n), n))

# ---------- path ----------
def reconstruct_path(parent, state):
    path = [state]
    while state in parent:
        state = parent[state]
        path.append(state)
    path.reverse()
    return path

# ----------- GUI -----------

class Puzzle:
    def __init__(self, root):
        self.root = root
        self.state = list(start)
        self.buttons = []

        frame = tk.Frame(root)
        frame.pack()

        for i in range(9):
            btn = tk.Button(frame, text="", width=5, height=2,
                            command=lambda i=i: self.move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        tk.Button(root, text="Greedy Solve", command=self.run_greedy).pack()
        tk.Button(root, text="A* Solve", command=self.run_astar).pack()

        self.update()

    def update(self):
        for i in range(9):
            text = "" if self.state[i] == 0 else str(self.state[i])
            self.buttons[i].config(text=text)

    def move(self, i):
        zero = self.state.index(0)
        r1, c1 = divmod(i, 3)
        r2, c2 = divmod(zero, 3)

        if abs(r1 - r2) + abs(c1 - c2) == 1:
            self.state[zero], self.state[i] = self.state[i], self.state[zero]
            self.update()

    def animate(self, path, i=0):
        if i >= len(path):
            return
        self.state = list(path[i])
        self.update()
        self.root.after(500, lambda: self.animate(path, i+1))

    def run_astar(self):
        path = solve_astar()
        self.animate(path)

    def run_greedy(self):
        path = solve_greedy()
        self.animate(path)


root = tk.Tk()
root.title("8 Puzzle Auto Solver")
app = Puzzle(root)
root.mainloop()
