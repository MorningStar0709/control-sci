$$
E = \left[ \begin{array}{l} E _ {1} \\ E _ {2} \end{array} \right] = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right]
$$

为非奇异,因此可进行解耦。

③ 导出积分型解耦系统

定出

$$
\begin{array}{l} E ^ {- 1} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] \\ F = \left[ \begin{array}{l} c _ {1} A ^ {2} \\ c _ {2} A ^ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 3 & 0 & 0 & 2 \\ 0 & - 2 & 0 & 0 \end{array} \right] \\ \end{array}
$$

再取

$$
\bar {L} = E ^ {- 1} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right]

\bar {K} = E ^ {- 1} F = \left[ \begin{array}{c c c c} 3 & 0 & 0 & 2 \\ 0 & - 2 & 0 & 0 \end{array} \right]
$$

则有

$$
\bar {A} = A - B E ^ {- 1} F = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \hline 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{array} \right]

\bar {B} = B E ^ {- 1} = \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \\ - & - \\ 0 & 0 \\ 0 & 1 \end{array} \right]

\overline {{c}} = c = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ \hline - & - & - & - \\ 0 & 0 & 1 & 0 \end{array} \right]
$$

容易看出， $\{\overline{A},\overline{C}\}$ 保持为能观测，且 $\{\overline{A},\overline{B},\overline{C}\}$ 已处于解耦规范形。所以，无需再进一步引入变换，也即有 Q=I。

④ 相对于解耦规范形确定状态反馈增益矩阵 $\tilde{K}$

将 $\tilde{K}$ 取为

$$
\widetilde {K} = \left[ \begin{array}{c c c c} k _ {1 0} & k _ {1 1} & 0 & 0 \\ \hline 0 & 0 & k _ {2 0} & k _ {2 1} \end{array} \right]
$$

则可得

$$
\bar {A} - \bar {B} \widetilde {K} = \left[ \begin{array}{c c c c} 0 & 1 & & \\ - k _ {1 0} & - k _ {1 1} & & \\ \hline & & 0 & 1 \\ & & - k _ {2 0} & - k _ {2 1} \end{array} \right]
$$

再来指定解耦后的单输入-单输出系统的期望特征值,分别为:

$$\lambda_ {1 1} ^ {*} = - 2, \quad \lambda_ {1 2} ^ {*} = - 4\lambda_ {2 1} ^ {*} = - 2 + j, \quad \lambda_ {2 2} ^ {*} = - 2 - j.$$

于是，通过求得

$$\alpha_ {1} ^ {*} (s) = (s + 2) (s + 4) = s ^ {2} + 6 s + 8\alpha_ {2} ^ {*} (s) = (s + 2 - j) (s + 2 + j) = s ^ {2} + 4 s + 5$$

就可定出

$$k _ {1 0} = 8, \quad k _ {1 1} = 6k _ {2 0} = 5, \quad k _ {2 1} = 4$$

从而

$$
\widetilde {K} = \left[ \begin{array}{c c c c} 8 & 6 & 0 & 0 \\ \hline - & - & - & - \\ 0 & 0 & 5 & 4 \end{array} \right]
$$

⑥ 定出对给定受控系统实现解耦控制和极点配置的控制矩阵对 $\{L, K\}$

$$
L = E ^ {- 1} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right]

K = E ^ {- 1} F + E ^ {- 1} \widetilde {K} = F + \widetilde {K} = \left[ \begin{array}{c c c c} 1 1 & 6 & 0 & 2 \\ 0 & - 2 & 5 & 4 \end{array} \right]
$$

⑥ 定出解耦后闭环控制系统的状态空间方程和传递函数矩阵

解耦控制系统的状态方程和输出方程为：
