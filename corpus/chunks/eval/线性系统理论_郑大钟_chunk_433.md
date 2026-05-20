$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = \frac {\partial H (\boldsymbol {x} , \boldsymbol {u} , \lambda)}{\partial \lambda} = A \boldsymbol {x} + B \boldsymbol {u}, \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \\ \dot {\lambda} = - \frac {\partial H (\boldsymbol {x} , \boldsymbol {u} , \lambda)}{\partial \boldsymbol {x}} = - A ^ {T} \lambda - C ^ {T} C \boldsymbol {x}, \quad \lambda (\infty) = 0 \end{array} \right. \tag {11.260}
$$

并且,性能指标 J 取极小也即控制取最优时,成立如下关系式:

$$\frac {\partial H (\boldsymbol {x} , \boldsymbol {u} , \lambda)}{\partial \boldsymbol {u}} = R \boldsymbol {u} ^ {*} + B ^ {T} \lambda = 0 \tag {11.261}$$

由此，即可导出最优控制 $u^{*}$ 为：

$$\boldsymbol {u} ^ {*} = - R ^ {- 1} B ^ {T} \lambda \tag {11.262}$$

现将（11.262）代入（11.260），可得到实现最优时的系统方程为：

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} ^ {*} = A \boldsymbol {x} ^ {*} - B R ^ {- 1} B ^ {T} \lambda , \quad \boldsymbol {x} ^ {*} (0) = \boldsymbol {x} _ {0} \\ \dot {\boldsymbol {\lambda}} = - C ^ {T} C \boldsymbol {x} ^ {*} - A ^ {T} \lambda , \quad \lambda (\infty) = 0 \end{array} \right. \tag {11.263}
$$

或者，将其表示为增广方程的形式为

$$
\left[ \begin{array}{c} \dot {x} ^ {*} \\ \dot {\lambda} \end{array} \right] = \left[ \begin{array}{c c} A & - B R ^ {- 1} B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right] \left[ \begin{array}{l} x ^ {*} \\ \lambda \end{array} \right], \left[ \begin{array}{l} x ^ {*} (0) \\ \lambda (\infty) \end{array} \right] = \left[ \begin{array}{l} x _ {0} \\ 0 \end{array} \right] \tag {11.264}
$$

这表明, 此 LQ 问题实现最优时系统的最优特征值即为

$$
\det \left(s I - \left[ \begin{array}{c c} A & - B R ^ {- 1} B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right]\right) = 0 \tag {11.265}
$$

的 $2n$ 个根中的 $n$ 个。再由矩阵 $M$ 的性质可知，方程（11.265）的根必对称于复平面的虚轴；即若 $\mu_{i}$ 为它的一个根，则一 $\mu_{i}$ 也必为其根。所以，总共 $2n$ 个根中， $n$ 个分布于左半复平面，另外 $n$ 个分布于右半复平面。但由状态空间法的分析结果知，最优系统必是渐近稳定的。这样，就证明了系统的最优特征值即为方程（11.265）的位于左半开复平面的 $n$ 个根。于是证明完成。

结论2 给定由(11.251)和(11.252)所描述的LQ问题,按图11.24所示构成状态反馈闭环系统。现设系统的最优特征值是 $\{\mu_1,\dots ,\mu_n\}$ 且为两两相异,并假定它们不等同于受控系统矩阵 $A$ 的特征值;再表 $\left[ \begin{array}{c}X_{i}\\ \Lambda_{i} \end{array} \right]$ 为矩阵 $M$ 的属于 $\mu_{l}$ 的特征向量,其中 $M$ 如(11.257)所定义。则给定LQ问题的最优控制律 $\pmb{u}^{*}$ 可按下式来确定:

$$
\left\{ \begin{array}{l} u ^ {*} = - K ^ {*} x ^ {*} (t) \\ K ^ {*} = R ^ {- 1} B ^ {T} \left[ \Lambda_ {1} \dots \Lambda_ {n} \right] \left[ X _ {1} \dots X _ {n} \right] ^ {- 1} \end{array} \right. \tag {11.266}
$$
