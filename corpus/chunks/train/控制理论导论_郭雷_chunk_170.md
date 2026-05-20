$$\lim _ {t _ {k} \rightarrow \infty} x (t + t _ {k}; 0, x _ {0}) = \lim _ {t _ {k} \rightarrow \infty} x (t; 0, x (t _ {k}; 0, x _ {0})) = x (t; 0, p).$$

从而 $x(t;0,p)\in \Omega (x_0)$ .这表明 $\Omega (x_0)$ 是微分方程(2.4.19）过点 $(0,p)$ 的轨线的不变集.

下面用反证法证 (3). 设当 $t \to +\infty$ 时, $x(t) \to \Omega(x_0)$ 不成立. 于是 $\exists \varepsilon_0 > 0$ , 和一序列 $\{t_m\}, t_m \to +\infty$ , 使得

$$\left| x \left(t _ {m}\right) - p \right| \geqslant \varepsilon_ {0}, \quad \forall m \geqslant 1, \forall p \in \Omega \left(x _ {0}\right).$$

但 $\{x(t_m)\}$ 有界，故有聚点 $x^{*} \in \Omega(x_{0})$ 。于是对充分大的 $m$ ，有

$$\left| x (t _ {m}) - x ^ {*} \right| < \varepsilon_ {0},$$

这与前不等式矛盾. 因此 (3) 成立.

定理 2.4.12(LaSalle 不变原理) 设 $D \subset R^{n}$ 为紧集，且是微分方程 (2.4.19) 的不变集。设定义在 D 上的实连续可微函数 $W(x)$ ，满足

$$\dot {W} (x) \mid_ {(2. 4. 1 9)} \leqslant 0, \quad \forall x \in D.$$

又设 $E \stackrel{\mathrm{def}}{=} \{x : \dot{W}(x) |_{(2.4.19)} = 0, x \in D\}$ , $M$ 是在 $E$ 中方程 (2.4.19) 的最大不变集. 那么当 $t \to +\infty$ 时有 $x(t:0, x_0) \to M$ .

证明 记 $\Omega(x_0)$ 是方程 (2.4.19) 以 $x_0 \in D$ 为初值的解 $x(t) \stackrel{\mathrm{def}}{=} x(t; 0, x_0)$ 的 $\omega$ 极限集。由 $\dot{W}(x)|_{(2.4.19)} \leqslant 0$ 知 $\dot{W}(x(t))$ 单调不增。再由 $W(x)$ 在紧集 $D$ 上的连续性知它在 $D$ 上有下界，因而有

$$\lim _ {t \rightarrow \infty} W (x (t)) = W ^ {*}.$$

于是 $\forall y \in \Omega(x_0)$ 有 $W(y) = W^*$ , 且 $\dot{W}(y(t))|_{(2.4.19)} = 0$ , 其中 $y(t) = x(t; 0, y) \in \Omega(x_0), \forall t \geqslant 0$ . 这表明 $\Omega(x_0)$ 是方程 (2.4.19) 在 $E$ 中不变集, 从而 $\Omega(x_0) \subset M$ . 根据引理 2.4.2, $x(t) \to \Omega(x_0) \subset M$ .

特别当 $M = \{0\}$ 时，微分方程(2.4.19)的零解渐近稳定.

为对微分方程解的稳定性问题进一步了解，读者可参阅文献 [1], [7].

下面不加证明地列出利用比较原理研究时变微分方程稳定性的几个结果。考虑向量微分方程

$$\dot {x} = f (t, x) \tag {2.4.26}$$

和标量微分方程

$$\frac {\mathrm{d} \omega}{\mathrm{d} t} = h (t, \omega), \tag {2.4.27}$$

其中 $f(\cdot, \cdot) \in C(J \times \mathbb{R}^n, \mathbb{R}^n)$ , $h(\cdot, \cdot) \in C(J \times \mathbb{R}_+, \mathbb{R}_+)$ , 且仅当 $w = 0$ 时有 $h(t, w) = 0$ .

定理 2.4.13 $^{[10]}$ 给定正定函数 $V(\cdot,\cdot)\in C(J\times\mathbb{R}^{n},\mathbb{R})$ ，如果 $V(t,x)$ 满足关于 x 的 Lipschitz 条件，并且

$$\left. D ^ {+} V \right| _ {(2. 3. 1)} \leqslant h (t, V),$$

则下列结论成立：

(1) 标量微分方程 (2.4.27) 的零解稳定蕴含向量微分方程 (2.4.26) 的零解稳定;  
(2) 如果 $V(t, x)$ 还具有无穷小上界，则方程 (2.4.27) 的零解的一致稳定蕴含方程 (2.4.26) 的零解一致渐近稳定；  
(3) 标量微分方程 (2.4.27) 的零解渐近稳定蕴含向量微分方程 (2.4.26) 的零解渐近稳定；  
(4) 如果 $V(t, x)$ 还具有无穷小上界，则方程 (2.4.27) 的零解一致渐近稳定蕴含方程 (2.4.26) 的零解一致渐近稳定；

(5) 如果存在 $a > 0, b > 0$ . 使得
