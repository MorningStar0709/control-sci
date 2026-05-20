这是因为 $\dot{V}(t,x)\leqslant 0$ 。因此对于所有 $t\geqslant t_0$ ，有 $\| x(t)\| < r$ 。因为 $V(t,x(t))$ 单调非增，下方有界且为0，所以当 $t$ 趋于无穷时， $V$ 是收敛的。现在有

$$\int_ {t _ {0}} ^ {t} W (x (\tau)) d \tau \leqslant - \int_ {t _ {0}} ^ {t} \dot {V} (\tau , x (\tau)) d \tau = V (t _ {0}, x (t _ {0})) - V (t, x (t))$$

因此， $\lim_{t \to \infty} \int_{t_0}^{t} W(x(\tau)) d\tau$ 存在且是有限的。因为 $x(t)$ 有界，故 $\dot{x}(t) = f(t, x(t))$ 对于所有 $t \geqslant t_0$ 有界，且对 $t$ 是一致的，因此， $x(t)$ 在 $[t_0, \infty)$ 上对 $t$ 是一致连续的，从而 $W(x(t))$ 在 $[t_0, \infty)$ 上对 $t$ 也是一致连续的，因为 $W(x)$ 在紧集 $B_r$ 上对 $x$ 是一致连续的。因此由引理8.2可得，当 $t$ 趋于无穷时， $W(x(t))$ 趋于零。如果所有假设都全局成立，且 $W_1(x)$ 是径向无界的，则对于任意 $x(t_0)$ ，可选取 $\rho$ 足够大，使得 $x(t_0) \in \{x \in R^n \mid W_2(x) \leqslant \rho\}$ 。

极限 $W(x(t))$ 趋于零表示当 t 趋于无穷时, $x(t)$ 都趋于 E, 其中

$$E = \{x \in D \mid W (x) = 0 \}$$

所以 $x(t)$ 的正极限集是 $E$ 的一个子集。 $x(t)$ 趋于 $E$ 比自治系统不变原理的要求弱得多，不变原理要求 $x(t)$ 趋于 $E$ 内的最大不变集。在自治系统情况下更强的结论是引理4.1所述的自治系统的性质，即正极限集是一个不变集。有一些特殊类型的非自治系统，其正极限集有某些不变性质①。然而对于一般的非自治系统，正极限集不是不变的。在自治系统情况下 $x(t)$ 趋于 $E$ 中的最大不变集这一事实，允许我们得到推论4.1，即证明除平凡解之外，集合 $E$ 不包含系统的全部轨线，从而建立原点的渐近稳定性。对于一般非自治系统，推论4.1不能证明其一致渐近稳定性。但下一个定理将说明如果除 $\dot{V}(t,x) \leqslant 0$ 之外，还可以证明 $V$ 在区间 $[t,t + \delta]$ 内是递减的，则可能得出系统是一致渐近稳定的结论②。

定理8.5 设 $D \subset R^n$ 是包含 $x = 0$ 的定义域, 并假设对于所有 $t \geqslant 0$ 和 $x \in D$ , $f(t, x)$ 是 $t$ 的分段连续函数, 且对于 $x$ 是局部利普希茨的。设 $x = 0$ 是 $\dot{x} = f(t, x)$ 在 $t = 0$ 时刻的一个平衡点。设 $V: [0, \infty) \times D \to R$ 是连续可微的函数, 使得对于某个 $\delta > 0$ , $\forall t \geqslant 0$ , $\forall x \in D$ , 满足

$$W _ {1} (x) \leqslant V (t, x) \leqslant W _ {2} (x)\dot {V} (t, x) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant 0V (t + \delta , \phi (t + \delta ; t, x)) - V (t, x) \leqslant - \lambda V (t, x), \quad 0 < \lambda < 1 ^ {(1)}$$

其中 $W_{1}(x)$ 和 $W_{2}(x)$ 是 D 上的连续正定函数, $\phi(\tau; t, x)$ 是系统始于 $(t, x)$ 的解, 则原点是一致渐近稳定的。如果所有假设全局成立, 且 $W_{1}(x)$ 是径向无界的, 则原点是全局一致渐近稳定的。如果

$$W _ {1} (x) \geqslant k _ {1} \| x \| ^ {c}, W _ {2} (x) \leqslant k _ {2} \| x \| ^ {c}, k _ {1} > 0, k _ {2} > 0, c > 0$$

则原点是指数稳定的。

◇

证明:选择 r>0, 使 $B_{r}\in D$ 。与定理 4.8 的证明相似, 可以证明

$$x \left(t _ {0}\right) \in \left\{x \in B _ {r} \mid W _ {2} (x) \leqslant \rho \right\} \Rightarrow x (t) \in \Omega_ {t, \rho}, \forall t \geqslant t _ {0}$$

其中 $\rho < \min_{\| x \| = r} W_1(x)$ ，因为 $\dot{V}(t, x) \leqslant 0$ 。现在，对于所有 $t \geqslant t_0$ 有

$$V (t + \delta , x (t + \delta)) \leqslant V (t, x (t)) - \lambda V (t, x (t)) = (1 - \lambda) V (t, x (t))$$

此外，由于 $\dot{V}(t,x)\leqslant 0$ ，所以有
