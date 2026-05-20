$$A - B K = (A - S C) + (S C - B K),$$

并且对于所有的 $x \in H$ 和 $t \geqslant 0$ , 有

$$T ^ {A - B K} (t) x = T ^ {A - S C} (t) x + \int_ {0} ^ {t} T ^ {A - S C} (t - s) (S C - B K) T ^ {A - B K} (s) x \mathrm{d} s.$$

现在我们证明，对于所有的 $x \in H$ ，我们有

$$
\left\{ \begin{array}{l} \int_ {0} ^ {\infty} \| C T ^ {A - B K} (s) x \| ^ {2} \mathrm{d} s <   \infty , \\ \int_ {0} ^ {\infty} \| K ^ {\prime} I ^ {A - B K} (s) x \| ^ {2} \mathrm{d} s <   \infty . \end{array} \right. \tag {10.3.6}
$$

事实上，令 $x(t) = T^{A - BK}(t)x$ ，并假定 $x \in \mathcal{D}(A) = \mathcal{D}(A - BK)$ ，从而 $x(t) \in \mathcal{D}(A - BK) = \mathcal{D}(A), \forall t \geqslant 0.$ 利用式(10.3.4)，我们得到

$$
\begin{array}{l} 2 \operatorname{Re} (P (A - B K) x (t), x (t)) + (C x (t), C x (t)) \\ + (R K x (t), K x (t)) \leqslant 0, \quad \forall t \geqslant 0. \\ \end{array}
$$

但是 $(A - BK)x(t) = \dot{x}(t), 2\mathrm{Re}(P\dot{x}(t), x(t)) - \frac{\mathrm{d}}{\mathrm{d}t} (Px(t), x(t))$ ，因此

$$
\begin{array}{l} (P x (t), x (t)) + \int_ {0} ^ {t} (C x (s), C x (s)) d s \\ + \int_ {0} ^ {t} (R K x (s), K x (s)) \mathrm{d} s \leqslant (P x, x). \tag {10.3.7} \\ \end{array}
$$

通过简单的极限运算，可知式(10.3.7)对所有 $x \in H$ 成立。从式(10.3.7)直接可得式(10.3.6).

由于 $\int_0^t\| T^{A - SC}(s)x\| ^2\mathrm{d}s <   \infty$ ，并且

$$
\begin{array}{l} \| x (t) \| \leqslant \| T ^ {A - S C} (t) x \| + \left\| \int_ {0} ^ {t} T ^ {A - S C} (t - s) (S C - B K) T ^ {A - B K} (s) x d s \right\| \\ \leqslant \mu \int_ {0} ^ {t} \| T ^ {A - S C} (t - s) \| \left(\| C x (s) \| + \| K x (s) \|\right) d s + \| T ^ {A - S C} (t) x \|, \\ \end{array}
$$

其中 $\mu = \max \{\| S\| ,\| B\|\}$ ，我们得到

$$
\begin{array}{l} \int_ {0} ^ {\infty} \| x (t) \| ^ {2} \mathrm{d} t \leqslant 2 \mu \left(\int_ {0} ^ {\infty} \| T ^ {A - S C} (t) \| ^ {2} \mathrm{d} t\right) \left(\int_ {0} ^ {\infty} (\| C x (s) \| + \| K x (s) \|) ^ {2} \mathrm{d} s\right) \\ + 2 \int_ {0} ^ {\infty} \| T ^ {A - S C} (t) x \| ^ {2} d t <   \infty , \\ \end{array}
$$

即式 (10.3.5) 成立. 证毕.

推论10.3.1 设 $A$ 是Hilbert空间 $H$ 上 $C_0$ 半群 $T(t)$ 的生成算子. 假定存在一对称非负算子 $P \in \mathcal{L}(H)$ 使得

$$(P A x, x) + (x, P A x) = - (x, x), \quad \forall x \in \mathcal {D} (A),$$

那么由 A 生成的 $C_{0}$ 半群 $T(t)$ 是指数稳定的.

证明 我们只需在引理 10.3.1 中取 C = I 和 K = 0，并注意 $(I, A)$ 总是能检测的，于是引理 10.3.1 意味着 $T(t) = T^{A}(t)$ 是指数稳定的．证毕．

定理10.3.2 设 $A$ 是 $H$ 上某 $C_0$ 半群的生成算子，而 $B \in \mathcal{L}(U, H)$ . 那么下列命题是等价的：

(1) $(A, B)$ 是指数能稳的；

(2) 对于任意初始值 $x_0 \in H$ , 存在 $u \in L^2(0, \infty; U)$ 使得式 (10.3.1) 的对应于控制 $u(t)$ 和初值 $x_0$ 的温和解 $x(t)$ 满足

$$\int_ {0} ^ {\infty} \left[ \| x (t) \| ^ {2} + \| u (t) \| ^ {2} \right] \mathrm{d} t < \infty ; \tag {10.3.8}$$
