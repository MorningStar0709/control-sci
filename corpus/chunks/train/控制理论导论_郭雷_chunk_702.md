$$\theta_ {n + 1} = \theta_ {n} + a _ {n} P _ {n} \varphi_ {n} (y _ {n + 1} - b _ {1} u _ {n} - \varphi_ {n} ^ {\mathrm{T}} \theta_ {n}), \tag {9.5.21}P _ {n + 1} = P _ {n} - a _ {n} P _ {n} \varphi_ {n} \varphi_ {n} ^ {\mathrm{T}} P _ {n}, \quad a _ {n} = (1 + \varphi_ {n} ^ {\mathrm{T}} P _ {n} \varphi_ {n}) ^ {- 1}, \tag {9.5.22}$$

其中初值 $\theta_0$ 及 $P_0 > 0$ 任取.

根据式 (9.5.9) 及 “必然等价原则”, LS 型 STR 为

$$
\begin{array}{l} u _ {n} = \frac {1}{b _ {1}} \left\{a _ {1 n} y _ {n} + \dots + a _ {p n} y _ {n - p + 1} - b _ {2 n} u _ {n - 1} - \dots - b _ {q n} u _ {n - q + 1} + y _ {n + 1} ^ {*} \right\} \\ = \frac {1}{b _ {1}} \left\{y _ {n + 1} ^ {*} - \theta_ {n} ^ {\mathrm{T}} \varphi_ {n} \right\}, \tag {9.5.23} \\ \end{array}
$$

其中 $a_{in}$ 及 $b_{in}$ 是 $\theta_{n}$ 的分量

$$\theta_ {n} = \left[ - a _ {1 n} \dots - a _ {p n}, b _ {2 n} \dots b _ {q n} \right] ^ {\mathrm{T}}.$$

显然，由方程 (9.5.18)\~方程 (9.5.23) 构成的闭环控制系统是输出信号的高度非线性方程.

下面我们将给出此STR的严格理论分析.

首先引进几个全节通用的记号：

$$\alpha_ {k} \stackrel {\text { def }} {=} \frac {(\varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}) ^ {2}}{1 + \varphi_ {k} ^ {\mathrm{T}} P _ {k} \varphi_ {k}}, \quad \delta_ {k} \stackrel {\text { def }} {=} \operatorname{tr} (P _ {k} - P _ {k + 1}), \tag {9.5.24}r _ {n} \stackrel {\text { def }} {=} 1 + \sum_ {i = 1} ^ {n} \| \varphi_ {i} \| ^ {2}, \quad \tilde {\theta} _ {k} = \theta - \theta_ {k}. \tag {9.5.25}$$

进一步，我们假定 $\{d_n\}$ 是非降的确定性正数序列，使

$$w _ {n} ^ {2} = O (d _ {n}) \quad \text { a.s., } \quad d _ {n + 1} = O (d _ {n}). \tag {9.5.26}$$

下面说明在条件(A1)下， $d_{n}$ 可取为

$$d _ {n} = n ^ {\delta}, \quad \forall \delta \in \left(\frac {2}{\beta}, 1\right), \tag {9.5.27}$$

其中 $\beta$ 由式 (9.5.6) 给出。事实上，利用 Markov 不等式有

$$\sum_ {n = 1} ^ {\infty} P (w _ {n + 1} ^ {2} \geqslant n ^ {\delta} | \mathcal {F} _ {n}) \leqslant \sum_ {n = 1} ^ {\infty} \frac {E [ | w _ {n + 1} | ^ {\beta} | \mathcal {F} _ {n} ]}{n ^ {\beta \delta / 2}} < \infty \quad \text { a.s. }$$

故利用 Borel-Cantelli-Lévy 引理 (定理 4.2.8) 可立即推出式 (9.5.27).

显然，若对 $\{w_{n}\}$ 有进一步的假设，则 $d_{n}$ 可取得更小。例如当 $\{w_{n}\}$ 是有界噪声时，可取 $d_{n} \equiv 1$ ；而当 $\{w_{n}\}$ 是正态白噪声时，可取 $d_{n} = \log n$ ，等等。

我们先给出两个引理，其关键的证明思想是借助于定理9.2.1(ii)用某一时变线性方程的解来控制非线性闭环控制系统的输出信号.

引理 9.5.1 考虑闭环控制系统 (9.5.19)～系统 (9.5.23). 若条件 (A1)～条件 (A3) 满足，则一定存在正随机序列 $\{L_{n}\}$ 使

$$y _ {n} ^ {2} \leqslant L _ {n}, \quad \forall n, \quad \text { a.s. } \tag {9.5.28}$$

且 $\{L_n\}$ 满足下列“线性时变”关系：

$$L _ {n + 1} \leqslant (\lambda + C \alpha_ {n} \delta_ {n}) L _ {n} + \xi_ {n}, \tag {9.5.29}$$
