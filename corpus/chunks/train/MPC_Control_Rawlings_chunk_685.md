in which A and B are given in (6.1), the cost penalties $\mathcal { Q }$ and R are given in (6.2) and (6.9), and

$$H _ {\mathbf {u}} = \mathcal {B} ^ {\prime} \mathcal {Q} \mathcal {B} + \mathcal {R}$$

The overall cost is a positive definite quadratic function in u because $R _ { 1 }$ and $R _ { 2 }$ are positive definite, and therefore so are $\mathcal { R } _ { 1 } , \mathcal { R } _ { 2 }$ , and $\mathcal { R }$ .

The iteration in the two players’ moves satisfies

$$
\begin{array}{l} \left(\mathbf {u} _ {1} ^ {p + 1}, \mathbf {u} _ {2} ^ {p + 1}\right) = \left(\left(w _ {1} \mathbf {u} _ {1} ^ {0} + (1 - w _ {1}) \mathbf {u} _ {1} ^ {p}\right), \left(w _ {2} \mathbf {u} _ {2} ^ {0} + (1 - w _ {2}) \mathbf {u} _ {2} ^ {p}\right)\right) \\ = (w _ {1} \mathbf {u} _ {1} ^ {0}, (1 - w _ {2}) \mathbf {u} _ {2} ^ {p}) + ((1 - w _ {1}) \mathbf {u} _ {1} ^ {p}, w _ {2} \mathbf {u} _ {2} ^ {0}) \\ \left(\mathbf {u} _ {1} ^ {p + 1}, \mathbf {u} _ {2} ^ {p + 1}\right) = w _ {1} \left(\mathbf {u} _ {1} ^ {0}, \mathbf {u} _ {2} ^ {p}\right) + w _ {2} \left(\mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {0}\right) \tag {6.14} \\ \end{array}
$$

Exercise 6.18 analyzes the cost decrease for a convex step with a positive definite quadratic function and shows

$$
\begin{array}{l} V (x (0), \mathbf {u} _ {1} ^ {p + 1}, \mathbf {u} _ {2} ^ {p + 1}) = V (x (0), \mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {p}) \\ - \frac {1}{2} \left[ \mathbf {u} ^ {p} - \mathbf {u} ^ {0} (x (0)) \right] ^ {\prime} P \left[ \mathbf {u} ^ {p} - \mathbf {u} ^ {0} (x (0)) \right] \tag {6.15} \\ \end{array}
$$

in which $P > 0$ is given by

$$
P = H _ {\mathbf {u}} D ^ {- 1} \tilde {\tilde {H}} D ^ {- 1} H _ {\mathbf {u}} \quad \tilde {\tilde {H}} = D - N
D = \left[ \begin{array}{c c} w _ {1} ^ {- 1} H _ {\mathbf {u}, 1 1} & 0 \\ 0 & w _ {2} ^ {- 1} H _ {\mathbf {u}, 2 2} \end{array} \right] \qquad N = \left[ \begin{array}{c c} - w _ {1} ^ {- 1} w _ {2} H _ {\mathbf {u}, 1 1} & H _ {\mathbf {u}, 1 2} \\ H _ {\mathbf {u}, 2 1} & - w _ {1} w _ {2} ^ {- 1} H _ {\mathbf {u}, 2 2} \end{array} \right]
$$

and $H _ { \mathbf { u } }$ is partitioned for the two players’ input sequences. Notice that the cost decrease achieved in a single iteration is quadratic in the distance from the optimum. An important conclusion is that each iteration in the cooperative game reduces the systemwide cost. This cost reduction is the key property that gives cooperative MPC its excellent convergence properties, as we show next.

The two players’ warm starts at the next sample are given by
