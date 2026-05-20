$$\Gamma \Delta^ {\prime} \Gamma \mathbf {v} = \mu \mathbf {v}, \quad \Delta^ {\prime} \Gamma \mathbf {v} = - \mu \Gamma \mathbf {v} \tag {3.3.8}$$

where, we used $\Gamma^{-1} = -\Gamma$ . Rearranging

$$(\Gamma \mathbf {v}) ^ {\prime} \Delta = - \mu (\Gamma \mathbf {v}) ^ {\prime} \tag {3.3.9}$$

Next, rearranging the eigenvalues of $\Delta$ as

$$
\mathbf {D} = \left[ \begin{array}{c c} - \mathbf {M} & \mathbf {0} \\ \mathbf {0} & \mathbf {M} \end{array} \right] \tag {3.3.10}
$$

where, $\mathbf{M}(-\mathbf{M})$ is a diagonal matrix with right-half-plane (left-half plane) eigenvalues. Let W, the modal matrix of eigenvectors corresponding to D, be defined as

$$
\mathbf {W} = \left[ \begin{array}{l l} \mathbf {W} _ {1 1} & \mathbf {W} _ {1 2} \\ \mathbf {W} _ {2 1} & \mathbf {W} _ {2 2} \end{array} \right], \tag {3.3.11}
$$

where, $[W_{11} \quad W_{21}]'$ are the n eigenvectors of the left-half-plane (stable) eigenvalues of $\Delta$ . Also,

$$\mathbf {W} ^ {- 1} \Delta \mathbf {W} = \mathbf {D}. \tag {3.3.12}$$

Let us now define a state transformation

$$
\left[ \begin{array}{l} \mathbf {x} (t) \\ \boldsymbol {\lambda} (t) \end{array} \right] = \mathbf {W} \left[ \begin{array}{l} \mathbf {w} (t) \\ \mathbf {z} (t) \end{array} \right] = \left[ \begin{array}{l l} \mathbf {W} _ {1 1} & \mathbf {W} _ {1 2} \\ \mathbf {W} _ {2 1} & \mathbf {W} _ {2 2} \end{array} \right] \left[ \begin{array}{l} \mathbf {w} (t) \\ \mathbf {z} (t) \end{array} \right]. \tag {3.3.13}
$$

Then, using (3.3.12) and (3.3.13), the Hamiltonian system (3.3.1) becomes

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {\mathbf {w}} (t) \\ \dot {\mathbf {z}} (t) \end{array} \right] = \mathbf {W} ^ {- 1} \left[ \begin{array}{c} \dot {\mathbf {x}} (t) \\ \dot {\boldsymbol {\lambda}} (t) \end{array} \right] = \mathbf {W} ^ {- 1} \Delta \left[ \begin{array}{c} \mathbf {x} (t) \\ \boldsymbol {\lambda} (t) \end{array} \right] = \mathbf {W} ^ {- 1} \Delta \mathbf {W} \left[ \begin{array}{c} \mathbf {w} (t) \\ \mathbf {z} (t) \end{array} \right] \\ = \mathbf {D} \left[ \begin{array}{c} \mathbf {w} (t) \\ \mathbf {z} (t) \end{array} \right]. \tag {3.3.14} \\ \end{array}
$$

Solving (3.3.14) in terms of the known final conditions, we have
