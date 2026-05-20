因此,系统为有限增益 $L_{2}$ 稳定的,且其 $L_{2}$ 增益小于或等于 $\gamma$ 。该结果给出了另一种计算 $L_{2}$ 增益上界的方法,对应于定理5.4的频域计算方法。注意方程(5.36)存在一个半正定解是 $L_{2}$ 增益小于或等于 $\gamma$ 的充要条件①。

在定理5.5中,假定所有假设条件全局成立。从定理的证明不难看出:如果假设条件只在一个有限定义域D内成立,那么只要方程(5.26)的解保持在D内,不等式(5.30)就成立。

推论5.4 假设在包含原点的定义域 $D \subset R^n$ 内定理5.5的假设条件都成立, 则对任意 $x_0 \in D$ 和任意 $u \in \mathcal{L}_{2e}$ , 方程(5.26)的解对所有 $t \in [0, \tau]$ 都满足 $x(t) \in D$ , 则有

$$\| y _ {\tau} \| _ {\mathcal {L} _ {2}} \leqslant \gamma \| u _ {\tau} \| _ {\mathcal {L} _ {2}} + \sqrt {2 V (x _ {0})}$$

当 $\| x_0\|$ 和 $\sup_{0\leqslant t\leqslant \tau}\| u(t)\|$ 都充分小时， $\dot{x} = f(x)$ 原点的渐近稳定性，保证了方程(5.26)的解 $x(t)$ 保持在原点的某个邻域内。这一结果将在下面的引理中用于证明小信号 $\mathcal{L}_2$ 稳定性。

引理5.1 假设定理5.5的假设条件在包含原点的定义域 $D \subset R^n$ 内成立, $f(x)$ 是连续可微的, 且 $x = 0$ 是 $\dot{x} = f(x)$ 的一个渐近稳定平衡点。那么存在 $k_1 > 0$ , 使得对每个 $x_0 (\| x_0 \| \leqslant k_1)$ , 系统(5.26)\~(5.27)是小信号有限增益 $\mathcal{L}_2$ 稳定的, 其 $\mathcal{L}_2$ 增益小于或等于 $\gamma$ 。

证明: 取 r > 0 且满足 $\{\|x\| \leqslant r\} \subset D$ 。根据定理 4.16（逆李雅普诺夫定理），存在 $r_{0} > 0$ 和连续可微的李雅普诺夫函数 $W(x)$ ，对所有 $\|x\| \leqslant r_{0}$ 及 K 类函数 $\alpha_{1}$ 到 $\alpha_{3}$ ，满足

$$\alpha_ {1} (\| x \|) \leqslant W (x) \leqslant \alpha_ {2} (\| x \|)\frac {\partial W}{\partial x} f (x) \leqslant - \alpha_ {3} (\| x \|)$$

W 沿方程(5.26)轨线的导数满足

$$
\begin{array}{l} \dot {W} (x, u) = \frac {\partial W}{\partial x} f (x, 0) + \frac {\partial W}{\partial x} [ f (x, u) - f (x, 0) ] \leqslant - \alpha_ {3} (\| x \|) + k L \| u \| \\ \leqslant - (1 - \theta) \alpha_ {3} (\| x \|) - \theta \alpha_ {3} (\| x \|) + k L \sup _ {0 \leqslant t \leqslant \tau} \| u (t) \| \\ \leqslant - (1 - \theta) \alpha_ {3} (\| x \|), \forall \| x \| \geqslant \alpha_ {3} ^ {- 1} \left(k L \sup _ {0 \leqslant t \leqslant \tau} \| u (t) \| / \theta\right) \\ \end{array}
$$

其中 $k$ 是 $\| \partial W / \partial x\|$ 的上界， $L$ 是函数 $f$ 关于 $u$ 的利普希茨常数，且 $0 < \theta < 1$ 。与定理5.2的证明相似，我们可应用定理4.18，证明存在一个K类函数 $\beta$ ，一个K类函数 $\gamma_0$ 以及正常数 $k_{1}$ 和 $k_{2}$ ，使得对于任意初始状态 $x_0, \| x_0 \| \leqslant k_1$ ，和任意输入 $u(t), \sup_{0 \leqslant t \leqslant \tau} \| u(t) \| \leqslant k_2$ ，对于所有 $0 \leqslant t \leqslant \tau$ ，解 $x(t)$ 满足

$$\| x (t) \| \leqslant \beta (\| x _ {0} \|, t) + \gamma_ {0} \left(\sup _ {0 \leqslant t \leqslant \tau} \| u (t) \|\right)$$

这样,通过选择足够小的 $k_{1}$ 和 $k_{2}$ ,可以保证对所有 $0 \leqslant t \leqslant \tau$ ,有 $\|x(t)\| \leqslant r$ 。这个引理是根据推论 5.4 得出的。
