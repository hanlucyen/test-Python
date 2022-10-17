import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 2),(4,5),(3,6),(0,7),(0,8)])

#nhóm nút theo cột
left_nodes = [1, 2,3]
middle_nodes = [7,0,8]
right_nodes = [4,5, 6]

# đặt vị trí theo cột (toạ độ x)
pos = {n: (0, i) for i, n in enumerate(right_nodes)}
pos.update({n: (1, i + 0.5) for i, n in enumerate(middle_nodes)})
pos.update({n: (2, i + 0.5) for i, n in enumerate(left_nodes)})

options={
    "font_size": 30,
    "node_size": 1000,
    "node_color": "blue",
    "edgecolors": "green",
    "linewidths": 5,
    "width": 4,
}


nx.draw_networkx(G, pos, **options)

# Đặt lề cho các trục để các nút không bị cắt
#gca là  đặt các trục ở hiện tại
ax = plt.gca()
ax.margins(0.3)
plt.axis("on")
plt.show()
