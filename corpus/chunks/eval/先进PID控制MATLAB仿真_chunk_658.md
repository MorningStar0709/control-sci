# 17.6.1 问题描述

以倒立摆的摆杆控制为例，考虑如下2阶非线性倒立摆系统：

$$\ddot {\theta} = f (\theta , \dot {\theta}) + g (\theta , \dot {\theta}) u + d (\theta , \dot {\theta}, t) \tag {17.27}$$

式中，f 和 g 为已知非线性函数； $u \in R$ 和 $y = \theta \in R$ 分别为系统的输入和输出； $d(\theta, \dot{\theta}, t)$ 为模型不确定性与外加干扰之和， $\left|d(\theta, \dot{\theta}, t)\right| \leqslant D$ 。

![](image/ef88609c0b9086d20ffe36e4c413e08c99f712425483ac277a83f61b135d65cd.jpg)
