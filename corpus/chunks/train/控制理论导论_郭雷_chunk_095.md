# 1.6.4 对给定形式的实矩阵

$$
\pmb {A} = \left[ \begin{array}{c c} {\pmb {A} _ {1}} & {\pmb {A} _ {3}} \\ {0} & {\pmb {A} _ {2}} \end{array} \right] \quad \text {和} \quad \pmb {B} = \left[ \begin{array}{c} {\pmb {B} _ {1}} \\ {\pmb {B} _ {2}} \end{array} \right],
$$

证明：如果系统

$$\dot {x} = A x + B u$$

是能控的，则必存在形如 $u = Kx + Bw$ 的状态反馈控制使闭环系统

$$\dot {\boldsymbol {x}} = (\boldsymbol {A} + \boldsymbol {B K}) \boldsymbol {x} + \boldsymbol {B w}$$

等价于系统

$$
\dot {\overline {{{x}}}} = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & \overline {{{A}}} _ {2} \end{array} \right] \overline {{{x}}} + \left[ \begin{array}{c} \overline {{{B}}} _ {1} \\ B _ {2} \end{array} \right] w.
$$

这里 $\overline{A}_2$ 和 $\overline{B}_1$ 是适当维数的实矩阵，且 $\overline{A}_2$ 和 $A_1$ 具有互不相同的特征值.

1.6.5 证明：若 $(A, B)$ 能控，且 $A$ 稳定，则方程

$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} + \boldsymbol {B B} ^ {\mathrm{T}} = 0$$

有唯一正定对称解 $P$ ，且类似于式 (1.1.16)，该解 $P$ 可由下式给出：

$$\boldsymbol {P} = \int_ {0} ^ {\infty} \mathrm{c} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \mathrm{c} ^ {\boldsymbol {A} t} \mathrm{d} t.$$

1.6.6 已知定常线性系统

$$
\left\{ \begin{array}{l} \dot {x} (t) = A x (t) + b u (t), \\ y (t) = C x (t), \end{array} \right.
$$

其中

$$
\boldsymbol {A} = \left[ \begin{array}{l l l l} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array} \right], \quad \boldsymbol {b} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 1 \end{array} \right], \quad \boldsymbol {C} = \left[ \begin{array}{l l l l} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right].
$$

如果预先给定复数集合 $A=\{-1,-1,-1,-1,-1\}$ ，试用动态输出反馈配置系统的极点，使闭环系统的极点集合为 A.
