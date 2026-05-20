$$
\begin{array}{l} \bar {N} (s) = \left[ \begin{array}{c c c} s & 0 & s (s + 1) \\ 0 & s + 1 & s + 2 \end{array} \right], \\ \widetilde {D} (s) = \left[ \begin{array}{c c c} s + 2 & 0 & 0 \\ 0 & s ^ {2} & 0 \\ 0 & 0 & s (s + 2) \end{array} \right] \\ \end{array}
$$

首先，来找出它的一个左 MFD $\vec{A}^{-1}(s)\vec{B}(s)$ 。为此求解如下的多项式矩阵方程：

$$
\left[ \begin{array}{l l l l l} - b _ {1 1} (s) & - b _ {1 2} (s) & - b _ {1 3} (s) & a _ {1 1} (s) & a _ {1 2} (s) \\ - b _ {2 1} (s) & - b _ {2 2} (s) & - b _ {2 3} (s) & a _ {2 1} (s) & a _ {2 2} (s) \end{array} \right]

\times \left[ \begin{array}{c c c} s + 2 & 0 & 0 \\ 0 & s ^ {2} & 0 \\ 0 & 0 & s (s + 2) \\ s & 0 & s (s + 1) \\ 0 & s + 1 & (s + 2) \end{array} \right] = 0
$$

并且，容易求出它的一组解为：

$$b _ {1 1} (s) = s, b _ {1 2} (s) = s + 1, b _ {1 3} (s) = 2 s + 1, a _ {1 1} (s) = s + 2, a _ {1 2} (s) = s ^ {2}b _ {2 1} (s) = s ^ {2} + 2 s, b _ {2 2} (s) = s + 1, b _ {3 3} (s) = s ^ {2} + 4 s + 2, a _ {2 1} (s) = (s + 2) ^ {2},a _ {2 2} (s) = s ^ {2}$$

也即可定出

$$
\bar {A} (s) = \left[ \begin{array}{l l} s + 2 & s ^ {2} \\ (s + 2) ^ {2} & s ^ {2} \end{array} \right], \quad \bar {B} (s) = \left[ \begin{array}{c c c} s & s + 1 & 2 s + 1 \\ s (s + 2) & s + 1 & s ^ {2} + 4 s + 2 \end{array} \right]
$$

考虑到上述 $\vec{A}(s)$ 和 $\vec{B}(s)$ 不是左互质的，因此进一步来求出 $\{\vec{A}(s),\vec{B}(s)\}$ 的最大左公因子 $\vec{R}(s)$

$$
\bar {R} (s) = \left[ \begin{array}{c c} 1 & 1 \\ s + 2 & 1 \end{array} \right]
$$

再计算 $\bar{R}(s)$ 的逆矩阵 $\bar{R}^{-1}(s)$ :

$$
\bar {R} ^ {- 1} (s) = \left[ \begin{array}{c c} - \frac {1}{s + 1} & \frac {1}{s + 1} \\ \frac {s + 2}{s + 1} & - \frac {1}{s + 1} \end{array} \right]
$$

那么就即可求出给定 $N(s)D^{-1}(s)$ 的一个左不可简约 $\mathbf{MFDA}^{-1}(s)B(s)$ ，其中 $A(s)$ 和 $B(s)$ 分别为：

$$
A (s) = \bar {R} ^ {- 1} (s) \bar {A} (s) = \left[ \begin{array}{l l} - \frac {1}{s + 1} & \frac {1}{s + 1} \\ \frac {s + 2}{s + 1} & - \frac {1}{s + 1} \end{array} \right] \left[ \begin{array}{l l} s + 2 & s ^ {2} \\ (s + 2) ^ {2} & s ^ {2} \end{array} \right]

- \left[ \begin{array}{c c} s + 2 & 0 \\ 0 & s ^ {2} \end{array} \right]

B (s) = \bar {R} ^ {- 1} (s) \bar {B} (s) = \left[ \begin{array}{l l} - \frac {1}{s + 1} & \frac {1}{s + 1} \\ \frac {s + 2}{s + 1} & - \frac {1}{s + 1} \end{array} \right] \left[ \begin{array}{c c c} s & s + 1 & 2 s + 1 \\ s (s + 2) & s + 1 & s ^ {2} + 4 s + 2 \end{array} \right]

= \left[ \begin{array}{c c c} s & 0 & s + 1 \\ 0 & s + 1 & s \end{array} \right]
$$
