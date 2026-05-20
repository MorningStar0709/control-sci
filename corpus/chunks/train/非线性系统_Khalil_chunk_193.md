证明: 假设存在 $P = P^{T} > 0, L, W$ 和 $\varepsilon > 0$ 满足式(6.14)到式(6.16)，令 $\mu = \varepsilon / 2$ ，回顾 $G(s - \mu) = C(sI - \mu I - A)^{-1}B + D$ 。由式(6.14)，有

$$P (A + \mu I) + (A + \mu I) ^ {\mathrm{T}} P = - L ^ {\mathrm{T}} L \tag {6.17}$$

由引理6.2可得 $G(s - \mu)$ 是正实的，因此 $G(s)$ 是严格正实的。另一方面，假设 $G(s)$ 是严格正实的,则存在 $\mu>0$ , 使 $G(s-\mu)$ 为正实的。由引理 6.2 可得存在矩阵 $P=P^{T}>0$ , L 和 W, 满足式 (6.15) 到式 (6.17)。令 $\varepsilon=2\mu$ , 即证明 P, L 和 W 满足式 (6.14) 到式 (6.16)。☐

引理6.4 线性时不变最小实现为 $\dot{x} = Ax + Bu$

$$y = C x + D uG (s) = C (s I - A) ^ {- 1} B + D,$$

- 如果 $G(s)$ 是正实的, 则系统是无源的;  
- 如果 $G(s)$ 是严格正实的, 则系统是严格无源的。

证明: 分别应用引理 6.2 和引理 6.3, 并用 $V(x) = (1/2)x^{\mathrm{T}}Px$ 作为存储函数。

$$
\begin{array}{l} u ^ {\mathrm{T}} y - \frac {\partial V}{\partial x} (A x + B u) = u ^ {\mathrm{T}} (C x + D u) - x ^ {\mathrm{T}} P (A x + B u) \\ = u ^ {\mathrm{T}} C x + \frac {1}{2} u ^ {\mathrm{T}} (D + D ^ {\mathrm{T}}) u - \frac {1}{2} x ^ {\mathrm{T}} (P A + A ^ {\mathrm{T}} P) x - x ^ {\mathrm{T}} P B u \\ = u ^ {\mathrm{T}} \left(B ^ {\mathrm{T}} P + W ^ {\mathrm{T}} L\right) x + \frac {1}{2} u ^ {\mathrm{T}} W ^ {\mathrm{T}} W u \\ + \frac {1}{2} x ^ {\mathrm{T}} L ^ {\mathrm{T}} L x + \frac {1}{2} \varepsilon x ^ {\mathrm{T}} P x - x ^ {\mathrm{T}} P B u \\ = \frac {1}{2} (L x + W u) ^ {\mathrm{T}} (L x + W u) + \frac {1}{2} \varepsilon x ^ {\mathrm{T}} P x \geqslant \frac {1}{2} \varepsilon x ^ {\mathrm{T}} P x \\ \end{array}
$$

在引理6.2的情况下， $\varepsilon=0$ ，可推出系统是无源的。在引理6.3的情况下， $\varepsilon>0$ ，可推出系统是严格无源的。
