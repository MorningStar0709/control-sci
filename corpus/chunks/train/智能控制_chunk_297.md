# 5.6.2 基于模糊补偿的控制

假设 $D(q)$ 、 $C(q,\dot{q})$ 和 $G(q)$ 为已知，且所有状态变量可测。定义误差函数为

$$s = \dot {\tilde {q}} + \Lambda \tilde {q} \tag {5.68}$$

式中， $\Lambda$ 为正定阵， $\widetilde{\boldsymbol{q}}(t)$ 为跟踪误差， $\widetilde{\boldsymbol{q}}(t)=\boldsymbol{q}(t)-\boldsymbol{q}_{\mathrm{d}}(t),\boldsymbol{q}_{\mathrm{d}}(t)$ 为理想角度。

定义

$$\dot {\boldsymbol {q}} _ {\mathrm{r}} (t) = \dot {\boldsymbol {q}} _ {\mathrm{d}} (t) - \boldsymbol {\Lambda} \tilde {\boldsymbol {q}} (t) \tag {5.69}$$

为了保证 $s \rightarrow 0$ ，定义 Lyapunov 函数

$$V (t) = \frac {1}{2} \mathbf {s} ^ {\mathrm{T}} \mathbf {D} \mathbf {s} \tag {5.70}$$

式中，D 为正定阵。

由于

$$s = \dot {\tilde {q}} + \Lambda \tilde {q} = \dot {q} - \dot {q} _ {\mathrm{d}} + \Lambda \tilde {q} = \dot {q} - \dot {q} _ {\mathrm{r}}D \dot {s} = D \ddot {q} - D \ddot {q} _ {\mathrm{r}} = \tau - C \dot {q} - G - F - D \ddot {q} _ {\mathrm{r}}$$

根据机械手物理特性,有 $s^{T}\dot{D}s = 2s^{T}Cs$ , 则

$$
\begin{array}{l} \dot {V} (t) = s ^ {\mathrm{T}} D \dot {s} + \frac {1}{2} s ^ {\mathrm{T}} \dot {D} s = - s ^ {\mathrm{T}} (- \tau + C \dot {q} + G + F + D \ddot {q} _ {\mathrm{r}} - C s) \\ = - s ^ {\mathrm{T}} \left(\boldsymbol {D} \ddot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {C} \dot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {G} + \boldsymbol {F} - \tau\right) \tag {5.71} \\ \end{array}
$$

式中，F 表示 $F(q, \dot{q}, \ddot{q})$ 为未知非线性函数。

采用基于MIMO的模糊系统 $F(q,\dot{q},\ddot{q}|\Theta)$ 来逼近未知函数 $F(q,\dot{q},\ddot{q})$ 。参考文献[15]，设计并分析以下两种基于模糊补偿的自适应控制律。
