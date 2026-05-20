由于 $\| \tilde{x}^{(i)}(0) \| \leqslant \omega (\tilde{x}^{(i)}(0)) \leqslant r$ 和 $\| \bar{f}(x) \| \leqslant 1$ ，解 $\tilde{x}^{(i)}(t)$ 属于紧集 $\{\| x \| \leqslant r + T\}$ ，其中 $0 < T < T^*$ ，因此序列 $\omega (\tilde{x}^{(i)}(t))$ 在区间 $t \in [0, T]$ 上有界，且对于 $i$ 是一致的。我们可以从序列 $\tilde{x}^{(i)}(t)$ 中选择一个子序列 $\bar{x}^{(i)}(t)$ ，该子系列在区间 $[0, T]$ 上一致收敛到定义在 $t \in [0, T^*)$ 上的解 $x(t)$ ，其中 $0 < T < T^*$ 。由式 (C.20) 及 $\lim_{i \to \infty} \tau_i = 0$ ，可推出 $\lim_{t \to T^*} \omega (x(t)) = \infty$ 。同样，当 $T^* = \infty$ 时，对于任意 $T > 0$ ，解 $x^{(i)}(t)$ 属于紧集 $\{\| x \| \leqslant r + T\}$ 。因此可选择一个在区间 $[0, T]$ 上一致收敛于解 $x(t)$ 的子序列 $\bar{x}^{(i)}(t)$ ，定义在 $t \in [0, \infty)$ 上，且 $\lim_{t \to T^*} \omega (\bar{x}(t)) = \infty$ 。这样，我们就证明了存在一个常数 $T^*(0 < T^* \leqslant \infty)$ 和一个解 $x(t)$ ，满足 $\omega (x(0)) \leqslant r$ 和 $\lim_{t \to T^*} \omega (x(t)) = \infty$ 。但这是不可能的，因为 $x(0) \in R_A$ 。由此可得，对于任意 $r > 0$ ，存在 $b = b(r) > 0$ ，使得方程 (C.13) 的解对于所有 $t \geqslant 0$ ，满足 $\omega (x(t)) \leqslant b, \omega (x(0)) \leqslant r$ 。常数 $b(r)$ 可选择为 $r$ 的递增函数，考虑到原点是稳定的，故当 $r$ 趋于零时， $b(r)$ 趋于零，而且当 $r$ 趋于无穷时， $b(r)$ 趋于无穷，因为 $b(r) \geqslant r$ 。可以找到一个 $\mathcal{K}_\infty$ 类函数 $\alpha(r)$ ，使得对于所有 $r \geqslant 0$ 满足 $b(r) \leqslant \alpha(r)$ 。这样，方程 (C.13) 的解满足

$$\omega (x (t)) \leqslant \alpha (\omega (x (0))), \forall t \geqslant 0, \forall x (0) \in R _ {A} \tag {C.21}$$

另一方面,给定任意正常数 r 和 $\eta$ , 可以证明存在 $T = T(\eta, r) > 0$ , 使

$$\omega (x (0)) < r \Rightarrow \omega (x (t)) < \eta , \forall t \geqslant T \tag {C.22}$$

否则,就会存在方程(C.13)的一个解序列 $x^{(i)}(t)$ 和常数 $\tau_{i}$ ,使

$$\lim _ {i \rightarrow \infty} \tau_ {i} = \infty , \quad \omega (x ^ {(i)} (0)) \leqslant r, \quad \omega (x ^ {(i)} (\tau_ {i})) \geqslant \eta$$

但是由式(C.21)可知,对于任意正常数 $\delta < \alpha^{-1}(\eta)$ ，方程(C.13)的每个解当 $\omega(x(\tau)) \leqslant \delta$ 时,对于所有 $t \geqslant \tau$ 均满足 $\omega(x(t)) < \eta$ 。因此当 $0 \leqslant t \leqslant \tau_{i}$ 时,有 $\omega(x^{(i)}(t)) \geqslant \delta$ 。由于对于所有 $t \geqslant 0$ 有 $\omega(x^{(i)}(t)) \leqslant \alpha(r)$ ，因此从序列 $x^{(i)}(t)$ 中选择一个子序列 $\tilde{x}^{(i)}(t)$ ，在每个区间 $[0, T]$ 上一致收敛，这里 $0 < T < \infty$ 。函数 $x(t) = \lim_{i \to \infty} \tilde{x}^{(i)}(t)$ 是方程(C.13)的解，对于所有 $t \geqslant 0$ ，有 $\omega(x(t)) \geqslant \delta$ 。然而这是不可能的，因为 $x(0) \in R_{A}$ 。因此 $T(\eta, r)$ 存在，重复证明引理4.5的步骤（有关全局一致渐近稳定性的证明），即可利用式(C.21)和式(C.22)证明存在一个KLC类函数 $\beta(r, s)$ ，有 $\beta(r, 0) \geqslant \alpha(r)$ ，满足式(C.15)。
