# (3) 非奇异线性变换的不变特性

从前面的研究中可以看到,为了便于研究系统固有特性,常常需要引入非奇异线性变换。例如:将A阵对角化或约当化,需进行P变换;将A,b化为可控标准型,需进行 $P^{-1}$ 变换;将A,c化为可观测标准型,需进行 $P^{T}$ 变换。虽然这些变换中的P阵各不相同,但都是非奇异矩阵。经过变换后,系统的固有特性是否会引起改变呢?这当然是人们在研究线性变换时所需要回答的一个重要问题。下面的研究将会表明,系统经过非奇异线性变换,其特征值、传递矩阵、可控性、可观测性等重要性质均保持不变。下面以P变换为例进行论证。

设系统动态方程为

$$\dot {x} = A x + B u, \quad y = C x + D u$$

令 $x = P\bar{x}$ ，变换后动态方程为

$$\dot {\bar {x}} = P ^ {- 1} A P \bar {x} + P ^ {- 1} B u, \quad y = \bar {y} = C P \bar {x} + D u$$

1) 变换后系统特征值不变。变换后系统的特征值为

$$
\begin{array}{l} \left| \lambda I - P ^ {- 1} A P \right| \\ = \mid \lambda P ^ {- 1} P - P ^ {- 1} A P \mid = \mid P ^ {- 1} \lambda P - P ^ {- 1} A P \mid \\ = | \boldsymbol {P} ^ {- 1} (\lambda \boldsymbol {I} - \boldsymbol {A}) \boldsymbol {P} | = | \boldsymbol {P} ^ {- 1} | | \lambda \boldsymbol {I} - \boldsymbol {A} | | \boldsymbol {P} | = | \boldsymbol {P} ^ {- 1} | | \boldsymbol {P} | | \lambda \boldsymbol {I} - \boldsymbol {A} | \\ = | \boldsymbol {P} ^ {- 1} \boldsymbol {P} | | \lambda \boldsymbol {I} - \boldsymbol {A} | = | \boldsymbol {I} | | \lambda \boldsymbol {I} - \boldsymbol {A} | = | \lambda \boldsymbol {I} - \boldsymbol {A} | \\ \end{array}
$$

可见,系统变换后与变换前的特征值完全相同,这说明对于非奇异线性变换,系统特征值具有不变性。

2) 变换后系统传递矩阵不变。变换后系统的传递矩阵为

$$
\begin{array}{l} \boldsymbol {G} ^ {\prime} (s) = \boldsymbol {C P} (s \boldsymbol {I} - \boldsymbol {P} ^ {- 1} \boldsymbol {A P}) ^ {- 1} \boldsymbol {P} ^ {- 1} \boldsymbol {B} + \boldsymbol {D} \\ = \boldsymbol {C P} (\boldsymbol {P} ^ {- 1} s \boldsymbol {I P} - \boldsymbol {P} ^ {- 1} \boldsymbol {A P}) ^ {- 1} \boldsymbol {P} ^ {- 1} \boldsymbol {B} + \boldsymbol {D} \\ = \boldsymbol {C P} [ \boldsymbol {P} ^ {- 1} (s \boldsymbol {I} - \boldsymbol {A}) \boldsymbol {P} ] ^ {- 1} \boldsymbol {P} ^ {- 1} \boldsymbol {B} + \boldsymbol {D} \\ = \boldsymbol {C P P} ^ {- 1} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {P P} ^ {- 1} \boldsymbol {B} + \boldsymbol {D} \\ = \boldsymbol {C} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} + \boldsymbol {D} = \boldsymbol {G} (s) \\ \end{array}
$$

这表明变换前与变换后系统的传递矩阵完全相同,系统的传递矩阵对于非奇异线性变换具有不变性。

3）变换后系统可控性不变。变换后系统可控性矩阵的秩为
