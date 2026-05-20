# 2. 自适应控制器的设计

采用模糊系统逼近 f，则控制律（8.6）变为

$$u = \frac {1}{g (\boldsymbol {x})} \left[ - \hat {f} (\boldsymbol {x} | \boldsymbol {\theta} _ {f}) + \ddot {x} _ {\mathrm{d}} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {E} \right] \tag {8.12}\hat {f} (\boldsymbol {x} \mid \theta_ {f}) = \theta_ {f} ^ {\mathrm{T}} \xi (\boldsymbol {x}) \tag {8.13}$$

式中， $\xi(x)$ 为模糊向量；参数 $\theta_{f}$ 根据自适应律而变化。

设计自适应律为

$$\dot {\boldsymbol {\theta}} _ {f} = - \gamma \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P b} \xi (\boldsymbol {x}) \tag {8.14}$$

![](image/d3f688c506fd1bf634ce3d4e5f2871c424b6e20b575c2cb4a6308f937e3380bd.jpg)
