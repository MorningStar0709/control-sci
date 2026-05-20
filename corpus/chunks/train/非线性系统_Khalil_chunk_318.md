$$\| f (t, x, \varepsilon) - f (t, x, 0) \| \leqslant L _ {1} \varepsilon \| x \|$$

运用这些估算,可以验证对于 $(t,y,\varepsilon)\in[0,\infty)\times D_{1}+[0,\varepsilon_{1}]$ ，方程(10.47)中的函数 $q(t,y,\varepsilon)$ 满足不等式 $\|q(t,y,\varepsilon)\|\leqslant L\|y\|$ ，其中L为正常数， $D_{1}=\{\|y\|<r_{1}\}$ ，选择 $r_{1}$ 和 $\varepsilon_{1}$ 充分小。根据(逆李雅普诺夫)定理4.14和引理9.1，可断定对于充分小的 $\varepsilon$ ，原点是原系统(10.39)的一个指数稳定平衡点。

例10.13 设线性系统为

$$\dot {x} = \varepsilon A (t) x$$

其中 $\varepsilon > 0$ 。假设 $A(t)$ 及其一阶与二阶导数是连续且有界的，此外按照定义 10.2，假设 $A(t)$ 的平均为

$$A _ {\mathrm{av}} = \lim _ {T \rightarrow \infty} \frac {1}{T} \int_ {t} ^ {t + T} A (\tau) d \tau$$

则平均系统为

$$\dot {x} = \varepsilon A _ {\mathrm{av}} x$$

假设 $A_{\mathrm{av}}$ 是赫尔维茨矩阵。由定理10.5可以推出，对于充分小的 $\varepsilon$ ，原时变系统的原点是指数稳定的。进一步假设矩阵 $A(t) = A_{\mathrm{tr}}(t) + A_{\mathrm{ss}}(t)$ 是瞬态分量 $A_{\mathrm{tr}}(t)$ 和稳态分量 $A_{\mathrm{ss}}(t)$ 之和，该瞬态分量按指数规律快速衰减为零，即

$$\| A _ {\mathrm{tr}} (t) \| \leqslant k _ {1} \exp (- \gamma t), \quad k _ {1} > 0, \gamma > 0$$

而稳态分量的元素由有限个具有不同频率的正弦项之和构成。瞬态分量的平均为零,因为

$$\frac {1}{T} \int_ {t} ^ {t + T} \| A _ {\mathrm{tr}} (\tau) \| d \tau \leqslant \frac {1}{T} \int_ {t} ^ {t + T} k _ {1} e ^ {- \gamma \tau} d \tau = \frac {k _ {1} e ^ {- \gamma t}}{\gamma T} [ 1 - e ^ {- \gamma T} ] \leqslant \frac {k _ {2}}{T + 1}$$

回顾例 10.12 中的第一种情况, 可以看出 $A(t)$ 有一个收敛函数为 $\sigma(T)=1/(T+1)$ 的平均函数, 因此, 定理 10.5 的 K 类函数是 $\alpha(\eta)=\eta$ 。设 $x(t,\varepsilon)$ 和 $x_{\mathrm{av}}(\varepsilon t)$ 表示初始状态相同的原系统和平均系统的解。根据定理 10.5 可得

$$x (t, \varepsilon) - x _ {\mathrm{av}} (\varepsilon t) = O (\varepsilon), \forall t \geqslant 0$$
