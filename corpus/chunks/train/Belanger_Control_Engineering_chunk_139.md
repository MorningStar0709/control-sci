# General Case $^{1}$

General Case

The eigenstructure can be more complex if A has repeated eigenvalues. Corresponding to a repeated root of multiplicity k, there will be at least one eigenvector and, at most k independent eigenvectors; a symmetric matrix, for example, always has k independent eigenvectors for such a root. If there are fewer than k eigenvectors, some (or all) of the eigenvectors will serve as starting points for chains of generalized eigenvectors. Let $v_{i}^{0}$ be an eigenvector of A, corresponding to the eigenvalue $s_{i}$ , and let $v_{i}^{1}, v_{i}^{2}, \ldots$ be the chain of generalized eigenvectors engendered by $v_{i}^{0}$ . The vectors satisfy

$$(A - s _ {i} I) \mathbf {v} _ {i} ^ {1} = \mathbf {v} _ {i} ^ {0}(A - s _ {i} I) \mathbf {v} _ {i} ^ {2} = \mathbf {v} _ {i} ^ {1}$$

•
•
•

$$(A - s _ {i} I) \mathbf {v} _ {i} ^ {j + 1} = \mathbf {v} _ {i} ^ {j}. \tag {3.71}$$

The chain continues as long as a nontrivial solution can be found for the next generalized eigenvector.

If several independent eigenvectors correspond to $s_i$ , each of those eigenvectors generates a chain of generalized eigenvectors. It can be shown that the eigenvectors and generalized eigenvectors corresponding to the eigenvalue $s_i$ are independent of each other and of the eigenvectors and generalized eigenvectors corresponding to other eigenvalues.

To generate the Jordan form of a matrix with repeated eigenvalues, we define the transformation matrix $T$ whose columns are the eigenvectors and generalized eigenvectors of the matrix $A$ . The general development requires unwieldy notation, so we present it with the special case

$$T = \left[ \mathbf {v} _ {1 1} ^ {0} \mathbf {v} _ {1 1} ^ {1} \mathbf {v} _ {1 1} ^ {2} \mathbf {v} _ {1 2} ^ {0} \mathbf {v} _ {1 2} ^ {1} \mathbf {v} _ {2 1} ^ {0} \mathbf {v} _ {2 1} ^ {1} \right]. \tag {3.72}$$

Here, $\mathbf{v}_{11}^{0}$ and $\mathbf{v}_{12}^{0}$ are eigenvectors corresponding to the eigenvalue $s_1$ ; $\mathbf{v}_{21}^{0}$ corresponds to $s_2$ . The other columns of $T$ are generalized eigenvectors.

The matrix $T^{-1}$ is defined by its rows, i.e.,

$$
T ^ {- 1} = \left[ \begin{array}{l} \mathbf {w} _ {1 1} ^ {0 ^ {T}} \\ \mathbf {w} _ {1 1} ^ {1 ^ {T}} \\ \mathbf {w} _ {1 1} ^ {2 ^ {T}} \\ \mathbf {w} _ {1 2} ^ {0 ^ {T}} \\ \mathbf {w} _ {1 2} ^ {1 ^ {T}} \\ \mathbf {w} _ {2 1} ^ {0 ^ {T}} \\ \mathbf {w} _ {2 1} ^ {1 ^ {T}} \end{array} \right] \tag {3.73}
$$
