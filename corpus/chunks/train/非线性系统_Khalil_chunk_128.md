$$
\begin{array}{l} \| x (t) \| \leqslant \alpha_ {1} ^ {- 1} (V (t, x (t))) \leqslant \alpha_ {1} ^ {- 1} (\sigma (V (t _ {0}, x (t _ {0})), t - t _ {0})) \\ \leqslant \alpha_ {1} ^ {- 1} \left(\sigma \left(\alpha_ {2} \left(\| x \left(t _ {0}\right) \|\right), t - t _ {0}\right)\right) \stackrel {\text { def }} {=} \beta \left(\| x \left(t _ {0}\right) \|, t - t _ {0}\right) \\ \end{array}
$$

引理4.2证明 $\beta$ 是 $\mathcal{KL}$ 类函数，因此不等式(4.20)成立，从而说明 $x = 0$ 是一致渐近稳定的。如果 $D = R^n$ ，则 $\alpha_{1},\alpha_{2}$ 和 $\alpha_{3}$ 是定义在 $[0,\infty)$ 上的函数，因而 $\alpha_{1}$ 以及 $\beta$ 都与 $c$ 无关。由于 $W_{1}(x)$ 径向无界，所以可选择 $c$ 任意大，使其包含 $\{W_2(x)\leqslant c\}$ 内的任何初始状态。因此，式(4.20)对于任何初始状态都成立，即证明了原点是全局一致渐近稳定的。

如果 $V(t,x)\geqslant 0$ ，则称函数 $V(t,x)$ 是半正定的。如果对于某个正定函数 $W_{1}(x)$ 有 $V(t,x)$ $\geqslant W_1(x)$ ，则称 $V(t,x)$ 是正定的。如果 $W_{1}(x)$ 径向无界，则称 $V(t,x)$ 也是径向无界的。如果 $V(t,x)\leqslant W_2(x)$ ，则称 $V(t,x)$ 是递减的。如果 $-V(t,x)$ 是正定的（或半正定的），则称函数

$V(t,x)$ 是负定的(或半负定的)。因此, 定理 4.8 和定理 4.9 指出, 若存在一个连续可微、正定的递减函数 $V(t,x)$ , 其沿系统轨线的导数是半负定的, 则原点是一致稳定的; 如果 $V(t,x)$ 沿系统轨线的导数是负定的, 则原点是一致渐近稳定的; 如果原点一致渐近稳定的条件对径向无界函数 $V(t,x)$ 全局成立, 则原点是全局一致渐近稳定的。

定理 4.10 设 x=0 是方程(4.15)的平衡点。 $D \subset R^{n}$ 是包含 x=0 的定义域。设 $V:[0,\infty) \times D \to R$ 是连续可微函数，且满足

$$k _ {1} \| x \| ^ {a} \leqslant V (t, x) \leqslant k _ {2} \| x \| ^ {a} \tag {4.25}\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - k _ {3} \| x \| ^ {a} \tag {4.26}$$

$\forall t \geqslant 0, \forall x \in D$ ，其中 $k_{1}, k_{2}, k_{3}$ 和 $a$ 是正常数，那么 $x = 0$ 是指数稳定的。如果上述假设全局成立，那么 $x = 0$ 是全局指数稳定的。

证明:借助图4.7,可以看出当 $t\geqslant t_{0}$ 时,对于足够小的c,始于 $\{k_{2}\parallel x\parallel^{a}\leqslant c\}$ 的轨线都有界。不等式(4.25)和不等式(4.26)表明V满足微分不等式

$$\dot {V} \leqslant - \frac {k _ {3}}{k _ {2}} V$$

根据引理 3.4(比较引理), 有

$$V (t, x (t)) \leqslant V (t _ {0}, x (t _ {0})) e ^ {- (k _ {3} / k _ {2}) (t - t _ {0})}$$

因此

$$
\begin{array}{l} \| x (t) \| \leqslant \left[ \frac {V (t , x (t))}{k _ {1}} \right] ^ {1 / a} \leqslant \left[ \frac {V \left(t _ {0} , x \left(t _ {0}\right)\right) e ^ {- \left(k _ {3} / k _ {2}\right) \left(t - t _ {0}\right)}}{k _ {1}} \right] ^ {1 / a} \\ \leqslant \left[ \frac {k _ {2} \| x (t _ {0}) \| ^ {a} e ^ {- (k _ {3} / k _ {2}) (t - t _ {0})}}{k _ {1}} \right] ^ {1 / a} = \left(\frac {k _ {2}}{k _ {1}}\right) ^ {1 / a} \| x (t _ {0}) \| e ^ {- (k _ {3} / k _ {2} a) (t - t _ {0})} \\ \end{array}
$$

所以,原点是指数稳定的。如果所有假设全局成立,则可选择 c 任意大,且上述不等式对于所有 $x(t_{0}) \in R^{n}$ 都成立。

例4.19 考虑标量系统
