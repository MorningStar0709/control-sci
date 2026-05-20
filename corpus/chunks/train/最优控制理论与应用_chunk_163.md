# 9.2 奇异线性二次型最优控制问题

把奇异和线性二次型这两个概念结合在一起就得到了奇异线性二次型问题这个概念。一个奇异线性二次型问题的奇异性等价于性能指标中的被积函数 $X^{\mathrm{T}}QX + U^{\mathrm{T}}RU$ 中矩阵 $\pmb{R}$ 的奇异性。奇异线性二次型问题可以是直接提出的，也可以作为对一般的最优控制问题应用二次变分原理的结果而产生的。

奇异二次型最优控制是一类常见的最优化奇异解问题,该问题可以

用数学语言描述如下：

考虑线性受控系统

$$\dot {\boldsymbol {X}} (t) = \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) \tag {9-8}$$

系数矩阵 A, B 是具有适当维数的常数矩阵。控制变量受如下不等式约束

$$\left| u _ {j} (t) \right| \leqslant 1, \quad j = 1, 2, \dots , r \tag {9-9}$$

性能指标仅取为状态的二次型,即

$$J = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {X} + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {X} ] \mathrm{d} t \tag {9-10}$$

假定其中的加权阵 P 和 Q 都是非负定对称阵。

哈密顿函数 H 为 U 的线性函数, 即

$$H = \frac {1}{2} X ^ {\mathrm{T}} Q X + \lambda^ {\mathrm{T}} (A X + B U) \tag {9-11}$$

根据极小值原理可知,在正常弧段上最优控制具有 Bang-Bang 形式,即

$$u ^ {*} = - \operatorname{sgn} \left\{\boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {\lambda} \right\} \tag {9-12}$$

协态方程与边界条件为

$$\dot {\boldsymbol {\lambda}} = - \frac {\partial H}{\partial \boldsymbol {X}} = - [ \boldsymbol {Q} \boldsymbol {X} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {\lambda} ], \quad \boldsymbol {\lambda} (T) = \boldsymbol {P} \boldsymbol {X} (T) \tag {9-13}$$

的解。

若存在奇异解,则在奇异弧段上有下式成立,

$$\frac {\partial \boldsymbol {H}}{\partial \boldsymbol {U}} = \boldsymbol {B} ^ {\mathrm{T}} \lambda \equiv \mathbf {0} \tag {9-14}\frac {\partial^ {2} H}{\partial U ^ {2}} = 0 \tag {9-15}$$

这时，控制满足极小值原理，但是，由极小值原理解不出最优控制的具体形式，需要用其他方法来计算奇异弧。

假设在某区间 $[t_1, t_2] \subset [t_0, t_f]$ 上存在奇异最优控制，则式(9-14)的关系在此区间上必然存在，进而必须满足 $\frac{\partial H}{\partial U}$ 的各阶导数为0的附加条件，由此条件可以得到奇异最优控制。

实际上,上述问题的奇异弧段必满足
