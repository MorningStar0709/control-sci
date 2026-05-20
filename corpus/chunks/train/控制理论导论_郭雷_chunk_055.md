$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {\overline {{x}}} _ {1} (t) \\ \dot {\overline {{x}}} _ {2} (t) \\ \dot {\overline {{x}}} _ {3} (t) \\ \dot {\overline {{x}}} _ {4} (t) \end{array} \right] = \left[ \begin{array}{c c c c} \overline {{A}} _ {1 1} & 0 & \overline {{A}} _ {1 3} & 0 \\ \overline {{A}} _ {2 1} & \overline {{A}} _ {2 2} & \overline {{A}} _ {2 3} & \overline {{A}} _ {2 4} \\ 0 & 0 & \overline {{A}} _ {3 3} & 0 \\ 0 & 0 & \overline {{A}} _ {4 3} & \overline {{A}} _ {4 4} \end{array} \right] \left[ \begin{array}{c} \overline {{x}} _ {1} (t) \\ \overline {{x}} _ {2} (t) \\ \overline {{x}} _ {3} (t) \\ \overline {{x}} _ {4} (t) \end{array} \right] + \left[ \begin{array}{c} \overline {{B}} _ {1} \\ \overline {{B}} _ {2} \\ 0 \\ 0 \end{array} \right] u (t),} \\ y (t) = [ \overline {{C}} _ {1} \quad 0 \quad \overline {{C}} _ {3} \quad 0 ] \left[ \begin{array}{c} \overline {{x}} _ {1} (t) \\ \overline {{x}} _ {2} (t) \\ \overline {{x}} _ {3} (t) \\ \overline {{x}} _ {4} (t) \end{array} \right], \end{array} \right. \tag {1.3.18}
$$

其中 $\overline{x}_1(t), \overline{x}_2(t), \overline{x}_3(t), \overline{x}_4(t)$ 分别为 $n_1, n_2, n_3, n_4$ 维的状态变量， $n_1 + n_2 + n_3 + n_4 = n, n_1 + n_2 = \mu, n_1 + n_3 = \nu$ . 而相应常值矩阵 $\overline{A}_{ij}, \overline{B}_l$ 和 $\overline{C}_k$ ( $i, j = 1, 2, 3, 4, l = 1, 2, k = 1, 3$ ) 的阶数与状态变量的维数相适应. 同时 $\overline{x}_1(t), \overline{x}_2(t)$ 是能控状态变量， $\overline{x}_1(t), \overline{x}_3(t)$ 是能观测状态变量，由 $(\overline{A}_{11}, \overline{B}_1, \overline{C}_1)$ 组成的子系统是完全能控和完全能观测的．如果令

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c} \overline {{{A}}} _ {1 1} & 0 & \overline {{{A}}} _ {1 3} & 0 \\ \overline {{{A}}} _ {2 1} & \overline {{{A}}} _ {2 2} & \overline {{{A}}} _ {2 3} & \overline {{{A}}} _ {2 4} \\ 0 & 0 & \overline {{{A}}} _ {3 3} & 0 \\ 0 & 0 & \overline {{{A}}} _ {4 3} & \overline {{{A}}} _ {4 4} \end{array} \right], \quad \overline {{{B}}} = \left[ \begin{array}{c} \overline {{{B}}} _ {1} \\ \overline {{{B}}} _ {2} \\ 0 \\ 0 \end{array} \right], \quad \overline {{{C}}} = [ \overline {{{C}}} _ {1} \quad 0 \quad \overline {{{C}}} _ {3} \quad 0 ],
$$

那么有

$$\overline {{{A}}} = T ^ {- 1} A T, \quad \overline {{{B}}} = T ^ {- 1} B, \quad \overline {{{C}}} = C T.$$

证明 首先选择子空间 $\chi_{12}, \chi_{11}, \chi_{22}, \chi_{21}$ :
