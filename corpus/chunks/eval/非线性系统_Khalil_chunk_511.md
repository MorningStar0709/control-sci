$$\sigma_ {\min} \left[ G (j \omega - \mu) + G ^ {T} (- j \omega - \mu) \right] \geqslant \sigma_ {2} - \mu k _ {0}, \forall | \omega | \leqslant \omega_ {3} \tag {C.37}$$

选择 $\mu < \min \{\sigma_1 / k_1, \sigma_2 / k_0\}$ ，保证对于所有 $\omega \in R, G(j\omega - \mu) + G^{\mathrm{T}}(-j\omega - \mu)$ 是正定的。

必要性: 假设 $G(s)$ 是严格的正实矩阵, 则存在 $\mu > 0$ , 使得 $G(s - \mu)$ 也是正实矩阵, 这就是说 $G(s)$ 是赫尔维茨正实矩阵, 从而

$$G (j \omega) + G ^ {T} (- j \omega) \geqslant 0, \forall \omega \in R$$

故 $G(\infty) + G^{\mathrm{T}}(\infty)\geqslant 0$

设 $\{A,B,C,D\}$ 是 $G(s)$ 的最小实现。根据引理6.3,存在P,L,W和 $\varepsilon$ ,满足式(6.14)到式(6.16)。
设 $\Phi(s)=(sI-A)^{-1}$ ，有

$$G (s) + G ^ {\mathrm{T}} (- s) = D + D ^ {\mathrm{T}} + C \Phi (s) B + B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} (- s) C ^ {\mathrm{T}}$$

用式(6.15)代换 C, 用式(6.16)代换 $D + D^{T}$ , 则有

$$
\begin{array}{l} G (s) + G ^ {\mathrm{T}} (- s) = W ^ {\mathrm{T}} W + \left(B ^ {\mathrm{T}} P + W ^ {\mathrm{T}} L\right) \Phi (s) B + B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} (- s) \left(P B + L ^ {\mathrm{T}} W\right) \\ = W ^ {T} W + W ^ {T} L \Phi (s) B + B ^ {T} \Phi^ {T} (- s) L ^ {T} W \\ + B ^ {T} \Phi^ {T} (- s) \left[ - A ^ {T} P - P A \right] \Phi (s) B \\ \end{array}
$$

利用式(6.14)，可得

$$G (s) + G ^ {\mathrm{T}} (- s) = \left[ W ^ {\mathrm{T}} + B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} (- s) L ^ {\mathrm{T}} \right] [ W + L \Phi (s) B ] + \varepsilon B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} (- s) P \Phi (s) B$$

由该方程可知,对于所有 $\omega\in R,G(j\omega)+G^{\mathrm{T}}(-j\omega)$ 是正定的,因为如果它在某一频率 $\omega$ 上是奇异的,就会存在 $x\in C^{p},x\neq0$ ,使得

$$\left(x ^ {*}\right) ^ {\mathrm{T}} \left[ G (j \omega) + G ^ {\mathrm{T}} (- j \omega) \right] x = 0 \Rightarrow \left(x ^ {*}\right) ^ {\mathrm{T}} B ^ {\mathrm{T}} \Phi^ {\mathrm{T}} (- j \omega) P \Phi (j \omega) B x = 0 \Rightarrow B x = 0$$

以及

$$\left(x ^ {*}\right) ^ {\mathrm{T}} \left[ G (j \omega) + G ^ {\mathrm{T}} (- j \omega) \right] x = 0 \Rightarrow \left(x ^ {*}\right) ^ {\mathrm{T}} \left[ W + L \Phi (- j \omega) B \right] ^ {\mathrm{T}} \left[ W + L \Phi (j \omega) B \right] x = 0$$

由于 Bx=0，上述方程表示 Wx=0，因此有

$$(x ^ {*}) ^ {\mathrm{T}} [ G (s) + G ^ {\mathrm{T}} (- s) ] x \equiv 0, \forall s$$

这与假设 $\det\left[G(s)+G^{\mathrm{T}}(-s)\right]$ 不恒等于零相矛盾。现在如果 $G(\infty)+G^{\mathrm{T}}(\infty)$ 是正定的，证明就此完成。否则，设 M 是任意 $p\times(p-q)$ 阶满秩矩阵，满足 $M^{\mathrm{T}}(D+D^{\mathrm{T}})M=M^{\mathrm{T}}W^{\mathrm{T}}WM=0$ ，则 WM=0，且
