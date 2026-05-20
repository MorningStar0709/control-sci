$$\lambda_ {1} ^ {1} (t) = - \frac {4 9}{1 9 4} t ^ {2} + \frac {5 1}{1 9 4} t - \frac {1}{9 7}\lambda_ {2} ^ {1} (t) = 1g ^ {1} (t) = \left(\frac {\partial H}{\partial u}\right) _ {1} = \left(\lambda_ {1} + \lambda_ {2} x _ {1} + \lambda_ {2} + \lambda_ {2} u\right) _ {1} = - \frac {4 8}{9 7} t + \frac {2 2}{9 7}$$

共轭系数

$$\beta^ {1} = \frac {\left\| g ^ {1} (t) \right\| ^ {2}}{\left\| g ^ {0} (t) \right\| ^ {2}} = \frac {\int_ {0} ^ {1} \left(- \frac {4 8}{9 7} t + \frac {2 2}{9 7}\right) ^ {2} \mathrm{d} t}{\int_ {0} ^ {1} \left(\frac {5}{2} - t\right) ^ {2} \mathrm{d} t} = \frac {1 9 2}{1 9 4 ^ {2}}$$

共轭梯度

$$
\begin{array}{l} P ^ {1} = - g ^ {1} + \beta^ {1} P ^ {0} = \frac {4 8}{9 7} t - \frac {2 2}{9 7} + \frac {1 9 2}{1 9 4 ^ {2}} \left(t - \frac {5}{2}\right) \\ = \frac {1 8 8 1 6}{1 9 4 ^ {2}} t - \frac {9 0 1 6}{1 9 4 ^ {2}} \\ \end{array}
$$

(3) K=2 时, 控制量为 $u^{2}$

$$u ^ {2} (t) = u ^ {1} (t) + \alpha^ {1} P ^ {1} = \frac {4 9}{9 7} \left(t - \frac {5}{2}\right) + \alpha^ {1} \left(\frac {1 8 8 1 6}{1 9 4 ^ {2}} t - \frac {9 0 1 6}{1 9 4 ^ {2}}\right)$$

同以上步骤, 将 $u^{2}(t)$ 代入状态方程和协态方程, 求出

$$x _ {1} ^ {2} (t), x _ {2} ^ {2} (t) \text {和} \lambda_ {1} ^ {2} (t) (\lambda_ {2} ^ {2} (t) = 1)$$

由 $J = x_{2}(1) = f(\alpha^{1})$

对 $\alpha^1$ 寻优，可得 $\alpha^1 = \frac{194}{196}$ ，于是

$$u ^ {2} (t) = t - \frac {3}{2}$$

可以证明 $u^{2}(t)=u^{*}(t)$ ，即为最优控制。这只要证明 $\left(\frac{\partial H}{\partial u}\right)_{2}=(\lambda_{1}+\lambda_{2}x_{1}+\lambda_{2}+\lambda_{2}u)_{2}=0$ 即可。所以这个例子只要两步迭代即可得到最优解。一般说来，共轭梯度法比梯度法收敛快，但接近最优解后收敛性仍是较慢的。一个补救办法是重新启动，即找出几个共轭梯度方向 $P^{0}, P^{1}, \cdots, P^{n-1}$ 后，令 $P^{n}=-g^{n}$ ，再用式(7-50)重新迭代，寻找共轭梯度方向。
