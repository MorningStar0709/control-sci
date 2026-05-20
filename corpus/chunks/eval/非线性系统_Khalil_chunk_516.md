至此完成了特殊情况下引理的证明。

一般情况: 现在设 A 在虚轴上有特征值, 则存在一个非奇异矩阵 Q, 使得

$$
Q A Q ^ {- 1} = \left[ \begin{array}{c c} {A _ {0}} & {0} \\ {0} & {A _ {n}} \end{array} \right], Q B = \left[ \begin{array}{c} {B _ {0}} \\ {B _ {n}} \end{array} \right], C Q ^ {- 1} = \left[ \begin{array}{c c} {C _ {0}} & {C _ {n}} \end{array} \right]
$$

其中 $A_0$ 有在虚轴上的特征值， $A_n$ 具有负实部的特征值。传递函数 $G(s)$ 可写为 $G(s) = G_0(s) + G_n(s)$ ，其中 $G_0(s) = C_0(sI - A_0)^{-1}B_0$ 的所有极点都在虚轴上， $G_n(s) = C_n(sI - A_n)^{-1}b_n + D$ 的所有极点都在左半开平面，因此 $G_0(s)$ 的极点是单极点，相应的留数矩阵都是半正定埃尔米特矩阵。根据此性质，可选择 $Q$ 使

$$A _ {0} + A _ {0} ^ {\mathrm{T}} = 0, \quad C _ {0} = B _ {0} ^ {\mathrm{T}}$$

为了理解上式,注意到 $G_{0}(s)$ 可写为

$$G _ {0} (s) = \frac {1}{s} F _ {0} + \sum_ {i = 1} ^ {m} \frac {1}{s ^ {2} + \omega_ {i} ^ {2}} \left(F _ {i} s + H _ {i}\right) = \frac {1}{s} F _ {0} + \sum_ {i = 1} ^ {m} \left[ \frac {1}{s - j \omega_ {i}} R _ {i} + \frac {1}{s + j \omega_ {i}} R _ {i} ^ {*} \right] \tag {C.43}$$

其中 $F_{0}$ 是半正定对称矩阵， $R_{i}$ 是半正定埃尔米特矩阵。如果式中每一项都可以找到一个具有性质(C.43)的最小实现，则并联连接将是 $G_{0}(s)$ 的最小实现，具有同样的性质，这可以通过 $(1 / s)F_{0}$ 和 $[1 / (s^{2} + \omega_{i}^{2})](F_{i}s + H_{i})$ 两项分别进行验证。如果 $r_0 = \mathrm{rank} F_0$ ，则 $(1 / s)F_{0}$ 具有维数为 $r_0$ 的最小实现，由 $\{0, N_0, N_0^{\mathrm{T}}\}$ 给出，其中 $F_{0} = N_{0}^{\mathrm{T}}N_{0}$ 。如果 $r_i = \mathrm{rank} R_i$ ，则 $[1 / (s^2 + \omega_i^2)](F_i s + H_i)$ 具有 $2r_i$ 维的最小实现，由下式给出：

$$
A _ {i} = \left[ \begin{array}{c c} 0 & \omega_ {i} I \\ - \omega_ {i} I & 0 \end{array} \right], B _ {i} = \left[ \begin{array}{l} M _ {i 1} \\ M _ {i 2} \end{array} \right], C _ {i} = \left[ \begin{array}{l l} M _ {i 1} ^ {\mathrm{T}} & M _ {i 2} ^ {\mathrm{T}} \end{array} \right]
$$

其中 $M_{i1}=\frac{1}{\sqrt{2}}(N_{i}+N_{i}^{*}),\quad M_{i2}=\frac{j}{\sqrt{2}}(N_{i}-N_{i}^{*}),\quad R_{i}=(N_{i}^{*})^{\mathrm{T}}N_{i}$

显然， $\{A_{i},B_{i},C_{i}\}$ 具有性质(C.43)。

由于 $G_{n}(s)$ 是正实赫尔维茨矩阵，由对特殊情况的证明可知，存在矩阵 $P_{n} = P_{n} > 0, L_{n}$ 和 $W$ ，满足 $P_{n}A_{n} + A_{n}^{\mathrm{T}}P_{n} = -L_{n}^{\mathrm{T}}L_{n}, P_{n}B_{n} = C_{n}^{\mathrm{T}} - L_{n}^{\mathrm{T}}W, W^{\mathrm{T}}W = D + D^{\mathrm{T}}$

容易验证 $P = Q^{T} \left[ \begin{array}{cc} I & 0 \\ 0 & P_{n} \end{array} \right] Q, \quad L = \left[ \begin{array}{cc} 0 & L_{n} \end{array} \right] Q$

和 W 满足方程(6.11)到方程(6.13)。
