# 11.2.1 Stribeck 摩擦模型描述

Stribeck 曲线是比较著名的摩擦模型 $^{[2]}$ 。如图 11-3 所示，该图表明了在不同的摩擦阶段，摩擦力矩与速度之间的关系，该关系即为 Stribeck 曲线。

Stribeck 摩擦模型可表示如下。

当 $\left|\dot{\theta}(t)\right|<\alpha$ 时，静摩擦为

$$
F _ {\mathrm{f}} (t) = \left\{ \begin{array}{l l} F _ {\mathrm{m}} & F (t) > F _ {\mathrm{m}} \\ F (t) & - F _ {\mathrm{m}} <   F <   F _ {\mathrm{m}} \\ - F _ {\mathrm{m}} & F (t) <   - F _ {\mathrm{m}} \end{array} \right. \tag {11.5}
$$

当 $\left|\dot{\theta}(t)\right|>\alpha$ 时，动摩擦为

$$F _ {\mathrm{f}} (t) = \left(F _ {\mathrm{c}} + (F _ {\mathrm{m}} - F _ {\mathrm{c}}) \mathrm{e} ^ {- \alpha_ {\mathrm{i}} | \dot {\theta} (t) |}\right) \mathrm{sgn} (\dot {\theta} (t)) + k _ {\mathrm{v}} \dot {\theta} \tag {11.6}$$

式中， $F(t)$ 为驱动力； $F_{m}$ 为最大静摩擦力； $F_{c}$ 为库仑摩擦力； $k_{v}$ 为黏性摩擦力矩比例系数； $\dot{\theta}(t)$ 为转动角速度； $\alpha$ 和 $\alpha_{1}$ 为非常小的、正的常数。

![](image/98147ae374c4ab41ba3b3218d9348fa6b0cc57d613bbc488b5fc936ca487e527.jpg)
