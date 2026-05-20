# 2. 自适应神经网络控制器的设计与分析

采用神经网络逼近 f，设计基于前馈加补偿的 PD 控制律，式（9.14）变为

$$u = \frac {1}{g (\boldsymbol {x})} \left[ - \hat {f} (\boldsymbol {x}) + \ddot {y} _ {\mathrm{d}} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {E} \right] \tag {9.17}\hat {f} (\boldsymbol {x}) = \hat {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {h} (\boldsymbol {x}) \tag {9.18}$$

式中， $h(x)$ 为神经网络高斯基函数，神经网络权值 $\hat{W}$ 根据自适应律而变化。

设计自适应律为

$$\dot {\boldsymbol {W}} = - \gamma \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P b h} (\boldsymbol {x}) \tag {9.19}$$
