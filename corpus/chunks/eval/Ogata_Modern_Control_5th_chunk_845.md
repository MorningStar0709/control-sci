$$
\mathbf {Q} ^ {- 1} \mathbf {A Q} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & - a _ {n} \\ 1 & 0 & \dots & 0 & - a _ {n - 1} \\ 0 & 1 & \dots & 0 & - a _ {n - 2} \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ 0 & 0 & \dots & 1 & - a _ {1} \end{array} \right]

\mathbf {C Q} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & 1 \end{array} \right]

\mathbf {Q} ^ {- 1} \mathbf {B} = \left[ \begin{array}{c} b _ {n} - a _ {n} b _ {0} \\ b _ {n - 1} - a _ {n - 1} b _ {0} \\ \cdot \\ \cdot \\ \cdot \\ b _ {1} - a _ {1} b _ {0} \end{array} \right]
$$

where the $b _ { k } \mathrm { } ^ { \prime } \mathrm { { s } } \left( k = 0 , 1 , 2 , \ldots , n \right)$ are those coefficients appearing in the numerator of the transfer function when $\mathbf { C } ( s \mathbf { I } - \mathbf { A } ) ^ { - 1 } \mathbf { B } + D$ is written as follows:

$$\mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + D = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}}$$

where $D = b _ { 0 }$

Solution. Let us consider the case where n=3. We shall show that

$$
\mathbf {Q} ^ {- 1} \mathbf {A Q} = (\mathbf {W N} ^ {*}) \mathbf {A} (\mathbf {W N} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \tag {10-153}
$$

Note that, by referring to Problem A–10–7, we have

$$
(\mathbf {W N} ^ {*}) \mathbf {A} (\mathbf {W N} ^ {*}) ^ {- 1} = \mathbf {W} [ \mathbf {N} ^ {*} \mathbf {A} (\mathbf {N} ^ {*}) ^ {- 1} ] \mathbf {W} ^ {- 1} = \mathbf {W} \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \mathbf {W} ^ {- 1}
$$

Hence, we need to show that

$$
\mathbf {W} \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \mathbf {W} ^ {- 1} = \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right]
$$

or

$$
\mathbf {W} \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \mathbf {W} \tag {10-154}
$$

The left-hand side of Equation (10–154) is
