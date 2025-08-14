import networkx as nx

def build_graph(ppi_df, node_scores):
    """Builds a networkx graph from PPI data and node scores."""
    G = nx.Graph()
    for node, score in node_scores.items():
        G.add_node(node, score=score)
        
    for _, row in ppi_df.iterrows():
        G.add_edge(
            row['protein1'],
            row['protein2'],
            weight=row['combined_score'] / 1000.0  # Normalize weight
        )
    return G
