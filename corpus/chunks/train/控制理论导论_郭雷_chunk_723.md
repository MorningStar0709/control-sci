# 其中假设

(i) 对任何 $t \geqslant 0, f_t(x): \mathbb{R}^d \to [0, \infty)$ 是 $x$ 的连续函数；且对任何 $x \in \mathbb{R}^d$ 当 $t \to \infty$ 时， $f_t(x) \to f(x)$ ;

(ii) 对任何固定 $x \in \mathbb{R}^d, \{f_t(x), \mathcal{F}_t\}$ 是适应序列，其中 $\{\mathcal{F}_t\}$ 是递增的 $\sigma-$ 代数族；

(iii) $D$ 是 $\mathbb{R}^d$ 中的紧子集，且与内点的闭包一致；

(iv) $\{\eta_t\}$ 是 $\mathbb{R}^d$ 中的独立序列，均匀分布于 $D$ 中。进一步， $\eta_t$ 与 $\mathcal{F}_t$ 是独立的。

考虑下列优化算法：

$$
x _ {t} = \left\{ \begin{array}{l l} {\eta_ {t},} & {\qquad \text {当} f _ {t} (\eta_ {t}) \leqslant f _ {t} (x _ {t - 1}) - \epsilon ,} \\ {x _ {t - 1},} & {\qquad \text {当} f _ {t} (\eta_ {t}) > f _ {t} (x _ {t - 1}) - \epsilon ,} \end{array} \right.
$$

其中 $x_0 = \eta_0$ ，且 $\epsilon > 0$ .

证明在上述条件下， $x_{t}$ 的极限几乎处处存在（记为 $x_{\infty}$ ），且 $x_{\infty} \in S(\epsilon)$ ，其中 $S(\epsilon)$ 是 $f(x)$ 在 D 上整体极小的 $\epsilon$ 邻域，即

$$S (\epsilon) \stackrel {\text { def }} {=} \{x \in D: f (x) \leqslant f ^ {*} + \epsilon \},$$

其中 $f^{*} \stackrel{\mathrm{def}}{=} \min_{x \in D} f(x)$ .

9.6.8 考虑下列由状态方程描述的线性随机系统：

$$x _ {t + 1} = A x _ {t} + B u _ {t} + w _ {t + 1},$$

其中 $x_{t} \in \mathbb{R}^{n}$ 是可观测的状态向量， $(A, B)$ 是未知但能控的矩阵对， $\{w_{t}\}$ 是正态白噪声序列。试设计一个自适应控制律，使得下列二次型指标：

$$J (u) \stackrel {\text { def }} {=} \lim _ {T \to \infty} \sup \frac {1}{T} \sum_ {t = 1} ^ {T} [ x _ {t} ^ {\mathrm{T}} Q x _ {t} + u _ {t} ^ {\mathrm{T}} R u _ {t} ]$$

达到极小，其中 $Q > 0, R > 0$ 是两个加权矩阵。（提示：可参考文献[8],[17].）
