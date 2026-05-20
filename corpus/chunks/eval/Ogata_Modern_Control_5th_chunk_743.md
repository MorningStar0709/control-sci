$$
\begin{array}{l} | s \mathbf {I} - \mathbf {A} + \mathbf {B K} | = \left| \left[ \begin{array}{c c c} s & 0 & 0 \\ 0 & s & 0 \\ 0 & 0 & s \end{array} \right] - \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & - 5 & - 6 \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right] \left[ \begin{array}{c c c} k _ {1} & k _ {2} & k _ {3} \end{array} \right] \right| \\ = \left| \begin{array}{c c c} s & - 1 & 0 \\ 0 & s & - 1 \\ 1 + k _ {1} & 5 + k _ {2} & s + 6 + k _ {3} \end{array} \right| \\ = s ^ {3} + (6 + k _ {3}) s ^ {2} + (5 + k _ {2}) s + 1 + k _ {1} \\ = s ^ {3} + 1 4 s ^ {2} + 6 0 s + 2 0 0 \\ \end{array}
$$

Thus,

$$6 + k _ {3} = 1 4, \quad 5 + k _ {2} = 6 0, \quad 1 + k _ {1} = 2 0 0$$

from which we obtain

$$k _ {1} = 1 9 9, \quad k _ {2} = 5 5, \quad k _ {3} = 8$$

or

$$
\mathbf {K} = \left[ \begin{array}{c c c} 1 9 9 & 5 5 & 8 \end{array} \right]
$$

Method 3: The third method is to use Ackermann’s formula. Referring to Equation (10–18), we have

$$
\mathbf {K} = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} \end{array} \right] ^ {- 1} \phi (\mathbf {A})
$$

Since

$$
\begin{array}{l} \phi (\mathbf {A}) = \mathbf {A} ^ {3} + 1 4 \mathbf {A} ^ {2} + 6 0 \mathbf {A} + 2 0 0 \mathbf {I} \\ = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & - 5 & - 6 \end{array} \right] ^ {3} + 1 4 \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & - 5 & - 6 \end{array} \right] ^ {2} \\ + 6 0 \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & - 5 & - 6 \end{array} \right] + 2 0 0 \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \\ = \left[ \begin{array}{c c c} 1 9 9 & 5 5 & 8 \\ - 8 & 1 5 9 & 7 \\ - 7 & - 4 3 & 1 1 7 \end{array} \right] \\ \end{array}
$$

and

$$
\left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & - 6 \\ 1 & - 6 & 3 1 \end{array} \right]
$$

we obtain

$$
\begin{array}{l} \mathbf {K} = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & - 6 \\ 1 & - 6 & 3 1 \end{array} \right] ^ {- 1} \left[ \begin{array}{c c c} 1 9 9 & 5 5 & 8 \\ - 8 & 1 5 9 & 7 \\ - 7 & - 4 3 & 1 1 7 \end{array} \right] \\ = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} 5 & 6 & 1 \\ 6 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c c c} 1 9 9 & 5 5 & 8 \\ - 8 & 1 5 9 & 7 \\ - 7 & - 4 3 & 1 1 7 \end{array} \right] \\ = \left[ \begin{array}{c c c} 1 9 9 & 5 5 & 8 \end{array} \right] \\ \end{array}
$$
