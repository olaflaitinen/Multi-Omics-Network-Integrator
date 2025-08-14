import argparse
import os
import yaml
from src.loader import load_omics_data, load_interaction_network
from src.integrator import score_nodes
from src.network_builder import build_graph
from src.analysis import find_hotspot_subnetworks
from src.visualize import plot_network, plot_interactive_network

def main():
    parser = argparse.ArgumentParser(description="Multi-Omics Network Integration Pipeline")
    parser.add_argument('--config', required=True, help='Path to the config YAML file.')
    parser.add_argument('--rnaseq', required=True, help='Path to RNA-Seq results CSV.')
    parser.add_argument('--proteomics', required=True, help='Path to Proteomics results CSV.')
    parser.add_argument('--ppi', required=True, help='Path to the PPI network TSV file.')
    parser.add_argument('--output_dir', required=True, help='Directory to save results.')
    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # 1. Load config
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    # 2. Load data
    print("Loading data...")
    rna_df = load_omics_data(args.rnaseq)
    prot_df = load_omics_data(args.proteomics)
    ppi_df = load_interaction_network(args.ppi)

    # 3. Integrate omics and score nodes
    print("Scoring nodes...")
    node_scores = score_nodes(rna_df, prot_df, ppi_df, config['scoring'])

    # 4. Build network
    print("Building network...")
    graph = build_graph(ppi_df, node_scores)

    # 5. Analyze network
    print("Finding hotspot subnetworks...")
    hotspots = find_hotspot_subnetworks(graph)
    hotspots.to_csv(os.path.join(args.output_dir, 'hotspot_subnetworks.csv'), index=False)
    print(f"Found {len(hotspots)} subnetworks. Results saved.")

    # 6. Visualize the largest hotspot
    print("Generating visualizations...")
    largest_hotspot_nodes = hotspots.iloc[0]['nodes'].split(', ')
    subgraph = graph.subgraph(largest_hotspot_nodes)
    
    plot_network(
        subgraph,
        os.path.join(args.output_dir, 'largest_hotspot_static.png'),
        "Largest Dysregulated Subnetwork"
    )
    
    plot_interactive_network(
        subgraph,
        os.path.join(args.output_dir, 'largest_hotspot_interactive.html'),
        "Largest Dysregulated Subnetwork"
    )
    print("Visualizations saved.")

if __name__ == "__main__":
    main()
