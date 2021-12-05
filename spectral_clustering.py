import numpy as np
import networkx as nx
from scipy.linalg import eigh
from sklearn.cluster import KMeans


class SpectralClusterer:
    """ Spectral clustering algorithm as described in the paper."""
    def __init__(self, seed):
        self._seed = seed
        self._k = None
        self.if_fit = False
        self._a = None
        self._d = None
        self._l = None
        self._v = None
        self._x = None
        self._f = None
        self._k = None
        self._v_k = None
        self._x_k = None
        self._y_k = None
        self._clf = None
        self._labels = None

    def fit(self, g):
        """ Fits the spectral clustering algorithm from the paper."""
        # get the affinity matrix, that is, in this case, the adjacency matrix of the graph g.
        a = np.array(nx.adjacency_matrix(g).todense())
        # get the diagonal matrix where the diagonal entry in row i
        # is the sum of the entries in a in row i
        d = np.diag(a.sum(axis=1))
        # d**(-1/2), invert and sqrt matrix d
        d_inv = np.linalg.inv(np.sqrt(d))
        # get the normalized laplacian of the adj. matrix a
        l = d_inv.dot(d - a).dot(d_inv)
        # eigen-decomposition of the laplacian matrix, get all of the eigenvalues and eigenvectors
        # eigenvectors are the columns of x, ordered in ascending order by their corresponding eigenvalues
        v, x = eigh(l)
        # get the second eigenvector = Fiedler vector for cluster viz
        f = x[:, 1]
        # get k, the optimal number of clusters for k-means
        # k is the index at which there is the maximum rate of change in the sequence of the
        # eigenvalue magnitudes
        k = np.diff(v).argmax() + 1
        # select k eigenvectors by the k largest eigenvalues
        v_k, x_k = v[:k], x[:, :k]
        # normalize the eigenvector matrix so that each row has unit lenght
        y_k = x_k / np.sqrt(np.power(x_k, 2).sum(axis=1)).reshape(-1, 1)
        # fit k-means to get the k clusters
        clf = KMeans(n_clusters=k, random_state=self._seed).fit(y_k)
        # extract the labels for plotting
        labels = clf.labels_

        self._a = a
        self._d = d
        self._l = l
        self._v, self._x = v, x
        self._f = f
        self._k = k
        self._v_k, self._x_k = v_k, x_k
        self._y_k = y_k
        self._clf = clf
        self._labels = labels
        self.if_fit = True

    def __call__(self, g):
        if not self.if_fit:
            self.fit(g)
        else:
            raise Exception("spectral clusterer has already been fit")

        return

    def get_labels(self, ):
        return self._labels

    def get_k(self, ):
        return self._k

    def get_v(self, ):
        return self._v

    def get_x(self, ):
        return self._x

    def get_v_k(self, ):
        return self._v_k

    def get_x_k(self, ):
        return self._x_k

    def get_a(self, ):
        return self._a

    def get_fiedler(self, ):
        return self._f

    def __repr__(self, ):
        return f"spectral clustering"
