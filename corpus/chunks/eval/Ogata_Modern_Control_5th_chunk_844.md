$$
\begin{array}{l} \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \mathbf {N} ^ {*} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \left[ \begin{array}{l} \mathbf {C} \\ \mathbf {C A} \\ \mathbf {C A} ^ {2} \end{array} \right] \\ = \left[ \begin{array}{c} \mathbf {C A} \\ \mathbf {C A} ^ {2} \\ - a _ {3} \mathbf {C} - a _ {2} \mathbf {C A} - a _ {1} \mathbf {C A} ^ {2} \end{array} \right] \tag {10-150} \\ \end{array}
$$

The Cayley–Hamilton theorem states that matrix A satisfies its own characteristic equation, or

$$\mathbf {A} ^ {3} + a _ {1} \mathbf {A} ^ {2} + a _ {2} \mathbf {A} + a _ {3} \mathbf {I} = \mathbf {0}$$

Hence,

$$- a _ {1} \mathbf {C A} ^ {2} - a _ {2} \mathbf {C A} - a _ {3} \mathbf {C} = \mathbf {C A} ^ {3}$$

Thus, the right-hand side of Equation (10–150) becomes the same as the right-hand side of Equation (10–149). Consequently,

$$
\mathbf {N} ^ {*} \mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \mathbf {N} ^ {*}
$$

which is Equation (10–148). This last equation can be modified to

$$
\mathbf {N} ^ {*} \mathbf {A} (\mathbf {N} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right]
$$

The derivation presented here can be extended to the general case of any positive integer n.

A–10–8. Consider a completely observable system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-151}y = \mathbf {C} \mathbf {x} + D u \tag {10-152}$$

Define

$$
\mathbf {N} = \left[ \begin{array}{c c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right]
$$

and

$$
\mathbf {W} = \left[ \begin{array}{c c c c c} a _ {n - 1} & a _ {n - 2} & \dots & a _ {1} & 1 \\ a _ {n - 2} & a _ {n - 3} & \dots & 1 & 0 \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ a _ {1} & 1 & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0 \end{array} \right]
$$

where the a’s are coefficients of the characteristic polynomial

$$\left| s \mathbf {I} - \mathbf {A} \right| = s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}$$

Define also

$$\mathbf {Q} = (\mathbf {W N} ^ {*}) ^ {- 1}$$

Show that
