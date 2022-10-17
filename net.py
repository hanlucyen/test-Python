
from grandiso import find_motifs
import networkx as nx

host = nx.fast_gnp_random_graph(10, 0.5)

motif = nx.Graph()
motif.add_edge("A", "B")
motif.add_edge("B", "C")
motif.add_edge("C", "D")
motif.add_edge("D", "A")

len(find_motifs(motif, host))
