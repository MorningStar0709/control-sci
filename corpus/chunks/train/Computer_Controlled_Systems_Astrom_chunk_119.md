# Jordan Form

If $\Phi$ has multiple eigenvalues, then it is generally not possible to diagonalize $\Phi$ . Let $\Phi$ be a $n \times n$ matrix and introduce the notation

$$
L _ {k} (\lambda) = \left( \begin{array}{c c c c c} \lambda & 1 & 0 & \dots & 0 \\ 0 & \lambda & 1 & & 0 \\ \vdots & \ddots & \ddots & \ddots & \\ 0 & \dots & 0 & \lambda & 1 \\ 0 & \dots & 0 & 0 & \lambda \end{array} \right)
$$

where $L_{k}$ is a $k \times k$ matrix. Then there exists a matrix $T$ such that

$$
T \Phi T ^ {- 1} = \left( \begin{array}{c c c c} L _ {k _ {1}} (\lambda_ {1}) & & & 0 \\ & L _ {k _ {2}} (\lambda_ {2}) & & \\ & & \ddots & \\ 0 & & & L _ {k _ {r}} (\lambda_ {r}) \end{array} \right) \tag {2.19}
$$

with $k_{1} + k_{2} + \cdots + k_{r} = n$ . The $\lambda_{i}$ are the eigenvalues of $\Phi$ , not necessarily distinct. Equation (2.19) is called the Jordan form. See Appendix B. In this form the transformed matrix, $\bar{\Phi}$ , has the eigenvalues in the diagonal and some 1's in the superdiagonal.
