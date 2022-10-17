import networkx as nx
G=nx.path_graph(4)
thanhpho={0:"tokyo",1:"berlin",2:"rome",3:"luan don"}
H=nx.relabel_nodes(G,thanhpho)
print("cac nut cua bieu do: ")
print(H.nodes())
print("cac canh cua bieu do: ")
print(H.edges())
nx.draw(H)
plt.savefig("path_graph_cities.png")
plt.show()
G = nx.path_graph (10)


