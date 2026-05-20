$$
\left\{ \begin{array}{l} \dot {x} = A x + B _ {1} w + B _ {2} u, \\ z = C _ {1} x + D _ {1 2} u, \\ \widehat {y} = \left[ \begin{array}{c} x \\ w \end{array} \right]. \end{array} \right. \tag {6.6.21}
$$

动态控制器有反馈结构

$$u = K _ {F I} (s) \widehat {y}, \tag {6.6.22}$$

其中

$$K _ {F I} (s) = K (s) \left[ C _ {1} D _ {1 2} \right],$$

即 $K_{FI}(s)$ 是受控对象 (6.6.21) 所对应的 $H_{\infty}$ 标准设计问题的解。注意到受控对象 (6.6.21), (6.4.1) 具有相同的结构，且满足定理 6.4.1 的条件，所以根据定理 6.4.1 可知，Riccati 方程 (6.6.6) 有半正定解 $X$ 使得 $A + (B_1 B_1^{\mathrm{T}} - B_2 B_2^{\mathrm{T}}) X$ 是稳定阵。

由充分性证明可知，该系统可以表示为如图6.6.1所示，且满足 $T_{vr}(s) < 1$ 。所以Riccati方程(6.6.16)有半正定解 $\Pi$ 使得 $A_{\Pi}$ 是稳定阵。

因为 $H_{\Pi}$ 与相应的Riccati方程解II之间有如下关系：

$$
H _ {\Pi} \left[ \begin{array}{c} I \\ \Pi \end{array} \right] = \left[ \begin{array}{c} I \\ \Pi \end{array} \right] A _ {\Pi},
$$

所以利用前述的 $H_{\Pi}$ 和 $H_T$ 的相似关系，得

$$
H _ {Y} T ^ {- 1} \left[ \begin{array}{c} I \\ \Pi \end{array} \right] = T ^ {- 1} \left[ \begin{array}{c} I \\ \Pi \end{array} \right] A _ {\Pi},

H _ {Y} \left[ \begin{array}{c} I \\ \Pi \widehat {Z} ^ {- 1} \end{array} \right] = \left[ \begin{array}{c} I \\ \Pi \widehat {Z} ^ {- 1} \end{array} \right] \widehat {Z} A _ {\Pi} \widehat {Z} ^ {- 1},
$$

其中 $\hat{Z}^{-1} = I + X\Pi$ 上式表明，与 $H_{Y}$ 对应的Riccati方程(6.6.7）的解为

$$Y = \Pi \widehat {Z} ^ {- 1} = \Pi (I + X \Pi) ^ {- 1} \geqslant 0, \tag {6.6.23}$$

且 $A^{\mathrm{T}} + (C_1^{\mathrm{T}}C_1 - C_2^{\mathrm{T}}C_2)Y = \hat{Z} A_{\Pi}\hat{Z}^{-1}$ 是稳定阵.

最后我们证明上述解 $X$ 和 $Y$ 满足 $\rho(XY) < 1$ . 事实上, 由式 (6.6.23) 可知

$$\Pi = Y (I - X Y) ^ {- 1} \geqslant 0.$$

令 $Y = N^{\mathrm{T}}N$ ，利用逆矩阵引理有

$$\Pi = N ^ {\mathrm{T}} N (I - X N ^ {\mathrm{T}} N) ^ {- 1} = N ^ {\mathrm{T}} (I - N X N ^ {\mathrm{T}}) ^ {- 1} N \geqslant 0. \tag {6.6.24}$$

因此若 $N$ 为非奇异阵，那么上式等价于

$$I - N X N ^ {T} > 0.$$

于是

$$\rho (X Y) = \rho (X N ^ {\mathrm{T}} N) = \rho (N X N ^ {\mathrm{T}}) < 1. \tag {6.6.25}$$

若 $N$ 为奇异阵，则不失一般性可假设

$$
N = \left[ \begin{array}{c c} N _ {1} & 0 \\ 0 & 0 \end{array} \right] S,
$$

其中 $N_{1}$ 和 $S$ 均为非奇异阵，且 $S^{\mathrm{T}}S = I$ 将上式代入式(6.6.24）得

$$
\left[ \begin{array}{c c} N _ {1} ^ {\mathrm{T}} (I - N _ {1} X _ {s} N _ {1} ^ {\mathrm{T}}) ^ {- 1} N _ {1} & 0 \\ 0 & 0 \end{array} \right] S \geqslant 0,
$$

其中 $X_{s}$ 是正定阵 $S^{\mathrm{T}}XS$ 与 $N$ 对应的分块阵．所以 $(I - N_{1}X_{s}N_{1}^{\mathrm{T}})^{-1} > 0,$ 即

$$
I - N X N ^ {\mathrm{T}} = \left[ \begin{array}{c c} (I - N _ {1} X _ {s} N _ {1} ^ {\mathrm{T}}) ^ {- 1} & 0 \\ 0 & 0 \end{array} \right] S \geqslant 0. \tag {6.6.26}
$$

与式 (6.6.25) 同理，得
