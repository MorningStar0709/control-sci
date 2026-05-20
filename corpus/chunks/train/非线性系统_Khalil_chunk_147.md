引理4.7 在上述假设条件下,如果以 $x_{2}$ 作为输入时系统(4.51)是输入-状态稳定的,且系统(4.52)的原点是全局一致渐近稳定的,那么系统(4.51)和系统(4.52)的级联系统的原点也是全局一致渐近稳定的。

证明: 设 $t_{0} \geqslant 0$ 为初始时刻, 方程(4.51) 和方程(4.52) 的解在全局范围内满足

$$\| x _ {1} (t) \| \leqslant \beta_ {1} (\| x _ {1} (s) \|, t - s) + \gamma_ {1} \left(\sup _ {s \leqslant \tau \leqslant t} \| x _ {2} (\tau) \|\right) \tag {4.53}\left\| x _ {2} (t) \right\| \leqslant \beta_ {2} \left(\left\| x _ {2} (s) \right\|, t - s\right) \tag {4.54}$$

其中 $t \geqslant s \geqslant t_0, \beta_1$ 和 $\beta_2$ 是 $\mathcal{KL}$ 类函数， $\gamma_1$ 是 $\mathcal{K}$ 类函数。以 $s = (t + t_0) / 2$ 代入式(4.53)，得

$$\left\| x _ {1} (t) \right\| \leqslant \beta_ {1} \left(\left\| x _ {1} \left(\frac {t + t _ {0}}{2}\right) \right\|, \frac {t - t _ {0}}{2}\right) + \gamma_ {1} \left(\sup _ {\frac {t + t _ {0}}{2} \leqslant \tau \leqslant t} \| x _ {2} (\tau) \|\right) \tag {4.55}$$

为了估计 $x_{1}((t + t_{0}) / 2)$ 的值，把 $s = t_0$ 代入式(4.53)，并以 $(t + t_0) / 2$ 代换 $t$ ，可到

$$\left\| x _ {1} \left(\frac {t + t _ {0}}{2}\right) \right\| \leqslant \beta_ {1} \left(\left\| x _ {1} (t _ {0}) \right\|, \frac {t - t _ {0}}{2}\right) + \gamma_ {1} \left(\sup _ {t _ {0} \leqslant \tau \leqslant \frac {t + t _ {0}}{2}} \| x _ {2} (\tau) \|\right) \tag {4.56}$$

利用式(4.54)可得 $\sup_{t_0\leqslant \tau \leqslant \frac{t + t_0}{2}}\| x_2(\tau)\| \leqslant \beta_2(\| x_2(t_0)\| ,0)$ (4.57)

$$\sup _ {\frac {t + t _ {0}}{2} \leqslant \tau \leqslant t} \| x _ {2} (\tau) \| \leqslant \beta_ {2} \left(\| x _ {2} (t _ {0}) \|, \frac {t - t _ {0}}{2}\right) \tag {4.58}$$

把式(4.56)到式(4.58)代入式(4.55)，并利用不等式

$$\left\| x _ {1} \left(t _ {0}\right) \right\| \leqslant \left\| x \left(t _ {0}\right) \right\|, \quad \left\| x _ {2} \left(t _ {0}\right) \right\| \leqslant \left\| x \left(t _ {0}\right) \right\|, \quad \left\| x (t) \right\| \leqslant \left\| x _ {1} (t) \right\| + \left\| x _ {2} (t) \right\|$$

得 $\| x(t)\| \leqslant \beta (\| x(t_0)\| ,t - t_0)$

其中

$$\beta (r, s) = \beta_ {1} \left(\beta_ {1} \left(r, \frac {s}{2}\right) + \gamma_ {1} \left(\beta_ {2} (r, 0)\right), \frac {s}{2}\right) + \gamma_ {1} \left(\beta_ {2} \left(r, \frac {s}{2}\right)\right) + \beta_ {2} (r, s)$$

很容易验证对于所有 $r \geqslant 0, \beta$ 是 $\mathcal{KL}$ 类函数。因此，系统(4.51)和系统(4.52)的级联系统的原点是全局一致渐近稳定的。
