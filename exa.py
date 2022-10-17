import matplotlib as mpl
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

pos=("a"(0,0),"b"(-1,0.3),"c"(2,0.17),"d"(4,0.255),"e"(5,0.03))
options={
    "font_size":36,
    "node_size":300,
    "node_color":"green",
    "edgecolors":"blue",
    "linewdths":5,
    "width":5,
}    
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())
nx.draw_networkx(G,pos,**options)
ax=plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
