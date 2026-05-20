- 如果对于所有 $z$ ，有 $\| \delta(z) \| \leqslant k \| z \|$ ，则方程(13.46)的原点是全局渐近稳定的。  
- 如果对于所有 $z$ ，有 $\| \delta(z) \| \leqslant k \| z \| + \varepsilon$ ，则状态 $z$ 是全局毕竟有界的，其界为 $\varepsilon c, c > 0$ 。

证明: 设 $V(z) = z^{T} Pz$ , 则

$$
\begin{array}{l} \dot {V} = z ^ {\mathrm{T}} [ P (A - B K) + (A - B K) ^ {\mathrm{T}} P ] z + 2 z ^ {\mathrm{T}} P B \delta (z) \\ \leqslant - \| z \| _ {2} ^ {2} + 2 \| P B \| _ {2} \| z \| _ {2} \| \delta (z) \| _ {2} \\ \end{array}
$$

如果 $\| \delta (z)\| _2\leqslant k\| z\| _2 + \varepsilon$ ，则有

$$
\begin{array}{l} \dot {V} \leqslant - \| z \| _ {2} ^ {2} + 2 k \| P B \| _ {2} \| z \| _ {2} ^ {2} + 2 \varepsilon \| P B \| _ {2} \| z \| _ {2} \\ = - \left(1 - \theta_ {1}\right) \| z \| _ {2} ^ {2} - \theta_ {1} \| z \| _ {2} ^ {2} + 2 k \| P B \| _ {2} \| z \| _ {2} ^ {2} + 2 \varepsilon \| P B \| _ {2} \| z \| _ {2} \\ \end{array}
$$

其中选择 $\theta_{1}\in (0,1)$ 足够接近1，使得 $k < \theta_{1} / (2\| PB\|_{2})$ 。因此

$$\dot {V} \leqslant - (1 - \theta_ {1}) \| z \| _ {2} ^ {2} + 2 \varepsilon \| P B \| _ {2} \| z \| _ {2}$$

如果 $\| \delta (z)\| _2\leqslant k\| z\| _2$ ，则在上面的不等式中令 $\varepsilon = 0$ ，可知原点是全局指数稳定的。如果 $\varepsilon >0$ ，则有

$$\dot {V} \leqslant - (1 - \theta_ {1}) (1 - \theta_ {2}) \| z \| _ {2} ^ {2}, \forall \| z \| _ {2} \geqslant \frac {2 \varepsilon \| P B \| _ {2}}{(1 - \theta_ {1}) \theta_ {2}} \stackrel {\mathrm{def}} {=} \varepsilon c _ {0}$$

其中 $\theta_{2} \in (0,1)$ 。由定理4.18可证明 $z(t)$ 是全局毕竟有界的，其界为 $\varepsilon c_{0} \sqrt{\lambda_{\max}(P) / \lambda_{\min}(P)}$ 。

从证明中明显看出,若 $\delta(z)$ 的边界条件仅在原点的一个邻域内成立,则可以证明该引理局部成立。

例13.18 考虑单摆方程 $\dot{x}_1 = x_2$ $\dot{x}_2 = -a\sin (x_1 + \delta_1) - bx_2 + cu$

其中 $x_{1}=\theta-\delta_{1},x_{2}=\dot{\theta},u=T$ 是力矩输入。设计目标是将单摆稳定在 $\theta=\delta_{1}$ 处。可线性化稳定反馈控制取为

$$u = \left(\frac {a}{c}\right) \sin (x _ {1} + \delta_ {1}) - \left(\frac {1}{c}\right) (k _ {1} x _ {1} + k _ {2} x _ {2})$$

其中选择 $k_{1}$ 和 $k_{2}$ , 使 $A - BK = \left[ \begin{array}{cc}0 & 1 \\ -k_{1} & -(k_{2} + b) \end{array} \right]$

为赫尔维茨矩阵。假设由于参数 a 和 c 的不确定性, 实际控制为

$$u = \left(\frac {\hat {a}}{\hat {c}}\right) \sin (x _ {1} + \delta_ {1}) - \left(\frac {1}{\hat {c}}\right) (k _ {1} x _ {1} + k _ {2} x _ {2})$$

其中 $\hat{a}, \hat{c}$ 是 a 和 c 的估计值。闭环系统为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - k _ {1} x _ {1} - (k _ {2} + b) x _ {2} + \delta (x) \\ \end{array}
$$

其中 $\delta (x) = \left(\frac{\hat{a}c - a\hat{c}}{\hat{c}}\right)\sin (x_1 + \delta_1) - \left(\frac{c - \hat{c}}{\hat{c}}\right)(k_1x_1 + k_2x_2)$
