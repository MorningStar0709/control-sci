$$\Delta_ {\varepsilon , \bar {t}} J _ {1} [ u ] = - \varepsilon \left[ H (x ^ {*} (\bar {t}), \bar {u}, \psi (\bar {t})) - H (x ^ {*} (\bar {t}), u ^ {*} (\bar {t}), \psi (\bar {t})) \right] + o (\varepsilon). \tag {7.1.43}$$

由此容易得出最优控制的必要条件. 由于 $u^{*}(t)$ 使式 (7.1.33) 中 $J_{1}[u]$ 取极小, 所以对形如式 (7.1.38) 的容许控制 $u(t)$ , 相应于 $J_{1}[u^{*}]$ 的改变量 $\Delta_{\varepsilon, \bar{t}} J_{1}[u]$ 满足

$$\Delta_ {\varepsilon , \bar {t}} J _ {1} [ u ] \geqslant 0.$$

由于 $\varepsilon > 0$ 的任意性可知

$$H (x ^ {*} (\bar {t}), \bar {u}, \psi (\bar {t})) \leqslant H (x ^ {*} (\bar {t}), u ^ {*} (\bar {t}), \psi (\bar {t})). \tag {7.1.44}$$

当 $u^{*}(t)$ 在 $t_f$ 连续时，用类似方法亦知不等式 (7.1.44) 在 $t_f$ 时刻成立。再考虑到 $\bar{u} \in \mathbb{U}_r$ 的任意性，可知式 (7.1.44) 对任意 $t \in \Omega(t_0, t_f; u^*)$ 成立。这表明

$$H (x ^ {*} (t), u ^ {*} (t), \psi (t)) = \max _ {\bar {u} \in \mathbf {U} _ {r}} H (x ^ {*} (t), \bar {u}, \psi (t)). \tag {7.1.45}$$

上述式 (7.1.45) 称为 $u^{*}(t), x^{*}(t), \psi(t)$ 满足的极大关系式.

现在证明 $H(x^{*}(t), u^{*}(t), \psi(t)) =$ 常数．事实上，记

$$H (t) \stackrel {\text { def }} {=} H (x ^ {*} (t), u ^ {*} (t), \psi (t)),H _ {\hat {u}} (t) \stackrel {{\mathrm{def}}} {{=}} H (x ^ {*} (t), \hat {u}, \psi (t)),$$

对于使 $u^{*}(t)$ 连续的任意时刻 $t \in [t_0, t_f]$ , 式 (7.1.45) 能表示为

$$H (t) = \max _ {\bar {u} \in \mathbb {U} _ {r}} H _ {\bar {u}} (t).$$

下面证明：

(1) $H(t)$ 是 $[t_0, t_f]$ 上的绝对连续函数；  
(2) 设 $\tau \in \Omega(t_0, t_f; u^*)$ , 则 $H(t)$ 在 $t = \tau$ 时是可微的, 且导数 $H'(\tau)$ 为零.

注意对 $\mathbb{U}_r$ 中每个固定 $\hat{u}, H_{\hat{u}}(t)$ 是 $t$ 的连续可微函数，且

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (H _ {\hat {u}} (t)) = \frac {\partial H _ {\hat {u}} (t)}{\partial x} \dot {x} ^ {*} (t) + \frac {\partial H _ {\hat {u}} (t)}{\partial \psi} \dot {\psi} (t) \\ = \left(- \frac {\partial l (x ^ {*} (t) , \hat {u})}{\partial x} + \psi^ {T} (t) \frac {\partial f (x ^ {*} (t) , \hat {u})}{\partial x}\right) f (x ^ {*} (t), u ^ {*} (t)) \\ - \left(- \frac {\partial l (x ^ {*} (t) , u ^ {*} (t))}{\partial x} + \psi^ {T} (t) \frac {\partial f (x ^ {*} (t) , u ^ {*} (t))}{\partial x}\right) f (x ^ {*} (t), \hat {u}). \\ \end{array}
$$

由此可见，对任意 $t \in [t_0, t_f]$ ，当 $\hat{u} = u^*(t)$ 时成立

$$\left. \frac {\mathrm{d}}{\mathrm{d} t} H _ {\hat {u}} (t) \right| _ {\hat {u} = u ^ {*} (t)} = 0. \tag {7.1.46}$$

现令 $\tau \in \Omega(t_0, t_f; u^*)$ . 任给 $\varepsilon > 0$ , 当 $s$ 充分接近 $\tau$ 时, 必有

$$\left| \frac {\mathrm{d}}{\mathrm{d} \tau} (H _ {u ^ {*} (s)} (\tau)) \right| < \varepsilon . \tag {7.1.47}$$
