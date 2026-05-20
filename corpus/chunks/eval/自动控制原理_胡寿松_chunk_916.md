# (2) 系统模型转换

由于传递函数模型描述的是系统的外部特性,而状态空间模型描述的是系统的内部特性,它们之间存在着内在的等效关系。利用 MATLAB 中的 tf2ss 命令可以实现传递函数模型到状态空间模型的转换,ss2tf 命令实现状态空间模型到传递函数模型的转换,ss2ss 实现状态空间模型之间的相似变换。相似变换后的系统状态空间模型矩阵与原模型矩阵关系为

$$\overline {{{\boldsymbol {A}}}} = \boldsymbol {T} \boldsymbol {A} \boldsymbol {T} ^ {- 1}, \quad \overline {{{\boldsymbol {B}}}} = \boldsymbol {T} \boldsymbol {B}, \quad \overline {{{\boldsymbol {C}}}} = \boldsymbol {C} \boldsymbol {T} ^ {- 1}$$

式中， $T$ 为非奇异变换矩阵； $\mathbf{A},\mathbf{B},\mathbf{C}$ 为原模型系数矩阵； $\overline{\mathbf{A}},\overline{\mathbf{B}},\overline{\mathbf{C}}$ 为变换后模型的系数矩阵。

命令格式： $[A,B,C,D] = tf2ss(num,den)$

$$[ \text { num,den } ] = \text { ss2tf(A,B,C,D) }\mathrm{sysT} = \mathrm{ss2ss(sys,T)}$$

其中，num, den 分别为分子分母多项式降幂排列的系数向量；T 表示相似变换矩阵。
