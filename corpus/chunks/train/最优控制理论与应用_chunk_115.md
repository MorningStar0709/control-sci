$$V (\boldsymbol {X}, t) = \min _ {u \in \Omega} \left\{F (\boldsymbol {X}, \boldsymbol {U}, t) \Delta t + \left(\frac {\partial V}{\partial \boldsymbol {X}}\right) ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \Delta t \right\} +V (X, t) + \frac {\partial V}{\partial t} \Delta t + o (\Delta t ^ {2})$$

从上式两端消去 $V(X,t)$ ，除以 $\Delta t$ ，再令 $\Delta t\to 0$ ，可得

$$- \frac {\partial V}{\partial t} = \min _ {u \in \Omega} \left\{F (\boldsymbol {X}, \boldsymbol {U}, t) + \left(\frac {\partial V}{\partial \boldsymbol {X}}\right) ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \right\} \tag {6-25}$$

引用以前使用过的哈密顿函数,有

$$H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) = F (\boldsymbol {X}, \boldsymbol {U}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \tag {6-26}\boldsymbol {\lambda} = \frac {\partial V}{\partial \boldsymbol {X}} \tag {6-27}$$

则式(6-25)可写成

$$
\begin{array}{l} - \frac {\partial V}{\partial t} = \min _ {u \in \Omega} H (X, U, \frac {\partial V}{\partial X}, t) \tag {6-28} \\ = H ^ {*} \left(\boldsymbol {X}, \boldsymbol {U}, \frac {\partial V}{\partial \boldsymbol {X}}, t\right) \\ \end{array}
$$

式(6-25)或(6-28)称为哈密顿-雅可比-贝尔曼方程,边界条件是式(6-22)。哈密顿-雅可比-贝尔曼方程在理论上很有价值,但它是 $V(X,t)$ 的一阶偏微分方程并带有取极小的运算,因此求解是非常困难的,一般情况得不到解析解,只能用计算机求数值解。对于线性二次问题,可以得到解析解,而且求解结果与用极小值原理或变分法所得结果相同。这时,哈密顿-雅可比-贝尔曼方程可归结为黎卡提方程。在实际计算线性二次问题时,一般用直接求解黎卡提方程来求最优控制。
