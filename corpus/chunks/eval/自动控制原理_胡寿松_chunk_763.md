# 2) 泛函变分的求法

定理10-1 设 $J[\pmb{x}]$ 是线性赋范空间 $\mathbf{R}^n$ 上的连续泛函，若在 $\pmb{x} = \pmb{x}_0$ 处 $J[\pmb{x}]$ 可微，其中 $\pmb{x}, \pmb{x}_0 \in \mathbb{R}^n$ ，则 $J[\pmb{x}]$ 的变分为

$$\delta J \left[ x _ {0}, \delta x \right] = \frac {\partial}{\partial \varepsilon} J \left[ x _ {0} + \varepsilon \delta x \right] | _ {\varepsilon = 0}, \quad 0 \leqslant \varepsilon \leqslant 1 \tag {10-18}$$

证明 因在 $x_0$ 处 $J[x]$ 可微，故必在 $x_0$ 处存在变分。因 $J[x]$ 连续，故由式(10-17)知 $J[x]$ 的增量为

$$
\begin{array}{l} \Delta J = J \left[ x _ {0} + \varepsilon \delta x \right] - J \left[ x _ {0} \right] \\ = L \left[ x _ {0}, \varepsilon \delta x \right] + r \left[ x _ {0}, \varepsilon \delta x \right] \\ \end{array}
$$

由于 $L[x_0, \varepsilon \delta x]$ 是 $\varepsilon \delta x$ 的线性连续泛函，故

$$L [ \boldsymbol {x} _ {0}, \varepsilon \delta \boldsymbol {x} ] = \varepsilon L [ \boldsymbol {x} _ {0}, \delta \boldsymbol {x} ]$$

又因 $r[x_0, \varepsilon \delta x]$ 是 $\varepsilon \delta x$ 的高阶无穷小，故

$$\lim _ {\varepsilon \rightarrow 0} \frac {r [ x _ {0} , \varepsilon \delta x ]}{\varepsilon} = 0$$

于是

$$
\begin{array}{l} \frac {\partial}{\partial \varepsilon} J [ x _ {0} + \varepsilon \delta x ] | _ {\varepsilon = 0} = \lim _ {\varepsilon \rightarrow 0} \frac {J [ x _ {0} + \varepsilon \delta x ] - J [ x _ {0} ]}{\varepsilon} \\ = \lim _ {\varepsilon \rightarrow 0} \frac {1}{\varepsilon} \left\{L \left[ x _ {0}, \varepsilon \delta x \right] + r \left[ x _ {0}, \varepsilon \delta x \right]\right\} \\ = \delta J [ x _ {0}, \delta x ] \\ \end{array}
$$

3) 泛函变分的规则。由变分定义可以看出，泛函的变分是一种线性映射，因而其运算规则类似于函数的线性运算。设 $L_{1}$ 和 $L_{2}$ 是函数 $\pmb{x},\dot{\pmb{x}}$ 和 $t$ 的函数，则有如下变分规则：

① $\delta (L_1 + L_2) = \delta L_1 + \delta L_2$   
② $\delta (L_{1}L_{2}) = L_{1}\delta L_{2} + L_{2}\delta L_{1};$   
③ $\delta \int_{a}^{b} L[x, \dot{x}, t] \mathrm{d}t = \int_{a}^{b} \delta L[x, \dot{x}, t] \mathrm{d}t;$   
④ $\delta\frac{dx}{dt}=\frac{d}{dt}\delta x.$

例10-1 已知连续泛函为

$$J = \int_ {t _ {0}} ^ {t _ {f}} L [ x, \dot {x}, t ] \mathrm{d} t$$

式中，x 和 $\dot{x}$ 为标量函数。试求泛函变分 $\delta J$ 。

解 根据定理 10-1, 可得
