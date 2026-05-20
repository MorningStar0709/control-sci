where, $\mathbf{P}(t)$ , the positive definite matrix, is the solution of the matrix differential Riccati equation (4.1.32)

$$
\begin{array}{l} \left[ \begin{array}{c c} \dot {p} _ {1 1} (t) & \dot {p} _ {1 2} (t) \\ \dot {p} _ {1 2} (t) & \dot {p} _ {2 2} (t) \end{array} \right] = - \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \\ - \left[ \begin{array}{c c} 0 & - 2 \\ 1 & - 3 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \\ + \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \frac {1}{0 . 0 0 4} \left[ \begin{array}{c c} 0 & 1 \end{array} \right] x \\ \left[ \begin{array}{l l} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] - \left[ \begin{array}{l l} 2 & 0 \\ 0 & 0 \end{array} \right] \tag {4.1.43} \\ \end{array}
$$

and $\mathbf{g}(t)$ , is the solution of the nonhomogeneous vector differential equation obtained from (4.1.34) as

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {g} _ {1} (t) \\ \dot {g} _ {2} (t) \end{array} \right] = - \left\{\left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \right. \\ - \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \frac {1}{0 . 0 0 4} \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \Bigg \} ^ {\prime} \left[ \begin{array}{c} g _ {1} (t) \\ g _ {2} (t) \end{array} \right] \\ - \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] ^ {\prime} \left[ \begin{array}{l l} 2 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} 1 \\ 0 \end{array} \right]. \tag {4.1.44} \\ \end{array}
$$

Simplifying the equations (4.1.43) and (4.1.44), we get

$$\dot {p} _ {1 1} (t) = 2 5 0 p _ {1 2} ^ {2} (t) + 4 p _ {1 2} (t) - 2\dot {p} _ {1 2} (t) = 2 5 0 p _ {1 2} (t) p _ {2 2} (t) - p _ {1 1} (t) + 3 p _ {1 2} (t) + 2 p _ {2 2} (t)\dot {p} _ {2 2} (t) = 2 5 0 p _ {2 2} ^ {2} (t) - 2 p _ {1 2} (t) + 6 p _ {2 2} (t) \tag {4.1.45}$$

with final condition (4.1.33) as

$$
\left[ \begin{array}{l l} p _ {1 1} (t _ {f}) & p _ {1 2} (t _ {f}) \\ p _ {1 2} (t _ {f}) & p _ {2 2} (t _ {f}) \end{array} \right] = \left[ \begin{array}{l l} 2 & 0 \\ 0 & 0 \end{array} \right] \tag {4.1.46}
$$

and
