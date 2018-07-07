
# coding: utf-8

# In[ ]:


import itertools
import random
import math
import networkx as nx
from networkx.generators.classic import empty_graph, path_graph, complete_graph
from collections import defaultdict
import itertools
import random
import math
import networkx as nx
from networkx.generators.classic import empty_graph, path_graph, complete_graph
import matplotlib.pyplot as plt


from collections import defaultdict
def fast_gnp_random_graph(n, p, seed=None, directed=False):
    """Returns a `G_{n,p}` random graph, also known as an Erdős-Rényi graph or
    a binomial graph.

    Parameters
    ----------
    n : int
        The number of nodes.
    p : float
        Probability for edge creation.
    seed : int, optional
        Seed for random number generator (default=None).
    directed : bool, optional (default=False)
        If ``True``, this function returns a directed graph.

    Notes
    -----
    The `G_{n,p}` graph algorithm chooses each of the `[n (n - 1)] / 2`
    (undirected) or `n (n - 1)` (directed) possible edges with probability `p`.

    This algorithm runs in `O(n + m)` time, where `m` is the expected number of
    edges, which equals `p n (n - 1) / 2`. This should be faster than
    :func:`gnp_random_graph` when `p` is small and the expected number of edges
    is small (that is, the graph is sparse).
  
    """
    G = empty_graph(n)
    print(G)
    print("check1")
    G.name="fast_gnp_random_graph(%s,%s)"%(n,p)

    if not seed is None:
        random.seed(seed)

    if p <= 0 or p >= 1:
        return nx.gnp_random_graph(n,p,directed=directed)

    w = -1
    lp = math.log(1.0 - p)

    if directed:
        G = nx.DiGraph(G)
        # Nodes in graph are from 0,n-1 (start with v as the first node index).
    v = 0
    while v < n:
        lr = math.log(1.0 - random.random())
        w = w + 1 + int(lr/lp)
        if v == w: # avoid self loops
                w = w + 1
        while  w >= n and v < n:
                w = w - n
                v = v + 1
                if v == w: # avoid self loops
                    w = w + 1
        if v < n:
                G.add_edge(v, w)
    else:
        # Nodes in graph are from 0,n-1 (start with v as the second node index).
        v = 1
        while v < n:
            lr = math.log(1.0 - random.random())
            w = w + 1 + int(lr/lp)
            while w >= v and v < n:
                w = w - v
                v = v + 1
            if v < n:
                G.add_edge(v, w)
    print(G)
    #nx.draw(G)
    print("check2")
    #nx.draw_random(G)
    print("check3")
    #nx.draw_circular(G)
    print("check4")
    #nx.draw_spectral(G)
    print("check5")
    #plt.show()
    print("check6")
    nx.draw(G)
   # nx.write_dot(G,'file.dot')
    #plt.savefig("fig.png")
    D=to_numpy_matrix(G)
    print(D)
    return G

