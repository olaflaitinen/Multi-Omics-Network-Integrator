import networkx as nx
import pandas as pd

def find_hotspot_subnetworks(graph, min_size=5):
    """Finds connected components and ranks them by total score."""
    # Find all connected components (subgraphs)
    components = [
        graph.subgraph(c).copy() for c in nx.connected_components(graph)
    ]
    
    hotspots = []
    for i, comp in enumerate(components):
        if len(comp.nodes) >= min_size:
            total_score = sum(nx.get_node_attributes(comp, 'score').values())
            avg_score = total_score / len(comp.nodes)
            hotspots.append({
                'subnetwork_id': i,
                'num_nodes': len(comp.nodes),
                'total_score': total_score,
                'avg_score': avg_score,
                'nodes': ', '.join(comp.nodes)
            })
    
    # Return as a sorted DataFrame
    if not hotspots:
        return pd.DataFrame()
    return pd.DataFrame(hotspots).sort_values('total_score', ascending=False)
