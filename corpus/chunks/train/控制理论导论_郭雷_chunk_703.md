其中常数 $\lambda \in (0,1), C > 0, \alpha_{n}$ 和 $\delta_{n}$ 由式 (9.5.24) 所定义，而 $\{\xi_{n}\}$ 是正随机序列，满足

$$\xi_ {n} = O (d _ {n} \log r _ {n}), \tag {9.5.30}$$

而 $d_{n}$ 和 $\pmb{r}_{n}$ 分别由式(9.5.26)和式(9.5.25)给出.

证明 将式 (9.5.23) 代入式 (9.5.20) 得

$$y _ {n + 1} = \varphi_ {n} ^ {\mathrm{T}} \bar {\theta} _ {n} + y _ {n + 1} ^ {*} + w _ {n + 1}. \tag {9.5.31}$$

于是利用式 (9.5.24) 及式 (9.5.26) 得

$$
\begin{array}{l} y _ {n + 1} ^ {2} \leqslant 2 \left(\varphi_ {n} ^ {\mathrm{T}} \hat {\theta} _ {n}\right) ^ {2} + O \left(d _ {n}\right) = 2 \alpha_ {n} \left[ 1 + \varphi_ {n} ^ {\mathrm{T}} P _ {n} \varphi_ {n} \right] + O \left(d _ {n}\right) \\ = 2 \alpha_ {n} \left[ 1 + \varphi_ {n} ^ {\mathrm{T}} P _ {n + 1} \varphi_ {n} + \varphi_ {n} ^ {\mathrm{T}} \left(P _ {n} - P _ {n + 1}\right) \varphi_ {n} \right] + O \left(d _ {n}\right) \\ \leqslant 2 \alpha_ {n} [ 2 + \delta_ {n} \| \varphi_ {n} \| ^ {2} ] + O (d _ {n}) \\ = 2 \alpha_ {n} \delta_ {n} \| \varphi_ {n} \| ^ {2} + O (d _ {n} + \log r _ {n}), \tag {9.5.32} \\ \end{array}
$$

其中用到了性质 $\varphi_{n}^{\mathrm{T}}P_{n + 1}\varphi_{n}\leqslant 1$ 及 $\alpha_{n} = O(\log r_{n})$ （见定理9.2.1(ii)).

利用最小相位条件 (A2) 从系统方程 (9.5.1) 不难知存在 $\lambda \in (0,1)$ 使

$$u _ {n - 1} ^ {2} = O \left(\sum_ {i = 0} ^ {n} \lambda^ {n - i} y _ {i} ^ {2}\right) + O (d _ {n}). \tag {9.5.33}$$

于是

$$\left\| \varphi_ {n} \right\| ^ {2} = \sum_ {i = 0} ^ {p - 1} y _ {n - i} ^ {2} + \sum_ {i = 1} ^ {q - 1} u _ {n - i} ^ {2} = O \left(\sum_ {i = 0} ^ {n} \lambda^ {n - i} y _ {i} ^ {2}\right) + O (d _ {n}).$$

定义

$$L _ {n} = \sum_ {i = 0} ^ {n} \lambda^ {n - i} y _ {i} ^ {2},$$

则显见式 (9.5.28) 满足，于是利用式 (9.5.32) 得

$$y _ {n + 1} ^ {2} \leqslant C \alpha_ {n} \delta_ {n} L _ {n} + O (d _ {n} \log r _ {n}), \tag {9.5.34}$$

其中 $C > 0$ 是某常数．据此及 $L_{n}$ 的定义，有

$$L _ {n + 1} = \lambda L _ {n} + y _ {n + 1} ^ {2} \leqslant (\lambda + C \alpha_ {n} \delta_ {n}) L _ {n} + O (d _ {n} \log r _ {n}).$$

这就是式 (9.5.29), 故引理得证.

引理9.5.2 在引理9.5.1的条件下，下式成立：

$$\left\| \varphi_ {n} \right\| ^ {2} = O (r _ {n} ^ {\epsilon} d _ {n}) \quad \text { a.s. } \quad \forall \epsilon > 0,$$

其中 $r_n$ 和 $d_n$ 分别由式 (9.5.25) 和式 (9.5.26) 定义.

证明 据式 (9.5.29)

$$
\begin{array}{l} L _ {n + 1} \leqslant \prod_ {j = 0} ^ {n} (\lambda + C \alpha_ {j} \delta_ {j}) L _ {0} + \sum_ {i = 0} ^ {n} \prod_ {j = i + 1} ^ {n} (\lambda + C \alpha_ {j} \delta_ {j}) \xi_ {i} \\ = \lambda^ {n + 1} \prod_ {j = 0} ^ {n} (1 + \lambda^ {- 1} C \alpha_ {j} \delta_ {j}) L _ {0} + \sum_ {i = 0} ^ {n} \lambda^ {n - i} \prod_ {j = i + 1} ^ {n} (1 + \lambda^ {- 1} C \alpha_ {j} \delta_ {j}) \xi_ {i}. \tag {9.5.35} \\ \end{array}
$$

为了分析上式中的乘积，首先从
