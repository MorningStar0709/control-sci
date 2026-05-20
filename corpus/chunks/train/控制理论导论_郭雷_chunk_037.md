系统零点的物理意义将在下一节中解释.

用状态空间方法描述系统时，首先需要选取一组状态变量，建立状态方程和量测方程。然而，一个系统的状态变量的选择及相应的状态方程和量测方程并不唯一。人们自然要问，不同的状态变量选择是否会改变系统的基本特征呢？下面讨论这类问题。

已知定常线性系统 (1.2.6), $T$ 是任意 $n \times n$ 实非奇异常矩阵 (其实, 复数矩阵也适用), 令

$$\widehat {x} (t) = T x (t), \tag {1.2.10}$$

那么变量 $\hat{x}(t)$ 与 $x(t)$ 包含着相同的信息量，所以 $\hat{x}(t)$ 也可以选做系统的状态变量。按照这组状态变量描述系统又可以得到系统 (1.2.6) 的一个状态空间描述。为了研究新的状态方程和量测方程，对等式 (1.2.10) 两边求导得

$$\dot {\hat {x}} (t) = T \dot {x} (t) = T A x (t) + T B u (t).$$

再利用 $x(t) = T^{-1}\hat{x} (t)$ 得

$$
\left\{ \begin{array}{l} \dot {\widehat {x}} (t) = \widehat {A} \widehat {x} (t) + \widehat {B} u (t), \\ y (t) = \widehat {C} \widehat {x} (t) + D u (t), \end{array} \right. \tag {1.2.11}
$$

其中 $\hat{A} = TAT^{-1}$ , $\hat{B} = TB$ , $\hat{C} = CT^{-1}$ .

称关系式 (1.2.10) 为系统 (1.2.5) 在状态空间中的坐标变换。经坐标变换得到由方程 (1.2.11) 描述的系统称为与系统 (1.2.6) 的代数等价系统。

由于

$$\det (s I _ {n} - \widehat {A}) = \det T (s I _ {n} - A) T ^ {- 1} = \det (s I _ {n} - A).$$

因此，坐标变换保持系统的特征多项式、特征方程和系统的极点不变，或者说代数等价系统有相同的特征多项式、特征方程和极点.

又因为

$$
\operatorname{rank} [ s \boldsymbol {I} _ {n} - \widehat {\boldsymbol {A}}, \widehat {\boldsymbol {B}} ] = \operatorname{rank} [ s \boldsymbol {I} _ {n} - \boldsymbol {A}, \boldsymbol {B} ]. \quad \operatorname{rank} \left[ \begin{array}{c} s \boldsymbol {I} _ {n} - \widehat {\boldsymbol {A}} \\ \widehat {\boldsymbol {C}} \end{array} \right] = \operatorname{rank} \left[ \begin{array}{c} s \boldsymbol {I} _ {n} - \boldsymbol {A} \\ \boldsymbol {C} \end{array} \right],
$$

以及

$$
\operatorname{rank} \left[ \begin{array}{c c} s \boldsymbol {I} _ {n} - \hat {\boldsymbol {A}} & \hat {\boldsymbol {B}} \\ \hat {\boldsymbol {C}} & \boldsymbol {D} \end{array} \right] = \operatorname{rank} \left[ \begin{array}{c c} s \boldsymbol {I} _ {n} - \boldsymbol {A} & \boldsymbol {B} \\ \boldsymbol {C} & \boldsymbol {D} \end{array} \right],
$$

故坐标变换保持系统的输入解耦零点、输出解耦零点和传输零点不变；换句话说，代数等价系统与原系统有相同的输入解耦零点、输出解耦零点和传输零点.

从系统 (1.2.11) 的状态方程和量测方程出发，可以求出它的传递函数矩阵为

$$\widehat {\boldsymbol {W}} (s) = \widehat {\boldsymbol {C}} (s \boldsymbol {I} _ {n} - \widehat {\boldsymbol {A}}) \widehat {\boldsymbol {B}} + \boldsymbol {D}$$

不难验证，它与系统(1.2.6)的传递函数矩阵 $W(s)$ 相等。因此，坐标变换保持系统的传递函数矩阵不变，或者说保持系统的输入输出特性不变。也可以说，代数等价系统有相同的传递函数矩阵，因而有相同的输入输出特性。这是可以理解的，因为坐标变换仅仅反映了系统内部状态变量的不同选择，而不影响系统的外部联系，所以它能保持系统的输入输出特性不变。
