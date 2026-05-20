# C. 12 证明引理 6.2

充分性: 假设存在 $P = P^{T} > 0$ , L 和 W, 满足式(6.11)到式(6.13)。以 $V(x) = x^{T}Px$ 作为 $\dot{x} = Ax$ 的李雅普诺夫函数, 则式(6.11)表明 $\dot{x} = Ax$ 的原点是稳定的。因此, A 没有 $\operatorname{Re}[s] > 0$ 的特征值。设 $\Phi(s) = (sI - A)^{-1}$ , 有

$$G (s) + G ^ {\mathrm{T}} \left(s ^ {*}\right) = D + D ^ {\mathrm{T}} + C \Phi (s) B + B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} \left(s ^ {*}\right) C ^ {\mathrm{T}}$$

用式(6.12)代换 C, 用式(6.13)代换 $D + D^{T}$ , 则

$$
\begin{array}{l} G (s) + G ^ {\mathrm{T}} \left(s ^ {*}\right) = W ^ {\mathrm{T}} W + \left(B ^ {\mathrm{T}} P + W ^ {\mathrm{T}} L\right) \Phi (s) B + B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} \left(s ^ {*}\right) \left(P B + L ^ {\mathrm{T}} W\right) \\ = W ^ {T} W + W ^ {T} L \Phi (s) B + B ^ {T} \Phi^ {T} \left(s ^ {*}\right) L ^ {T} W \\ + B ^ {T} \Phi^ {T} (s ^ {*}) [ (s + s ^ {*}) P - A ^ {T} P - P A ] \Phi (s) B \\ \end{array}
$$

由式(6.11)，可得

$$
\begin{array}{l} G (s) + G ^ {\mathrm{T}} \left(s ^ {*}\right) = \left[ W ^ {\mathrm{T}} + B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} \left(s ^ {*}\right) L ^ {\mathrm{T}} \right] [ W + L \Phi (s) B ] \tag {C.38} \\ + (s + s ^ {*}) B ^ {T} \Phi^ {T} (s ^ {*}) P \Phi (s) B \\ \end{array}
$$

说明对于所有 $\operatorname{Re}[s] \geqslant 0$ 的 $s$ , 有 $G(s) + G^{\mathrm{T}}(s^{*}) \geqslant 0$ , 也就是说对于 $j\omega$ 不是 $G(s)$ 的元素极点的 $\omega, G(j\omega) + G^{\mathrm{T}}(-j\omega)$ 是半正定的, 上式还说明 $G(s)$ 满足定义6.4的第三个条件。设 $j\omega_{0}$ 是 $G(s)$ 任一元素的 $m$ 阶极点, 那么对于任意 $p$ -维复向量 $x$ , 在以 $j\omega_{0}$ 为圆心, 以任意小 $\rho$ 为半径的半圆弧上, $(x^{*})^{\mathrm{T}}G(s)x$ 的取值为

$$(x ^ {*}) ^ {\mathrm{T}} G (s) x \approx (x ^ {*}) ^ {\mathrm{T}} K _ {0} x \rho^ {- m} e ^ {- j m \theta}, - \frac {\pi}{2} \leqslant \theta \leqslant \frac {\pi}{2}$$

因此 $\rho^m\mathrm{Re}[(x^*)^\mathrm{T}G(s)x]\approx \mathrm{Re}[(x^*)^\mathrm{T}K_0x]\cos m\theta +\mathrm{Im}[(x^*)^\mathrm{T}K_0x]\sin m\theta$

当 $m > 1$ 时，该表达式符号不定，而式(C.38)表示它是非负的。因此， $m$ 必须限制为1。当 $m = 1$ 时，取 $\theta$ 近似为 $-\pi / 2,0$ 和 $\pi / 2$ ，则 $\operatorname{Im}[(x^*)^{\mathrm{T}}K_0x] = 0, \operatorname{Re}[(x^*)^{\mathrm{T}}K_0x] \geqslant 0$ ，故 $K_0$ 为半正定埃尔米特矩阵。

必要性:首先证明一个特例,即 A 为赫尔维茨矩阵时的必要性,然后扩展到一般情况,即 A 在虚轴上有特征值时的必要性。

特例:证明中用到谱因子分解的结果,这里只引用,不加证明。

引理C.5 设 $p \times p$ 正则有理传递函数矩阵 $U(s)$ 为正实赫尔维茨矩阵, 则存在一个 $r \times p$ 的正则有理赫尔维茨传递函数矩阵 $V(s)$ , 使

$$U (s) + U ^ {\mathrm{T}} (- s) = V ^ {\mathrm{T}} (- s) V (s) \tag {C.39}$$

其中 r 是 $U(s) + U^{\mathrm{T}}(-s)$ 的正常秩 (normal rank)，即在域为有理函数时 s 的秩，并且对于 $\operatorname{Re}[s] > 0$ ，秩 $V(s) = r_{\circ}$ 。

证明: 见文献[214]定理 2。
