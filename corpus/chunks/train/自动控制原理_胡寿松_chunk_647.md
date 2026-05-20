# 5. 线性定常连续系统的可观测性判据

考虑输入 u = 0 时系统的状态方程和输出方程

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x}, \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0}, \quad t \geqslant 0, \quad \boldsymbol {y} = \boldsymbol {C} \boldsymbol {x} \tag {9-124}$$

式中，x 为 n 维状态向量；y 为 q 维输出向量；A 和 C 分别为 $n \times n$ 和 $q \times n$ 的常值矩阵。

格拉姆矩阵判据 线性定常连续系统(9-124)完全可观测的充分必要条件是,存在有限时刻 $t_{1}>0$ ,使如下定义的格拉姆矩阵:

$$\boldsymbol {M} \left(0, t _ {1}\right) \triangleq \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {C} \mathrm{e} ^ {\boldsymbol {A} t} \mathrm{d} t \tag {9-125}$$

为非奇异。

证明 充分性: 已知 $M(0, t_{1})$ 非奇异, 欲证系统为完全可观测。

由式(9-124)可得

$$\mathbf {y} (t) = \boldsymbol {C} \boldsymbol {\Phi} (t, 0) \boldsymbol {x} _ {0} = \boldsymbol {C} \mathrm{e} ^ {A t} \boldsymbol {x} _ {0} \tag {9-126}$$

将式(9-126)左乘 $e^{A^{T}t}C^{T}$ ，然后从0到 $t_{1}$ 积分，得

$$\int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {y} (t) \mathrm{d} t = \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {C} \mathrm{e} ^ {\boldsymbol {A} t} \mathrm{d} t \boldsymbol {x} _ {0} = \boldsymbol {M} (0, t _ {1}) \boldsymbol {x} _ {0} \tag {9-127}$$

已知 $M(0, t_1)$ 非奇异，即 $M^{-1}(0, t_1)$ 存在，故由式(9-127)得

$$\boldsymbol {x} _ {0} = \boldsymbol {M} ^ {- 1} (0, t _ {1}) \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {y} (t) \mathrm{d} t$$

这表明，在 $M(0, t_1)$ 非奇异的条件下，总可以根据 $[0, t_1]$ 上的输出 $y(t)$ ，唯一地确定非零初始状态 $x_0$ 。因此，系统为完全可观测。充分性得证。

必要性：已知系统完全可观测，欲证 $M(0,t_{1})$ 非奇异。

采用反证法。反设 $M(0, t_1)$ 奇异，假设存在某一非零 $\bar{x}_0 \in R^n$ ，使

$$
\begin{array}{l} \boldsymbol {x} _ {0} ^ {\mathrm{T}} \boldsymbol {M} (0, t _ {1}) \bar {\boldsymbol {x}} _ {0} = \int_ {0} ^ {t _ {1}} \bar {\boldsymbol {x}} _ {0} ^ {\mathrm{T}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {C} \mathrm{e} ^ {\boldsymbol {A} t} \bar {\boldsymbol {x}} _ {0} \mathrm{d} t \\ = \int_ {0} ^ {t _ {1}} \mathbf {y} ^ {\mathrm{T}} (t) \mathbf {y} (t) \mathrm{d} t \\ = \int_ {0} ^ {t _ {1}} \| \mathbf {y} (t) \| ^ {2} d t = 0 \tag {9-128} \\ \end{array}
$$

成立，这意味着

$$\mathbf {y} (t) = \mathbf {C e} ^ {A t} \overline {{{\mathbf {x}}}} _ {0} \equiv \mathbf {0}, \quad \forall t \in [ 0, t _ {1} ]$$
