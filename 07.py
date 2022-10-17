>>> g = nx.Graph()
>>> g.add_node('TP.HCM')
>>> g.add_node('Dong Nai')
>>> g.add_node('Ba Ria Vung Tau')
>>> g.add_node('Lam Dong')
>>> g.add_node('Can Tho')
>>> g.add_node('Long An')
>>> g.add_edge('TP.HCM', 'Dong Nai')
>>> g.add_edge('TP.HCM', 'Ba Ria Vung Tau')
>>> g.add_edge('TP.HCM', 'Long An')
>>> g.add_edge('Dong Nai', 'Lam Dong')
>>> g.add_edge('Dong Nai', 'Ba Ria Vung Tau')
>>> print (g.number_of_nodes())
6
>>> print (g.number_of_edges())
5
>>> print (g.nodes())
['TP.HCM', 'Dong Nai', 'Ba Ria Vung Tau', 'Lam Dong', 'Can Tho', 'Long An']
>>> print (g.edges())
[('TP.HCM', 'Dong Nai'), ('TP.HCM', 'Ba Ria Vung Tau'), ('TP.HCM', 'Long An'), ('Dong Nai', 'Lam Dong'), ('Dong Nai', 'Ba Ria Vung Tau')]
>>> print (g.degree('TP.HCM'))
[('TP.HCM', 3), ('Dong Nai', 3), ('Ba Ria Vung Tau', 2), ('Lam Dong', 1), ('Can Tho', 0), ('Long An', 1)]
>>> print (g.degree())

.............................................................................. ? sinh viên ?i?n vào
>>> print (list(g.neighbors('TP.HCM')))
.............................................................................. ? sinh viên ?i?n vào
>>> g.has_edge('Lam Dong', 'Long An')
............................................................ ? sinh viên ?i?n vào
>>> nx.shortest_path(g, 'Lam Dong', 'Long An') # ?ã có m?ng l??i ???ng ?i
........................................................................... ? sinh viên ?i?n vào
>>> nx.shortest_path(g, 'Lam Dong', 'Can Tho') # hi?n t?i ch?a xây d?ng m?ng ???ng ?i
........................................................................... ? sinh viên ?i?n tên Exception
>>> g.add_node('Tien Giang')
>>> g.add_edge('Tien Giang', 'Long An')
>>> g.add_edge('Tien Giang', 'Can Tho')
>>> nx.shortest_path(g, 'Lam Dong', 'Can Tho') # hi?n t?i ?ã b? sung thêm ???ng ?i
........................................................................... ? sinh viên ?i?n vào
>>> nx.shortest_path_length(g, 'Lam Dong', 'Ba Ria Vung Tau')
............................................................ ? sinh viên ?i?n vào
>>> nx.shortest_path_length(g, 'Dong Nai', 'Ba Ria Vung Tau')
............................................................ ? sinh viên ?i?n vào
>>> nx.shortest_path_length(g, 'Lam Dong', 'Long An')
