# (1) 前向传播: 计算网络的输出

隐层神经元的输入为所有输入的加权之和,即

$$x _ {j} = \sum_ {i} w _ {i j} x _ {i} \tag {7.7}$$

隐层神经元的输出 $x_{j}^{\prime}$ 采用 S 函数激发 $x_{j}$ ，得

$$x _ {j} ^ {\prime} = f (x _ {j}) = \frac {1}{1 + \mathrm{e} ^ {- x _ {j}}} \tag {7.8}$$

则

$$\frac {\partial x _ {j} ^ {\prime}}{\partial x _ {j}} = x _ {j} ^ {\prime} (1 - x _ {j} ^ {\prime})$$

输出层神经元的输出为

$$y _ {n} (k) = \sum_ {j} w _ {j 0} x _ {j} ^ {\prime} \tag {7.9}$$

网络输出与理想输出误差为

$$e (k) = y (k) - y _ {n} (k)$$

误差性能指标函数为

$$E = \frac {1}{2} e (k) ^ {2} \tag {7.10}$$
