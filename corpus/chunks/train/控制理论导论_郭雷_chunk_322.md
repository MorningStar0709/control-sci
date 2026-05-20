# $\phi$ -混合过程

设 $\{\xi_{k}\}, k=1,2,\cdots$ ，是随机向量列。对任意非负整数 $s\geqslant0$ 及 $h\geqslant0$ 定义 $\sigma$ -代数 $F_{0}^{s}\stackrel{\operatorname{def}}{=} \sigma\{\xi_{k},0\leqslant k\leqslant s\}$ 及 $F_{s+h}^{\infty}\stackrel{\operatorname{def}}{=} \sigma\{\xi_{k},s+h\leqslant k<\infty\}$ ，这里用 $\sigma\{\xi_{k},0\leqslant k\leqslant s\}$ 表示随机向量 $\{\xi_{k},0\leqslant k\leqslant s\}$ 生成的 $\sigma$ -代数。

如果存在确定性数列 $\phi(h) \underset{h \to \infty}{\longrightarrow} 0$ ，使

$$\sup _ {A \in \mathcal {F} _ {s + h} ^ {\infty}, B \in \mathcal {F} _ {0} ^ {s}} | P (A | B) - P (A) | \leqslant \phi (h), \quad \forall s \geqslant 0, \forall h \geqslant 0, \tag {4.3.10}$$

那么称 $\{\xi_k\}$ 为 $\phi$ -混合过程， $\phi(h)$ 叫混合系数.

当 $\{\xi_k\}$ 为相互独立的随机变量序列时，只要取 $\phi(h) \equiv 0, \forall h \geqslant 1$ 式 (4.3.10) 显然成立。所以这时 $\{\xi_k\}$ 是 $\phi-$ 混合过程。因此 $\phi$ 混合过程是对独立序列的一种推广。事实上， $\phi-$ 混合过程包含了相当广的一类过程，下面举两个例子。

例 4.3.5 h-相依过程. 如果对任何 $k \geqslant 0, \xi_{k}$ 和 $\{\xi_{k+h+j}, j = 0, 1, \cdots\}$ 相互独立，那么称 $\{\xi_{k}\}$ 为 h-相依过程. 很明显，h-相依过程是 $\phi$ -混合过程.

例 4.3.6 滑动平均 (MA) 过程. 设 $\{w_{k}\}$ 为相互独立的随机变量序列, $c_{1}, c_{2}, \cdots, c_{r}$ 为常数, 设

$$\xi_ {k} = w _ {k} + c _ {1} w _ {k - 1} + \dots + c _ {r} w _ {k - r},$$

由于 $\xi_{k}$ 和 $\{\xi_{k+r+1+j}, j=0,1,\cdots\}$ 相互独立，所以 $\{\xi_{k}\}$ 是 $(r+1)$ -相依过程，因此是 $\phi$ -混合过程.

$\phi$ -混合过程刻画了过程的一种弱相关性，式 (4.3.10) 表明，当 $h$ 增大时， $\mathcal{F}_0^s$ 和 $\mathcal{F}_{s + h}^\infty$ 两个 $\sigma$ -代数之间的相关性逐渐减弱。这样一类过程经常用来描述实际中出现的一些弱相关过程。

设 $(\phi_k, \mathcal{F}_k)$ 为适应过程，设 $\phi_k$ 是 $r$ 维的。不妨设 $\mathcal{F}_k = \mathcal{F}_0^k$ 。我们证明对任何 $\mathcal{F}_{m + h}^\infty$ 可测的随机变量 $x_{m + h}$ ，只要 $|x_{m + h}| \leqslant 1$ 就有

$$\left| E \left(x _ {m + h} \mid \mathcal {F} _ {m}\right) - E x _ {m + h} \right| \leqslant 2 \phi (k), \tag {4.3.11}$$

这里 $\phi (k)$ 为式(4.3.10)的混合系数.

我们用简单函数逼近 $x_{m + h}$ 来证．先设 $x_{m + h}$ 为示性函数： $x_{m + h} = I_A, A \in \mathcal{F}_{m + h}^{\infty}$ 反设存在 $B \in \mathcal{F}_m, P(B) > 0$ 使得除 $B$ 上的零测集外

$$\left| E \left(x _ {m + h} \mid \mathcal {F} _ {m}\right) - E x _ {m + h} \right| > \phi (k), \quad \forall \omega \in B.$$

用 $\phi$ -混合性式 (4.3.10) 就有

$$
\begin{array}{l} \phi (h) <   \left| \frac {1}{P (B)} \int_ {B} \left(E (x _ {m + h} | \mathcal {F} _ {m}) - P (A)\right) \mathrm{d} P \right| \\ = \left| \frac {1}{P (B)} \left(P (A B) - P (B) P (A)\right) \right| \leqslant \phi (h). \\ \end{array}
$$

所得矛盾证明式 (4.3.11) 对示性函数成立, 并且式 (4.3.11) 右端的系数可取为 1 而不是 2.

由此知对非负的简单函数 $x_{m + h} = \sum_{i}a_{i}I_{A_{i}},0 < a_{i}\leqslant 1$ (因为 $|x_{m + h}|\leqslant 1)$ 同样的不等式也成立．用单调收敛定理知对非负的 $x_{m + h}$ ，只要它是 $\mathcal{F}_{m + h}^{\infty}$ 可测，且 $|x_{m + h}|\leqslant 1,(4.3.11)$ 必成立，并且右端系数可取为1.对于一般的满足条件的 $x_{m + h}$ 可以分解为正部 $x_{m + h}^{+}$ 和负部 $x_{m + h}^{-}:x_{m + h} = x_{m + h}^{+} - x_{m + h}^{-}$ 根据上述结果，$|E(x_{m+h}^{+}|\mathcal{F}_{m})-Ex_{m+h}^{+}|\leqslant\phi(k)$ ，对 $x_{m+h}^{-}$ 同样的不等式也成立，所以式(4.3.11)成立.
