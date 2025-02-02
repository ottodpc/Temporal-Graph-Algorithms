import networkx as nx
import matplotlib.pyplot as plt
 
G_dense = nx.gnm_random_graph(n=50, m=500, seed=42) 
 
G_geometric = nx.random_geometric_graph(50, radius=0.2, seed=42)
 
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
nx.draw(G_dense, with_labels=True, node_color="lightblue", edge_color="gray")
plt.title("Graphe dense (m élevé)")
 
plt.subplot(1, 2, 2)
pos = nx.spring_layout(G_geometric)
nx.draw(G_geometric, pos, with_labels=True, node_color="orange", edge_color="gray")
plt.title("Graphe géométrique aléatoire (données désordonnées)")
 
plt.tight_layout()
plt.savefig("exemples_concrets.png")
plt.show()