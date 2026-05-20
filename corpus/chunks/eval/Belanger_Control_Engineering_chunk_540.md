# Example 9.7

For the discrete-time system with $A = \begin{bmatrix} 0 & 1 \\ -5 & 1.5 \end{bmatrix}$ , $\mathbf{b} = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$ , $C = [1 - 0]$ , and $D = 0$ , calculate (i) the transfer function and (ii) the matrix $A^k$ .

Solution

$$
\mathrm{(i)} \qquad (z I - A) = \left[ \begin{array}{c c} z & - 1 \\ . 5 & z - 1. 5 \end{array} \right] \tag {i}

(z I - A) ^ {- 1} = \frac {1}{z ^ {2} - 1 . 5 z + . 5} \left[ \begin{array}{c c} z - 1. 5 & 1 \\ -. 5 & z \end{array} \right]

(z I - A) ^ {- 1} \mathbf {b} = \frac {1}{z ^ {2} - 1 . 5 z + . 5} \left[ \begin{array}{c} - z + 2. 5 \\ z +. 5 \end{array} \right]
$$

and

$$
\frac {\widehat {y}}{\widehat {u}} = \frac {- z + 2 . 5}{(z - 1) (z - . 5)}.
\begin{array}{l} z (z I - A) ^ {- 1} = \frac {z}{(z ^ {2} - 1 . 5 z + . 5)} \left[ \begin{array}{c c} z - 1. 5 & 1 \\ -. 5 & z \end{array} \right]. \tag {ii} \\ = \left[ \begin{array}{c c} \frac {- z}{z - 1} + \frac {2 z}{z - . 5} & \frac {2 z}{z - 1} - \frac {2 z}{z - . 5} \\ \frac {- z}{z - 1} + \frac {1 z}{z - . 5} & \frac {2 z}{z - 1} - \frac {1 z}{z - . 5} \end{array} \right]. \\ \end{array}
$$

The inverse is

$$
A ^ {k} = \left[ \begin{array}{c c} - 1 + 2 (. 5) ^ {k} & 2 - 2 (. 5) ^ {k} \\ - 1 + (. 5) ^ {k} & 2 - (. 5) ^ {k} \end{array} \right].
$$

By this time, the reader will have noticed that many similarities exist between discrete- and continuous-time systems. Observability is defined the same way except that, in discrete-time systems, the observation interval is for those k greater than some positive $k_{1}$ . The criteria are the same. There is a slight difference with respect to controllability, which is defined as the ability to reach to origin from any initial state. Reachability, in contrast, is defined as the ability to reach any state from any other state in a finite number of time steps. The controllability criteria of the continuous-time case are directly applicable to reachability.
