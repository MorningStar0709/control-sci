而因 $(A, B, C, E(p))$ 为观测器形实现，故再由 $(A, \overline{C}_{\bullet})$ 能观测和PBH秩判据即知

$$\{s I - A, \overline {{{C}}} _ {\bullet} \} \text {为右互质} \tag {10.59}$$

由此，存在多项式阵 $U_{11}(s)$ 和 $U_{12}(s)$ 使成立

$$
\left[ \begin{array}{c c} {- U _ {1 1} (s)} & {U _ {1 2} (s)} \\ {P _ {r} (s)} & {\Psi_ {L} (s)} \end{array} \right] \text {为单模阵} \tag {10.60}

\left[ \begin{array}{l l} - U _ {1 1} (s) & U _ {1 2} (s) \\ P _ {r} (s) & \Psi_ {L} (s) \end{array} \right] \left[ \begin{array}{l} - \bar {C} _ {\bullet} \\ s I - A \end{array} \right] = \left[ \begin{array}{l} I _ {\bullet} \\ 0 \end{array} \right] \tag {10.61}
$$

现将(10.57)和(10.61)合并,就得到所要推导的关系式:

$$
\begin{array}{l} \left[ \begin{array}{c c c} - U _ {1 1} (s) & U _ {1 2} (s) & \mathbf {0} \\ P _ {r} (s) & \Psi_ {L} (s) & \mathbf {0} \\ - R (s) & - X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c c} I _ {m} & \mathbf {0} & \mathbf {0} \\ \mathbf {0} & s I - A & B \\ \mathbf {0} & - C & E (s) \end{array} \right] \\ = \left[ \begin{array}{c c c} I _ {s} & 0 & 0 \\ 0 & P _ {r} (s) & Q _ {r} (s) \\ 0 & - R (s) & W (s) \end{array} \right] \left[ \begin{array}{c c c} - U _ {1 1} (s) & U _ {1 2} (s) (s I - A) & U _ {1 2} (s) B \\ I _ {m} & \bar {C} _ {\bullet} & - Y (s) \\ 0 & 0 & I _ {p} \end{array} \right] \tag {10.62} \\ \end{array}
$$

而且，上式中位于最左边的矩阵由(10.60)可知必为单模阵，而位于最右边的矩阵则由于

$$
\begin{array}{l} \left[ \begin{array}{c c} - U _ {1 1} (s) & U _ {1 2} (s) (s I - A) \\ I _ {m} & \bar {C} _ {o} \end{array} \right] = \left[ \begin{array}{c c} - U _ {1 1} (s) & I _ {n} - U _ {1 1} (s) \bar {C} _ {o} \\ I _ {m} & \bar {C} _ {o} \end{array} \right] \\ = \left[ \begin{array}{c c} I _ {s} & - U _ {1 1} (s) \\ 0 & I _ {m} \end{array} \right] \left[ \begin{array}{l l} 0 & I _ {s} \\ I _ {m} & \bar {C} _ {s} \end{array} \right] = \text {单模阵} \tag {10.63} \\ \end{array}
$$

可知也为单模阵。

② 进而，由(10.32)知， $\{P(s), Q(s)\}$ 和 $\{P_{r}(s), Q_{r}(s)\}$ 之间成立如下的关系式；

$$P _ {r} (s) = M (s) P (s), Q _ {r} (s) = M (s) Q (s) \tag {10.64}$$

其中 $M(s)$ 为单模阵。于是，可构造如下的一个单模阵

$$
\left[ \begin{array}{c c c} I _ {n} & 0 & 0 \\ 0 & M ^ {- 1} (s) & 0 \\ 0 & 0 & I _ {q} \end{array} \right] \tag {10.65}
$$

并将其左乘于式(10.62)，可得到如下的为进一步推证结论所需要的关系式：
