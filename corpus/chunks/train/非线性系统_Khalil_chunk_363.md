$$
\begin{array}{l} a (\alpha) = \left. \frac {\partial f}{\partial x} \right| _ {x = \alpha , u = c \sqrt {\alpha}} = \left[ \frac {1}{A (x)} \left(\frac {- c}{2 \sqrt {x}}\right) - \frac {A ^ {\prime} (x)}{A ^ {2} (x)} (u - c \sqrt {x}) \right] _ {x = \alpha , u = c \sqrt {\alpha}} \\ = - \frac {c \sqrt {\alpha}}{2 \alpha A (\alpha)} \\ \end{array}
$$

和 $b(\alpha) = \frac{\partial f}{\partial u}\Big|_{x = \alpha ,u = c\sqrt{\alpha}} = \frac{1}{A(\alpha)}$

假设已知上界为 $c$ ，选择 $k_{1}$ 和 $k_{2}$ 为

$$k _ {1} (\alpha) = \frac {2 \zeta \omega_ {n}}{b (\alpha)}, \quad k _ {2} (\alpha) = \frac {\omega_ {n} ^ {2}}{b (\alpha)}$$

其中 $0 < \zeta < 1, 2\zeta \omega_{n} \gg |a(\alpha)|$ ，上式的选取要使得闭环系统的特征值（近似）为

$$s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2} = 0$$

的根。因此，闭环系统在固定增益控制器下的线性化为

$$\dot {\xi} _ {\delta} = A _ {f} (\alpha) \xi_ {\delta} + B _ {f} r _ {\delta}, \quad y _ {\delta} = C _ {f} \xi_ {\delta}$$

其中 $A_{f}(\alpha) = \left[ \begin{array}{cc}a(\alpha) - 2\zeta \omega_{n} & -\omega_{n}^{2}\\ 1 & 0 \end{array} \right],\quad B_{f} = \left[ \begin{array}{c}2\zeta \omega_{n}\\ -1 \end{array} \right],\quad C_{f} = \left[ \begin{array}{ll}1 & 0 \end{array} \right]$

从指令输入 $r_{\delta}$ 到输出 $y_{\delta}$ 的闭环传递函数为

$$\frac {2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}{s ^ {2} + [ 2 \zeta \omega_ {n} - a (\alpha) ] s + \omega_ {n} ^ {2}}$$

现在先把假设 r 为常数的情况放在一边,考虑 r 为时变信号的情况,此时增益分配 PI 控制器方程为

$$u = - k _ {1} (r) e - k _ {2} (r) \sigma , \quad \dot {\sigma} = e = x - r$$

其中 r 代换了原方程中的 $\alpha$ ，以使增益 $k_{1}$ 和 $k_{2}$ 直接随 r 而变化。在增益分配控制器下闭环非线性系统为 $\dot{x} = f(x, -k_{1}(r)(x - r) - k_{2}(r)\sigma)$

$$\dot {\sigma} = x - r$$

当 $r=\alpha$ 时，系统具有平衡点 $(x_{\mathrm{ss}},\sigma_{\mathrm{ss}})$ ，这说明在增益分配控制器下，闭环非线性系统对每个 $\alpha$ 都能工作在期望的工作点上。在 $(x,\sigma)=(x_{\mathrm{ss}},\sigma_{\mathrm{ss}})$ 对系统线性化，且 $r=\alpha$ 时得

$$\xi_ {\delta} = A _ {s} (\alpha) \xi_ {\delta} + B _ {s} (\alpha) r _ {\delta}, \quad y _ {\delta} = C _ {s} \xi_ {\delta}$$

其中

$$
A _ {s} (\alpha) = \left[ \begin{array}{c c} a (\alpha) - 2 \zeta \omega_ {n} & - \omega_ {n} ^ {2} \\ 1 & 0 \end{array} \right], \quad B _ {s} (\alpha) = \left[ \begin{array}{c} 2 \zeta \omega_ {n} + \gamma (\alpha) \\ - 1 \end{array} \right], \quad C _ {s} = \left[ \begin{array}{l l} 1 & 0 \end{array} \right]
$$

且 $\gamma(\alpha) = -b(\alpha)k_{2}^{\prime}(\alpha)\sigma_{\mathrm{ss}}(\alpha) = A^{\prime}(\alpha)c\sqrt{\alpha}/A^{2}(\alpha)$ 。从指令输入 $r_{\delta}$ 到输出 $y_{\delta}$ 的闭环传递函数为
