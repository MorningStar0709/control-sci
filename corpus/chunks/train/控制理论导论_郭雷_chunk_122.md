如果 $A_{2} = 0$ ，那么 $x_{2}(t)$ 为常值外干扰，由式 (1.8.36) 知 $\dot{x}_{2e} = -G_{2}C\tilde{x}_{1e}$ 。这说明干扰补偿信号是估计误差 $\tilde{x}_{1e}$ 通过一个具有常增益阵的积分器给出的。这是大家熟知的。稳定的闭环系统如果对常值干扰是无静差的，那么在它的补偿器回路中必包含有积分器。一般情况下，为补偿外部干扰，在它的补偿器回路中应包含一个与外部模型相同的动力学模型。

定理 1.8.1 只是给出了系统 (1.8.29) 存在一个带有干扰补偿的动态补偿器的充分条件，并给出了设计方法。但这些条件是否必要呢？答案是肯定的。从定理 1.8.1 的证明中可以发现，动态补偿器 (1.8.34) \~ (1.8.36) 对状态 $x_{1}(t)$ 是输出调节的，只要注意到 $V_{1}=0$ 和 $V_{2}=0$ 就够了。所以也称这个动态补偿器为全状态输出调节器，下面分析带有全状态输出调节器的结构，进而说明定理 1.8.1 的条件也是必要的。

考虑系统 (1.8.29), 并且规定 $z(t) = x_{1}(t), C_{2} = 0, D_{1} = I_{n_{1}}, D_{2} = 0$ . 这时这个系统可以写成

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = A _ {1} x _ {1} (t) + A _ {3} x _ {2} + B _ {1} u (t), \\ \dot {x} _ {2} (t) = A _ {2} x _ {2} \\ y (t) = C _ {1} x _ {1} (t), \\ z (t) = x _ {1} (t). \end{array} \right. \tag {1.8.39}
$$

设系统 (1.8.2) 是系统 (1.8.39) 的一个动态补偿器。如果式 (1.8.2) 使闭环系统内部稳定和输出调节，那么这个动态补偿器叫做系统 (1.8.39) 的一个全状态输出调节器。关于全状态输出调节器的结构性质，有以下定理：

定理 1.8.2 已知定常线性系统 (1.8.39) 和它的动态补偿器 (1.8.2). (1.8.2) 成为系统 (1.8.39) 的一个全状态输出调节器的充分必要条件是，闭环系统

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {x} _ {1} (t) \\ \dot {x} _ {c} (t) \end{array} \right] = \left[ \begin{array}{c c} A _ {1} + B _ {1} F C _ {1} & B _ {1} F _ {c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c} \\ B _ {c} C _ {1} & A _ {c} \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {c} (t) \end{array} \right] + \left[ \begin{array}{c} A _ {3} \\ 0 \end{array} \right] x _ {2} (t),} \\ \dot {x} _ {2} (t) = A _ {2} x _ {2}, \\ z (t) = x _ {1} (t), \end{array} \right.
$$

是内部稳定的，并且存在 $l \times n_2$ 矩阵 $\pmb{V}_2$ ，使得

$$\boldsymbol {B} _ {1} \boldsymbol {F} _ {\mathrm{c}} \boldsymbol {V} _ {2} = \boldsymbol {A} _ {3}, \quad \boldsymbol {A} _ {\mathrm{c}} \boldsymbol {V} _ {2} = \boldsymbol {V} _ {2} \boldsymbol {A} _ {2}. \tag {1.8.40}$$

证明 必要性. 设动态补偿器 (1.8.2) 是系统 (1.8.39) 的一个全状态输出调节器, 那么闭环系统是内部稳定的, 即

$$
\sigma \left(\left[ \begin{array}{c c} A _ {1} + B _ {1} F C _ {1} & B _ {1} F _ {c} \\ B _ {c} C _ {1} & A _ {c} \end{array} \right]\right) \subset \mathbb {C} ^ {-},
$$

同时对任意 $x_{2}(t_{0}) = x_{20}$ 都有 $\lim_{t\to \infty}z(t) = 0.$ 依引理1.8.1知，存在 $n_1\times n_2,l\times n_2$ 矩阵 $\pmb{V}_{1}$ 和 $\pmb{V}_{2}$ ，使得

$$
\left\{ \begin{array}{l} (A _ {1} + B _ {1} F C _ {1}) V _ {1} - V _ {1} A _ {2} + B _ {1} F _ {\mathrm{c}} V _ {2} = A _ {3}, \\ B _ {1} C _ {1} V _ {1} + A _ {\mathrm{c}} V _ {2} - V _ {2} A _ {2} = 0, \\ V _ {1} = 0. \end{array} \right. \tag {1.8.41}
$$

因此有
