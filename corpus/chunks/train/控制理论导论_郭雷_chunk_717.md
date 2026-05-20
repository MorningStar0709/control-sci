引理 9.6.1 考虑由式 (9.6.11) 给出的参数估计值，其中 $\{\theta_{t}\}$ 和 $\{P_{t}\}$ 由 WLS 算法 (9.2.25)\~(9.2.28) 给出， $\{\beta_{t}\}$ 是任意有界序列。若条件 A1) 满足，则 $\tilde{\theta}_{t} \stackrel{\operatorname{def}}{=} \theta - \hat{\theta}_{t}$ 满足下列两条性质：

i) $\| P_t^{-\frac{1}{2}}\tilde{\theta}_t\|^2 = O(1),$ a.s.;   
ii) $\sum_{i=1}^{t} (\phi_i^{\mathrm{T}} \tilde{\theta}_i)^2 = o(r_t) + O(1)$ , a.s.,

其中 $\phi_{i}$ 是回归向量，而 $r_t \stackrel{\mathrm{def}}{=} 1 + \sum_{i=1}^{t} \| \phi_i\|^2$ .

下面，我们将说明如何选取 $\{\beta_t\}$ 使得由式(9.6.11)中 $\hat{\theta}_t$ 给出的估计多项式 $A_{t}(z)$ 与 $B_{t}(z)$ 具有所需互质性.

对由式 (9.6.9) 所定义的参数 $\theta$ , 定义 ( $n \stackrel{\mathrm{def}}{=} \max(p, q)$ )

$$
A (\theta) = \left( \begin{array}{c c c c} - a _ {1} & 1 & \dots & 0 \\ - a _ {2} & 0 & \ddots & \vdots \\ \vdots & \vdots & \ddots & 1 \\ - a _ {n} & 0 & \dots & 0 \end{array} \right), \quad b (\theta) = \left( \begin{array}{c} b _ {1} \\ \vdots \\ b _ {n} \end{array} \right). \tag {9.6.12}
$$

容易证明 (见本节习题), $(A(\theta), b(\theta))$ 能控 $\Longleftrightarrow A(z)$ 与 $B(z)$ 互质 $\Longleftrightarrow M(\theta)$ 非奇异, 其中 $M(\theta)$ 是 Sylvester 矩阵

$$
M (\theta) = \left( \begin{array}{c c c c c c c c} 1 & & & 0 & 0 & & & 0 \\ a _ {1} & \ddots & & & b _ {1} & \ddots & & \\ \vdots & \ddots & \ddots & & \vdots & \ddots & \ddots & \\ \vdots & & \ddots & 1 & \vdots & & \ddots & 0 \\ a _ {n} & & & a _ {1} & b _ {n} & & & b _ {1} \\ & \ddots & & \vdots & & \ddots & & \vdots \\ & & \ddots & \vdots & & & \ddots & \vdots \\ 0 & & & a _ {n} & 0 & & & b _ {n} \end{array} \right). \tag {9.6.13}
$$

我们下面选取 $\{\beta_t\}$ 使得 $M(\hat{\theta}_t)$ 一致非奇异即可，这可转化为在单位立方体

$$
D \stackrel {\mathrm{def}} {=} \left\{x \in \mathbb {R} ^ {d}   \Big |   0 \leqslant x _ {i} \leqslant 1, \quad 1 \leqslant i \leqslant d \right\}, \quad x = \left( \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \end{array} \right), \quad d = p + q
$$

上优化下列非负多元函数的问题：

$$f _ {t} (x) \stackrel {\text { def }} {=} \left| \det M (\theta_ {t} + P _ {t} ^ {\frac {1}{2}} x) \right|, \quad x \in \mathbb {R} ^ {d}, t \geqslant 0. \tag {9.6.14}$$

为此，假设 $\{\eta_t\}$ 是在 $D$ 上具有均匀分布的 $d-$ 维独立随机向量序列，并且与 $\{w_t\}$ 独立。取 $\gamma > 0$ 使

$$1 \geqslant 2 \gamma + \gamma^ {2}. \tag {9.6.15}$$

递推地定义 $\{\beta_{t}\}$ 如下：

$$
\beta_ {t} = \left\{ \begin{array}{l l} {\eta_ {t},} & {\text {当} f _ {t} (\eta_ {t}) \geqslant (1 + \gamma) f _ {t} (\beta_ {t - 1}),} \\ {\beta_ {t - 1},} & {\text {当} f _ {t} (\eta_ {t}) <   (1 + \gamma) f _ {t} (\beta_ {t - 1}).} \end{array} \right. \tag {9.6.16}
$$
