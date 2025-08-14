import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

def plot_network(graph, output_path, title="Network"):
    """Generates and saves a static network plot."""
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(graph, k=0.5, iterations=50)
    
    node_scores = list(nx.get_node_attributes(graph, 'score').values())
    
    nx.draw(
        graph, pos, with_labels=True,
        node_size=[s * 100 + 50 for s in node_scores],
        node_color=node_scores,
        cmap=plt.cm.viridis,
        font_size=8,
        width=0.5
    )
    plt.title(title, fontsize=16)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_interactive_network(graph, output_path, title="Interactive Network"):
    """Generates and saves an interactive pyvis network plot."""
    net = Network(height="750px", width="100%", notebook=True, heading=title)
    net.from_nx(graph)
    
    # Adjust node properties for better visualization
    for node in net.nodes:
        node['size'] = node['score'] * 5 + 10 # Scale size by score
        node['title'] = f"Gene: {node['id']}\nScore: {node['score']:.2f}"

    net.show_buttons(filter_=['physics'])
    net.save_graph(output_path)
