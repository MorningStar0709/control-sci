由 $f(x,u), \frac{\partial f(x,u)}{\partial x}, \frac{\partial l(x,u)}{\partial x}$ 的连续性和 $\mathbb{U}_r$ 的紧性，从式 (7.1.46) 知存在有限常数 $d$ , 使得

$$\left[ \frac {d}{d t} (H _ {\hat {u}} (t)) \right] < d, \quad \forall t \in [ t _ {0}, t _ {f} ], \hat {u} \in \mathbb {U} _ {r} ^ {*}.$$

于是对于任意 $\tau \in \Omega(t_0, t_f; u^*)$ 和充分接近 $\tau$ 的 $s$ , 有

$$- d | s - \tau | < H _ {\hat {u}} (s) - H _ {\hat {u}} (\tau) < d | s - \tau |, \quad \forall \hat {u} \in \mathbb {U} _ {r} ^ {*}. \tag {7.1.48}$$

利用式 (7.1.48) 的左端不等式有

$$
\begin{array}{l} H (s) - H (\tau) = H _ {u ^ {*} (s)} (s) - H _ {u ^ {*} (\tau)} (\tau) \\ \geqslant H _ {u ^ {*} (\tau)} (s) - H _ {u ^ {*} (\tau)} (\tau) > - d | s - \tau |, \\ \end{array}
$$

而利用式 (7.1.48) 的右端不等式则有

$$
\begin{array}{l} H (s) - H (\tau) = H _ {u ^ {*} (s)} (s) - H _ {u ^ {*} (\tau)} (\tau) \\ \leqslant H _ {u ^ {*} (s)} (s) - H _ {u ^ {*} (s)} (\tau) <   - d | s - \tau |. \\ \end{array}
$$

联合此两不等式得到

$$- d | s - \tau | < H (s) - H (\tau) < d | s - \tau |, \tag {7.1.49}H _ {u ^ {*} (\tau)} (s) - H _ {u ^ {*} (\tau)} (\tau) \leqslant H (s) - H (\tau) \leqslant H _ {u ^ {*} (s)} (s) - H _ {u ^ {*} (s)} (\tau). \tag {7.1.50}$$

在区间 $[t_0, t_f]$ 上任取有限个长度不为零的区间 $I_i = [s_i, \tau_i]$ , $\tau_i \in \Omega(t_0, t_f; u^*)$ , $i = 1, \dots, m$ , 从不等式 (7.1.49) 可得

$$\sum_ {i = 1} ^ {m} \left| H (s _ {i}) - H (\tau_ {i}) \right| \leqslant d \sum_ {i = 1} ^ {m} \left| s _ {i} - \tau_ {i} \right|.$$

由此可知， $H(t)$ 是 $[t_0,t_f]$ 上的绝对连续函数，(1)得证.

在不等式 (7.1.50) 两端除以 $|s - \tau|$ 可得

$$\left| \frac {H (s) - H (\tau)}{s - \tau} \right| \leqslant \max \left\{\left| \frac {H _ {u ^ {*} (\tau)} (s) - H _ {u ^ {*} (\tau)} (\tau)}{s - \tau} \right|, \left| \frac {H _ {u ^ {*} (s)} (s) - H _ {u ^ {*} (s)} (\tau)}{s - \tau} \right| \right\}.$$

当 $s$ 充分接近 $\tau$ 时， $s \in \Omega(t_0, t_f; u^*)$ 。由上式从不等式 (7.1.47) 可知

$$\left| \frac {H (s) - H (\tau)}{s - \tau} \right| < \varepsilon ,$$

从而

$$H ^ {\prime} (\tau) = \frac {\mathrm{d}}{\mathrm{d} t} (H (t)) \Big | _ {t = \tau} = 0, \quad \forall \tau \in \Omega (t _ {0}, t _ {f}; u ^ {*}).$$

于是根据 $H(t)$ 的绝对连续性可知在 $[t_0, t_f]$ 上

$$H (x ^ {*} (t), u ^ {*} (t), \psi (t)) = \text {常数}, \qquad t _ {0} \leqslant t \leqslant t _ {f}.$$

当 $\mathbb{U}_r\subset \mathbb{R}^r$ 为开集时，记 $\mathbb{U}_r^* = \{u^* (t)\in \mathbb{U}_r\mid t\in [t_0,t_f]\}$ .易知 $\overline{\mathbb{U}}_r^*$ 为 $\mathbb{U}_r$ 中紧集，并且

$$H (t) = \max _ {\hat {u} \in \mathbf {U} _ {r}} H _ {\hat {u}} (t) = \max _ {\hat {u} \in \overline {{\mathbf {U}}} _ {r} ^ {*}} H _ {\hat {u}} (t).$$

见图7.1.1:
