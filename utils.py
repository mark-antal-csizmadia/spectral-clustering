import numpy as np
import networkx as nx
import pandas as pd


def read_data(from_file_name, dataset_name):
    """ Reads data. """
    if dataset_name == "example1":
        df_edges = pd.read_csv(from_file_name, sep=",", header=None, skiprows=0, names=["src", "dst"])
        vertices_np = \
            np.unique(np.hstack([df_edges["src"].unique(), df_edges["dst"].unique()]))
        df_vertices = pd.DataFrame(data={"id": vertices_np})
    elif dataset_name == "example2":
        df_edges = pd.read_csv(from_file_name, sep=",", header=None, skiprows=0, names=["src", "dst", "w"])
        vertices_np = \
            np.unique(np.hstack([df_edges["src"].unique(), df_edges["dst"].unique()]))
        df_vertices = pd.DataFrame(data={"id": vertices_np})
    else:
        raise FileNotFoundError(f"no such dataset: {dataset_name}")

    return df_edges, df_vertices


def make_graph(df_edges, if_weighted):
    """Makes graph from pd edge list."""
    # create graph
    g = nx.from_pandas_edgelist(
        df=df_edges,
        source="src",
        target="dst",
        edge_attr="w" if if_weighted else None,
        create_using=nx.Graph,
        edge_key=None
    )

    return g
