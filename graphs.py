import queue
import networkx as nx
import matplotlib.pyplot as plt
import time

def bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []
    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph.neighbors(vertex):
                if node not in visited:
                    q.put(node)
    return order

def dfs(graph, start_node):
    visited = set()
    order = []
    def dfs_recursive(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    dfs_recursive(start_node)
    return order

def visualize_search(order, title, G, pos):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle(title)
    
    for i, node in enumerate(order, start=1):
        ax1.cla()
        ax2.cla()
        
        # Draw graph
        ax1.set_title(f"{title} (Step {i})")
        nx.draw(G, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes], ax=ax1)
        
        # Update traversal order array
        ax2.set_title("Traversal Order")
        ax2.plot(range(i), order[:i], 'ro-')
        ax2.set_xlim(0, len(order))
        ax2.set_ylim(-0.5, max(order) + 0.5)
        ax2.set_xticks(range(len(order)))
        ax2.set_yticks(range(max(order) + 1))
        ax2.grid(True)
        
        plt.draw()
        plt.pause(1.5)
    
    plt.show()
    time.sleep(0.5)

def generate_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G

G = generate_graph(20, 30)
pos = nx.spring_layout(G)

bfs_order = bfs(G, start_node=0)
print("BFS Order:", bfs_order)
visualize_search(bfs_order, 'BFS Visualization', G, pos)

dfs_order = dfs(G, start_node=0)
print("DFS Order:", dfs_order)
visualize_search(dfs_order, 'DFS Visualization', G, pos)
