# AI_Lab-Report-03

This repository contains a Python implementation of the Graph Coloring Problem using the Backtracking algorithm, completed for the CSE316 Artificial Intelligence Lab.

## Objective

The main goal of this experiment is to determine whether an undirected graph can be colored using $K$ colors such that no two adjacent vertices share the same color. The implementation focuses on recursive state exploration and constraint satisfaction, ensuring that vertex neighbors are checked for color conflicts before proceeding.

## How to Run

Ensure you have a file named input.txt in the same directory as the script. Then, run the Python script using the following command:
```bash
python lab.py

```
## Example Test Case

**Input:**

```text

4 5 3
0 1
0 2
1 2
1 3
2 3
```

**Output:**
```text
Coloring Possible with 3 Colors
Color Assignment: [1, 2, 3, 1]

```
