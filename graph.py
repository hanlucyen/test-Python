#%%
import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()
G.add_edge(1,2)
G.add_edge(1.3)
G.add_edge(1,5)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)

#explicitly set positions
pos={1: (0,0), 2:  (-1,0.3), 3: (2,0.17), 4: (4,0.255), 5: (5,0.03)}

options={
    "font_size":36,
    "node_size":3000,
    "node_color":"green",
    "edgecolors":"blue",
    "linewdths":5,
    "width":5
}
nx.draw_networkx(G,pos,**options)

#set margins for the axes so that nodes aren't clipped
ax=plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()

