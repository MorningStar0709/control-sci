$$
\mathbf {M} ^ {- 1} \mathbf {A M} = \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right]
$$

The preceding derivation can be easily extended to the general case of any positive integer n.

A–10–3. Consider a completely state controllable system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

Define

$$
\mathbf {M} = \left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

and

$$
\mathbf {W} = \left[ \begin{array}{c c c c c} a _ {n - 1} & a _ {n - 2} & \dots & a _ {1} & 1 \\ a _ {n - 2} & a _ {n - 3} & \dots & 1 & 0 \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ a _ {1} & 1 & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0 \end{array} \right]
$$

where the $\boldsymbol { a _ { i } } ^ { \prime }$ s are coefficients of the characteristic polynomial

$$| s \mathbf {I} - \mathbf {A} | = s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}$$

Define also

$$\mathbf {T} = \mathbf {M W}$$

Show that

$$
\mathbf {T} ^ {- 1} \mathbf {A T} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ . & . & . & & . \\ . & . & . & & . \\ . & . & . & & . \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right], \qquad \mathbf {T} ^ {- 1} \mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \\ . \\ . \\ . \\ 0 \\ 1 \end{array} \right]
$$

Solution. Let us consider the case where n=3. We shall show that

$$
\mathbf {T} ^ {- 1} \mathbf {A} \mathbf {T} = (\mathbf {M} \mathbf {W}) ^ {- 1} \mathbf {A} (\mathbf {M} \mathbf {W}) = \mathbf {W} ^ {- 1} (\mathbf {M} ^ {- 1} \mathbf {A} \mathbf {M}) \mathbf {W} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \tag {10-143}
$$

Referring to Problem A–10–2, we have

$$
\mathbf {M} ^ {- 1} \mathbf {A M} = \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right]
$$

Hence, Equation (10–143) can be rewritten as

$$
\mathbf {W} ^ {- 1} \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \mathbf {W} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right]
$$

Therefore, we need to show that

$$
\left[ \begin{array}{l l l} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \mathbf {W} = \mathbf {W} \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \tag {10-144}
$$

The left-hand side of Equation (10–144) is
