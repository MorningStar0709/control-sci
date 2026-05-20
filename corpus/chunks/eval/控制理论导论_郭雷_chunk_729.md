其中 $n = [t / a]$ 表示 $t / a$ 的整数部分。考虑到 $p(t - na)$ 的有界性和 $\varepsilon > 0$ 的任意性，从上述不等式得到 $\lim_{t \to \infty} p(t) / t = \omega_0$ 。对于 $\omega_0 = -\infty$ 的情形可类似地处理。因此式 (10.1.4) 成立。由于 $\|T(t)\|$ 在任意有界区间上总是有界的，故式 (10.1.5) 直接从式 (10.1.4) 推出。证毕。

定理10.1.1 设 $A$ 和 $T(t)$ 如上．那么如下四种稳定性概念是等价的：

(1) $T(t)$ 是指数渐近稳定的；  
(2) $T(t)$ 是一致渐近稳定的；  
(3) $T(t)$ 是强 $L^p$ -稳定的;  
(4) $T(t)$ 是一致指数渐近稳定的.

证明 $(4) \Longrightarrow (1) \Longrightarrow (3)$ 和 $(4) \Longrightarrow (2)$ 是直接的. 现在设 (2) 成立. 依引理 10.1.1, 我们有 $\omega_0 < 0$ , 并且我们可以选择 $\omega \in \mathbb{R}$ , $\omega_0 < \omega < 0$ , 使得式 (10.1.5) 成立. 这证明了 $(2) \Longrightarrow (4)$ .

剩下证明 (3) $\Longrightarrow$ (4). 于是我们设 (3) 成立, $p \geqslant 1$ . 对于 $x \in X$ , 我们定义映射 $S: X \to L^{p}(0, \infty; X)$ ,

$$(S x) (t) = T (t) x, \quad \forall t \geqslant 0.$$

容易验证 $S$ 是 $X$ 到 $L^p (0,\infty ;X)$ 的一闭线性算子，并且 $\mathcal{D}(S) = X$ 根据闭图像定理， $S$ 是有界的，从而存在一正常数 $c$ 使得

$$\int_ {0} ^ {\infty} \| T (t) x \| ^ {p} \mathrm{d} t \leqslant c \| x \| ^ {p}, \quad \forall x \in X.$$

今选择一正数 $\omega >\omega_0$ 使得式(10.1.5)满足，于是当 $t > 0$ 时，我们有

$$
\begin{array}{l} \frac {1 - \mathrm{e} ^ {- p \omega t}}{p \omega} \| T (t) x \| ^ {p} = \int_ {0} ^ {t} \mathrm{e} ^ {- p \omega (t - s)} \| T (t) x \| ^ {p} \mathrm{d} s \\ \leqslant \int_ {0} ^ {t} \mathrm{e} ^ {p \omega (s - t)} \| T (s) \| ^ {p} \| T (t - s) x \| ^ {p} \mathrm{d} s \\ \leqslant M ^ {p} \int_ {0} ^ {t} \| T (s) x \| ^ {p} d s \leqslant c M ^ {p} \| x \| ^ {p}. \\ \end{array}
$$

因此存在一常数 $\mu > 0$ 使得 $\| T(t) \| \leqslant \mu, \forall t \geqslant 0$ . 于是

$$
\begin{array}{l} t \| T (t) x \| ^ {p} = \int_ {0} ^ {t} \| T (t) x \| ^ {p} d s \\ \leqslant \int_ {0} ^ {t} \| T (s) \| ^ {p} \| T (t - s) x \| ^ {p} d s \\ \leqslant c \mu^ {p} \| x \| ^ {p}, \quad \forall t > 0, x \in X, \\ \end{array}
$$

即 $\| T(t)\| \leqslant \mu (c / t)^{1 / p},\forall t > 0.$ 这表明对于一充分大的 $t_1 > 0,\| T(t_1)\| < 1.$ 这样，根据 $\omega_0$ 的定义，我们有 $\omega_0 < 0,$ 从而(4)成立.证毕.

今后我们将使用术语“一致有界半群”代替“一致稳定半群”。同样地，在所有其余稳定性概念中，我们将省略术语“渐近”。因此我们有下列5种稳定性概念：

(1) 一致或指数稳定性;  
(2) 强稳定性;   
(3) 弱稳定性;   
(4) 一致有界半群;  
(5) 弱 $L^p$ -稳定性.

一个自然的问题是弱 $L^p$ -稳定性是否蕴含指数稳定性？我们将在Hilbert空间情形给出肯定的回答.

直接从稳定性的定义，显然有

$$(1) \Longrightarrow (2) \Longrightarrow (3) \Longrightarrow (4).$$

回忆一下，对于有穷维线性系统来说，上述的前3种稳定性概念是等价的。但是在无穷维空间中，一般来说，它们却未必是比等价的。下面举例说明。

例10.1.1 设 $\ell^2$ 表示所有平方可和数列组成的Hilbert空间，在 $\ell^2$ 中定义
