import time
from pathlib import Path
import argparse
from utils import read_data, make_graph
from spectral_clustering import SpectralClusterer
from plot import plot_a, plot_f, plot_v, plot_graph


# arg parse
parser = argparse.ArgumentParser(description='spectral clustering')
parser.add_argument('--dataset_name', type=str, choices=["example1", "example2"], help='name of the dataset',
                    required=True)
parser.add_argument('--seed', type=int, default=0, help='random seed (default: 0, experiments done with 123)',
                    required=True)

if __name__ == "__main__":
    # tic tac
    start_time = time.time()
    print("script starts")

    # args parse
    args = parser.parse_args()
    from_file_name = Path("data") / Path(args.dataset_name + ".dat")

    # read edges of graph
    df_edges, df_vertices = read_data(from_file_name=from_file_name, dataset_name=args.dataset_name)
    print(f"read graph with {df_edges.shape[0]} edges and {df_vertices.shape[0]} nodes")

    # make graph from edge list
    g = make_graph(df_edges=df_edges, if_weighted=True if args.dataset_name == "example2" else False)

    # fit spectral clustering algorithm
    sc = SpectralClusterer(seed=args.seed)
    sc(g)

    # get results and variables
    # a is the affinity (here adjacency) matrix of graph g
    a = sc.get_a()
    # v si the list of eigenvalues (in ascending order) and x is the matrix of eigenvectors (columns) ordered by
    # the eigenvalues
    v, x = sc.get_v(), sc.get_x()
    # f is the fiedler vector (2nd eigenvector)
    f = sc.get_fiedler()
    # k is the optimal number of clusters (the largest change in the sequence of eigenvalues)
    k = sc.get_k()
    # labels are k cluster ids found via k-means
    labels = sc.get_labels()
    print(f"finished spectral clustering for {args.dataset_name}, found {k} clusters")

    # plot the labeled graph
    plot_graph(g=g, labels=labels, path_save=Path("assets") / Path(args.dataset_name + "_labels.png"))
    # plot the adjacency matrix
    plot_a(a=a, path_save=Path("assets") / Path(args.dataset_name + "_a.png"))
    # plot the fiedler vector
    plot_f(f=f, dataset_name=args.dataset_name, path_save=Path("assets") / Path(args.dataset_name + "_f.png"))
    # plot the eigenvalues
    plot_v(v=v, dataset_name=args.dataset_name, path_save=Path("assets") / Path(args.dataset_name + "_v.png"))

    # done
    print(f"script finished execution in {time.time() - start_time:.4f} seconds")
