一项是 13.4.2 节中用到的反馈线性项。无论哪种情况，s 方程都可以表示为

$$\dot {s} = L _ {g} L _ {f} ^ {\rho - 1} h (x) v + \Delta (t, x, v)$$

假设对于所有 $(t,x,v)\in [0,\infty)\times D\times R$ ，有

$$\left| \frac {\Delta (t , x , v)}{L _ {g} L _ {f} ^ {\rho - 1} h (x)} \right| \leqslant \varrho (x) + \kappa_ {0} | v |, \quad 0 \leqslant \kappa_ {0} < 1$$

$\varrho$ 和 $\kappa_0$ 已知，则 $v = -\beta (x)\operatorname {sgn}(s)$

其中 $\beta(x) \geqslant \varrho(x)/(1 - \kappa_{0}) + \beta_{0}, \beta_{0} > 0$ ，而且用 $\operatorname{sat}(s/\varepsilon)$ 代换 $\operatorname{sgn}(s)$ 可得到其连续逼近。以下内容留给读者证明（见习题 14.13）：对于连续滑模控制器，存在一个可能与 $\varepsilon$ 和初始状态有关的有限时间 $T_{1}$ ，以及一个与 $\varepsilon$ 和初始状态无关的正常数 k，使得对于所有 $t \geqslant T_{1}$ ，有 $|y(t) - r(t)| \leqslant k\varepsilon$ 。
