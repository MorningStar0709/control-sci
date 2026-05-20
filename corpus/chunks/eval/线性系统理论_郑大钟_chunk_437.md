$$\hat {\mathbf {y}} (s) = N (s) \hat {\zeta} (s), D (s) \hat {\zeta} (s) = \hat {\mathbf {u}} ^ {*} (s) \tag {11.292}$$

其中 $\hat{\zeta}(s)$ 为受控系统的部分状态的拉普拉斯变换， $\hat{y}(s)$ 和 $\hat{u}^{*}(s)$ 分别为输出和输入的拉普拉斯变换。再表

$$D _ {f} (s) = \left(D ^ {T} (- s) R D (s) + N ^ {T} (- s) N (s)\right) D ^ {- 1} (s) \tag {11.293}$$

那么可得

$$
\begin{array}{l} D _ {f} (s) \hat {\boldsymbol {u}} ^ {*} (s) = \left(D ^ {T} (- s) R D (s) + N ^ {T} (- s) N (s)\right) D ^ {- 1} (s) \hat {\boldsymbol {u}} ^ {*} (s) \\ = (D ^ {T} (- s) R D (s) + N ^ {T} (- s) N (s)) \hat {\zeta} (s) \tag {11.294} \\ \end{array}
$$

显然，方程

$$\left(D ^ {T} (- s) R D (s) + N ^ {T} (- s) N (s)\right) \hat {\zeta} (s) = 0 \tag {11.295}$$

仅当 $s = \mu_{i} (i = 1, \cdots, n)$ 时具有非平凡解 $\hat{\zeta}(\mu_{i})$ 。于是，在定出 $\hat{\zeta}(\mu_{i})$ 后，由 (11.292) 和 (11.268) 可得

$$D \left(\mu_ {i}\right) \hat {\xi} \left(\mu_ {i}\right) = U _ {i} = - K ^ {*} X _ {i} \tag {11.296}$$

从而又可导出

$$- K ^ {*} \left[ X _ {1}, \dots , X _ {n} \right] = \left[ D \left(\mu_ {1}\right) \hat {\zeta} \left(\mu_ {1}\right), \dots , D \left(\mu_ {n}\right) \hat {\zeta} \left(\mu_ {n}\right) \right] \tag {11.297}$$

其中 $X_{i}$ ( $i = 1, \cdots, n$ ) 线性无关，为闭环矩阵相应于 $\mu_{i}$ 的特征向量。但由 $G_{j}(s)$ 的控制器形实现的属性可知，特征向量 $X_{i}$ 满足如下的关系式：

$$X _ {i} = \Psi (\mu_ {i}) \hat {\zeta} (\mu_ {i}), i = 1, \dots , n \tag {11.298}$$

其中

$$
\Psi (s) = \left[ \begin{array}{c c c} s ^ {k _ {1} - 1} & & \\ \vdots & & \\ \vdots & & \\ s & & \\ 1 & & \\ \hdashline & \ddots & \\ & & s ^ {k _ {p} - 1} \\ & & \vdots \\ & & s \\ & & 1 \end{array} \right] \tag {11.299}
$$

而 $k_{j}(j=1,\cdots,p)$ 为 $D(s)$ 的列次数。这样，由式(11.297)和(11.298)就即可导出计算最优反馈阵 $K^{*}$ 的基本公式为：

$$
\begin{array}{l} K ^ {*} = - \left[ D \left(\mu_ {1}\right) \hat {\zeta} \left(\mu_ {1}\right), \dots , D \left(\mu_ {n}\right) \hat {\zeta} \left(\mu_ {n}\right) \right] \\ \cdot \left[ \Psi \left(\mu_ {1}\right) \hat {\zeta} \left(\mu_ {1}\right), \dots , \Psi \left(\mu_ {n}\right) \hat {\zeta} \left(\mu_ {n}\right) \right] ^ {- 1} \tag {11.300} \\ \end{array}
$$

最后,我们来给出在复频率域内直接求解 LQ 问题的算法,它可归纳如下:

第1步：由给定的系数矩阵和加权矩阵 $A, B, Q = C^T C$ 和 $R$ ，计算

$$G _ {o} (s) = C (s I - A) ^ {- 1} B,$$

并找出它的一个不可简约右 MFD $G_{o}(s)=N(s)D^{-1}(s)$ 。

第2步：计算代数方程

$$\det (D ^ {T} (- s) R D (s) + N ^ {T} (- s) N (s)) = 0$$

的在左半开复平面上的 n 个根 $\{\mu_{1},\cdots,\mu_{n}\}$ ，设其为两两相异。如果不是两两相异，则下面计算特征向量的过程将要复杂得多。

第 3 步：找出方程

$$[ D ^ {T} (- \mu_ {i}) R D (\mu_ {i}) + N ^ {T} (- \mu_ {i}) N (\mu_ {i}) ] \hat {\zeta} (\mu_ {i}) = 0$$

的非平凡解 $\hat{\zeta}(\mu_{i}), i=1,\cdots,n$ 。

第 4 步：计算 $\Psi(\mu_{i}), i=1,\cdots,n$ 。

第5步：由计算

$$K ^ {*} = - \left[ D \left(\mu_ {1}\right) \hat {\zeta} _ {1} \left(\mu_ {1}\right), \dots , D \left(\mu_ {n}\right) \hat {\zeta} \left(\mu_ {n}\right) \right]\cdot \left[ \Psi \left(\mu_ {1}\right) \hat {\zeta} \left(\mu_ {1}\right), \dots , \Psi \left(\mu_ {n}\right) \hat {\zeta} \left(\mu_ {n}\right) \right] ^ {- 1}$$

即得到最优反馈矩阵。
