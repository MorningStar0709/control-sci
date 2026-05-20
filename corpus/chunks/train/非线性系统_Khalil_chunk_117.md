被积函数是形如 $t^{k-1}\exp(\lambda_{i}t)$ 的各项之和, 其中 $Re\lambda_{i}<0$ , 因此积分存在。矩阵 P 是对称且正定的。正定的证明如下: 假设 P 不是正定的, 那么存在一个向量 $x\neq0$ , 使 $x^{T}Px=0$ 。然而

$$
\begin{array}{l} \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} = 0 \Rightarrow \int_ {0} ^ {\infty} x ^ {\mathrm{T}} \exp (A ^ {\mathrm{T}} t) Q \exp (A t) x d t = 0 \\ \Rightarrow \exp (A t) x \equiv 0, \forall t \geqslant 0 \Rightarrow x = 0 \\ \end{array}
$$

由于 $\exp (At)$ 对于所有 $t$ 都是满秩的，与假设相矛盾，所以 $P$ 是正定的。现在，把式(4.13)代入方程(4.12)的左边，得

$$
\begin{array}{l} P A + A ^ {\mathrm{T}} P = \int_ {0} ^ {\infty} \exp (A ^ {\mathrm{T}} t) Q \exp (A t) A d t + \int_ {0} ^ {\infty} A ^ {\mathrm{T}} \exp (A ^ {\mathrm{T}} t) Q \exp (A t) d t \\ = \int_ {0} ^ {\infty} \frac {d}{d t} \exp (A ^ {\mathrm{T}} t) Q \exp (A t) d t = \left. \exp (A ^ {\mathrm{T}} t) Q \exp (A t) \right| _ {0} ^ {\infty} = - Q \\ \end{array}
$$

该式表明 $P$ 确实是方程(4.12)的一个解。为了证明它是唯一的解，假设存在另一个解 $\tilde{P} \neq P$ ，则

$$(P - \tilde {P}) A + A ^ {\mathrm{T}} (P - \tilde {P}) = 0$$

左乘 $\exp (A^{\mathrm{T}}t)$ ，右乘 $\exp (At)$ ，得

$$0 = \exp (A ^ {\mathrm{T}} t) [ (P - \tilde {P}) A + A ^ {\mathrm{T}} (P - \tilde {P}) ] \exp (A t) = \frac {d}{d t} \left\{\exp (A ^ {\mathrm{T}} t) (P - \tilde {P}) \exp (A t) \right\}$$

因此， $\exp (A^{\mathrm{T}}t)(P - \tilde{P})\exp (At)\equiv$ 常数 $\forall t$

特别地,由于 $\exp(A0)=I$ ,有

$$(P - \tilde {P}) = \exp (A ^ {\mathrm{T}} t) (P - \tilde {P}) \exp (A t) \to 0 \quad \text {当} t \to \infty$$

因此, $\tilde{P}=P_{0}$

对 Q 的正定要求可以放宽, Q 可以为半正定矩阵, 形式为 $Q = C^{T}C$ , 其中矩阵对 $(A, C)$ 是可观测的, 其证明留给读者(见习题 4.22)。

方程(4.12)是线性代数方程,可以通过 $Mx = y$ 的形式重新排列求解,其中, $x$ 和 $y$ 由 $P$ 和 $Q$ 的元素以向量形式叠加来定义,在下一个例题中将进行说明。有多种有效的数值方法可以解这类方程①。

例4.13 设 $A = \left[ \begin{array}{ll}0 & -1\\ 1 & -1 \end{array} \right],Q = \left[ \begin{array}{ll}1 & 0\\ 0 & 1 \end{array} \right],P = \left[ \begin{array}{ll}p_{11} & p_{12}\\ p_{12} & p_{22} \end{array} \right]$

其中根据对称性，有 $p_{12} = p_{21}$ 。李雅普诺夫方程(4.12)可写成

$$
\left[ \begin{array}{r r r} 0 & 2 & 0 \\ - 1 & - 1 & 1 \\ 0 & - 2 & - 2 \end{array} \right] \left[ \begin{array}{l} p _ {1 1} \\ p _ {1 2} \\ p _ {2 2} \end{array} \right] = \left[ \begin{array}{r} - 1 \\ 0 \\ - 1 \end{array} \right]
$$

该方程的唯一解为

$$
\left[ \begin{array}{l} p _ {1 1} \\ p _ {1 2} \\ p _ {2 2} \end{array} \right] = \left[ \begin{array}{c} 1. 5 \\ - 0. 5 \\ 1. 0 \end{array} \right] \Rightarrow P = \left[ \begin{array}{c c} 1. 5 & - 0. 5 \\ - 0. 5 & 1. 0 \end{array} \right]
$$

矩阵 P 是正定的, 因为其前主子式为正(1.5 和 1.25)。因此, A 的所有特征值都在复平面的左半开平面内。
