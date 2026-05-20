$$\mathcal {H} = \frac {\partial V}{\partial x} f + \frac {1}{2} \left[ h ^ {\mathrm{T}} J + \frac {\partial V}{\partial x} G \right] \left(\gamma^ {2} I - J ^ {\mathrm{T}} J\right) ^ {- 1} \left[ h ^ {\mathrm{T}} J + \frac {\partial V}{\partial x} G \right] ^ {\mathrm{T}} + \frac {1}{2} h ^ {\mathrm{T}} h \leqslant 0$$

证明系统为有限增益 $L_{2}$ 稳定的,其 $L_{2}$ 增益小于或等于 $\gamma$ 。

提示:令

$$\gamma^ {2} I - J ^ {\mathrm{T}} (x) J (x) = W ^ {\mathrm{T}} (x) W (x), L (x) = - \left[ W ^ {\mathrm{T}} (x) \right] ^ {- 1} \left[ h ^ {\mathrm{T}} (x) J (x) + \frac {\partial V}{\partial x} G (x) \right] ^ {\mathrm{T}}$$

进而证明对于任意 u，下面的不等式成立：

$$\frac {\partial V}{\partial x} f + \frac {\partial V}{\partial x} G u = - \frac {1}{2} [ L + W u ] ^ {\mathrm{T}} [ L + W u ] + \frac {\gamma^ {2}}{2} u ^ {\mathrm{T}} u - \frac {1}{2} y ^ {\mathrm{T}} y + \mathcal {H}$$

5.18 (见文献[199])考虑系统

$$\dot {x} = f (x) + G (x) u + K (x) w, \quad y = h (x)$$

其中 u 为控制输入, $\omega$ 为扰动输入。函数 f, G, K 和 h 光滑,且 $f(0)=0, h(0)=0$ 。设 $\gamma>0$ , 并假设对任意 x, 存在光滑半正定函数 $V(x)$ , 满足

$$\frac {\partial V}{\partial x} f (x) + \frac {1}{2} \frac {\partial V}{\partial x} \left[ \frac {1}{\gamma^ {2}} K (x) K ^ {\mathrm{T}} (x) - G (x) G ^ {\mathrm{T}} (x) \right] \left(\frac {\partial V}{\partial x}\right) ^ {\mathrm{T}} + \frac {1}{2} h ^ {\mathrm{T}} (x) h (x) \leqslant 0$$

证明在反馈控制 $u = -G^{\mathrm{T}}(x)(\partial V/\partial x)^{\mathrm{T}}$ 下，从 $\omega$ 到 $\begin{bmatrix} y \\ u \end{bmatrix}$ 的闭环映射是有限增益 $L_{2}$ 稳定的，其 $L_{2}$ 增益小于或等于 $\gamma$ 。

5.19 （见文献[200]）本习题的目的是证明：不论函数空间定义在 $R_{+} = [0,\infty)$ 上，还是定义在整个实数轴 $R = (-\infty ,\infty)$ 上，形如方程(5.24)\~(5.25)的线性时不变系统，其 $\mathcal{L}_2$ 增益都是相同的,其中A为赫尔维茨矩阵。设 $L_{2}$ 是 $R_{+}$ 上的平方可积函数空间,其范数为 $\|u\|_{L_{2}}^{2}=\int_{0}^{\infty}u^{\mathrm{T}}(t)u(t)$ , $L_{2R}$ 为R上的平方可积函数空间,其范数为 $\|u\|_{L_{2R}}^{2}=\int_{-\infty}^{\infty}u^{\mathrm{T}}(t)u(t)dt$ 。设 $\gamma_{2}$ 和 $\gamma_{2R}$ 分别为 $L_{2}$ 和 $L_{2R}$ 上的 $L_{2}$ 增益。因为 $L_{2}$ 是 $L_{2R}$ 的子集,显然 $\gamma_{2}\leqslant\gamma_{2R}$ 。通过证明对于每个 $\varepsilon>0$ ,存在信号 $u\in L_{2}$ ,使得 $y\in L_{2}$ ,且 $\|y\|_{L_{2}}\geqslant(1-\varepsilon)\gamma_{2R}\|u\|_{L_{2}}$ ,进而证明 $\gamma_{2}=\gamma_{2R}$ 。

(a) 给定 $\varepsilon > 0$ ，证明总可以选择 $0 < \delta < 1$ ，使得

$$\frac {1 - \varepsilon / 2 - \sqrt {\delta}}{\sqrt {1 - \delta}} \geqslant 1 - \varepsilon$$

(b) 证明总可以选取 $u \in \mathcal{L}_{2R}$ 和时间 $t_1 < \infty$ ，使得
