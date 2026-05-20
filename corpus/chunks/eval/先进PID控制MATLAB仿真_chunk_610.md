# 16.1.3 基于 Riccati 方程的 $H_{\infty}$ 控制

定理 $^{[1]}$ ：针对式（16.4），存在反馈控制器，使得闭环系统稳定且

$$\left\| T _ {\mathrm{sw}} (s) \right\| _ {\infty} < 1 \tag {16.9}$$

成立的充分必要条件是 Riccati 方程

$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {X} + \boldsymbol {X A} + \boldsymbol {X} \left(\boldsymbol {B} _ {1} \boldsymbol {B} _ {1} ^ {\mathrm{T}} - \boldsymbol {B} _ {2} \boldsymbol {B} _ {2} ^ {\mathrm{T}}\right) \boldsymbol {X} + \boldsymbol {C} _ {1} ^ {\mathrm{T}} \boldsymbol {C} _ {1} = 0 \tag {16.10}$$

具有使 $A + \left( B_{1} B_{1}^{\mathrm{T}} - B_{2} B_{2}^{\mathrm{T}} \right) X$ 稳定的半正定解 $X \geqslant 0$ 。如果有解，则增益为

$$\boldsymbol {K} = - \boldsymbol {B} _ {2} ^ {\mathrm{T}} \boldsymbol {X} \tag {16.11}$$

满足要求的控制器为

$$u = K x \tag {16.12}$$

![](image/7e40287a733e0974a5ed9e74773aede871fe3e58f4cd028027a8ecf68e9feb16.jpg)
