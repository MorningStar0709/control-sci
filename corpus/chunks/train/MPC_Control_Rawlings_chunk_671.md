$$
\left[ \begin{array}{c} \mathbf {u} _ {1} ^ {0} \\ \mathbf {u} _ {2} ^ {0} \end{array} \right] = \left[ \begin{array}{c c} K _ {1} & 0 \\ 0 & K _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] + \left[ \begin{array}{c c} 0 & L _ {1} \\ L _ {2} & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p}
$$

Substituting the optimal control into the iteration gives

$$
\left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p + 1} = \underbrace {\left[ \begin{array}{c c} w _ {1} K _ {1} & 0 \\ 0 & w _ {2} K _ {2} \end{array} \right]} _ {\overline {{K}}} \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] + \underbrace {\left[ \begin{array}{c c} (1 - w _ {1}) I & w _ {1} L _ {1} \\ w _ {2} L _ {2} & (1 - w _ {2}) I \end{array} \right]} _ {L} \left[ \begin{array}{c} \mathbf {u} _ {1} \\ \mathbf {u} _ {2} \end{array} \right] ^ {p}
$$

Finally writing this equation in the plantwide notation, we express the iteration as

$$\mathbf {u} ^ {p + 1} = \overline {{K}} x (0) + L \mathbf {u} ^ {p}$$

The convergence of the two players’ control iteration is governed by the eigenvalues of L. If L is stable, the control sequence converges to

$$\mathbf {u} ^ {\infty} = (I - L) ^ {- 1} \overline {{K}} x (0) \quad | \lambda | < 1 \text { for } \lambda \in \operatorname{eig} (L)$$

in which

$$
(I - L) ^ {- 1} \overline {{K}} = \left[ \begin{array}{c c} w _ {1} I & - w _ {1} L _ {1} \\ - w _ {2} L _ {2} & w _ {2} I \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} w _ {1} K _ {1} & 0 \\ 0 & w _ {2} K _ {2} \end{array} \right]

(I - L) ^ {- 1} \overline {{K}} = \left[ \begin{array}{c c} I & - L _ {1} \\ - L _ {2} & I \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} K _ {1} & 0 \\ 0 & K _ {2} \end{array} \right]
$$
