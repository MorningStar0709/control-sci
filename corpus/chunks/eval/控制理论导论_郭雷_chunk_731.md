$$
s (A) = \left\{ \begin{array}{l l} {\sup \big \{\operatorname{Re} \lambda   \big |   \lambda \in \sigma (A) \big \},} & {\quad \text {如果} \sigma (A) \neq \varnothing ,} \\ {- \infty ,} & {\quad \text {如果} \sigma (A) = \varnothing ,} \end{array} \right.
\omega (A) = \inf \left\{\left(\log \| T (t) \|\right) / t \mid t > 0 \right\},
$$

这里我们约定 $\log 0 = -\infty$ . $s(A)$ 和 $\omega(A)$ 通常分别叫做 $A$ 的谱界和由 $A$ 生成的半群 $T(t)$ 增长阶. 从引理10.1.1得到

$$\omega (A) = \inf \big \{\omega \in \mathbb {R} \mid \exists M _ {\omega} \geqslant 1 \text {使得} \| T (t) \| \leqslant M _ {\omega} e ^ {\omega t}, \forall t \geqslant 0 \big \}.$$

当 $X$ 是有穷维空间时，熟知有

$$s (A) = \omega (A). \tag {10.1.6}$$

在无穷维情形，一般来说，等式 (10.1.6) 可能不再成立。从 Hille-Yosida 定理我们看到

$$s (A) \leqslant \omega (A). \tag {10.1.7}$$

实际上，有例子表明 $s(A)$ 可以严格小于 $\omega(A)$ .

注意 $\omega(A)$ 本质上刻划了 $T(t)$ 的增长速度：从 $\omega(A)$ 的定义可知，当 $\omega > \omega(A)$ 时，存在常数 $M \geqslant 1$ 使得

$$\| T (t) \| \leqslant M \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0.$$

因此 $T(t)$ 的指数稳定性等价于条件 $\omega(A) < 0$ . 可见条件 (10.1.6) 是非常重要的, 因为在这种情况下, 只要 $s(A) < 0$ , 即

$$\sup \left\{\operatorname{Re} \lambda \mid \lambda \in \sigma (A) \right\} < 0,$$

则线性系统 (10.1.1) 就是指数稳定的。于是在式 (10.1.6) 成立的情况下， $T(t)$ 的指数稳定性完全由 $A$ 的谱决定。所以条件 (10.1.6) 常常叫做谱确定增长假设。研究在什么条件下谱确定增长假设成立，是一个十分重要的问题。许多作者致力于研究这一问题，得到了丰富的结果。

定理10.1.3 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 是 $T(t)$ 的生成算子。如果 $T(t)$ 对 $t > t_0$ 是可微的，则谱确定增长假设成立。

证明 我们只需证明 $\omega(A) \leqslant s(A)$ . 设 $T(t)$ 满足 $\|T(t)\| \leqslant M\mathrm{e}^{\omega t}, \forall t \geqslant 0$ . 假定相反, 即 $s(A) < \omega(A)$ , 那么存在 $\zeta \in \mathbb{R}$ 使得 $s(A) < \zeta < \omega(A)$ . 根据第5章的定理5.3.18, 从 $T(t)$ 对于 $t > t_0$ 的可微性推出存在3个常数 $a \in \mathbb{R}, b > 0$ 和 $c > 0$ 使得

$$\rho (A) \supset \Sigma = \left\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda \geqslant a - b \log | \operatorname{Im} \lambda | \right\}, \tag {10.1.8}\| R (\lambda ; A) \| \leqslant c | \operatorname{Im} \lambda |, \quad \forall \lambda \in \Sigma , \operatorname{Re} \lambda \leqslant \omega , \tag {10.1.9}$$

并且半群 $T(t)$ 可以表示成

$$T (t) x = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} \mathrm{e} ^ {\lambda t} R (\lambda ; A) x \mathrm{d} \lambda , \quad t > \frac {3}{b}, \tag {10.1.10}$$

这里积分回道 $\Gamma$ 位于 $\Sigma$ 中，由 $\Gamma_{1},\Gamma_{2}$ 和 $\Gamma_{3}$ 三部分组成：
