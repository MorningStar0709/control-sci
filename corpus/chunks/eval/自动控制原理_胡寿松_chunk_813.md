$$\operatorname{rank} \mathbf {G} _ {j} = n; \quad \forall j = 1, 2, \dots , m \tag {10-84}$$

式中， $b_{j}\in R^{n}$ ，由式(10-77)定义； $G_{j}$ 为 $n\times n$ 矩阵，由式(10-79)定义。

事实上，正常系统与可控系统存在包含关系。在矩阵 $G_{j}$ 中，若增加一些线性无关的列，则 $G_{j}$ 的行秩不变。因此，式(10-84)可写为

$$
\begin{array}{l} \operatorname{rank} \left[ \begin{array}{c c c c} \boldsymbol {b} _ {j} & \boldsymbol {A b} _ {j} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {j} \end{array} \right] \\ = \operatorname{rank} \left[ \begin{array}{l l l l l l l l l l} \boldsymbol {b} _ {1} & \boldsymbol {A b} _ {1} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {1} & \dots & \boldsymbol {b} _ {m} & \boldsymbol {A b} _ {m} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {m} \end{array} \right] = n \tag {10-85} \\ \end{array}
$$

对式(10-85)进行列初等变换，并考虑到式(10-77)，则式(10-85)又可写为

$$\operatorname{rank} [ \boldsymbol {B} \quad \boldsymbol {A B} \quad \dots \quad \boldsymbol {A} ^ {n - 1} \boldsymbol {B} ] = n \tag {10-86}$$

上式正好是系统(10-74)完全可控的充分必要条件。因此，正常子空间包含于可控子空间。这种包含关系表明，系统可控是系统正常的前提条件。因此，在问题10-1中提出了可控要求。显然，对于单输入系统， $j = 1$ ，系统正常与系统可控彼此等价。
