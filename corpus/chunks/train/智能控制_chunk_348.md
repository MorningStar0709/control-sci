# (2) 反向传播: 采用 $\delta$ 学习算法, 调整各层间的权值

根据梯度下降法,权值的学习算法如下:

输出层及隐层的连接权值 $\omega_{j2}$ 学习算法为

$$\Delta w _ {j o} = - \eta \frac {\partial E}{\partial w _ {j o}} = \eta \cdot e (k) \cdot \frac {\partial y _ {n}}{\partial w _ {j o}} = \eta \cdot e (k) \cdot x _ {j} ^ {\prime}$$

式中， $\eta$ 为学习速率， $\eta\in[0,1]$ 。

$k+1$ 时刻网络的权值为

$$w _ {j o} (k + 1) = w _ {j o} (k) + \Delta w _ {j 2}$$

隐层及输入层连接权值 $w_{ij}$ 学习算法为

$$\Delta w _ {i j} = - \eta \frac {\partial E}{\partial w _ {i j}} = \eta \cdot e (k) \cdot \frac {\partial y _ {n}}{\partial w _ {i j}}$$

式中， $\frac{\partial y_n}{\partial w_{ij}} = \frac{\partial y_n}{\partial x_j'}\cdot \frac{\partial x_j'}{\partial x_j}\cdot \frac{\partial x_j}{\partial w_{ij}} = w_{jo}\cdot \frac{\partial x_j'}{\partial x_j}\cdot x_i = w_{jo}\cdot x_j'(1 - x_j')\cdot x_i$

$k+1$ 时刻网络的权值为

$$w _ {i j} (k + 1) = w _ {i j} (k) + \Delta w _ {i j}$$

为了避免权值的学习过程发生振荡、收敛速度慢,需要考虑上次权值变化对本次权值变化的影响,即加入动量因子 $\alpha$ 。此时的权值为

$$w _ {j o} (k + 1) = w _ {j o} (k) + \Delta w _ {j o} + \alpha (w _ {j o} (k) - w _ {j o} (k - 1)) \tag {7.11}w _ {i j} (k + 1) = w _ {i j} (k) + \Delta w _ {i j} + \alpha (w _ {i j} (k) - w _ {i j} (k - 1)) \tag {7.12}$$

式中， $\alpha$ 为动量因子， $\alpha \in [0,1]$ 。

将对象输出对输入的敏感度 $\frac{\partial y(k)}{\partial u(k)}$ 称为 Jacobian 信息, 其值可由神经网络辨识而得。辨识算法如下: 取 BP 网络的第一个输入为 $u(k)$ , 即 $x_{1} = u(k)$ , 则

$$\frac {\partial y (k)}{\partial u (k)} \approx \frac {\partial y _ {n} (k)}{\partial u (k)} = \frac {\partial y _ {n} (k)}{\partial x _ {j} ^ {\prime}} \times \frac {\partial x _ {j} ^ {\prime}}{\partial x _ {j}} \times \frac {\partial x _ {j}}{\partial x _ {1}} = \sum_ {j} w _ {j 0} x _ {j} ^ {\prime} (1 - x _ {j} ^ {\prime}) w _ {1 j} \tag {7.13}$$
