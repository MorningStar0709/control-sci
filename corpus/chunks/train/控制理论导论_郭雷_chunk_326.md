# 随机微分方程

为了把微分方程拓广到带噪声的情形，必须引进随机微分的概念。设 $(a_{t},\mathcal{F}_{t})$ ， $(b_{t},\mathcal{F}_{t})$ 为适应过程， $\| a_t\|^{\frac{1}{2}}\in \mathcal{P}_T,b_t\in \mathcal{P}_T.$

如下定义的过程 $\xi_{t}$

$$\xi_ {t} = \xi_ {0} + \int_ {0} ^ {t} a _ {s} \mathrm{d} s + \int_ {0} ^ {t} b _ {s} \mathrm{d} w _ {s} \tag {4.3.18}$$

叫伊滕过程. 如果 $a_{t}$ 和 $b_{t}$ 对 $\mathcal{F}_t^\xi \stackrel{\mathrm{def}}{=} \sigma \{\xi_\lambda, \lambda \leqslant t\}$ 适应，则 $\xi_{t}$ 叫扩散过程.

我们也称由式 (4.3.18) 定义的过程 $\xi_{t}$ 有随机微分

$$\mathrm{d} \xi_ {t} = a _ {t} \mathrm{d} t + b _ {t} \mathrm{d} w _ {t}. \tag {4.3.19}$$

在微积分中，我们知道复合函数的导数： $\frac{\mathrm{d}f(y)}{\mathrm{d}x} = f'(y)\frac{\mathrm{d}y}{\mathrm{d}x}$ 但当 $y$ 是伊滕过程 $\xi_{t}$ 时，这样的链式求导方法不成立，也就是说， $\mathrm{d}f(\xi_t)$ 不等于 $f'(\xi_t)\mathrm{d}\xi_t$

定理 4.3.3 (伊滕公式) 设 $(a_{t}, \mathcal{F}_{t})$ 为 l 维适应过程， $\|a_{t}\|^{\frac{1}{2}} \in \mathcal{P}_{T}, (B_{t}, \mathcal{F}_{t})$ 是 $l \times m$ 适应过程阵， $\|B_{t}\| \in \mathcal{P}_{T}, (w_{t}, \mathcal{F}_{t})$ 为 m 维 Wiener 过程。设偏导数 $f_{t}(t, x)$ ， $f_{x}(t, x)$ ， $f_{xx}(t, x)$ 连续，这里 $f_{t}(t, x) \stackrel{\operatorname{def}}{=} \frac{\partial f(t, x)}{\partial t}$ ，

$$
f _ {x} (t, x) \stackrel {\text { def }} {=} \left[ \begin{array}{c} \frac {\partial f (t , x)}{\partial x ^ {l}} \\ \vdots \\ \frac {\partial f (t , x)}{\partial x ^ {l}} \end{array} \right], \quad f _ {x x} (t, x) \stackrel {\text { def }} {=} \left[ \begin{array}{c c c} \frac {\partial^ {2} f (t , x)}{\partial x ^ {1} \partial x ^ {1}} & \dots & \frac {\partial^ {2} f (t , x)}{\partial x ^ {l} \partial x ^ {1}} \\ \vdots & & \vdots \\ \frac {\partial^ {2} f (t , x)}{\partial x ^ {1} \partial x ^ {l}} & \dots & \frac {\partial^ {2} f (t , x)}{\partial x ^ {l} \partial x ^ {l}} \end{array} \right],
\boldsymbol {x} = \left[ x ^ {1}, \dots , x ^ {l} \right] ^ {\mathrm{T}}.
$$

那么

$$\mathrm{d} f (t, \xi_ {t}) = \left[ f _ {t} (t, \xi_ {t}) + f _ {x} ^ {\mathrm{T}} (t, \xi_ {t}) a _ {t}, + \frac {1}{2} \operatorname{tr} f _ {x x} (t, \xi_ {t}) B _ {t} B _ {t} ^ {\mathrm{T}} \right] \mathrm{d} t + f _ {x} ^ {\mathrm{T}} (t, \xi_ {t}) B _ {t} \mathrm{d} w _ {t}, \tag {4.3.20}$$

把式 (4.3.20) 和确定性运算相比，这里多了一项 $\frac{1}{2} \operatorname{tr} f_{xx}(t, \xi_t) B_t B_t^{\mathrm{T}} \mathrm{d}t$ 。这项出现的原因，粗略地讲， $(\mathrm{d}w_t)^2$ 的阶数并不是 $(\mathrm{d}t)^2$ ，而是 $dt$ 。

例4.3.7 设 $f(t, x) = x^{\mathrm{T}}C_{t}x$ ，用伊滕公式 (4.3.20) 知
