# 14.3.2 阻抗模型的建立

在阻抗模型中，阻抗控制目标为 x 跟踪理想的阻抗轨迹 $x_{d}$ ，由式（14.14）可知， $x_{d}$ 可由下述模型求得

$$\boldsymbol {M} _ {\mathrm{m}} \ddot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {B} _ {\mathrm{m}} \dot {\boldsymbol {x}} _ {\mathrm{d}} + \boldsymbol {K} _ {\mathrm{m}} \boldsymbol {x} _ {\mathrm{d}} = - \boldsymbol {F} _ {\mathrm{e}} + \boldsymbol {M} _ {\mathrm{m}} \ddot {\boldsymbol {x}} _ {\mathrm{c}} + \boldsymbol {B} _ {\mathrm{m}} \dot {\boldsymbol {x}} _ {\mathrm{c}} + \boldsymbol {K} _ {\mathrm{m}} \boldsymbol {x} _ {\mathrm{c}} \tag {14.16}$$

式中， $\boldsymbol{x}_{\mathrm{d}}(0) = \boldsymbol{x}_{\mathrm{c}}(0)$ ; $\dot{\boldsymbol{x}}_{\mathrm{d}}(0) = \dot{\boldsymbol{x}}_{\mathrm{c}}(0)$ 。

根据工作空间直角坐标与关节角位置的转换及工作空间关节末端节点直角坐标 $(x_{1}, x_{2})$ 的动力学模型，设计加在关节末端节点的控制律 $F_{x}$ ，并通过 $F_{x}$ 与 $\tau$ 之间的映射关系，求出实际的关节扭矩 $\tau$ 。

机械手动态方程具有下面特性 $^{[3,6]}$ :

特性 1 惯性矩阵 $D_{x}(q)$ 对称正定。

特性 2 矩阵 $\dot{D}_{x}(q)-2C_{x}(q,\dot{q})$ 是斜对称的。

![](image/410eadd7aafb8aebab03045a7d8f63382715dc268d2d664b8df6f7f860259ff9.jpg)
