import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
 
fig, ax = plt.subplots(figsize=(8, 4))
 
def draw_tree(ax, x, y, width, height, label):
    rect = Rectangle((x, y), width, height, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, label, ha='center', va='center', fontsize=10)
 
draw_tree(ax, 0.2, 0.6, 0.2, 0.1, "[0, 10]")
draw_tree(ax, 0.1, 0.4, 0.2, 0.1, "[0, 4]")
draw_tree(ax, 0.3, 0.4, 0.2, 0.1, "[6, 10]")
 
ax.annotate("", xy=(0.2, 0.5), xytext=(0.15, 0.6),
            arrowprops=dict(arrowstyle="->", color="black"))
ax.annotate("", xy=(0.4, 0.5), xytext=(0.35, 0.6),
            arrowprops=dict(arrowstyle="->", color="black"))
 
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.title("Arbre rouge-noir : Division d'une plage de temps")
plt.savefig("schema_arbre_rouge_noir.png")
plt.show()