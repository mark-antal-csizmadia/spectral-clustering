import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns


def plot_graph(g, labels=None, path_save=None):
    """Plots graph."""
    plt.figure(figsize=(12, 12))
    nx.draw(g, node_size=64, node_color=labels, cmap='viridis')

    if path_save is not None:
        plt.savefig(path_save)


def plot_a(a, path_save=None):
    """ Plots adjacency matrix of graph g."""
    plt.figure(figsize=(6, 4))
    sns.heatmap(a, vmin=0, vmax=1)
    plt.tight_layout()

    if path_save is not None:
        plt.savefig(path_save)


def plot_f(f, dataset_name, path_save=None):
    """ Plots Fiedler vector, that is, the 2nd eigenvector. Entry values are sorted by magnitude
    in ascending order."""
    plt.figure(figsize=(6, 4))
    plt.scatter(np.arange(f.size) + 1, np.sort(f))
    plt.grid("on")
    plt.xlabel("Fiedler vector entries by index (sorted by magnitude in ascending order)")
    plt.ylabel("Fiedler vector entry magnitudes")
    plt.title(f"Fiedler vector of {dataset_name}")
    plt.tight_layout()

    if path_save is not None:
        plt.savefig(path_save)


def plot_v(v, dataset_name, path_save=None):
    """ Plots the eigenvalues sorted by magnitude in ascending order."""
    plt.figure(figsize=(6, 4))
    plt.scatter(np.arange(v.size) + 1, v)
    plt.grid("on")
    plt.xlabel("Eigenvalues by index (in ascending order)")
    plt.ylabel("Eigenvalue magnitudes")
    plt.title(f"Eigenvalues of {dataset_name}")
    plt.tight_layout()

    if path_save is not None:
        plt.savefig(path_save)


def plot_v_zoom(v, k, dataset_name, path_save=None):
    """ Plots the eigenvalues sorted by magnitude in ascending order (zoomed in)"""
    plt.figure(figsize=(6, 4))
    extend_by = 5
    plt.plot(np.arange(v[:k+extend_by].size) + 1, v[:k+extend_by], '-o')
    plt.grid("on")
    plt.xlabel("Eigenvalues by index (in ascending order, zoomed in)")
    plt.ylabel("Eigenvalue magnitudes, zoomed in")
    plt.title(f"Eigenvalues of {dataset_name}, zoomed in")
    plt.tight_layout()

    if path_save is not None:
        plt.savefig(path_save)
