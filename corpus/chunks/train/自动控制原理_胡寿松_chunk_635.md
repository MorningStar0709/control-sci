# 3. 线性定常连续系统的可控性判据

考虑线性定常连续系统的状态方程

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t), \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0}, \quad t \geqslant 0 \tag {9-83}$$

其中，x 为 n 维状态向量；u 为 p 维输入向量；A 和 B 分别为 $n \times n$ 和 $n \times p$ 常值矩阵。下面根据 A 和 B 给出系统可控性的常用判据。

格拉姆矩阵判据 线性定常连续系统式(9-83)完全可控的充分必要条件是,存在时刻 $t_{1}>0$ ,使如下定义的格拉姆矩阵:

$$\boldsymbol {W} \left(0, t _ {1}\right) \triangleq \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} \boldsymbol {B} ^ {T} \mathrm{e} ^ {- \boldsymbol {A} ^ {T} t} \mathrm{d} t \tag {9-84}$$

为非奇异。

证明 充分性: 已知 $W(0, t_{1})$ 为非奇异, 欲证系统完全可控。

已知 W 非奇异, 故 $W^{-1}$ 存在。对任一非零初始状态 $x_{0}$ 可选取控制 $u(t)$ 为

$$\boldsymbol {u} (t) = - \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {W} ^ {- 1} \left(0, t _ {1}\right) \boldsymbol {x} _ {0}, \quad t \in \left[ t _ {0}, t _ {1} \right] \tag {9-85}$$

则在 $u(t)$ 作用下系统(9-83) 在 $t_{1}$ 时刻的解为

$$
\begin{array}{l} \boldsymbol {x} \left(t _ {1}\right) = \mathrm{e} ^ {\boldsymbol {A} t _ {1}} \boldsymbol {x} _ {0} + \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} \left(t _ {1} - t\right)} \boldsymbol {B u} (t) \mathrm{d} t \\ = \mathrm{e} ^ {\boldsymbol {A} t _ {1}} \boldsymbol {x} _ {0} - \mathrm{e} ^ {\boldsymbol {A} t _ {1}} \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} \boldsymbol {B} ^ {T} \mathrm{e} ^ {- \boldsymbol {A} ^ {T} t} \mathrm{d} t \boldsymbol {W} ^ {- 1} (0, t _ {1}) \boldsymbol {x} _ {0} \\ = \mathrm{e} ^ {A t _ {1}} x _ {0} - \mathrm{e} ^ {A t _ {1}} W (0, t _ {1}) W ^ {- 1} (0, t _ {1}) x _ {0} = 0, \quad \forall x _ {0} \in R ^ {n} \\ \end{array}
$$

这表明，对任一取定的初始状态 $x_0 \neq 0$ ，都存在有限时刻 $t_1 > 0$ 和控制 $u(t)$ ，使状态由 $x_0$ 转移到 $t_1$ 时刻的状态 $x(t_1) = 0$ ，于是根据定义可知系统完全可控。充分性得证。

必要性:已知系统完全可控,欲证 $W(0,t_{1})$ 为非奇异。

采用反证法。设 $W(0, t_1)$ 为奇异，则存在某个非零向量 $\pmb{x}_0 \in R^n$ ，使

$$\boldsymbol {W} \left(0, t _ {1}\right) \bar {\boldsymbol {x}} _ {0} = \mathbf {0} \tag {9-86}$$

成立，由此可导出
