# 2. 自适应模糊控制器的设计

采用模糊系统逼近 f 和 g，则控制律式(5.20)变为

$$u = \frac {1}{\hat {g} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {g})} \left[ - \hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) + y _ {m} ^ {(n)} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {e} \right] \tag {5.26}\hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) = \boldsymbol {\theta} _ {f} ^ {\mathrm{T}} \boldsymbol {\xi} (\boldsymbol {x}), \hat {g} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {g}) = \boldsymbol {\theta} _ {g} ^ {\mathrm{T}} \boldsymbol {\eta} (\boldsymbol {x}) \tag {5.27}$$

式中， $\xi(x)$ 和 $\eta(x)$ 为模糊向量，参数 $\theta_{f}^{T}$ 和 $\theta_{g}^{T}$ 根据自适应律而变化。

设计自适应律为

$$\dot {\boldsymbol {\theta}} _ {f} = - \gamma_ {1} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {P b} \boldsymbol {\xi} (\boldsymbol {x}) \tag {5.28}\dot {\boldsymbol {\theta}} _ {g} = - \gamma_ {2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {P b} \boldsymbol {\eta} (\boldsymbol {x}) u \tag {5.29}$$

式中， $\gamma_{1},\gamma_{2}$ 为正常数，P 为正定阵，由式(5.39)给出。

自适应模糊控制系统如图 5-11 所示。
