# 2. 极点配置

状态方程 $\dot{x} = Ax + Bu$ 的全状态反馈控制系统闭环特征多项式为 $(sI - (A - BK))$ ，基于极点配置的增益及控制律为

$$u (k) = - K x \tag {17.12}\boldsymbol {K} = \operatorname{place} (\boldsymbol {A}, \boldsymbol {B}, P) \tag {17.13}$$

式中 place 为 MATLAB 下的极点配置命令。

![](image/6dbaa20de9e218ea05e86e20d42c9784826d0b7d503e9b9f18164ebe1edfef0d.jpg)
