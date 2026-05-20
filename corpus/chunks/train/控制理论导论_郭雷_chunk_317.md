# 平稳性、遍历性

下面讨论离散时间的过程，但对连续时间都有相应的结果。设 $\{\xi_k\}$ 为 $m$ 维随机向量列。若 $E\xi_{k} = \mu$ 不依赖时间 $k$ ，并且相关函数 $R(k,j) \stackrel{\mathrm{def}}{=} E\xi_{k}\xi_{j}^{*} = R(k - j)$ 只依赖于时间差 $k - j$ ，那么 $\{\xi_k\}$ 叫宽平稳过程。这里“\*”表示转置并取复共轭。

例4.3.1 设 $\{\xi_k\}$ 为实iid序列， $E\xi_{k} = \mu ,E\xi_{k}\xi_{k}^{\mathrm{T}} = R,$ 那么

$$
E \xi_ {k} \xi_ {j} ^ {\mathrm{T}} = \left\{ \begin{array}{l l} {{\mu \mu^ {\mathrm{T}},}} & {{\quad \text {若} | k - j | > 0,}} \\ {{R,}} & {{\quad \text {若} k - j = 0,}} \end{array} \right.
$$

所以 $\{\xi_{k}\}$ 是宽平稳过程.

例 4.3.2 设 $\{w_{k}\}$ 是零均值、不相关的随机序列： $Ew_{k}=0,\forall k,E|w_{k}|^{2}=1,$ $Ew_{k}w_{j}^{*}=0,\forall k\neq j,-\infty<k<\infty,-\infty<j<\infty.$

设 $c_{k}$ 为复数列； $\sum_{k = -\infty}^{\infty}|c_k|^2 < \infty$ ，那么 $\xi_{k} = \sum_{j = -\infty}^{\infty}c_{k - j}w_{j}$ 为宽平稳过程．这里求和到无穷是指均方意义下的极限．这是因为

$$E \xi_ {k} \xi_ {s} ^ {*} = E \left(\sum_ {j = - \infty} ^ {\infty} c _ {k - j} w _ {j}\right) \left(\sum_ {l = - \infty} ^ {\infty} c _ {s - l} w _ {l}\right) ^ {*} = \sum_ {j = - \infty} ^ {\infty} c _ {k - s + j} c _ {j} ^ {*}.$$

我们引进直交增量过程的概念．设对任意 $t \in (-\infty, \infty)$ , $E \| \eta_t \|^2 < \infty$ ，并对任意 $t_2 > s_2 \geqslant t_1 > s_1$ ，有

$$E \left(\eta_ {t _ {2}} - \eta_ {s _ {2}}\right) \left(\eta_ {t _ {1}} - \eta_ {s _ {1}}\right) ^ {*} = 0,$$

那么 $\eta_{t}$ 叫正交增量过程.

和直交增量过程对应有函数阵 $F(t)$

$$E (\eta_ {t} - \eta_ {s}) (\eta_ {t} - \eta_ {s}) ^ {*} \stackrel {\text { def }} {=} F (t) - F (s).$$

$F(t)$ 叫谱函数.

设 $f(t)$ 为确定性函数，如果

$$\int_ {- \infty} ^ {\infty} \| f (t) \| ^ {2} \mathrm{d} F (t) < \infty ,$$

则称 $f \in L_2(\mathrm{d}F)$ .

设 $f(t)$ 为阶梯函数

$$
f (t) = \sum_ {i = 1} ^ {n - 1} c _ {i} I _ {(t _ {i}, t _ {i + 1})} (t), \quad I _ {(t _ {i}, t _ {i + 1} ]} (t) = \left\{ \begin{array}{l l} 1, & \text {若} t \in (t _ {i}, t _ {i + 1} ], \\ 0, & \text {其他}, \end{array} \right. t _ {1} <   t _ {2} <   \dots <   t _ {n},
$$

那么可定义随机积分

$$\int_ {- \infty} ^ {\infty} f (t) \mathrm{d} \eta_ {t} \stackrel {\text { def }} {=} \sum_ {i = 1} ^ {n - 1} c _ {i} (\eta_ {t _ {i + 1} + 0} - \eta_ {t _ {i} - 0}). \tag {4.3.1}$$

对任一 $f \in L_2(\mathrm{d}F)$ , 必存在阶梯函数 $f_n(t)$ , 使

$$\int_ {- \infty} ^ {\infty} \| f (t) - f _ {n} (t) \| ^ {2} \mathrm{d} F (t) \underset {n \rightarrow \infty} {\longrightarrow} 0.$$

可以证明， $\int_{-\infty}^{\infty}f_n(t)\mathrm{d}\eta_t$ 存在均方极限，也就是存在随机变量 $\zeta$ ，使 $E\| \zeta -$ $\int_{-\infty}^{\infty}f_n(t)\mathrm{d}\eta_t\| ^2\underset {n\to \infty}{\longrightarrow}0.$

定义随机积分为
