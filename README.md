# Graph Traversal Visualization

This project demonstrates the visualization of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms on a randomly generated graph using Python, NetworkX, and Matplotlib.

## Description

The program generates a random connected graph and performs BFS and DFS starting from a specified node. It visualizes the traversal process step-by-step, highlighting the current node being visited and displaying the traversal order as an array in real-time.

## Requirements

- Python 3.x
- NetworkX
- Matplotlib

You can install the required Python packages using pip:

```sh
pip install networkx matplotlib
```
## Files
graph_traversal.py: The main script containing the BFS, DFS, graph generation, and visualization functions.
Usage
Clone the repository (if hosted on a version control system like GitHub):

```sh
git clone https://github.com/ishan-sharma-3004/graph-traversal-visualization.git
cd graph-traversal-visualization
```

```sh
python graph_traversal.py
```
## Functions
bfs(graph, start_node)
Performs Breadth-First Search on the graph starting from start_node.

Parameters:

graph: The graph on which BFS is performed.
start_node: The starting node for BFS.
Returns:

order: A list of nodes in the order they are visited during BFS.
dfs(graph, start_node)
Performs Depth-First Search on the graph starting from start_node.

Parameters:

graph: The graph on which DFS is performed.
start_node: The starting node for DFS.
Returns:

order: A list of nodes in the order they are visited during DFS.
visualize_search(order, title, G, pos)
Visualizes the traversal process.

Parameters:
order: A list of nodes in the order they are visited.
title: The title of the plot.
G: The graph to be visualized.
pos: The positions of the nodes for visualization.
generate_graph(n, m)
Generates a random connected graph with n nodes and m edges.

Parameters:

n: Number of nodes.
m: Number of edges.
Returns:

G: A randomly generated connected graph.
Example Output
When you run the script, it generates a random graph and visualizes the BFS and DFS traversals. The traversal order is displayed as an array, updating in real-time as nodes are visited.
