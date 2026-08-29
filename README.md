# 🧩 8-Puzzle Solver — A\* & Greedy Search

A Python implementation of the **8-Puzzle problem** using two AI search algorithms:

- **A\* Search**
- **Greedy Best-First Search**

The project includes a simple **Tkinter GUI** that allows the user to interact with the puzzle and automatically solve it using either algorithm.

## 📌 About the Project

The **8-Puzzle** is a sliding puzzle consisting of 8 numbered tiles and one empty space arranged in a 3×3 grid.

The goal is to move the tiles until the puzzle reaches the target configuration:

```text
1 2 3
4 5 6
7 8 _
```

This project demonstrates how different search strategies can be used to find a path from an initial state to the goal state.

## 🤖 Algorithms

### A\* Search

A\* evaluates each state using:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` = cost from the initial state to the current state.
- `h(n)` = estimated cost from the current state to the goal.
- `f(n)` = total estimated cost.

The project uses the **Misplaced Tiles heuristic**:

```text
h(n) = number of misplaced tiles
```

The blank space is not counted.

A\* is designed to find an optimal solution when the heuristic is admissible.

### Greedy Best-First Search

Greedy Search selects states based only on the heuristic:

```text
f(n) = h(n)
```

It focuses on the state that appears closest to the goal without considering the cost already spent.

This can make it faster in some cases, but it does **not guarantee an optimal solution**.

## 🔍 A\* vs Greedy Search

| Algorithm  | Evaluation    | Optimal? | Main Idea                           |
| ---------- | ------------- | -------- | ----------------------------------- |
| **A\***    | `g(n) + h(n)` | Yes\*    | Considers cost + estimated distance |
| **Greedy** | `h(n)`        | No       | Focuses only on estimated distance  |

> - A\* optimality depends on the heuristic and implementation conditions.

## 🖥️ Features

- Interactive 8-Puzzle GUI
- Manual tile movement
- Automatic solving with **A\***
- Automatic solving with **Greedy Search**
- Animated solution path
- Misplaced Tiles heuristic
- Path reconstruction

## 🛠️ Technologies Used

- Python
- Tkinter
- Priority Queue
- Recursion
- Graph Search Algorithms

## 📂 Project Structure

```text
Puzzel-Algorithms/
│
├── puzzle_solver.py
├── README.md
└── ...
```

## 🚀 How to Run

Make sure Python is installed.

Run:

```bash
python puzzle_solver.py
```

The GUI will open automatically.

## 🎮 How to Use

### Manual Mode

Click on a tile next to the empty space to move it.

### Greedy Search

Click:

```text
Greedy Solve
```

The program will calculate and animate a solution using Greedy Best-First Search.

### A\* Search

Click:

```text
A* Solve
```

The program will calculate and animate a solution using A\* Search.

## 🧠 Example

Initial state:

```text
7 2 4
5 _ 6
8 3 1
```

Goal state:

```text
1 2 3
4 5 6
7 8 _
```

The selected search algorithm explores possible states until it finds a path to the goal.

## 📚 Concepts Demonstrated

This project demonstrates practical applications of:

- Artificial Intelligence
- Uninformed and informed search
- Heuristic functions
- State-space representation
- Priority queues
- Graph traversal
- Path reconstruction
- Recursion

## 👨‍💻 Author

**Mostafa Emad**

GitHub: [@mostafa-emad23](https://github.com/mostafa-emad23)
