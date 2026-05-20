# 6. 运动的模态

在数学上, 线性微分方程的解由特解和齐次微分方程的通解组成。通解由微分方程的特征根所决定, 它代表自由运动。如果 $n$ 阶微分方程的特征根是 $\lambda_1, \lambda_2, \cdots, \lambda_n$ 且无重根, 则把函数 $\mathbf{e}^{\lambda_1 t}, \mathbf{e}^{\lambda_2 t}, \cdots, \mathbf{e}^{\lambda_n t}$ 称为该微分方程所描述运动的模态, 也叫振型。每一种模态代表一种类型的运动形态, 齐次微分方程的通解则是它们的线性组合, 即

$$y _ {o} (t) = c _ {1} \mathrm{e} ^ {\lambda_ {1} t} + c _ {2} \mathrm{e} ^ {\lambda_ {2} t} + \dots + c _ {n} \mathrm{e} ^ {\lambda_ {n} t}$$

式中，系数 $c_{1}, c_{2}, \cdots, c_{n}$ 是由初始条件决定的常数。

如果特征根中有多重根 $\lambda$ ，则模态会具有形如 $t e^{\lambda t}, t^{2} e^{\lambda t}, \cdots$ 的函数；如果特征根中有共轭复根 $\lambda = \sigma \pm j\omega$ ，则其共轭复模态 $e^{(\sigma + j\omega)t}$ 与 $e^{(\sigma - j\omega)t}$ 可写成实函数模态 $e^{\alpha} \sin \omega t$ 与 $e^{\alpha} \cos \omega t$ 。

在例2-6中，微分方程的特征根 $\lambda = -0.5\pm j0.866$ ，故其共轭复模态是 $\mathrm{e}^{(-0.5 + j0.866)t}$ 与 $\mathbf{e}^{(-0.5 - j0.866)t}$ ，或 $\mathrm{e}^{-0.5t}\sin 0.866t$ 与 $\mathrm{e}^{-0.5t}\cos 0.866t$ ，而微分方程的齐次通解为

$$u _ {o} (t) = c _ {1} \mathrm{e} ^ {- 0. 5 t} \sin 0. 8 6 6 t + c _ {2} \mathrm{e} ^ {- 0. 5 t} \cos 0. 8 6 6 t$$

由给定初始条件 $u_{o}(0) = 0.1\mathrm{V}, i(0) = 0.1\mathrm{A}$ 可求得 $c_{1} = 0.173, c_{2} = 0.1$ ，故得

$$u _ {o} (t) = 0. 1 7 3 \mathrm{e} ^ {- 0. 5 t} \sin 0. 8 6 6 t + 0. 1 \mathrm{e} ^ {- 0. 5 t} \cos 0. 8 6 6 t$$

这个结果与例2-6中解 $u_{o}(t)$ 的零输入分量 $0.2\mathrm{e}^{-0.5t}\sin (0.866t + 30^{\circ})$ 是一致的。
