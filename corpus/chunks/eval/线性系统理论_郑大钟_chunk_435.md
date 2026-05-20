第4步：计算最优反馈阵

$$K ^ {*} = R ^ {- 1} B ^ {T} \left[ \Lambda_ {1}, \dots , \Lambda_ {n} \right] \left[ X _ {1}, \dots , X _ {n} \right] ^ {- 1}$$

而最优控制律即为 $u^{*} = -K^{*}x^{*}(t)$ 。

结论 4 如果在结论 2 和 3 中 $\{\mu_{1},\cdots,\mu_{n}\}$ 不是两两相异的，则只要将 $X_{i}$ 和 $\Lambda_{i}$ 用矩阵 M 的线性无关广义特征向量来代替，相应的结论和算法仍成立。

复频率域 LQ 问题的直接求解 在这一部分中，我们将从 LQ 问题的复频率域形式出发来直接求解最优反馈矩阵 $K^{*}$ 。为此，首先把由(11.251)和(11.252)所描述的 LQ 问题变换成为复频率域形式，即复频率域 LQ 问题。随后，在此基础上，来导出计算 $K^{*}$ 的基本公式。

由前面的分析中可知，当LQ问题实现最优即性能指标（11.252）取极小时，其最优控制 $\pmb{u}^{*}$ 、最优状态轨线 $x^{*}$ 和协状态 $\lambda$ 之间，成立如下的关系式：

$$\dot {\boldsymbol {x}} ^ {*} = A \boldsymbol {x} ^ {*} + B \boldsymbol {u} ^ {*}, \boldsymbol {x} ^ {*} (0) = \boldsymbol {x} _ {0} \tag {11.278}\dot {\boldsymbol {\lambda}} = - A ^ {T} \boldsymbol {\lambda} - C ^ {T} C \boldsymbol {x} ^ {*}, \quad \boldsymbol {\lambda} (\infty) = 0 \tag {11.279}\boldsymbol {u} ^ {*} = - R ^ {- 1} B ^ {T} \boldsymbol {\lambda} \tag {11.280}$$

现形式地引入输出向量 $y = C x^{*}$ 和 $\eta = -B^{T} \lambda$ ，则上述关系式还可改写成如下的形式：

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} ^ {*} = A \boldsymbol {x} ^ {*} + B \boldsymbol {u} ^ {*}, \quad \boldsymbol {x} ^ {*} (0) = \boldsymbol {x} _ {0} \\ \boldsymbol {y} = C \boldsymbol {x} ^ {*} \end{array} \right. \tag {11.281}

\left\{ \begin{array}{l} \dot {\boldsymbol {\lambda}} = - A ^ {T} \boldsymbol {\lambda} - C ^ {T} \boldsymbol {y}, \quad \boldsymbol {\lambda} (\infty) = \mathbf {0} \\ \boldsymbol {\eta} = - B ^ {T} \boldsymbol {\lambda} \end{array} \right. \tag {11.282}
\boldsymbol {u} ^ {*} = R ^ {- 1} \eta \tag {11.283}
$$

不难看出，相应于式(11.281)—(11.283)的系统结构图如图11.25所示。其中

$$G _ {o} (s) = C (s I - A) ^ {- 1} B \tag {11.284}$$

为受控系统的传递函数矩阵,而附加引入的传递函数矩阵 $\widetilde{G}_{o}(s)$ 则为:

$$
\begin{array}{l} \widetilde {G} _ {o} (s) = B ^ {T} \left(s I + A ^ {T}\right) ^ {- 1} C ^ {T} = \left[ C (s I + A) ^ {- 1} B \right] ^ {T} \\ = - [ C (- s I - A) ^ {- 1} B ] ^ {T} = - G _ {o} ^ {T} (- s) \tag {11.285} \\ \end{array}
$$

进一步,由图 11.25 的系统结构图可导出,从 v 到 $\varepsilon$ 的闭环传递函数矩阵 $G_{f}(s)$ 为:

$$
\begin{array}{l} G _ {f} (s) = \left[ I + R ^ {- 1} G _ {o} ^ {T} (- s) G _ {o} (s) \right] ^ {- 1} \left(- R ^ {- 1} G _ {o} ^ {T} (- s) G _ {o} (s)\right) \\ = \left[ R + G _ {o} ^ {T} (- s) G _ {o} (s) \right] ^ {- 1} \left(- G _ {o} ^ {T} (- s) G _ {o} (s)\right) \tag {11.286} \\ \end{array}
$$

这表明,系统的最优特征值 $\{\mu_{1},\cdots,\mu_{n}\}$ ，也即方程 $\det(sI-M)=0$ 的位于左半开复平面的 n 个根，就等同于方程

$$\det \left(R + G _ {o} ^ {T} (- s) G _ {o} (s)\right) = 0 \tag {11.287}$$

的 n 个根。
