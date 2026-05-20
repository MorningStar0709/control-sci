# 14.2.1 工作空间直角坐标与关节角位置的转换

![](image/5f753640caa56a6221fdf707bdfaab8144ad2dac8e1b903eba12cfd8a9255148.jpg)

<details>
<summary>text_image</summary>

x₂
m₂
(x₁, x₂)
l₂
q₂
m₁
l₁
q₁
O
x₁
</details>

图 14-3 二自由度机械手

将工作空间中的关节末端节点直角坐标 $(x_{1},x_{2})$ 转为二关节角位置 $(q_{1},q_{2})$ 的问题，即机械手的逆向运动学问题。

根据图 14-3 可得末端在工作空间中的位置为

$$x _ {1} = l _ {1} \cos q _ {1} + l _ {2} \cos (q _ {1} + q _ {2}) \tag {14.4}x _ {2} = l _ {1} \sin q _ {1} + l _ {2} \sin (q _ {1} + q _ {2})$$

则

$$x _ {1} ^ {2} + x _ {2} ^ {2} = l _ {1} ^ {2} + l _ {2} ^ {2} + 2 l _ {1} l _ {2} \cos q _ {2}$$

从而可得

$$q _ {2} = \operatorname{arc} \cos \left(\frac {x _ {1} ^ {2} + x _ {2} ^ {2} - l _ {1} ^ {2} - l _ {2} ^ {2}}{2 l _ {1} l _ {2}}\right) \tag {14.5}$$

根据文献[4]，取 $p_1 = \arctan \frac{x_2}{x_1}$ ， $p_2 = \arccos \frac{x_1^2 + x_2^2 + l_1^2 - l_2^2}{2l_1\sqrt{x_1^2 + x_2^2}}$ ，则

$$
q _ {1} = \left\{ \begin{array}{l l} p _ {1} - p _ {2}, & q _ {2} > 0 \\ p _ {1} + p _ {2}, & q _ {2} \leqslant 0 \end{array} \right. \tag {14.6}
$$

定义 $x = \left[x_{1} x_{2}\right]$ ， $q = \left[q_{1} q_{2}\right]$ ，则 $\mathrm{d}\pmb {x} = \frac{\partial\pmb{x}}{\partial\pmb{q}}\mathrm{d}\pmb{q}$ ，定义 $J = \frac{\partial\pmb{x}}{\partial\pmb{q}}$ ，则

$$\mathrm{d} x = J \cdot \mathrm{d} q$$

式中， $J = \left[ \begin{array}{ll}\frac{\partial x_1}{\partial q_1} & \frac{\partial x_1}{\partial q_2}\\ \frac{\partial x_2}{\partial q_1} & \frac{\partial x_2}{\partial q_2} \end{array} \right]$ ，表示机械手末端端点速度与机械臂关节角速度之间关系的雅可比矩阵。

由式（14.4）可得 $\frac{\partial x_1}{\partial q_1} = -l_1\sin q_1 - l_2\sin (q_1 + q_2)$ ， $\frac{\partial x_1}{\partial q_2} = -l_2\sin (q_1 + q_2)$ ， $\frac{\partial x_2}{\partial q_1} = l_1\cos q_1 + l_2\cos (q_1 + q_2)$ ， $\frac{\partial x_2}{\partial q_2} = l_2\cos (q_1 + q_2)$ ，则

$$
\boldsymbol {J} (\boldsymbol {q}) = \left[ \begin{array}{l l} - l _ {1} \sin (q _ {1}) - l _ {2} \sin (q _ {1} + q _ {2}) & - l _ {2} \sin (q _ {1} + q _ {2}) \\ l _ {1} \cos (q _ {1}) + l _ {2} \cos (q _ {1} + q _ {2}) & l _ {2} \cos (q _ {1} + q _ {2}) \end{array} \right] \tag {14.7}
