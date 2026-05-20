为赫尔维茨矩阵,其中 $A=\frac{\partial f}{\partial x},\quad B=\frac{\partial f}{\partial u},\quad C=\frac{\partial h}{\partial x},\quad C_{m}=\frac{\partial h_{m}}{\partial x}$

是以 $(x, u, v) = (x_{\mathrm{ss}}, u_{\mathrm{ss}}, \alpha_v)$ 赋值的所有雅可比矩阵。与前面不同的是，允许控制器增益与 $\alpha$ 有关（ $\alpha$ 是分配变量 $\rho$ 的冻结值）。在状态反馈情况下，可消去 $z$ 及其状态方程(12.34)，并取 $y_m = x, L = 0, M_1 = -K_2, M_2 = -K_1, M_3 = 0$ ，其中 $K = [K_1 K_2]$ 设计为对于所有 $(\alpha, w) \in D_\rho \times D_w$ ，使

$$
\left[ \begin{array}{c c} A - B K _ {1} & - B K _ {2} \\ C & 0 \end{array} \right]
$$

为赫尔维茨矩阵。

在固定增益控制器(12.33)\~(12.35)下,当 $\rho=\alpha$ 时,闭环系统

$$\dot {x} = f (x, L z + M _ {1} \sigma + M _ {2} h _ {m} (x, w) + M _ {3} e, v, w) \tag {12.36}\dot {\sigma} = e = h (x, w) - r \tag {12.37}\dot {z} = F z + G _ {1} \sigma + G _ {2} h _ {m} (x, w) \tag {12.38}y = h (x, w) \tag {12.39}$$

有一个平衡点 $(x_{\mathrm{ss}},\sigma_{\mathrm{ss}},z_{\mathrm{ss}})$ ，在该点e=0。在点 $(x,\sigma,z)=(x_{\mathrm{ss}},\sigma_{\mathrm{ss}},z_{\mathrm{ss}})$ 对系统线性化，并且 $\rho=\alpha$ ，得

$$\dot {\xi} _ {\delta} = A _ {f} (\alpha , w) \xi_ {\delta} + B _ {f} (\alpha , w) \rho_ {\delta} \tag {12.40}y _ {\delta} = C _ {f} (\alpha , w) \xi_ {\delta} \tag {12.41}$$

其中

$$
\xi_ {\delta} = \left[ \begin{array}{l} {x - x _ {\mathrm{ss}}} \\ {\sigma - \sigma_ {\mathrm{ss}}} \\ {z - z _ {\mathrm{ss}}} \end{array} \right], \quad \rho_ {\delta} = \rho - \alpha = \left[ \begin{array}{l} {r _ {\delta}} \\ {v _ {\delta}} \end{array} \right], \quad y _ {\delta} = y - \alpha_ {r}

A _ {f} = \mathcal {A} _ {c}, \quad B _ {f} = \left[ \begin{array}{c c} - B M _ {3} & E \\ - I & 0 \\ 0 & 0 \end{array} \right], \quad C _ {f} = \left[ \begin{array}{l l l} C & 0 & 0 \end{array} \right]
E = \left. \frac {\partial f}{\partial v} (x, u, v, w) \right| _ {x = x _ {\mathrm{ss}}, u = u _ {\mathrm{ss}}, v = \alpha_ {v}}
$$

因此，当 $\rho = \alpha$ 时，平衡点 $(x_{\mathrm{ss}},\sigma_{\mathrm{ss}},z_{\mathrm{ss}})$ 是指数稳定的。
