# 6.4.2 Delta(δ) 学习规则

假设误差准则函数为

$$E = \frac {1}{2} \sum_ {p = 1} ^ {P} (d _ {p} - y _ {p}) ^ {2} = \sum_ {p = 1} ^ {P} E _ {p} \tag {6.2}$$

式中， $d_{p}$ 代表期望的输出（导师信号）； $y_{p}$ 为网络的实际输出， $y_{p} = f(\mathbf{W}^{\mathrm{T}}X_{p}),\mathbf{W}$ 为网络所有权值组成的向量，即

$$\boldsymbol {W} = \left(w _ {0}, w _ {1}, \dots , w _ {n}\right) ^ {\mathrm{T}} \tag {6.3}$$

$X_{p}$ 为输入模式, 即

$$\boldsymbol {X} _ {p} = \left(x _ {p 0}, x _ {p 1}, \dots , x _ {p n}\right) ^ {\mathrm{T}} \tag {6.4}$$

式中，训练样本数为 $p = 1, 2, \cdots, P$ 。

神经网络学习的目的是通过调整权值W，使误差准则函数最小。可采用梯度下降法来实现权值的调整，其基本思想是沿着E的负梯度方向不断修正W值，直到E达到最小，这种方法的数学表达式为

$$\Delta \boldsymbol {W} = \eta \left(- \frac {\partial E}{\partial W _ {i}}\right) \tag {6.5}\frac {\partial E}{\partial W _ {i}} = \sum_ {p = 1} ^ {P} \frac {\partial E _ {p}}{\partial W _ {i}} \tag {6.6}$$

其中

$$E _ {p} = \frac {1}{2} \left(d _ {p} - y _ {p}\right) ^ {2} \tag {6.7}$$

令网络输出为 $\theta_{p} = W^{T} X_{p}$ ，则 $y_{p} = f(\theta_{p})$

$$\frac {\partial E _ {p}}{\partial W _ {i}} = \frac {\partial E _ {p}}{\partial \theta_ {p}} \frac {\partial \theta_ {p}}{\partial W _ {i}} = \frac {\partial E _ {p}}{\partial y _ {p}} \frac {\partial y _ {p}}{\partial \theta_ {p}} X _ {i p} = - (d _ {p} - y _ {p}) f ^ {\prime} (\theta_ {p}) X _ {i p} \tag {6.8}$$

$\pmb{W}$ 的修正规则为

$$\Delta w = \eta \sum_ {p = 1} ^ {P} \left(d _ {p} - y _ {p}\right) f ^ {\prime} \left(\theta_ {p}\right) X _ {i p} \tag {6.9}$$

式 $(6.9)$ 称为 $\delta$ 学习规则,又称误差修正规则。

Hebb 学习规则和 Delta 学习规则都属于传统的权值调节方法,而一种更先进的方法是通过 Lyapunov 稳定性理论来获得权值调节律的。
