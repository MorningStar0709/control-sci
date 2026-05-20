$$\theta_ {n + 1} = \theta_ {n} + a _ {n} P _ {n} \varphi_ {n} (y _ {n + 1} - \varphi_ {n} ^ {\mathrm{T}} \theta_ {n}), \tag {9.5.11}P _ {n + 1} = P _ {n} - a _ {n} P _ {n} \varphi_ {n} \varphi_ {n} ^ {\mathrm{T}} P _ {n}, \tag {9.5.12}a _ {n} = \left(1 + \varphi_ {n} ^ {\mathrm{T}} P _ {n} \varphi_ {n}\right) ^ {- 1}, \tag {9.5.13}$$

其中初值 $\theta_0$ 及 $P_0 > 0$ 任取.

根据“必然等价原则”(忽略估计值 $\theta_{n}$ 之方差的影响), 将式 (9.5.8) 中的 $\theta$ 用上述 $\theta_{n}$ 所取代得到如下 LS 型自校正调节器 (STR):

$$\theta_ {n} ^ {\mathrm{T}} \varphi_ {n} = y _ {n + 1} ^ {*} \tag {9.5.14}$$

或

$$
\begin{array}{l} u _ {n} = \frac {1}{b _ {1 n}} \left\{a _ {1 n} y _ {n} + \dots + a _ {p n} y _ {n - p + 1} \right. \\ - b _ {2 n} u _ {n - 1} - \dots - b _ {q n} u _ {n - q + 1} + y _ {n + 1} ^ {*} \}, \tag {(9.5.15)} \\ \end{array}
$$

其中 $a_{in}, b_{jn}$ 为 $\theta_n$ 的分量

$$\theta_ {n} \stackrel {\text { def }} {=} [ - a _ {1 n} \dots - a _ {p n}, b _ {1 n} \dots b _ {q n} ] ^ {\mathrm{T}}.$$

注意到理想情形下的闭环方程为式 (9.5.10), 我们自然期望在适应控制 (9.5.14) 作用下, 闭环方程满足

$$y _ {n} - y _ {n} ^ {*} - w _ {n} \approx 0, \quad \forall n.$$

通常我们期望如下定义的 $n$ 步“闭环跟踪误差”的积累：

$$R _ {n} \stackrel {\text { def }} {=} \sum_ {i = 1} ^ {n} (y _ {i} - y _ {i} ^ {*} - w _ {i}) ^ {2} \tag {9.5.16}$$

满足

$$R _ {n} = o (n) \quad \text { a.s. } \tag {9.5.17}$$

直观地讲，式(9.5.17)意味着误差“ $y_{n} - y_{n}^{*} - w_{n}$ ”在平均意义下趋于零.

利用 (A1) 容易证明

$$R _ {n} = o (n) \Leftrightarrow J _ {n} \underset {n \to \infty} {\longrightarrow} \sigma_ {w} ^ {2} \qquad \mathrm{a.s.}$$

其中 $J_{n}$ 由式(9.5.5)给出，而 $\sigma_w^2$ 定义为 $\lim_{n\to \infty}\frac{1}{n}\sum_{i = 1}^{n}w_i^2$ (假定极限存在).

因此，STR(9.5.14) 最优的充分必要条件是式 (9.5.17) 成立。一个自然的问题是，对 LS 型 STR, $R_n$ 是否一定满足式 (9.5.17)? 进一步， $R_n$ 的增加速度到底有多快？后一问题实质上是 STR 的控制精度或收敛速度问题。我们将在下面讨论这两个问题。

我们先讨论一个简单而又经典的情形.

对系统 (9.5.1), 注意到

$$\lim _ {z \rightarrow \infty} \frac {B (z ^ {- 1})}{A (z ^ {- 1})} = b _ {1},$$

因此 $B(z)$ 的首项系数 $b_{1}$ 通常称为“高频增益”。当 $b_{1}$ 已知时，仅需估计下列参数向量：

$$\theta = \left[ - a _ {1} \dots - a _ {p} b _ {2} \dots b _ {q} \right] ^ {\mathrm{T}}. \tag {9.5.18}$$

相应地，此时回归向量 $\varphi_{n}$ 应定义为

$$\varphi_ {n} = \left[ y _ {n} \dots y _ {n - p + 1}, u _ {n - 1} \dots u _ {n - q + 1} \right] ^ {\mathrm{T}}. \tag {9.5.19}$$

而系统 (9.5.1) 可写成如下回归形式：

$$y _ {n + 1} - b _ {1} u _ {n} = \theta^ {\mathrm{T}} \varphi_ {n} + w _ {n + 1}. \tag {9.5.20}$$

对上式中 $\theta$ 的LS估计算法为
