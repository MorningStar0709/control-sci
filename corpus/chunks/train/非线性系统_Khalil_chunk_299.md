$$\| B (t) \| = \left\| \frac {\partial f}{\partial x} (t, x _ {0} (t), 0) - \frac {\partial f}{\partial x} (t, 0, 0) \right\| \leqslant L \| x _ {0} (t) \|$$

另一方面,根据方程(10.7)的原点的指数稳定性和定理4.15可知,线性系统 $\dot{y}=A_{0}(t)y$ 的原点是指数稳定的。因此,与例9.6相似,可以用 $\lim_{t\to\infty}x_{0}(t)=0$ 证明线性系统 $\dot{z}=A(t)z$ 的原点是指数稳定的。

由于 $\left\|x_{0}(t)\right\|$ 有界，且 $g_{1}(t,x_{0}(t))=\left[\partial f/\partial\varepsilon\right](t,x_{0}(t),0)$ ，可知对于所有 $t\geqslant t_{0},g_{1}$ 是有界的。因此由定理 5.1 可得， $x_{1}(t)$ 是有界的。由简单的归纳法，可论证 $x_{2}(t),\cdots,x_{k-1}(t)$ 有界。

至此,我们已经验证了对于足够小的 $|\varepsilon|$ ,精确解 $x(t,\varepsilon)$ 和近似解 $\sum_{k=0}^{N-1}x_{k}(t)\varepsilon^{k}$ 在 $[t_{0},\infty)$ 上是一致有界的。其余要做的是分析逼近误差 $e=x-\sum_{k=0}^{N-1}x_{k}(t)\varepsilon^{k}$ 。该误差分析与10.1节中所做的分析非常相似。误差满足式(10.10),其中 $\rho_{1}$ 和 $\rho_{2}$ 当 $\varepsilon_{1}$ 足够小时,对于所有 $(t,e,\varepsilon)\in[t_{0},\infty)\times B_{\lambda}\times[-\varepsilon_{1},\varepsilon_{1}]$ 满足式(10.11),式(10.13)和

$$\left\| \frac {\partial \rho_ {1}}{\partial e} (t, e, \varepsilon) \right\| \leqslant k _ {1} (\| e \| + | \varepsilon |)$$

误差方程(10.10)可看成 $\dot{e}=A(t)e$ 的扰动,其中的扰动项满足

$$\| \rho_ {1} (t, e, \varepsilon) + \rho_ {2} (t, \varepsilon) \| \leqslant k _ {1} (\| e \| + | \varepsilon |) \| e \| + k _ {2} | \varepsilon | ^ {N} \leqslant k _ {1} (\lambda + | \varepsilon |) \| e \| + k _ {2} | \varepsilon | ^ {N}$$

注意到 $\| e(t_0, \varepsilon) \| = O(\varepsilon^N)$ , 由引理9.4可得, 当 $t \geqslant t_0$ 时, 对于足够小的 $|\varepsilon|$ , 有 $\| e(t, \varepsilon) \| = O(\varepsilon^N)$ 。

例10.5 例10.4的电路可表示为

$$\dot {x} _ {1} = 1. 2 - x _ {1} - h (x _ {1}) - \varepsilon (x _ {1} - x _ {2})\dot {x} _ {2} = 1. 2 - x _ {2} - h (x _ {2}) - \varepsilon (x _ {2} - x _ {1})$$

其中 $h(v) = 1.5\left(17.76v - 103.79v^{2} + 229.62v^{3} - 226.31v^{4} + 83.72v^{5}\right)$

当 $\varepsilon=0$ 时, 非扰动系统含有两个孤立的一阶子系统

$$\dot {x} _ {1} = 1. 2 - x _ {1} - h (x _ {1})\dot {x} _ {2} = 1. 2 - x _ {2} - h (x _ {2})$$

可以验证,这两个系统中的每个都有3个平衡点0.063,0.285和0.884。雅可比函数 $-1+h'(x_{i})$ 在点 $x_{i}=0.063$ 处和 $x_{i}=0.884$ 处为负,在点 $x_{i}=0.285$ 处为正。因此,在0.063处和0.884处的平衡点是指数稳定的,而在0.285处的平衡点是非稳定的。当两个一阶系统连接在一起时,复合二阶系统就有9个平衡点,其中只有4个是指数稳定的,它们是(0.063,0.063),(0.063,0.884),(0.884,0.063)和(0.884,0.884)。定理10.2指出,如果初始状态 $x(0)$ 属于这些平衡点中任何一个的吸引区的一个紧子集,则例10.4中计算的近似解就对于所有 $t\geqslant0$ 都是成立的。图10.3所示是在一段足够长的时间区间上系统达到稳定状态的仿真。在这个特例中,初始状态(0.15,0.6)属于(0.063,0.884)的吸引区。
