# Multi-Omics Network Integrator

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Language](https://img.shields.io/badge/language-Python-blue.svg)
[![Python Version](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/downloads/)

A Python toolkit to integrate transcriptomic (RNA-Seq) and proteomic (Mass Spectrometry) data to construct and analyze dysregulated signaling networks in disease. This project is based on methods developed during my PhD research on neurodegeneration at the University of Luxembourg.

### Workflow Overview

The core idea is to identify differentially expressed genes and proteins, map them onto a known protein-protein interaction (PPI) network, and then analyze the resulting subnetwork to find key drivers of dysregulation.

```
+--------------------------+      +--------------------------+
|   RNA-Seq Count Data     |      | Proteomics Intensity Data|
+--------------------------+      +--------------------------+
             |                                 |
             ▼                                 ▼
+--------------------------+      +--------------------------+
|  Differential Expression |      |  Differential Abundance  |
|      (e.g., DESeq2)      |      |      (e.g., t-test)      |
+--------------------------+      +--------------------------+
             |                                 |
             └─────────────┐   ┌─────────────┘
                           ▼   ▼
            +-----------------------------------+
            |  Combined List of Dysregulated    |
            |        Genes and Proteins         |
            +-----------------------------------+
                           |
                           ▼
            +-----------------------------------+
            |   Fetch Interactions from a PPI   |
            |   Database (e.g., STRING-DB)      |
            +-----------------------------------+
                           |
                           ▼
            +-----------------------------------+
            | Construct & Visualize Integrated  |
            |         Signaling Network         |
            |   (Nodes colored by omics data)   |
            +-----------------------------------+
                           |
                           ▼
            +-----------------------------------+
            |  Analyze Network for Hubs, Hubs,   |
            |    and Dysregulated Pathways      |
            +-----------------------------------+
```

### Features

-   **Data Loading & Validation**: Handles RNA-Seq counts, proteomics intensities, and metadata.
-   **Differential Analysis**: Wrapper for `pydeseq2` for RNA-Seq and `scipy` t-tests for proteomics.
-   **Network Construction**: Fetches high-confidence interactions from STRING-DB for a given list of proteins.
-   **Data Integration**: Overlays transcriptomic and proteomic log2-fold-changes and p-values as attributes onto network nodes.
-   **Network Analysis**: Identifies key hub proteins based on network centrality.
-   **Interactive Visualization**: Generates a dynamic, explorable HTML network graph using `pyvis`.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/olaflaitinen/Multi-Omics-Network-Integrator.git
    cd Multi-Omics-Network-Integrator
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Quick Start

The best way to get started is to run the example walkthrough in the Jupyter Notebook. This will guide you through every step of the analysis using the provided sample data.

```bash
cd notebooks
jupyter-lab walkthrough.ipynb
```

### Configuration

Analysis parameters (e.g., p-value cutoffs, species for STRING-DB) can be easily modified in the `config/analysis_config.yaml` file without changing the source code.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
