# (2) 反向传播: 采用梯度下降法, 调整各层间的权值

输出层及隐层的连接权值 $w_{jl}$ 学习算法为

$$\Delta w _ {j l} = - \eta \frac {\partial E _ {p}}{\partial w _ {j l}} = \eta e _ {l} \frac {\partial x _ {l}}{\partial w _ {j l}} = \eta e _ {l} x _ {j} ^ {\prime}$$

式中， $\eta$ 为学习速率， $\eta\in[0,1]$ 。

$k+1$ 时刻网络的权值为

$$w _ {j l} (k + 1) = w _ {j l} (k) + \Delta w _ {j l}$$

隐层及输入层连接权值 $w_{ij}$ 学习算法为

$$\Delta w _ {i j} = - \eta \frac {\partial E _ {p}}{\partial w _ {i j}} = \eta \sum_ {l = 1} ^ {N} e _ {l} \frac {\partial x _ {l}}{\partial w _ {i j}}$$

式中， $\frac{\partial x_{l}}{\partial w_{ij}}=\frac{\partial x_{l}}{\partial x_{j}^{\prime}}\cdot\frac{\partial x_{j}^{\prime}}{\partial x_{j}}\cdot\frac{\partial x_{j}}{\partial w_{ij}}=w_{il}\cdot\frac{\partial x_{j}^{\prime}}{\partial x_{j}}\cdot x_{i}=w_{jl}\cdot x_{j}^{\prime}(1-x_{j}^{\prime})\cdot x_{i}$ 。

$t+1$ 时刻网络的权值为

$$w _ {i j} (k + 1) = w _ {i j} (k) + \Delta w _ {i j}$$

如果考虑上次权值对本次权值变化的影响,需要加入动量因子 $\alpha$ ,此时的权值为

$$w _ {j l} (k + 1) = w _ {j l} (k) + \Delta w _ {j l} + \alpha \left(w _ {j l} (k) - w _ {j l} (k - 1)\right) \tag {7.18}w _ {i j} (k + 1) = w _ {i j} (k) + \Delta w _ {i j} + \alpha \left(w _ {i j} (k) - w _ {i j} (k - 1)\right) \tag {7.19}$$

式中， $\alpha$ 为动量因子， $\alpha\in[0,1]$ 。
