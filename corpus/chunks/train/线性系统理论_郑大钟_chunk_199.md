# 5.7 线性二次型最优控制问题

LQ 问题 线性二次型最优控制问题简称为 LQ（Linear Quadratic）问题。在 LQ 问题中，受控系统为线性系统：

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0}, t \in [ 0, t _ {f} ] \tag {5.171}$$

其中 x 为 n 维状态，u 为 p 维输入，A 和 B 为相应维数的常量矩阵；性能指标为相对于状态和输入的一个二次型性能函数：

$$J (\boldsymbol {u} (\cdot)) = \frac {1}{2} \boldsymbol {x} ^ {T} \left(t _ {f}\right) S \boldsymbol {x} \left(t _ {f}\right) + \frac {1}{2} \int_ {0} ^ {t _ {f}} \left[ \boldsymbol {x} ^ {T} (t) Q \boldsymbol {x} (t) + \boldsymbol {u} ^ {T} (t) R \boldsymbol {u} (t) \right] d t \tag {5.172}$$

其中， $x(t_{i})$ 为 $t = t_{i}$ 时的末状态，加权阵 S 为 $n \times n$ 正半定对称阵，Q 为 $n \times n$ 正半定对称阵，R 为 $p \times p$ 正定对称阵。通常，加权阵 S, Q 和 R 是由设计者事先所选定的。性能指标 $J(u(\cdot))$ 是以函数 $u(\cdot)$ 为宗量的一个标量函数，对应于不同的控制函数 $u(\cdot)$ 性能指标 $J(u(\cdot))$ 取为不同的标量值，所以 $J(u(\cdot))$ 为 $u(\cdot)$ 的一个泛函。

所谓LQ最优控制问题，就是寻找一个控制 $u^{*}(\cdot)$ ，使得系统沿着由指定初态 $\pmb{x}_0$ 出发的相应轨线 $x^{*}(\cdot)$ ，其性能指标满足关系式：

$$J (\boldsymbol {u} ^ {*} (\cdot)) = \min _ {\boldsymbol {u} (\cdot)} J (\boldsymbol {u} (\cdot)) \tag {5.173}$$

并且，称这样的控制函数 $\boldsymbol{u}^{*}(\cdot)$ 为 LQ 问题的最优控制， $\boldsymbol{x}^{*}(\cdot)$ 为相应的最优轨线， $J(\boldsymbol{u}^{*}(\cdot))$ 为最优性能值。从数学上看，LQ 最优控制问题归结为，对由 (5.172) 所给出的泛函，在系统状态方程 (5.171) 的约束下，相对于 $\boldsymbol{u}(\cdot)$ 求条件极值的问题。

进一步, 还可把 LQ 问题区分为有限时间 LQ 问题和无限时间 LQ 问题。在有限时间 LQ 问题中, 末时刻 $t_f$ 是固定的且为有限值; 而在无限时间 LQ 问题中, 末时刻 $t_f = \infty$ 。下面的讨论中可以看到, 两类 LQ 问题的最优控制 $\pmb{u}^{*}(\cdot)$ 有着很大的区别, 同时对受控系统的要求也有着显著的不同。

此外，从工程应用的角度，则可把LQ最优控制问题分类为调节问题和跟踪问题。所谓调节问题，就是综合最优控制 $u^{*}(\cdot)$ ，使在其作用下把系统由初始状态 $x_{0}$ 驱动到零平衡状态 $x_{e}=0$ ，同时性能指标 $J(u^{*}(\cdot))$ 取为极小值。跟踪问题中，则要求在使系统的输出 $y(t)$ 跟踪已知的或未知的参考信号 $y_{0}(t)$ 的同时，使某个相应的二次型性能指标为极小。事实上，可以把跟踪问题看成为是调节问题的一种推广。因此，下面的讨论中，我们将主要研究 LQ 调节问题，在此基础上通过比较简单的推广就可导出相应于跟踪问题的对应结果。

有限时间LQ调节问题的最优解 考虑如下的LQ问题

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0}, t \in [ 0, t _ {f} ] \tag {5.174}J (\boldsymbol {u} (\cdot)) = \frac {1}{2} \boldsymbol {x} \left(\iota_ {f}\right) S \boldsymbol {x} \left(\iota_ {f}\right) + \frac {1}{2} \int_ {0} ^ {\iota_ {f}} \left(\boldsymbol {x} ^ {T} Q \boldsymbol {x} + \boldsymbol {u} ^ {T} R \boldsymbol {u}\right) d t \tag {5.175}$$

则其最优解 $u^{*}(\cdot)$ , $x^{*}(\cdot)$ 和 $J^{*}\triangleq J(u^{*}(\cdot))$ 由下列结论给出。
