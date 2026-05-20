$$
\begin{array}{l} \left[ \begin{array}{c} \dot {g} _ {1} (t) \\ \dot {g} _ {2} (t) \end{array} \right] = - \left\{\left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \right. \\ - \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \frac {1}{0 . 0 4} \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \Bigg \} ^ {\prime} \left[ \begin{array}{c} g _ {1} (t) \\ g _ {2} (t) \end{array} \right] \\ - \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] ^ {\prime} \left[ \begin{array}{l l} 2 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} 2 t \\ 0 \end{array} \right]. \tag {4.1.54} \\ \end{array}
$$

Simplifying the equations (4.1.53) and (4.1.54), we get

$$\dot {p} _ {1 1} (t) = 2 5 p _ {1 2} ^ {2} (t) + 4 p _ {1 2} (t) - 2\dot {p} _ {1 2} (t) = 2 5 p _ {1 2} (t) p _ {2 2} (t) - p _ {1 1} (t) + 3 p _ {1 2} (t) + 2 p _ {2 2} (t)\dot {p} _ {2 2} (t) = 2 5 p _ {2 2} ^ {2} (t) - 2 p _ {1 2} (t) + 6 p _ {2 2} (t) \tag {4.1.55}$$

with final condition (4.1.33) as

$$
\left[ \begin{array}{l l} p _ {1 1} \left(t _ {f}\right) & p _ {1 2} \left(t _ {f}\right) \\ p _ {1 2} \left(t _ {f}\right) & p _ {2 2} \left(t _ {f}\right) \end{array} \right] = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \tag {4.1.56}
$$

and

$$\dot {g} _ {1} (t) = \left[ 2 5 p _ {1 2} (t) + 2 \right] g _ {2} (t) - 4 t\dot {g} _ {2} (t) = - g _ {1} (t) + [ 3 + 2 5 p _ {2 2} (t) ] g _ {2} (t) \tag {4.1.57}$$

with final condition

$$
\left[ \begin{array}{l} g _ {1} (t _ {f}) \\ g _ {2} (t _ {f}) \end{array} \right] = \left[ \begin{array}{l} 0 \\ 0 \end{array} \right]. \tag {4.1.58}
$$

See the plots of the Riccati coefficients $p_{11}(t), p_{12}(t)$ and $p_{22}(t)$ in Figure 4.6 and coefficients $g_1(t)$ and $g_2(t)$ in Figure 4.7. Also see the plots of the optimal control $u^*(t)$ in Figure 4.9 and optimal states $x_1^*(t)$ and $x_2^*(t)$ in Figure 4.8.
