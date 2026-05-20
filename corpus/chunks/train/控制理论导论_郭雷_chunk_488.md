在方程 (7.1.9) 中 $\left.\frac{\partial f}{\partial x}\right|_{*}, \left.\frac{\partial f}{\partial u}\right|_{*}$ 分别为 $n \times n$ 和 $n \times r$ 矩阵值函数，即

$$\left. \frac {\partial f}{\partial x} \right| _ {*} = \left[ \frac {\partial f _ {i} (x ^ {*} (t) , u ^ {*} (t))}{\partial x _ {j}} \right],\left. \frac {\partial f}{\partial u} \right| _ {*} = \left[ \frac {\partial f _ {i} (x ^ {*} (t) , u ^ {*} (t))}{u _ {k}} \right].$$

将式 (7.1.7) 和式 (7.1.8) 代入 $J_{1}[u]$ 得到

$$
\begin{array}{l} J _ {1} (\varepsilon) \stackrel {\text { def }} {=} J _ {1} [ u ^ {*} + \varepsilon \delta u ] \\ = k \left(x ^ {*} \left(t _ {f}\right) + \varepsilon \delta x \left(t _ {f}\right) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x \left(t _ {f}\right) + o \left(\varepsilon^ {2}\right)\right) \\ + \psi^ {T} (t _ {f}) \cdot \left[ x ^ {*} (t _ {f}) + \varepsilon \delta x (t _ {f}) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x (t _ {f}) + o (\varepsilon^ {2}) \right] \\ - \psi^ {\mathrm{T}} (t _ {0}) x _ {0} - \int_ {t _ {0}} ^ {t _ {f}} \dot {\psi} ^ {\mathrm{T}} (t) \left[ x ^ {*} (t) + \varepsilon \delta x (t) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x (t) + o (\varepsilon^ {2}) \right] \mathrm{d} t \\ - \int_ {t _ {0}} ^ {t _ {f}} H (x ^ {*} (t) + \varepsilon \delta x (t) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x (t) + o (\varepsilon^ {2}), u ^ {*} (t) + \varepsilon \delta u (t), \psi (t)) d t. \\ \end{array}
$$

注意到

$$
\begin{array}{l} J _ {1} (0) = k \left(x ^ {*} \left(t _ {f}\right)\right) + \psi^ {\mathrm{T}} \left(t _ {f}\right) x ^ {*} \left(t _ {f}\right) - \psi^ {\mathrm{T}} \left(t _ {0}\right) x _ {0} \\ - \int_ {t _ {0}} ^ {t _ {f}} \dot {\psi} ^ {\mathbf {T}} (t) x ^ {*} (t) \mathrm{d} t - \int_ {t _ {0}} ^ {t _ {f}} H (x ^ {*} (t), u ^ {*} (t), \psi (t)) \mathrm{d} t, \\ \end{array}
$$

于是有

$$
\begin{array}{l} \Delta J _ {1} (\varepsilon) \stackrel {\text { def }} {=} J _ {1} (\varepsilon) - J _ {1} (0) = J _ {1} [ u ^ {*} + \varepsilon \delta u ] - J _ {1} [ u ^ {*} ] \\ = \Delta k (\varepsilon) + \psi^ {\mathrm{T}} (t _ {f}) \cdot \left[ \varepsilon \delta x (t _ {f}) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x (t _ {f}) + o (\varepsilon^ {2}) \right] \\ - \int_ {t _ {0}} ^ {t} \dot {\psi} ^ {\mathrm{T}} (t) \left[ \varepsilon \delta x (t) + \frac {\varepsilon^ {2}}{2} \delta^ {2} x (t) + o (\varepsilon^ {2}) \right] \mathrm{d} t - \int_ {t _ {0}} ^ {t _ {f}} \Delta H (\cdot) \mathrm{d} t, \tag {7.1.11} \\ \end{array}
$$

其中
