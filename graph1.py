import networkx 
G=nx.Graph()
G.add_node("A")
G.add_nodes_from(["B","C","D","E"])
G.add_edge(*("A","B"))
G.add_adges_from([("A","C"),("B","D"),("B","E"),("C","E")])
pos={A:(0,0),B:(-1,0.3),C:(2,0.17),D:(4,0.255),E:(5,0.03)}
options={
    "font_size":36,
    "node_size":300,
    "node_color":"green",
    "edgecolors":"blue",
    "linewdths":5,
    "width":5
}
print(G.nodes())
print(G.edges())
nx.draw_networkx(G,pos,**options)

ax=plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
