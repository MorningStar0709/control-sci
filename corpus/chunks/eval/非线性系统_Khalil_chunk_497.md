$$\| x (t) \| \leqslant U _ {r} \left(t - t _ {0}\right), \forall t \geqslant t _ {0}, \forall \| x \left(t _ {0} \right\rVert < r \tag {C.9}$$

根据式(C.8)和式(C.9)，显然有

$$\| x (t) \| \leqslant \min \{\alpha (\| x (t _ {0}) \|), U _ {r} (t - t _ {0}) \}, \forall t \geqslant t _ {0}, \forall \| x (t _ {0}) \| < r$$

因此，不等式(4.20)成立，此时 $\beta (r,s) = \min \{\alpha (r),U_r(s)\}$

全局一致渐近稳定性: 如果对于所有 $x(t_{0}) \in R^{n}$ ，式(4.20)都成立，则与上一种情况一样，很容易看出原点是全局一致渐近稳定的。为了从相反方向证明，注意到在当前情况下，函数 $\bar{\delta}(\varepsilon)$ 具有一个附加性质，即当 $\varepsilon$ 趋于无穷时， $\bar{\delta}(\varepsilon)$ 趋于无穷，因而可选择 K 类函数 $\alpha$ 属于 $K_{\infty}$ 类，且对于所有 $x(t_{0}) \in R^{n}$ ，不等式(C.7)都成立，对于任意 r > 0，不等式(C.9)成立。设

$$\psi (r, s) = \min \left\{\alpha (r), \inf _ {\rho \in (r, \infty)} U _ {\rho} (s) \right\}$$

则有 $\| x(t)\| \leqslant \psi (\| x(t_0)\| ,t - t_0),\quad \forall t\geqslant t_0,\forall x(t_0)\in R^n$

如果 $\psi$ 是 $\mathcal{KL}$ 类函数，则证明就此完成，但事实并非如此，所以定义函数

$$\phi (r, s) = \int_ {r} ^ {r + 1} \psi (\lambda , s) d \lambda + \frac {r}{(r + 1) (s + 1)}$$

为正,并且具有以下性质:

- 对于每个固定的 $s \geqslant 0, \phi(r, s)$ 关于 $r$ 是连续且严格递增的；  
- 对于每个固定的 $r \geqslant 0, \phi(r, s)$ 关于 $s$ 严格递减，且当 $s$ 趋于无穷时趋于零；  
$\phi (r,s)\geqslant \psi (r,s)$

因此 $\| x(t)\| \leqslant \phi (\| x(t_0)\| ,t - t_0),\forall t\geqslant t_0,\forall x(t_0)\in R^n$ (C.10)

根据式(C.10)和式(C.7)的全局性,可知

$$\| x (t) \| \leqslant \sqrt {\alpha (\| x (t _ {0}) \|) \phi (\| x (t _ {0}) \| , t - t _ {0})}, \forall t \geqslant t _ {0}, \forall x (t _ {0}) \in R ^ {n}$$

这样,不等式(4.20)全局成立,此时 $\beta(r,s)=\sqrt{\alpha(r)\phi(r,s)}$ 。
