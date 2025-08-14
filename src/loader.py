import pandas as pd

def load_omics_data(file_path):
    """Loads differential expression/abundance data."""
    return pd.read_csv(file_path).set_index('gene')

def load_interaction_network(file_path):
    """Loads a PPI network from a TSV file."""
    return pd.read_csv(file_path, sep='\t')
