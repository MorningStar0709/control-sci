# 4.4 比较函数

当从自治系统过渡到非自治系统时,会有一定的困难,因为初始状态为 $x(t_{0}) = x_{0}$ 的非自治系统 $\dot{x} = f(t, x)$ , 其解与 t 和 $t_{0}$ 都有关系。为了处理这一新问题, 我们将改进稳定性和渐近稳定性的定义, 使它们在初始时刻 $t_{0}$ 一致成立。改进定义 4.1 可达到要求的一致性, 这说明存在更明晰的定义, 这些定义用到了特殊的比较函数, 即 K 类函数和 KL 类函数。

定义4.2 如果连续函数 $\alpha: [0, a) \to [0, \infty)$ 严格递增，且 $\alpha(0) = 0$ ，则 $\alpha$ 属于 $\mathcal{K}$ 类函数。如果 $a = \infty$ ，且当 $r$ 趋于无穷时 $\alpha(r)$ 趋于无穷，则 $\alpha$ 属于 $\mathcal{K}_{\infty}$ 类函数。

定义4.3 对于连续函数 $\beta: [0, a) \times [0, \infty) \to [0, \infty)$ ，如果对于每个固定的 $s$ ，映射 $\beta(r, s)$ 都是关于 $r$ 的 $\kappa$ 类函数，并且对于每个固定的 $r$ ，映射 $\beta(r, s)$ 是 $s$ 的递减函数，且当 $s$ 趋于无穷时 $\beta(r, s)$ 趋于零，则 $\beta$ 属于 $\kappa\mathcal{L}$ 类函数。

例4.16

\- 函数 $\alpha(r) = \arctan(r)$ 是严格递增的, 因为 $\alpha'(r) = 1/(1 + r^2) > 0$ , 因此 $r$ 属于 $\mathcal{K}$ 类函数。但它不属于 $\mathcal{K}_{\infty}$ 类函数, 因为 $\lim_{r \to \infty} \alpha(r) = \pi/2 < \infty$ 。

\- 函数 $\alpha(r) = r^c$ 对于任意正实数 $c$ 都是严格递增的, 因为 $\alpha'(r) = cr^{c-1} > 0$ , 且 $\lim_{r \to \infty} \alpha(r) = \infty$ , 因此 $\alpha(r)$ 属于 $\mathcal{K}_{\infty}$ 类函数。

\- 函数 $\alpha(r) = \min\{r, r^2\}$ 连续，严格递增，且 $\lim_{r \to \infty} \alpha(r) = \infty$ 。因此， $\alpha(r)$ 属于 $\mathcal{K}_{\infty}$ 类函数。注意，在 $r = 1$ 处 $\alpha(r)$ 不是连续可微的。 $\mathcal{K}$ 类函数不要求连续可微性。

\- 函数 $\beta(r, s) = r / (ksr + 1)$ , 对于任意正实数 $k$ , 对 $r$ 都是严格递增的。因为

$$
\begin{array}{r l} & {\frac {\partial \beta}{\partial r} = \frac {1}{(k s r + 1) ^ {2}} > 0} \\ & {\text {但对} s \text {是严格递减的}, \text {因为}} \\ & {\frac {\partial \beta}{\partial s} = \frac {- k r ^ {2}}{(k s r + 1) ^ {2}} <   0} \end{array}
$$

而且当 s 趋于无穷时 $\beta(r,s)$ 趋于零，因此 $\beta(r,s)$ 属于 KL 类函数。

\- 函数 $\beta (r,s) = r^{c}e^{-s}$ 对于任意正实数 $c$ ，都属于KL类函数。

下一引理论述了K类函数和KL类函数的一些常用性质,这些性质将在后面用到。引理的证明留给读者(见习题4.34)。

引理4.2 设 $\alpha_{1}$ 和 $\alpha_{2}$ 是 $[0, a)$ 上的 $\kappa$ 类函数, $\alpha_{3}$ 和 $\alpha_{4}$ 是 $\kappa_{\infty}$ 类函数, $\beta$ 是 $\kappa L$ 类函数, $\alpha_{i}^{-1}$ 表示 $\alpha_{i}$ 的反函数, 则

- $\alpha_{1}^{-1}$ 在 $[0, \alpha_{1}(a))$ 上有定义，且属于 $\kappa$ 类函数。  
- $\alpha_{3}^{-1}$ 在 $[0, \infty)$ 上有定义，且属于 $\kappa_{\infty}$ 类函数。  
- $\alpha_{1} \circ \alpha_{2}$ 属于 $K$ 类函数。  
- $\alpha_{3} \circ \alpha_{4}$ 属于 $K_{\infty}$ 类函数。  
- $\sigma(r,s)=\alpha_{1}(\beta(\alpha_{2}(r),s))$ 属于KL类函数。

下面的两个引理把K类函数和KL类函数引入了李雅普诺夫分析法。

引理4.3 设 $V: D \to R$ 是定义域为 $D \subset R^n$ 且包含原点的连续正定函数, 并设对于某个 $r > 0$ 有 $B_r \subset D$ , 则对于所有 $x \in B_r$ , 存在定义在 $[0, r]$ 上的 $\mathcal{K}$ 类函数 $\alpha_1$ 和 $\alpha_2$ , 满足
