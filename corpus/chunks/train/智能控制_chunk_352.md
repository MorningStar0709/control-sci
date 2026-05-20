# (1) 前向传播: 计算网络的输出

隐层神经元的输入为所有输入的加权之和,即

$$x _ {j} = \sum_ {i} w _ {i j} x _ {i} \tag {7.14}$$

隐层神经元的输出 $x'_{j}$ 采用 S 函数激发 $x_{j}$ ，得

$$x _ {j} ^ {\prime} = f \left(x _ {j}\right) = \frac {1}{1 + \mathrm{e} ^ {- x _ {j}}} \tag {7.15}$$

则

$$\frac {\partial x _ {j} ^ {\prime}}{\partial x _ {j}} = x _ {j} ^ {\prime} \left(1 - x _ {j} ^ {\prime}\right)$$

输出层神经元的输出为

$$x _ {l} = \sum_ {j} w _ {j l} x _ {j} ^ {\prime} \tag {7.16}$$

网络第 l 个输出与相应理想输出 $x_{l}^{0}$ 的误差为

$$e _ {l} = x _ {l} ^ {0} - x _ {l}$$

第 p 个样本的误差性能指标函数为

$$E _ {p} = \frac {1}{2} \sum_ {l = 1} ^ {N} e _ {l} ^ {2} \tag {7.17}$$

式中，N 为网络输出层的个数。
