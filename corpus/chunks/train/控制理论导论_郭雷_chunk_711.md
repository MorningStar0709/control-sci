于是利用式(9.5.51)，式(9.5.65)及 $\| \tilde{\theta}_{n + 1}\| ^2 = O(\log r_n)$ 知对任何 $k\leqslant \tau_{n},\forall n\geqslant 1$

$$
\begin{array}{l} u _ {k} ^ {2} = \frac {1}{[ \tilde {b} _ {1} (\tau_ {n} + 1) ] ^ {2}} \{\tilde {b} _ {1} (\tau_ {n} + 1) u _ {k} \} ^ {2} \\ = \frac {1}{\left[ \tilde {b} _ {1} \left(\tau_ {n} + 1\right) \right] ^ {2}} \left\{\left[ \varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {\tau_ {n} + 1} - \tilde {b} _ {1} \left(\tau_ {n} + 1\right) u _ {k} \right] - \varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {\tau_ {n} + 1} \right\} ^ {2} \\ \leqslant \frac {2}{[ \tilde {b} _ {1} (\tau_ {n} + 1) ] ^ {2}} \left\{\left| \varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {\tau_ {n} + 1} - \tilde {b} _ {1} (\tau_ {n} + 1) u _ {k} \right| ^ {2} + \left(\varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {\tau_ {n} + 1}\right) ^ {2} \right\} \\ = O \left(\left(\log r _ {\tau_ {n}}\right) \left[ \left\| \varphi_ {k} \right\| ^ {2} - u _ {k} ^ {2} \right]\right) + O \left(\log r _ {\tau_ {n}}\right) \\ = O ((\log r _ {\tau_ {n}}) L _ {k}) + O (d _ {\tau_ {n}} \log r _ {\tau_ {n}}), \\ \end{array}
$$

其中 $L_{k} \stackrel{\mathrm{def}}{=} \sum_{i=0}^{k} \lambda^{k-i} y_{i}^{2}$ . 将上式与式 (9.5.51) 相结合得 $\forall k \leqslant \tau_{n}$

$$\left\| \varphi_ {k} \right\| ^ {2} = O ((\log r _ {\tau_ {n}}) L _ {k}) + O (d _ {\tau_ {n}} \log r _ {\tau_ {n}}).$$

再将此式代入式 (9.5.50) 得 $\forall k \leqslant \tau_{n}$

$$y _ {k + 1} ^ {2} = O \left(\alpha_ {k} \delta_ {k} \left(\log r _ {\tau_ {n}}\right) L _ {k}\right) + O \left(d _ {\tau_ {n}} \log r _ {\tau_ {n}}\right).$$

由此及 $L_{k}$ 的定义知存在常数 $C > 0$ ，使 $\forall k\leqslant \tau_n$

$$L _ {k + 1} \leqslant (\lambda + C \alpha_ {k} \delta_ {k} \log r _ {\tau_ {n}}) L _ {k} + O (d _ {\tau_ {n}} \log^ {2} r _ {\tau_ {n}}).$$

类似于引理9.5.4的证明可得

$$\sup _ {k \leqslant \tau_ {n}} \| \varphi_ {k} \| ^ {2} = O (r _ {\tau_ {n}} ^ {\epsilon} d _ {\tau_ {n}}), \quad \forall \epsilon > 0,$$

故式 (9.5.63) 成立，进而，据此及定理 9.2.1 从式 (9.5.49) 不难推出式 (9.5.64). 证毕.

在以下的讨论中，每当我们说 $u_{n}$ 由式(9.5.15)定义时，自然假定

$$P (b _ {1} (n) \neq 0, \forall n) = 1, \tag {9.5.67}$$

此处 $b_{1}(n)$ 与那里的 $b_{1n}$ 相同（如此改写是为了下面书写方便）.

条件 (9.5.67) 可通过对噪声附加条件来保证。事实上，若 $\{w_{n}\}$ 的所有有穷维分布关于 Lebesgue 测度是绝对连续的，则条件 (9.5.67) 必成立（见本节习题）。

定义

$$D _ {1} = \left\{\omega : \liminf _ {n \to \infty} \sqrt {\log r _ {n - 1}} \cdot | b _ {1} (n) | \neq 0 \right\}. \tag {9.5.68}$$

对任何常数 $a \in (0, |b_1|)$ , 定义 $\{\tau_n\}$ 如下:
