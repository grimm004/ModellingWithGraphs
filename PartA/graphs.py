import networkx as nx
import matplotlib.pyplot as plt
import graph1
import graph2
import graph3
import graph4
import graph5

plt.subplot(111)
nx.draw(graph1.Graph(), with_labels=True, font_weight='bold')
plt.subplot(112)
nx.draw(graph2.Graph(), with_labels=True, font_weight='bold')
plt.subplot(113)
nx.draw(graph3.Graph(), with_labels=True, font_weight='bold')
plt.subplot(114)
nx.draw(graph4.Graph(), with_labels=True, font_weight='bold')
plt.subplot(115)
nx.draw(graph5.Graph(), with_labels=True, font_weight='bold')

plt.show()
