其中 $\varepsilon > 0$ 为给定的充分小正数。显然 $\varepsilon > 0$ 越小表示该系统对干扰的抑制能力就越强。

若令 $Q = M^{\mathrm{T}}M$ ， $R = N^{\mathrm{T}}N$ ，并且定义广义输出信号为

$$
z _ {0} = \left[ \begin{array}{c} M \\ 0 \end{array} \right] x + \left[ \begin{array}{c} 0 \\ N \end{array} \right] u = C _ {1} x + D _ {1 2} u,
$$

则有 $J = \| z_0\| _2^2$ ，且式(6.1.20）等价于

$$\sup _ {w \in L _ {q} ^ {2}} \frac {\| z _ {0} \| _ {2} ^ {2}}{\| w \| _ {2} ^ {2}} \leqslant \varepsilon^ {2}. \tag {6.1.21}$$

因此，根据引理6.1.1，使得闭环系统稳定且满足式(6.1.20)的反馈控制器 $u = K(s)y$ 可以通过解 $H_{\infty}$ 标准设计问题来得到。容易验证，如果定义 $z = \varepsilon^{-1}z_0$ ，并定义广义受控对象的状态空间实现为

$$
\left\{ \begin{array}{l} \dot {x} = A x + B _ {1} w + B _ {2} u, \\ z = \varepsilon^ {- 1} C _ {1} x + \varepsilon^ {- 1} D _ {1 2} u, \\ y = C _ {2} x + D _ {2 1} w, \end{array} \right. \tag {6.1.22}
$$

即

$$
P (s) = \left[ \begin{array}{c c} 0 & \varepsilon^ {- 1} D _ {1 2} \\ D _ {2 1} & 0 \end{array} \right] + \left[ \begin{array}{c} \varepsilon^ {- 1} C _ {1} \\ C _ {2} \end{array} \right] \{s I - A \} ^ {- 1} \left[ \begin{array}{c} B _ {1} \\ B _ {2} \end{array} \right],
$$

那么如图6.1.3所示系统的闭环传递函数 $T_{2w}(s)$ 满足

$$\| T _ {z w} (s) \| _ {\infty} = \sup _ {u \in L _ {2}} \frac {\| z \| _ {2} ^ {2}}{\| w \| _ {2} ^ {2}} \leqslant 1,$$

从而式 (6.1.21) 成立.
