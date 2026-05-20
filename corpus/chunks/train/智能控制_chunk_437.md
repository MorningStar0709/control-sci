$$\ddot {\boldsymbol {e}} + \boldsymbol {k} _ {\mathrm{v}} \dot {\boldsymbol {e}} + \boldsymbol {k} _ {\mathrm{p}} \boldsymbol {e} = \boldsymbol {D} _ {0} ^ {- 1} (\Delta \boldsymbol {D} \ddot {\boldsymbol {q}} + \Delta \boldsymbol {C} \dot {\boldsymbol {q}} + \Delta \boldsymbol {G} + \boldsymbol {d}) \tag {9.44}$$

由式(9.44)可见,由于模型建模的不精确会导致控制性能的下降,因此,需要对建模不精确部分进行逼近。

取 $\boldsymbol{x}=(\boldsymbol{e}\quad\dot{\boldsymbol{e}})^{\mathrm{T}}$ ，建模不精确部分为 $f=D_{0}^{-1}(\Delta D\ddot{q}+\Delta C\dot{q}+\Delta G+d)$ ，则可将式(9.44)转化为如下误差状态方程

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {f} \tag {9.45}$$

式中， $A=\begin{pmatrix}0&I\\-k_{p}&-k_{v}\end{pmatrix},B=\begin{pmatrix}0\\I\end{pmatrix},I$ 为单位阵。

假设模型不确定项 f 为已知, 则修正的控制律为

$$\boldsymbol {\tau} = \boldsymbol {D} _ {0} (\boldsymbol {q}) \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} - k _ {\mathrm{v}} \dot {\boldsymbol {e}} - k _ {\mathrm{p}} \boldsymbol {e}\right) + \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} _ {0} (\boldsymbol {q}) - \boldsymbol {D} _ {0} (\boldsymbol {q}) f \tag {9.46}$$

将式 $(9.46)$ 代入式 $(9.39)$ 中，则得到稳定的闭环系统式 $(9.41)$ 。

在实际工程中,模型不确定项 f 为未知,为此,需要对不确定项 f 进行逼近,从而在控制律中实现对不确定项 f 的补偿。
