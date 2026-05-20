# 思考题与习题 3

3-1 已知年龄的论域为[0,200],且设“年老O”和“年轻Y”两个模糊集的隶属函数分别为

$$
\begin{array}{l} \mu_ {0} (a) = \left\{ \begin{array}{l l} 0 & 0 \leqslant a \leqslant 5 0 \\ \frac {a - 5 0}{2 0} & 5 0 \leqslant a \leqslant 7 0 \\ 1. 0 & a \geqslant 7 0 \end{array} \right. \\ \mu_ {\mathrm{Y}} (a) = \left\{ \begin{array}{l l} 1. 0 & 0 \leqslant a \leqslant 2 5 \\ \frac {7 0 - a}{4 5} & 2 5 \leqslant a \leqslant 7 0 \\ 0 & a \geqslant 7 0 \end{array} \right. \\ \end{array}
$$

试设计“很年轻 W”、“不老也不年轻 V”两个模糊集的隶属函数，并采用 Matlab 实现针对上述 4 个隶属函数的仿真。

3-2 已知模糊矩阵 P, Q, R, S, $P = \begin{bmatrix} 0.6 & 0.9 \\ 0.2 & 0.7 \end{bmatrix}, Q = \begin{bmatrix} 0.5 & 0.7 \\ 0.1 & 0.4 \end{bmatrix}, R = \begin{bmatrix} 0.2 & 0.3 \\ 0.7 & 0.7 \end{bmatrix},$ $S = \begin{bmatrix} 0.1 & 0.2 \\ 0.6 & 0.5 \end{bmatrix}$ 。求：

(1) $(\pmb {P}\circ \pmb {Q})\circ \pmb{R}$

(2) $(\mathbf{P} \cup \mathbf{Q}) \circ \mathbf{S}$

(3) $(\pmb{P} \circ \pmb{S}) \cup (\pmb{Q} \circ \pmb{S})$

3-3 求解模糊关系方程

$$
\left[ \begin{array}{l l l} 0. 8 & 0. 5 & 0. 6 \\ 0. 4 & 0. 8 & 0. 5 \end{array} \right] \circ \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] = \left[ \begin{array}{l} 0. 5 \\ 0. 6 \end{array} \right]
$$

3-4 如果 $A = \frac{1}{x_1} + \frac{0.5}{x_2}$ 且 $B = \frac{0.1}{y_1} + \frac{0.5}{y_2} + \frac{1}{y_3}$ , 则 $C = \frac{0.2}{z_1} + \frac{1}{z_2}$ 。现已知 $A_1 = \frac{0.8}{x_1} + \frac{0.1}{x_2}$ 且 $B_1 = \frac{0.5}{y_1} + \frac{0.2}{y_2} + \frac{0}{y_3}$ , 利用模糊推理公式(3.27)和式(3.28)求 $C_1$ , 并采用Matlab进行仿真。
