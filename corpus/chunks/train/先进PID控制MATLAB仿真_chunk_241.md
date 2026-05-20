# 4.2.1 Levant 微分器

微分器中需要注意的问题是既要尽量准确求导，又要对信号的测量误差和输入噪声具有鲁棒性。Levant $^{[3]}$ 提出了一种基于滑模技术的非线性微分器，其中二阶滑模微分器表达式为

$$\dot {x} = uu = u _ {1} - \lambda | x - v (t) | ^ {1 / 2} \operatorname{sgn} (x - v (t)) \tag {4.3}\dot {u} _ {1} = - \alpha \operatorname{sgn} (x - v (t))$$

其中

$$\alpha > C, \lambda^ {2} \geqslant 4 C \frac {\alpha + C}{\alpha - C} \tag {4.4}$$

并且 C > 0，是输入信号 $v(t)$ 导数的 Lipschitz 常数上界。

采用二阶 Levant 微分器，可实现 x 跟踪 $v(t)$ ， $u_{1}$ 跟踪 $\dot{v}(t)$ 。对于 Levant 微分器，需要事先知道输入信号 $v(t)$ 导数的 Lipschitz 常数上界，才能设计微分器参数，这就限制了输入信号的类型。而且，对于这种微分器，抖振现象不可避免。

![](image/8ce9a0eb1d89412979f840f2e2bbab9bf71e0f1ade56eb281ab2da45e48f71d5.jpg)
