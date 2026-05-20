当式(4.20)中的K类函数 $\beta$ 取 $\beta(r,s)=kre^{-\lambda s}$ 的形式时,会出现一致渐近稳定性的特例。这种情况非常重要,将被当成平衡点的独特稳定性提出来。

定义4.5 对于方程(4.15)的平衡点 $x = 0$ ，如果存在正常数 $c, k$ 和 $\lambda$ ，满足

$$\| x (t) \| \leqslant k \| x \left(t _ {0}\right) \| e ^ {- \lambda \left(t - t _ {0}\right)}, \forall \| x \left(t _ {0}\right) \| < c \tag {4.21}$$

则该平衡点是指数稳定的。如果式(4.21)对于任何初始状态 $x(t_{0})$ 都成立，则该平衡点是全局指数稳定的。

自治系统的李雅普诺夫理论可以扩展到非自治系统。定理4.1到定理4.4的每一条都可以通过不同的论述扩展到非自治系统中。这里不证明所有这些扩展①，只讨论一致稳定性和一致渐近稳定性，因为这是多数非自治系统中李雅普诺夫法要遇到的情况。

定理4.8 设 $x = 0$ 是方程(4.15)的一个平衡点, $D \subset R^n$ 是包含 $x = 0$ 的定义域, $V: [0, \infty) \times D \to R$ 是连续可微函数, 且满足

$$W _ {1} (x) \leqslant V (t, x) \leqslant W _ {2} (x) \tag {4.22}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant 0 \tag {4.23}$$

$\forall t \geqslant 0, \forall x \in D$ ，其中 $W_{1}(x)$ 和 $W_{2}(x)$ 都是 $D$ 上的连续正定函数。那么， $x = 0$ 是一致稳定的。

证明： $V$ 沿方程(4.15)的轨线的导数为

$$\dot {V} (t, x) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant 0$$

选择 r>0 和 c>0，满足 $B_{r}\subset D$ 和 $c<\min_{\|x\|=r}W_{1}(x)$ ，那么 $\{x\in B_{r}|W_{1}(x)\leqslant c\}$ 在 $B_{r}$ 内。与时间有关的集合 $\Omega_{t,c}$ 定义如下：

$$\Omega_ {t, c} = \{x \in B _ {r} \mid V (t, x) \leqslant c \}$$

由于

$$W _ {2} (x) \leqslant c \Rightarrow V (t, x) \leqslant c$$

所以集合 $\Omega_{t,c}$ 包含 $\{x\in B_r|W_2(x)\leqslant c\}$ 。此外，由于

$$V (t, x) \leqslant c \Rightarrow W _ {1} (x) \leqslant c$$

所以 $\Omega_{t,c}$ 是 $\{x\in B_r|W_1(x)\leqslant c\}$ 的子集。因此，对于所有 $t\geqslant 0$

$$\{x \in B _ {r} \mid W _ {2} (x) \leqslant c \} \subset \Omega_ {t, c} \subset \{x \in B _ {r} \mid W _ {1} (x) \leqslant c \} \subset B _ {r} \subset D$$

这五个嵌套的集合如图4.7所示。图4.7与图4.1相似，不同之处在于图4.7中曲面 $V(t,x) = c$ 与 $t$ 有关，所以它处于独立于时间的曲面 $W_{1}(x) = c$ 和 $W_{2}(x) = c$ 之间。

由于在 $D$ 上, 对于任何 $t_0 \geqslant 0$ 和 $\dot{V}(t,x) \leqslant 0$ , 有 $x_0 \in \Omega_{t_0,c}$ , 所以对于所有 $t \geqslant t_0$ , 始于 $(t_0,x_0)$ 的解保持在 $\Omega_{t,c}$ 内。因此, 对于所有未来时刻, 始于 $\{x \in B_r | W_2(x) \leqslant c\}$ 的任何解都保持在 $\Omega_{t,c}$ 内, 从而也保持在 $\{x \in B_r | W_1(x) \leqslant c\}$ 内。因此, 对于所有 $t \geqslant t_0$ , 解都有定义且有界。又由于 $\dot{V} \leqslant 0$ , 所以有

![](image/5d4175e2ef1310bc364696f221726ab8e8fe1a1cd1b9f7df17b502654a62b523.jpg)

<details>
<summary>text_image</summary>

-D
-Br
-{W1≤c}
-W2≤c
{V≤c}
</details>

图4.7 定理4.8的证明中所用集合的几何表示

$$V (t, x (t)) \leqslant V (t _ {0}, x (t _ {0})), \forall t \geqslant t _ {0}$$
