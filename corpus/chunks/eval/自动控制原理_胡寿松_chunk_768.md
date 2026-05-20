$$\delta J = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial L}{\partial \boldsymbol {x}} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {\mathrm{T}} \delta \boldsymbol {x} \mathrm{d} t + \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {\mathrm{T}} \delta \boldsymbol {x} \Big | _ {t _ {0}} ^ {t _ {f}}$$

由定理 10-2, 令 $\delta J = 0$ , 再由定理 10-3, 考虑到 $\delta x$ 任意, 立即证得本定理的结论式 (10-22) 和式 (10-23)。

在一般情况下，欧拉方程是一个时变二阶非线性微分方程，求解时所需的两点边界值由横截条件式(10-23)提供。由于在两端固定情况下，必有 $\delta x(t_0) = 0$ 和 $\delta x(t_f) = 0$ ，因此定理10-4中的横截条件退化为已知边界条件 $x(t_0) = x_0$ 和 $x(t_f) = x_f$ 。

应当指出, 欧拉方程是泛函极值的必要条件, 而不是充分必要条件。在处理实际泛函极值问题时, 可从实际问题的性质出发, 判断泛函极值的存在性, 并直接利用欧拉方程求出极值轨线 $x^{*}(t)$ 。

例10-2 设有泛函

$$J [ \pmb {x} ] = \int_ {0} ^ {\pi / 2} [ \dot {x} ^ {2} (t) - x ^ {2} (t) ] \mathrm{d} t$$

已知边界条件为 $x(0) = 0, x(\pi / 2) = 2$ 。求使泛函达到极值的极值轨线 $x^{*}(t)$ 。

解 本例 $L(x, \dot{x}) = \dot{x}^2 - x^2$ ，因

$$\frac {\partial L}{\partial x} = - 2 x, \quad \frac {\partial L}{\partial \dot {x}} = 2 \dot {x}, \quad \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {x}} = 2 \ddot {x}$$

故欧拉方程为

$$\ddot {x} (t) + x (t) = 0$$

其通解为

$$x ^ {*} (t) = c _ {1} \cos t + c _ {2} \sin t$$

在上式中，分别代入已知边界条件 $x(0) = 0$ 和 $x(\pi /2) = 2$ ，可求出 $c_{1} = 0,c_{2} = 2$ 。于是求出

$$x ^ {*} (t) = 2 \sin t$$
