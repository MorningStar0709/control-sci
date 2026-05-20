这表明 $T(t)$ 的半群性质成立．条件(1)是显然的．最后，对于任意 $\pmb {x}\in H$ ，我们有

$$
\begin{array}{l} \| T (t) x - x \| ^ {2} = \sum_ {n = 1} ^ {\infty} | e ^ {\lambda_ {n} t} - 1 | ^ {2} | (x, e _ {n}) | ^ {2} \\ = \sum_ {n = 1} ^ {N} \left| e ^ {\lambda_ {n} t} - 1 \right| ^ {2} \left| (x, e _ {n}) \right| ^ {2} + \sum_ {n = N + 1} ^ {\infty} \left| e ^ {\lambda_ {n} t} - 1 \right| ^ {2} \left| (x, e _ {n}) \right| ^ {2} \\ \leqslant \sup _ {1 \leqslant n \leqslant N} | e ^ {\lambda_ {n} t} - 1 | ^ {2} \| x \| ^ {2} + K \sum_ {n = N + 1} ^ {\infty} | (x, e _ {n}) | ^ {2}, \\ \end{array}
$$

其中 $K$ 为一正常数. 但当 $N$ 充分大时, $K \sum_{n=N+1}^{\infty} |(x, e_n)|^2$ 可以任意小, 并且对于每一固定的 $N$ , $\lim_{t \downarrow 0} \sup_{1 \leqslant n \leqslant N} |e^{\lambda_n t} - 1| = 0$ . 因此, $\lim_{t \downarrow 0} \|T(t)x - x\| = 0, \forall x \in H$ . 从而 $T(t)$ 是 $H$ 上一 $C_0$ 半群.

定理5.3.1 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群．那么

(a) $\| T(t)\|$ 在 $[0,\infty)$ 的每一有界子区间上是有界的；

(b) $\forall x \in X, T(t)x$ 对 $t \geqslant 0$ 是强连续的；

(c) 存在常数 $M \geqslant 1$ 和 $\omega \in \mathbb{R}$ 使得

$$\| T (t) \| \leqslant M \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0. \tag {5.3.5}$$

证明 (a) 对于任意固定的 $x \in X$ , 根据 $C_0$ 半群的定义, 存在正常数 $\delta$ 和 $C$ 使得 $\|T(t)x\| \leqslant C$ , $\forall t \in [0, \delta]$ . 今取一任意固定正数 $L$ . 对于任意 $t \in [0, L]$ , 记 $k = [t / \delta](t / \delta$ 的整数部分), 则 $t = k\delta + r$ , 其中 $0 \leqslant k \leqslant k_0 = [L / \delta]$ , $0 \leqslant r < \delta$ . 因此

$$
\begin{array}{l} \| T (t) x \| = \| T (\delta) ^ {k} T (r) x \| \leqslant \| T (\delta) \| ^ {k} \| T (r) x \| \\ \leqslant C \max \left\{1, \| T (\delta) \| ^ {k _ {0}} \right\} <   \infty , \quad \forall t \in [ 0, L ]. \\ \end{array}
$$

从而根据一致有界性定理， $\| T(t)\|$ 在 $[0,L]$ 上有界；

(b) 对于任意固定的 $t_0 > 0$ , 我们有

$$\| T (t _ {0} + \delta) x - T (t _ {0}) x \| \leqslant \| T (t _ {0}) \| \| T (\delta) x - x \|, \quad \forall \delta > 0,$$

和

$$\| T (t _ {0} - \delta) x - T (t _ {0}) x \| \leqslant \| T (t _ {0} - \delta) \| \| T (\delta) x - x \|, \quad \forall \delta \in (0, t _ {0}).$$

于是根据已经得到的结论 (a), $\lim_{\delta \to 0} \| T(t_0 + \delta)x - T(t_0)\| = 0$ ，即 $T(t)$ 在 $t = t_0$ 处是强连续的；

(c), 首先注意 $\| T(t)\|$ 在[0,1]上有界，故依据 $T(t)$ 的半群性质，我们有

$$\| T (t) \| = \| T ([ t ]) T (t - [ t ]) \| \leqslant \| T (1) \| ^ {[ t ]} \| T (t - [ t ]) \|,$$

这里 $[t]$ 表示正数 $t$ 的整数部分。设 $\| T(1)\| = \mathbf{e}^{\omega},\omega \in \mathbb{R}$ 于是若令
