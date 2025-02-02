import matplotlib.pyplot as plt
import networkx as nx
 
G = nx.Graph()
 
G.add_nodes_from(["u", "v", "w1", "w2"])
edges = [
    ("u", "w1", {"time": 1}),
    ("u", "w2", {"time": 2}),
    ("v", "w1", {"time": 1}),
    ("v", "w2", {"time": 2}),
    ("u", "w1", {"time": 3}),
    ("v", "w1", {"time": 3}),
]
 
pos = {"u": (0, 1), "v": (0, -1), "w1": (1, 0), "w2": (2, 0)}
edge_labels = {(u, v): f"t={d['time']}" for u, v, d in G.edges(data=True)}

plt.figure(figsize=(8, 4))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
 
plt.axhspan(-0.5, 1.5, xmin=0.25, xmax=0.75, color="yellow", alpha=0.3, label="Fenêtre Δ-twins")
plt.legend(loc="upper right")
plt.title("Exemple de Δ-twins entre u et v")
plt.show()