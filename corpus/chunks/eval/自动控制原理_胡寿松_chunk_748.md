# (4) 性能指标

在状态空间中,可以采用不同的控制向量函数去实现使系统由已知初态到要求的末态(或目标集)的转移。性能指标则是衡量系统在不同控制向量作用下工作优良度的标准。

性能指标的内容与形式,取决于最优控制问题所要完成的任务。不同的最优控制问题,有不

同的性能指标,其一般形式可以归纳为

$$J = \varphi [ \boldsymbol {x} (t _ {f}), t _ {f} ] + \int_ {t _ {0}} ^ {t _ {f}} L [ \boldsymbol {x} (t), \boldsymbol {u} (t), t ] \mathrm{d} t \tag {10-3}$$

式中， $\varphi(\cdot)$ 和 $L(\cdot)$ 为连续可微的标量函数。 $\varphi[x(t_f), t_f]$ 称为末值项， $\int_{t_0}^{t_f} L[x(t), u(t), t] \mathrm{d}t$ 称为过程项，两者均有具体的物理含意。

根据最优控制问题的基本组成部分,可以概括最优控制问题的一般提法:在满足系统方程(10-1)的约束条件下,在容许控制域 $\Omega$ 中确定一个最优控制律 $u^{*}(t)$ ,使系统状态 $x(t)$ 从已知初态 $x_{0}$ 转移到要求的目标集(10-2),并使性能指标(10-3)达到极值。

通常,最优控制问题可用下列泛函形式表示:

$$\min _ {\boldsymbol {u} (t) \in \Omega} J = \varphi [ \boldsymbol {x} \left(t _ {f}\right), t _ {f} ] + \int_ {t _ {0}} ^ {t _ {f}} L [ \boldsymbol {x} (t), \boldsymbol {u} (t), t ] d t\text { s. t. } \quad ① \dot {\boldsymbol {x}} (t) = \boldsymbol {f} [ \boldsymbol {x} (t), \boldsymbol {u} (t), t ], \quad \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}② \psi [ x (t _ {f}), t _ {f} ] = 0$$
