$$
\boldsymbol {\Phi} (t) = \left[ \begin{array}{c c c c} \mathrm{e} ^ {\lambda_ {1} t} & & 0 \\ & \mathrm{e} ^ {\lambda_ {2} t} & & \\ 0 & & \ddots & \\ & & & \mathrm{e} ^ {\lambda_ {n} t} \end{array} \right] \tag {9-40}
$$

设 $\mathbf{A}$ 矩阵为 $m\times m$ 约当阵

$$
\mathbf {A} = \left[ \begin{array}{c c c c} \lambda & 1 & 0 \\ & \lambda & \ddots \\ & 0 & \ddots & 1 \\ & & & \lambda \end{array} \right]
$$

则

$$
\boldsymbol {\Phi} (t) = \left[ \begin{array}{c c c c c} \mathrm{e} ^ {\lambda t} & t \mathrm{e} ^ {\lambda t} & \frac {t ^ {2}}{2} \mathrm{e} ^ {\lambda t} & \dots & \frac {t ^ {m - 1}}{(m - 1) !} \mathrm{e} ^ {\lambda t} \\ 0 & \mathrm{e} ^ {\lambda t} & t \mathrm{e} ^ {\lambda t} & \dots & \frac {t ^ {m - 2}}{(m - 2) !} \mathrm{e} ^ {\lambda t} \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & t \mathrm{e} ^ {\lambda t} \\ 0 & 0 & 0 & \dots & \mathrm{e} ^ {\lambda t} \end{array} \right] \tag {9-41}
$$

用幂级数展开式即可证明式(9-40)和式(9-41)成立。

例 9-4 设系统状态方程为

$$
\left[ \begin{array}{l} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right]
$$

试求状态方程的解。

解 用拉氏变换求解

$$
s \boldsymbol {I} - \boldsymbol {A} = \left[ \begin{array}{l l} s & 0 \\ 0 & s \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] = \left[ \begin{array}{l l} s & - 1 \\ 2 & s + 3 \end{array} \right]

(s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} = \frac {\operatorname{adj} (s \boldsymbol {I} - \boldsymbol {A})}{| s \boldsymbol {I} - \boldsymbol {A} |} = \frac {1}{(s + 1) (s + 2)} \left[ \begin{array}{l l} s + 3 & 1 \\ - 2 & s \end{array} \right]

= \left[ \begin{array}{l l} \frac {2}{s + 1} - \frac {1}{s + 2} & \frac {1}{s + 1} - \frac {1}{s + 2} \\ \frac {- 2}{s + 1} + \frac {2}{s + 2} & \frac {- 1}{s + 1} + \frac {2}{s + 2} \end{array} \right]

\boldsymbol {\Phi} (t) = \mathscr {L} ^ {- 1} [ (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} ] = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right]
$$

状态方程的解为

$$
\left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] = \boldsymbol {\Phi} (t) \left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{c c} 2 \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} & \mathrm{e} ^ {- t} - \mathrm{e} ^ {- 2 t} \\ - 2 \mathrm{e} ^ {- t} + 2 \mathrm{e} ^ {- 2 t} & - \mathrm{e} ^ {- t} + 2 \mathrm{e} ^ {- 2 t} \end{array} \right] \left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \end{array} \right]
$$
