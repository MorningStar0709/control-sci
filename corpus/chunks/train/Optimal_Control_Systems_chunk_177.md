$$
\left[ \begin{array}{c} \mathbf {w} (t) \\ \mathbf {z} (t) \end{array} \right] = \left[ \begin{array}{c c} e ^ {- \mathbf {M} (t - t _ {f})} & \mathbf {0} \\ \mathbf {0} & e ^ {\mathbf {M} (t - t _ {f})} \end{array} \right] \left[ \begin{array}{c} \mathbf {w} (t _ {f}) \\ \mathbf {z} (t _ {f}) \end{array} \right]. \tag {3.3.15}
$$

Rewriting (3.3.15)

$$
\left[ \begin{array}{c} \mathbf {w} (t _ {f}) \\ \mathbf {z} (t) \end{array} \right] = \left[ \begin{array}{c c} e ^ {\mathbf {M} (t - t _ {f})} & \mathbf {0} \\ \mathbf {0} & e ^ {\mathbf {M} (t - t _ {f})} \end{array} \right] \left[ \begin{array}{c} \mathbf {w} (t) \\ \mathbf {z} (t _ {f}) \end{array} \right]. \tag {3.3.16}
$$

Next, from (3.3.13) and using the final condition (3.3.4)

$$
\begin{array}{l} \boldsymbol {\lambda} \left(t _ {f}\right) = \mathbf {W} _ {2 1} \mathbf {w} \left(t _ {f}\right) + \mathbf {W} _ {2 2} \mathbf {z} \left(t _ {f}\right) \\ = \mathbf {F} \mathbf {x} (t _ {f}) \\ = \mathbf {F} \left[ \mathbf {W} _ {1 1} \mathbf {w} (t _ {f}) + \mathbf {W} _ {1 2} \mathbf {z} (t _ {f}) \right]. \tag {3.3.17} \\ \end{array}
$$

Solving the previous relation for $\mathbf{z}(t_{f})$ in terms of $\mathbf{w}(t_{f})$

$$\mathbf {z} (t _ {f}) = \mathbf {T} (t _ {f}) \mathbf {w} (t _ {f}), \text {where}\mathbf {T} \left(t _ {f}\right) = - \left[ \mathbf {W} _ {2 2} - \mathbf {F W} _ {1 2} \right] ^ {- 1} \left[ \mathbf {W} _ {2 1} - \mathbf {F W} _ {1 1} \right]. \tag {3.3.18}$$

Again, from (3.3.16)

$$
\begin{array}{l} \mathbf {z} (t) = e ^ {- \mathbf {M} (t _ {f} - t)} \mathbf {z} (t _ {f}) \\ = e ^ {- \mathbf {M} (t _ {f} - t)} \mathbf {T} (t _ {f}) \mathbf {w} (t _ {f}) \\ = e ^ {- \mathbf {M} (t _ {f} - t)} \mathbf {T} (t _ {f}) e ^ {- \mathbf {M} (t _ {f} - t)} \mathbf {w} (t). \tag {3.3.19} \\ \end{array}
$$

Rewriting the previous relation as

$$\mathbf {z} (t) = \mathbf {T} (t) \mathbf {w} (t), \text { where, }\mathbf {T} (t) = e ^ {- \mathbf {M} (t _ {f} - t)} \mathbf {T} (t _ {f}) e ^ {- \mathbf {M} (t _ {f} - t)}. \tag {3.3.20}$$

Finally, to relate $\mathbf{P}(t)$ in (3.3.3) to the relation (3.3.20) for $\mathbf{T}(t)$ , let us use (3.3.13) to write

$$
\begin{array}{l} \boldsymbol {\lambda} (t) = \mathbf {W} _ {2 1} \mathbf {w} (t) + \mathbf {W} _ {2 2} \mathbf {z} (t) \\ = \mathbf {P} (t) \mathbf {x} (t) \\ = \mathbf {P} (t) \left[ \mathbf {W} _ {1 1} \mathbf {w} (t) + \mathbf {W} _ {1 2} \mathbf {z} (t) \right] \tag {3.3.21} \\ \end{array}
$$

and by (3.3.20), the previous relation can be written as

$$\left[ \mathbf {W} _ {2 1} + \mathbf {W} _ {2 2} \mathbf {T} (t) \right] \mathbf {w} (t) = \mathbf {P} (t) \left[ \mathbf {W} _ {1 1} + \mathbf {W} _ {1 2} \mathbf {T} (t) \right] \mathbf {w} (t). \tag {3.3.22}$$

Since the previous relation should hold good for all $\mathbf{x}(t_{0})$ and hence for all states $\mathbf{w}(t)$ , it implies that the analytical expression to the solution of $\mathbf{P}(t)$ is given by

$$\boxed {\mathbf {P} (t) = \left[ \mathbf {W} _ {2 1} + \mathbf {W} _ {2 2} \mathbf {T} (t) \right] \left[ \mathbf {W} _ {1 1} + \mathbf {W} _ {1 2} \mathbf {T} (t) \right] ^ {- 1}.} \tag {3.3.23}$$
