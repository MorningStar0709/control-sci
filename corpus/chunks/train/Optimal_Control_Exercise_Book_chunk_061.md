$$
\left[ \begin{array}{c} x _ {1} ^ {*} \\ x _ {2} ^ {*} \end{array} \right] = \frac {1}{5} e ^ {- 6 t} \left[ \begin{array}{c} k _ {1} (2 e ^ {5 t} + 3) + 2 k _ {2} (e ^ {5 t} - 1) \\ 3 k _ {1} (e ^ {5 t} - 1) + k _ {2} (3 e ^ {5 t} + 2) \end{array} \right] + \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] \quad k _ {1}, k _ {2} \in \mathbb {R}, \quad p ^ {*} (t) \geq 0 \tag {227}

\left[ \begin{array}{c} x _ {1} ^ {*} \\ x _ {2} ^ {*} \end{array} \right] = \frac {1}{5} e ^ {- 6 t} \left[ \begin{array}{c} k _ {1} (2 e ^ {5 t} + 3) + 2 k _ {2} (e ^ {5 t} - 1) \\ 3 k _ {1} (e ^ {5 t} - 1) + k _ {2} (3 e ^ {5 t} + 2) \end{array} \right] + \left[ \begin{array}{c} - 1 \\ - 1 \end{array} \right] \quad k _ {1}, k _ {2} \in \mathbb {R}, \quad p ^ {*} (t) <   0 \tag {228}
$$

After obtaining the switching time, for which $p _ { 1 } ^ { * }$ changes sign, we can rewrite the controller by choosing $u ^ { * } = 1 \operatorname { i f } p _ { 1 } ^ { * } = 0$ . Therefore, the general solution is a bang-bang controller (in which the controller switches abruptly between two inputs). We can rewrite the controller as:

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 1 & \text { if } p _ {1} ^ {*} \geq 0 \\ - 1 & \text { if } p _ {1} ^ {*} <   0 \end{array} \right. \tag {229}
$$
