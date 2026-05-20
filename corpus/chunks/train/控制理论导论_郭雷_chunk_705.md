$$\sum_ {i = 0} ^ {n} y _ {i} ^ {2} = O (n) + O \left(r _ {n} ^ {\epsilon} d _ {n}\right), \quad \forall \epsilon > 0.$$

据此利用条件 (A2) 从式 (9.5.1) 可得

$$\sum_ {i = 0} ^ {n} u _ {i} ^ {2} = O (n) + O \left(r _ {n} ^ {\epsilon} d _ {n}\right), \quad \forall \epsilon > 0.$$

因此，由上两式得 $\forall \epsilon > 0$

$$
\begin{array}{l} r _ {n} = 1 + \sum_ {i = 0} ^ {n} \| \varphi_ {i} \| ^ {2} = O (n) + O \left(r _ {n} ^ {\epsilon} d _ {n}\right) \\ = O (n) + O \left(r _ {n} ^ {\epsilon} n ^ {\delta}\right), \quad \forall \delta \in \left(\frac {2}{\beta}, 1\right). \\ \end{array}
$$

取 $\epsilon$ 充分小使 $\epsilon +\delta <  1$ ，可得

$$\frac {r _ {n}}{n} = O (1) + O \left(\left[ \frac {r _ {n}}{n} \right] ^ {\epsilon} \cdot \frac {1}{n ^ {1 - \epsilon - \delta}}\right) = O (1) + o \left(\left[ \frac {r _ {n}}{n} \right] ^ {\epsilon}\right)$$

由此看出式 (9.5.41) 必成立. 证毕

上述定理9.5.1中证明了 $R_{n}$ 的增长速度不超过 $O(n^{\epsilon}d_{n}), \forall \epsilon > 0$ , 但 $R_{n}$ 的精确增长速度到底有多大? 这一问题与STR的收敛速度密切相关. 下面将通过STR的对数律来回答此问题.

定理 9.5.2 $^{[16]}$ 在定理 9.5.1 的条件下, 若 $B(z)$ 与 $A(z)-1$ 互质, $|a_{p}|+|b_{q}|\neq0$ , 则对闭环系统下列对数律成立:

$$\lim _ {n \rightarrow \infty} \frac {R _ {n}}{\log n} = (p + q - 1) \sigma_ {w} ^ {2} \quad \text { a.s. }$$

且LS估计有重对数律的收敛速度

$$\| \theta_ {n} - \theta \| = O \left(\sqrt {\frac {\log \log n}{n}}\right) \quad \text { a.s. }$$

其中 $R_{n}$ 由(9.5.16)定义， $\sigma_w^2\stackrel {\mathrm{def}}{=}E[w_{n + 1}^2 |\mathcal{F}_n] > 0.$

下面考虑一般情形，即式(9.5.1)的高频增益 $b_{1}$ 也是未知的。此时，未知参数 $\theta$ 及回归向量 $\varphi_{n}$ 应分别由式(9.5.2)和式(9.5.3)所定义，而对 $\theta$ 的估计由LS算法(9.5.11)\~(9.5.13)给出。我们将沿用式(9.5.24)和式(9.5.25)中引入的记号 $\alpha_{k},\delta_{k},\tau_{k}$ 和 $\tilde{\theta}_{k}$ 。

自然地，此时STR应由式(9.5.14)或式(9.5.15)给出。但如此一来，遇到的第一个问题就是 $u_{n}$ 可能有时无法定义，这是因为集合 $\{b_{1n} = 0\}$ 的概率可能为正的，除非对噪声 $\{w_n\}$ 的分布作进一步的假定。若我们不想对噪声附加更多的限制，克服此困难的一个自然而简单的方法是对 $b_{1n}$ 做微小的修正。例如，可以用下式定义的 $b_{1n}$ ：

$$
\hat {b} _ {1 n} = \left\{ \begin{array}{l l} b _ {1 n}, & \text {若} | b _ {1 n} | \geqslant \frac {1}{\sqrt {\log r _ {n - 1}}} \\ b _ {1 n} + \frac {\mathrm{sgn} (b _ {1 n})}{\sqrt {\log r _ {n - 1}}}, & \text {若} | b _ {1 n} | <   \frac {1}{\sqrt {\log r _ {n - 1}}} \end{array} \right. \tag {9.5.42}
$$

来代替式 (9.5.15) 中的分母 $b_{1n}$ 而得到

$$
\begin{array}{l} u _ {n} = \frac {1}{\hat {b} _ {1 n}} \left\{a _ {1 n} y _ {n} + \dots + a _ {p n} y _ {n - p + 1} - b _ {2 n} u _ {n - 1} \right. \\ - \dots - b _ {q n} u _ {n - q + 1} + y _ {n + 1} ^ {*} \}, \tag {9.5.43} \\ \end{array}
$$

其中 $\operatorname{sgn}(\cdot)$ 是符号函数定义为
