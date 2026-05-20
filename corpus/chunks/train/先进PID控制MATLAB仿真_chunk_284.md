# 5.4.2 扩张观测器的分析

参考文献[7]，定义

$$
\boldsymbol {\eta} = \left[ \begin{array}{c c c} \eta_ {1} & \eta_ {2} & \eta_ {3} \end{array} \right] ^ {\mathrm{T}}
$$

式中

$$\eta_ {1} = \frac {x _ {1} - \hat {x} _ {1}}{\varepsilon^ {2}}, \eta_ {2} = \frac {x _ {2} - \hat {x} _ {2}}{\varepsilon}, \eta_ {3} = f - \hat {\sigma}$$

由于

$$
\begin{array}{l} \varepsilon \dot {\eta} _ {1} = \frac {\dot {x} _ {1} - \dot {\hat {x}} _ {1}}{\varepsilon} = \frac {1}{\varepsilon} \left(x _ {2} - \left(\hat {x} _ {2} + \frac {\alpha_ {1}}{\varepsilon} (y - \hat {x} _ {1})\right)\right) \\ = \frac {1}{\varepsilon} \left(x _ {2} - \hat {x} _ {2} - \frac {\alpha_ {1}}{\varepsilon} (y - \hat {x} _ {1})\right) = - \frac {\alpha_ {1}}{\varepsilon^ {2}} \left(x _ {1} - \hat {x} _ {1}\right) + \frac {1}{\varepsilon} \left(x _ {2} - \hat {x} _ {2}\right) = - \alpha_ {1} \eta_ {1} + \eta_ {2} \\ \varepsilon \dot {\eta} _ {2} = \varepsilon \frac {\dot {x} _ {2} - \dot {\hat {x}} _ {2}}{\varepsilon} = \left(b u + f (\cdot) - \left(b u + \hat {\sigma} + \frac {\alpha_ {2}}{\varepsilon^ {2}} (y - \hat {x} _ {1})\right)\right) \\ = \left(f (\cdot) - \hat {\sigma} - \frac {\alpha_ {2}}{\varepsilon^ {2}} (y - \hat {x} _ {1})\right) = - \frac {\alpha_ {2}}{\varepsilon^ {2}} (x _ {1} - \hat {x} _ {1}) + (f - \hat {\sigma}) = - \alpha_ {2} \eta_ {1} + \eta_ {3} \\ \end{array}
\varepsilon \dot {\eta} _ {3} = \varepsilon (\dot {f} - \dot {\hat {\sigma}}) = \varepsilon \left(\dot {f} - \frac {\alpha_ {3}}{\varepsilon^ {3}} (y - \hat {x} _ {1})\right) = \varepsilon \dot {f} - \frac {\alpha_ {3}}{\varepsilon^ {2}} (y - \hat {x} _ {1}) = - \alpha_ {3} \eta_ {1} + \varepsilon \dot {f}
$$

则观测误差状态方程可写为

$$\varepsilon \dot {\eta} = \overline {{{A}}} \eta + \varepsilon \overline {{{B}}} \dot {f} \tag {5.39}$$

式中

$$
\overline {{{A}}} = \left[ \begin{array}{l l l} - \alpha_ {1} & 1 & 0 \\ - \alpha_ {2} & 0 & 1 \\ - \alpha_ {3} & 0 & 0 \end{array} \right], \overline {{{B}}} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right]
$$

矩阵 $\overline{A}$ 的特征方程为

$$
\left| \lambda I - \overline {{A}} \right| = \left| \begin{array}{c c c} \lambda + \alpha_ {1} & - 1 & 0 \\ \alpha_ {2} & \lambda & - 1 \\ \alpha_ {3} & 0 & \lambda \end{array} \right| = 0
$$

则

$$\left(\lambda + \alpha_ {1}\right) \lambda^ {2} + \alpha_ {3} + \alpha_ {2} \lambda = 0$$

且

$$\lambda^ {3} + \alpha_ {1} \lambda^ {2} + \alpha_ {2} \lambda + \alpha_ {3} = 0 \tag {5.40}$$
