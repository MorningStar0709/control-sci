7.10 令 $G(s) = \overline{A}^{-1}(s)\overline{B}(s)$ 是一个可简约 MFD, $L(s) = \gcd\{\overline{A}(s), \overline{B}(s)\}$ , 且取 $A(s) = L^{-1}(s)\overline{A}(s)$ 和 $B(s) = L^{-1}(s)\overline{B}(s)$ , 证明 $A^{-1}(s)B(s)$ 是 $G(s)$ 的一个不

可简约左 MFD。

7.11 定出下列可简约右 MFD 的一个不可简约 MFD:

$$
G (s) = \left[ \begin{array}{c c} s ^ {3} + s ^ {2} + s + 1 & s ^ {2} + s \\ s ^ {2} + 1 & 2 s \end{array} \right] \left[ \begin{array}{c c} s ^ {4} + s ^ {2} & s ^ {3} \\ s ^ {2} + 1 & - s ^ {2} + 2 s \end{array} \right] ^ {- 1}
$$

7.12 令 $\overline{A}^{-1}(s)\overline{B}(s)$ 是一个可简约左 MFD, $V(s)$ 是使 $[\overline{A}(s)\overline{B}(s)]V(s) = [L(s)\mathbf{0}]$ 的一个单模阵, $L(s)$ 为 $\overline{A}(s)$ 和 $\overline{B}(s)$ 的一个 gcld。再表

$$
V ^ {- 1} (s) = U (s) = \left[ \begin{array}{c c} U _ {1 1} (s) & U _ {1 2} (s) \\ \hline U _ {2 1} (s) & U _ {2 2} (s) \\ \hline q & p \end{array} \right] \Bigg \} p
$$

证明： $U_{11}^{-1}(s)U_{12}(s)$ 是 $\overline{A}^{-1}(s)\overline{B}(s)$ 的一个不可简约左MFD。

7.13 给定传递函数矩阵为:

$$
G (s) = \left[ \begin{array}{c c} \frac {s ^ {2}}{(s + 1) ^ {2} (s + 2) ^ {2}} & \frac {s + 1}{(s + 2) ^ {2}} \\ \frac {- s}{(s + 2) ^ {2}} & \frac {1}{(s + 2)} \end{array} \right]
$$

定出其史密斯-麦克米伦形。

7.14 给定系统的状态空间描述为:

$$
\begin{array}{l} \dot {x} = \left[ \begin{array}{l l l} 1 & 2 & 1 \\ 0 & 1 & 0 \\ 0 & 3 & 2 \end{array} \right] x + \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \\ 1 & 1 \end{array} \right] u \\ y = \left[ \begin{array}{l l l} 1 & 0 & 1 \\ 1 & 1 & 1 \end{array} \right] x \\ \end{array}
$$

试求系统传递函数矩阵 $G(s)$ 的一个不可简约的 MFD。

7.15 设有右 MFD $N(s)D^{-1}(s)$ ，其中

$$
D (s) = \left[ \begin{array}{c c} s ^ {2} + 2 s & 1 \\ 3 s ^ {3} + 4 s ^ {2} - 4 s + 3 & 3 s - 2 \end{array} \right]
$$

试论证：对任意的 $2 \times 2$ 多项式矩阵 $N(s), N(s) D^{-1}(s)$ 均必为不可简约的。
