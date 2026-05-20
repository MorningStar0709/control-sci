$$\dot {x} = - x z, \quad \varepsilon \dot {z} = - (z - \sin^ {2} x) (z - e ^ {a x}) (z - 2 e ^ {2 a x}), \quad a > 0$$

11.14 （见文献[105]）考虑线性自治奇异扰动系统

$$\dot {x} = A _ {1 1} x + A _ {1 2} z\varepsilon \dot {z} = A _ {2 1} x + A _ {2 2} z$$

其中， $x \in R^{n}, z \in R^{m}$ ， $A_{22}$ 是赫尔维茨矩阵。

(a) 证明对于足够小的 $\varepsilon$ ，系统有一个精确慢流形 $z = -L(\varepsilon)x$ ，其中， $L$ 满足代数方程

$$- \varepsilon L (A _ {1 1} - A _ {1 2} L) = A _ {2 1} - A _ {2 2} L$$

(b) 证明变量代换 $\eta = z + L(\varepsilon)x$ 可将系统转换为块三角 (block triangular) 形式。

(c) 证明系统的特征值聚集为一组数量级为 $O(1)$ 的 $n$ 个慢特征值和数量级为 $O(1 / \varepsilon)$ 的 $m$ 个快特征值。

(d) 设 $H(\varepsilon)$ 为线性方程 $\varepsilon(A_{11} - A_{12}L)H - H(A_{22} + \varepsilon LA_{12}) + A_{12} = 0$

的解,证明相似变换 $\left[\begin{array}{c}\xi\\ \eta\end{array}\right]=\left[\begin{array}{ccc}I-\varepsilon HL & -\varepsilon H\\ L & I\end{array}\right]\left[\begin{array}{c}x\\ z\end{array}\right]$

将系统变换为块模式 $\dot{\xi}=A_{s}(\varepsilon)\xi,\quad\varepsilon\dot{\eta}=A_{f}(\varepsilon)\eta$

其中， $A_{s}$ 和 $A_{f}/\varepsilon$ 的特征值分别是整个奇异扰动系统的慢特征值和快特征值。

(e) 证明 x 上的快模式分量是 $O(\varepsilon)$ 。

(f) 在当前情况下,给出 Tikhonov 定理的独立证明。

11.15 考虑线性奇异扰动系统

$$\dot {x} = A _ {1 1} x + A _ {1 2} z + B _ {1} u (t), \quad x (0) = \xi\varepsilon \dot {z} = A _ {2 1} x + A _ {2 2} z + B _ {2} u (t), \quad z (0) = \eta$$

其中， $x \in R^{n}$ ， $z \in R^{m}$ ， $u \in R^{p}$ ， $A_{22}$ 是赫尔维茨矩阵，且对于所有 $t \geqslant 0$ ， $u(t)$ 一致有界。设 $\bar{x}(t)$ 是降阶系统 $\dot{x} = A_{0}x + B_{0}u(t), \quad x(0) = \xi$

的解。其中， $A_{0}=A_{11}-A_{12}A_{22}^{-1}A_{21},B_{0}=B_{1}-A_{12}A_{22}^{-1}B_{2}$ 。

(a) 证明在任何紧区间 $[0, t_1]$ 上，有 $x(t, \varepsilon) - \bar{x}(t) = O(\varepsilon)$ 。

(b) 证明如果 $A_0$ 是赫尔维茨矩阵, 则对于所有 $t \geqslant 0$ , 有 $x(t, \varepsilon) - \bar{x}(t) = O(\varepsilon)$ 。

提示: 利用前一个习题中的变换。

11.16 考虑奇异扰动系统

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = - x _ {2} + z, \quad \varepsilon \dot {z} = \arctan (1 - x _ {1} - z)$$

(a) 求降阶模型和边界层模型。

(b) 分析边界层模型的稳定特性。

(c) 设 $x_{1}(0)=x_{2}(0)=z(0)=0$ ，求该解的 $O(\varepsilon)$ 逼近。运用数值算法，计算当 $\varepsilon=0.1$ 时在时间区间 [0,10] 上的精确解和近似解。

(d) 研究逼近在无限时间区间上的有效性。

(e) 证明系统有唯一平衡点,并运用奇异扰动法分析其稳定性。该平衡点是渐近稳定的吗? 是全局渐近稳定的吗? 是指数稳定的吗? 对有效的稳定性分析,计算 $\varepsilon$ 的上界 $\varepsilon^{*}$ 。

11.17 对于奇异扰动系统 $\dot{x} = -2x + x^2 + z, \varepsilon \dot{z} = x - x^2 - z$

重复习题 11.16。在(c)中设 $x(0)=z(0)=1$ ，且时间区间为 $[0,5]$ 。

11.18 对于奇异扰动系统 $\dot{x}=xz^{3}$ $\varepsilon\dot{z}=-2x^{4/3}-2z$

重复习题 11.16。在(c)中设 $x(0)=z(0)=1$ ，且时间区间为 $[0,1]$ 。
