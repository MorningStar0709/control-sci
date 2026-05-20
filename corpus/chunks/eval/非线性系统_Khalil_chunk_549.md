$$\left\| \mathcal {X} (t) - \mathcal {X} _ {r} (t) \right\| \leqslant \mu , \quad \forall t \in [ T (\varepsilon), T _ {3} ] \tag {C.105}$$

取 $\varepsilon_{3}^{*}=\min\left\{\varepsilon_{5},\varepsilon_{6}\right\}$ ，则由式(C.103)到式(C.105)即可得式(14.115)。

最后,假设系统(C.96)的原点是指数稳定的,根据(逆李雅普诺夫)定理4.14可知,存在连续可微的李雅普诺夫函数 $V_{1}(\mathcal{X})$ ,它在球 $B_{r}\subset\mathcal{R}$ 上,满足不等式

$$b _ {1} \| \mathcal {X} \| ^ {2} \leqslant V _ {1} (\mathcal {X}) \leqslant b _ {2} \| \mathcal {X} \| ^ {2}, \quad \frac {\partial V _ {1}}{\partial \mathcal {X}} F (\mathcal {X}, 0) \leqslant - b _ {3} \| \mathcal {X} \| ^ {2}, \quad \left\| \frac {\partial V _ {1}}{\partial \mathcal {X}} \right\| \leqslant b _ {4} \| \mathcal {X} \|$$

其中 $r, b_{1}, b_{2}, b_{3}$ 和 $b_{4}$ 是正常数。利用 $F$ 和 $\Delta$ 的局部利普希茨性质及 $F(0,0) = 0$ 和 $\Delta(0,0) = 0$ ，可证明复合李雅普诺夫函数 $V_{2}(\mathcal{X},\eta) = V_{1}(\mathcal{X}) + W(\eta)$ 满足

$$\dot {V} _ {2} \leqslant - y ^ {\mathrm{T}} Q y$$

其中 $Q = \left[ \begin{array}{cc}b_{3} & -\beta_{1}\\ -\beta_{1} & (1 / \varepsilon) - \beta_{2} \end{array} \right],\quad \mathcal{Y} = \left[ \begin{array}{l}\| \mathcal{X}\| \\ \| \eta \| \end{array} \right]$

这里 $\beta_{1}$ 和 $\beta_{2}$ 为非负常数。对于足够小的 $\varepsilon$ ，矩阵 $Q$ 是正定的，因此存在原点的一个邻域 $\mathcal{N}$ ，与 $\varepsilon$ 无关，且 $\varepsilon_{7} > 0$ ，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_{7}$ ，原点是指数稳定的，并且当 $t$ 趋于无穷时， $\mathcal{N}$ 内的每条轨线收敛于原点。根据式(14.114)，存在 $\varepsilon_{8} > 0$ ，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_{8}$ ，始于 $S \times Q$ 的解在有限的时间内进入 $\mathcal{N}$ 。因此，对于每个 $0 < \varepsilon \leqslant \varepsilon_{4}^{*} = \min \{\varepsilon_{7}, \varepsilon_{8}\}$ ，原点是指数稳定的，且 $S \times Q$ 是吸引区的一个子集。
