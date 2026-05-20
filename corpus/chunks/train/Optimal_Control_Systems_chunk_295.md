# 5.4 Steady-State Regulator System

Let us now introduce a transformation as

$$
\left[ \begin{array}{l} \mathbf {x} (k) \\ \boldsymbol {\lambda} (k) \end{array} \right] = \mathbf {W} \left[ \begin{array}{l} \mathbf {v} (k) \\ \mathbf {z} (k) \end{array} \right] = \left[ \begin{array}{l l} \mathbf {W} _ {1 1} & \mathbf {W} _ {1 2} \\ \mathbf {W} _ {2 1} & \mathbf {W} _ {2 2} \end{array} \right] \left[ \begin{array}{l} \mathbf {v} (k) \\ \mathbf {z} (k) \end{array} \right]. \tag {5.4.26}
$$

Then, using (5.4.26), (5.4.24) and the Hamiltonian system (5.4.12), we get

$$
\begin{array}{l} \left[ \begin{array}{c} \mathbf {v} (k) \\ \mathbf {z} (k) \end{array} \right] = \mathbf {W} ^ {- 1} \left[ \begin{array}{c} \mathbf {x} ^ {*} (k) \\ \boldsymbol {\lambda} ^ {*} (k) \end{array} \right] = \mathbf {W} ^ {- 1} \mathbf {H} \left[ \begin{array}{c} \mathbf {x} ^ {*} (k + 1) \\ \boldsymbol {\lambda} ^ {*} (k + 1) \end{array} \right] \\ = \mathbf {W} ^ {- 1} \mathbf {H} \mathbf {W} \left[ \begin{array}{c} \mathbf {v} (k + 1) \\ \mathbf {z} (k + 1) \end{array} \right] = \mathbf {D} \left[ \begin{array}{c} \mathbf {v} (k + 1) \\ \mathbf {z} (k + 1) \end{array} \right] \\ = \left[ \begin{array}{c c} \mathbf {M} & 0 \\ 0 & \mathbf {M} ^ {- 1} \end{array} \right] \left[ \begin{array}{l} \mathbf {v} (k + 1) \\ \mathbf {z} (k + 1) \end{array} \right]. \tag {5.4.27} \\ \end{array}
$$

The solution of $(5.4.27)$ in terms of the final conditions is found by first writing it as

$$
\left[ \begin{array}{c} \mathbf {v} (k + 1) \\ \mathbf {z} (k + 1) \end{array} \right] = \mathbf {D} ^ {- 1} \left[ \begin{array}{c} \mathbf {v} (k) \\ \mathbf {z} (k) \end{array} \right].
$$

Then solving this for the given final conditions, we get

$$
\left[ \begin{array}{c} \mathbf {v} (k) \\ \mathbf {z} (k) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {M} ^ {(k _ {f} - k)} & 0 \\ 0 & \mathbf {M} ^ {- (k _ {f} - k)} \end{array} \right] \left[ \begin{array}{c} \mathbf {v} (k _ {f}) \\ \mathbf {z} (k _ {f}) \end{array} \right]. \tag {5.4.28}
$$

Here, since $\mathbf{M}$ is unstable (i.e., it does not go to zero as $(k_f - k) \to \infty$ ), we rewrite (5.4.28) as

$$
\left[ \begin{array}{c} \mathbf {v} (k _ {f}) \\ \mathbf {z} (k) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {M} ^ {- (k _ {f} - k)} & 0 \\ 0 & \mathbf {M} ^ {- (k _ {f} - k)} \end{array} \right] \left[ \begin{array}{c} \mathbf {v} (k) \\ \mathbf {z} (k _ {f}) \end{array} \right]. \tag {5.4.29}
$$
