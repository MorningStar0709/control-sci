设 $\phi (t;x)$ 表示方程(C.13)在 $t = 0$ 时刻始于 $x$ 的解。因为 $\| \tilde{f} (x)\|$ 有界，因此 $\phi (t;x)$ 对于所有 $t\leqslant 0$ 都有定义，又由于 $R_{A}$ 是不变集（见引理8.1），因此对于所有 $t\leqslant 0$ ，有 $\phi (t;x)\in R_A$ 。

定义 $g: R_A \to R$ 为 $g(x) = \inf_{t \leqslant 0} \{\omega(\phi(t; x))\}$ (C.23)

显然,根据定义有 $g(\phi(t;x)) \leqslant g(x), \forall t \geqslant 0, \forall x \in R_{A}$ (C.24)

$$\alpha^ {- 1} (\omega (x)) \leqslant g (x) \leqslant \omega (x), \forall x \in R _ {A} \tag {C.25}$$

方程(C.25)的第一个不等式成立,因为根据方程(C.21),有 $\omega(x)\leqslant\alpha(\omega(\phi(t;x))),\forall t\leqslant0$ 。下面证明对于 $x\in R_{A}$ ,且当 $x\neq0$ 时, $g(x)$ 是局部利普希茨的,这相当于证明 $g(x)$ 在紧集 $H=\{x\in R_{A}|c_{1}\leqslant\omega(x)\leqslant c_{2}\}$ 上是利普希茨的,其中 $c_{2}>c_{1}>0$ 。不等式(C.15)表示

$$c _ {1} \leqslant \omega (x) \leqslant \beta (\omega (\phi (t; x)), - t), \quad \forall t < 0, \forall x \in H$$

设 $T_{1}$ 满足 $\beta (2c_2,T_1) = c_1$ ，则对于所有 $t\leqslant -T_{1}$ ，有

$$\beta (2 c _ {2}, T _ {1}) = c _ {1} \leqslant \beta (\omega (\phi (t; x)), - t) \leqslant \beta (\omega (\phi (t; x)), T _ {1})$$

因此 $\omega (\phi (t;x))\geqslant 2c_{2}\geqslant 2\omega (x)\geqslant 2g(x),\quad \forall t\leqslant -T_{1},\forall x\in H$

说明对于所有 $x \in H$ ，在区间 $[-T_1, 0]$ 内到达定义 $g(x)$ 的下确界。根据 $\phi(t; x)$ 对于任意紧时间区间，在 $H$ 上是 $x$ 的利普希茨函数（见定理3.4），以及 $\omega$ 在 $R_A$ 上是局部利普希茨的，可推出 $g(x)$ 在 $H$ 上也是利普希茨的。注意当 $c_1 = 0$ 时上述结论不成立，所以我们不证明 $g(x)$ 在 $x = 0$ 处是局部利普希茨的。但 $g(x)$ 对于所有 $x \in R_A$ 是连续的，这是因为 $g(0) = 0, g(x) \leqslant \omega(x)$ （根据式(C.25))且 $\omega(x)$ 是连续的。

定义函数 $\tilde{V}: R_A \to R$ 为 $\tilde{V}(x) = \sup_{t \geqslant 0} \left\{ g(\phi(t; x)) \frac{1 + 2t}{1 + t} \right\}$ (C. 26)

利用式(C.24)和式(C.25),容易验证

$$\alpha^ {- 1} (\omega (x)) \leqslant g (x) \leqslant \tilde {V} (x) \leqslant 2 g (x) \leqslant 2 \omega (x) \tag {C.27}$$

现在通过证明 $\tilde{V}(x)$ 是 $H = \{x\in R_A|c_1\leqslant \omega (x)\leqslant c_2\} (c_2 > c_1 > 0)$ 上的利普希茨函数，证明 $\tilde{V}(x)$ 对 $x\in R_A(x\neq 0)$ 是局部利普希茨的。由式(C.15)和式(C.25)，可得对于所有 $x\in H$ ，有

$$g (\phi (t; x)) \frac {1 + 2 t}{1 + t} \leqslant 2 \omega (\phi (t; x)) \leqslant 2 \beta (\omega (x), t) \leqslant 2 \beta (c _ {2}, t)$$

设 $T_{2} > 0$ 满足 $4\beta (c_2,T_2) = \alpha^{-1}(c_1)$ ，则对于所有 $t\geqslant T_2$ ，有

$$g (\phi (t; x)) \frac {1 + 2 t}{1 + t} \leqslant \frac {1}{2} \alpha^ {- 1} (c _ {1}) \leqslant \frac {1}{2} \alpha^ {- 1} (\omega (x)) \leqslant \frac {1}{2} \tilde {V} (x)$$
