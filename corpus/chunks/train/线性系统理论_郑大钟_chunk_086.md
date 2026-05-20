$$
\begin{array}{l} G = e ^ {A T} = \left[ \begin{array}{c c} 1 & 0. 5 (1 - e ^ {- 2 T}) \\ 0 & e ^ {- 2 T} \end{array} \right] = \left[ \begin{array}{l l} 1 & 0. 0 9 1 \\ 0 & 0. 8 1 9 \end{array} \right] \\ H = \left(\int_ {0} ^ {T} e ^ {A t} d t\right) B = \left(\int_ {0} ^ {T} \left[ \begin{array}{c c} 1 & 0. 5 (1 - e ^ {- 2 t}) \\ 0 & e ^ {- 2 t} \end{array} \right] d t\right) \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \\ = \left[ \begin{array}{c c} T & 0. 5 T + 0. 2 5 e ^ {- 2 T} - 0. 2 5 \\ 0 & - 0. 5 e ^ {- 2 T} + 0. 5 \end{array} \right] \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \\ = \left[ \begin{array}{c} 0. 5 T + 0. 2 5 e ^ {- 2 T} - 0. 2 5 \\ - 0. 5 e ^ {- 2 T} + 0. 5 \end{array} \right] = \left[ \begin{array}{l} 0. 0 0 5 \\ 0. 0 9 1 \end{array} \right] \\ \end{array}
$$

于是，给定连续系统的离散化模型的状态方程即为：

$$
\left[ \begin{array}{l} x _ {1} (k + 1) \\ x _ {2} (k + 1) \end{array} \right] = \left[ \begin{array}{l l} 1 & 0. 0 9 1 \\ 0 & 0. 8 1 9 \end{array} \right] \left[ \begin{array}{l} x _ {1} (k) \\ x _ {2} (k) \end{array} \right] + \left[ \begin{array}{l} 0. 0 0 5 \\ 0. 0 9 1 \end{array} \right] u (k)
$$
