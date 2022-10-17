import matplotlib as mpl
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_nodes_from["A","B","C","D","E"]
G.add_edges_from[("A","B")("A","C"), ("B","D"), ("B","E"), ("C", "E")]
pos={A:(0,0),B:(-1,0.3),C:(2,0.17),D:(4,0.255),E:(5,0.03)}
options={
    "font_size":36,
    "node_size":300,
    "node_color":"green",
    "edgecolors":"blue",
    "linewdths":5,
    "width":5
}
print(G.nodes()) # returns a list
print(G.edges()) # returns a list
nx.draw_networkx(G,pos,**options)

ax=plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
