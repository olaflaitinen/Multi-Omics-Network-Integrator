import pandas as pd
import numpy as np

def score_nodes(rna_df, prot_df, ppi_df, config):
    """Calculates a score for each gene based on omics data."""
    p_thresh = config.get('p_value_threshold', 0.05)
    rna_w = config.get('rna_weight', 0.5)
    prot_w = config.get('protein_weight', 0.5)
    
    # Get all unique nodes from the PPI network
    all_nodes = pd.unique(ppi_df[['protein1', 'protein2']].values.ravel('K'))
    
    scores = {}
    for node in all_nodes:
        rna_score = 0
        prot_score = 0
        
        # Score from RNA-Seq
        if node in rna_df.index and rna_df.loc[node, 'padj'] < p_thresh:
            rna_score = -np.log10(rna_df.loc[node, 'padj'])

        # Score from Proteomics
        if node in prot_df.index and prot_df.loc[node, 'padj'] < p_thresh:
            prot_score = -np.log10(prot_df.loc[node, 'padj'])
            
        scores[node] = (rna_w * rna_score) + (prot_w * prot_score)
        
    return scores
