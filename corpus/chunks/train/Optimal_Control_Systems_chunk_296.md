Next, at the final time $k_{f}$ , using (5.4.16) and (5.4.26) we have

$$
\begin{array}{l} \boldsymbol {\lambda} \left(k _ {f}\right) = \mathbf {W} _ {2 1} \mathbf {v} \left(k _ {f}\right) + \mathbf {W} _ {2 2} \mathbf {z} \left(k _ {f}\right) = \mathbf {P} \left(k _ {f}\right) \mathbf {x} \left(k _ {f}\right) = \mathbf {F} \left(k _ {f}\right) \mathbf {x} \left(k _ {f}\right), \\ = \mathbf {F} (k _ {f}) \left[ \mathbf {W} _ {1 1} \mathbf {v} (k _ {f}) + \mathbf {W} _ {1 2} \mathbf {z} (k _ {f}) \right] \tag {5.4.30} \\ \end{array}
$$

the solution of which becomes

$$\mathbf {z} (k _ {f}) = \mathbf {T} (k _ {f}) \mathbf {v} (k _ {f}) \tag {5.4.31}$$

where,

$$\mathbf {T} (k _ {f}) = - \left[ \mathbf {W} _ {2 2} - \mathbf {F} (k _ {f}) \mathbf {W} _ {1 2} \right] ^ {- 1} \left[ \mathbf {W} _ {2 1} - \mathbf {F} (k _ {f}) \mathbf {W} _ {1 1} \right]. \tag {5.4.32}$$

Now, using (5.4.29) and (5.4.31)

$$
\begin{array}{l} \mathbf {z} (k) = \mathbf {M} ^ {- (k _ {f} - k)} \mathbf {z} (k _ {f}) \\ = \mathbf {M} ^ {- (k _ {f} - k)} \mathbf {T} (k _ {f}) \mathbf {v} (k _ {f}) \\ = \mathbf {M} ^ {- (k _ {f} - k)} \mathbf {T} (k _ {f}) \mathbf {M} ^ {- (k _ {f} - k)} \mathbf {v} (k). \tag {5.4.33} \\ \end{array}
$$

This means that at each value of $k$ ,

$$\mathbf {z} (k) = \mathbf {T} (k) \mathbf {v} (k) \tag {5.4.34}$$

where,

$$\mathbf {T} (k) = \mathbf {M} ^ {- (k _ {f} - k)} \mathbf {T} (k _ {f}) \mathbf {M} ^ {- (k _ {f} - k)}. \tag {5.4.35}$$

Now we relate $\mathbf{P}(k)$ in (5.4.16) with $\mathbf{T}(k)$ in (5.4.34) by first using (5.4.26) and (5.4.16) to get

$$
\begin{array}{l} \boldsymbol {\lambda} ^ {*} (k) = \mathbf {W} _ {2 1} \mathbf {v} (k) + \mathbf {W} _ {2 2} \mathbf {z} (k) \\ = \mathbf {P} (k) \mathbf {x} ^ {*} (k) = \mathbf {P} (k) \left[ \mathbf {W} _ {1 1} \mathbf {v} (k) + \mathbf {W} _ {1 2} \mathbf {z} (k) \right] \tag {5.4.36} \\ \end{array}
$$

and then using (5.4.34)

$$\left[ \mathbf {W} _ {2 1} + \mathbf {W} _ {2 2} \mathbf {T} (k) \right] \mathbf {v} (k) = \mathbf {P} (k) \left[ \mathbf {W} _ {1 1} + \mathbf {W} _ {1 2} \mathbf {T} (k) \right] \mathbf {v} (k). \tag {5.4.37}$$

Since this must hold good for all $\mathbf{x}(0)$ and hence for all $\mathbf{v}(k)$ , leading to

$$\boxed {\mathbf {P} (k) = \left[ \mathbf {W} _ {2 1} + \mathbf {W} _ {2 2} \mathbf {T} (k) \right] \left[ \mathbf {W} _ {1 1} + \mathbf {W} _ {1 2} \mathbf {T} (k) \right] ^ {- 1}.} \tag {5.4.38}$$

Finally, we have the nonrecursive analytical solution (5.4.38) to the matrix difference Riccati equation (5.3.20). Let us note that the solution (5.4.38) requires the relations (5.4.35) and (5.4.32) and the eigenvalues (5.4.24), eigenvectors (5.4.25), and the given terminal cost matrix $\mathbf{F}(k_{f})$ .
