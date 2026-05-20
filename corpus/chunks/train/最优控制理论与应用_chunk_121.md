# 7.1 直接法

（一）梯度法 这是一种直接方法，应用比较广泛。它的特点是：先猜测任意一个控制函数 $U(t)$ ，它可能并不满足 H 取极小的必要条件，然后用迭代算法根据 H 梯度减小的方向来改善 $U(t)$ ，使它最后满足必要条件。

计算步骤如下：

1. 先猜测 $[t_0, t_f]$ 中的一个控制向量 $U^K(t) = U^0(t)$ , $K$ 是迭代步数，初始时 $K = 0$ 。 $U^0$ 的决定要凭工程经验，猜得合理，计算收敛得就快。

2. 在第 K 步, 以估计值 $U^{K}$ 和给定的初始条件 $X(t_{0})$ , 从 $t_{0}$ 到 $t_{f}$ 顺向积分状态方程, 求出状态向量 $X^{K}(t)$ 。

3. 用 $U^{K}(t)$ 、 $X^{K}(t)$ 和横截条件求得的终端值 $\lambda(t_{\mathrm{f}})$ ，从 $t_{f}$ 到 $t_{0}$ 反向积分协态方程，求出协态向量 $\lambda^{K}(t)$ 。

4. 计算哈密顿函数 $H$ 对 $U$ 的梯度向量 $\pmb{g}^{\kappa}$

$$\boldsymbol {g} ^ {\kappa} \triangleq \left(\frac {\partial H}{\partial \boldsymbol {U}}\right) _ {\kappa}$$

$\left(\frac{\partial H}{\partial U}\right)_K$ 表示在 $U^K, X^K, \lambda^K$ 处取值。当这些量非最优值时， $g^K \neq 0$ 。

5. 修正控制向量

$$\boldsymbol {U} ^ {K + 1} = \boldsymbol {U} ^ {K} - \alpha^ {K} \boldsymbol {g} ^ {K} \tag {7-3}$$

$\alpha^{K}$ 是一个步长因子, 它是待定的数。选择 $\alpha^{K}$ 使指标达到极小。这是一维寻优问题, 有很多现成的优化方法可用。如分数法, 0.618 法, 抛物线法, 立方近似法等。式(7-3)表明迭代是沿着梯度 $g^{K}$ 的负方向进行的。

6. 计算是否满足下列指标

$$\left| \frac {J (\boldsymbol {U} ^ {K + 1}) - J (\boldsymbol {U} ^ {K})}{J (\boldsymbol {U} ^ {K})} \right| < \varepsilon \tag {7-4}$$

$\varepsilon$ 是指定小量, 若满足则停止计算, 否则, 令 $K = K + 1$ , 转步骤2。另一停止计算的标准是

$$\left\| \boldsymbol {g} ^ {K} \right\| < \varepsilon \tag {7-5}$$

例7-1 考虑下面的一阶非线性状态方程

$$\dot {x} = - x ^ {2} + u \quad x (0) = 1 0 \tag {7-6}$$

用梯度法寻找最优控制使下面的指标最小

$$J = \frac {1}{2} \int_ {0} ^ {1} \left(x ^ {2} + u ^ {2}\right) \mathrm{d} t \tag {7-7}$$

解 哈密顿函数为

$$H = \frac {1}{2} \left(x ^ {2} + u ^ {2}\right) - \lambda x ^ {2} + \lambda u \tag {7-8}$$

协态方程为

$$\dot {\lambda} = - \frac {\partial H}{\partial x} = - x + 2 \lambda x \tag {7-9}$$

因 $x(1)$ 自由，由横截条件得

$$\lambda^ {0} (1) = 0 \tag {7-10}$$

1. 选初始估计 $u^0(t) = 0$ 。

2. 将 $u^0(t) = 0$ 代入状态方程(7-6)可得

$$\frac {\mathrm{d} x}{x ^ {2}} = - \mathrm{d} t \tag {7-11}$$

积分上式可得

$$- \frac {1}{x} = - t + c \tag {7-12}$$

代入初始条件: t=0, $x(0)=10$ , 确定积分常数

$$c = - \frac {1}{1 0} \tag {7-13}$$

代入式(7-12)即可得

$$x (t) = x ^ {0} (t) = \frac {1 0}{1 0 t + 1} \tag {7-14}$$

3. 将 $x^0(t)$ 代入协态方程 $(7 - 9)$ , 且由边界条件 $\lambda^0(1) = 0$ 从 $t = 1$ 倒向积分可得

$$\lambda^ {0} (t) = \frac {1}{2} \left[ 1 - \frac {(1 + 1 0 t) ^ {2}}{1 2 1} \right] \quad \lambda^ {0} (1) = 0$$

4. 由 $\frac{\partial H}{\partial u} = u + \lambda$

则 $\left(\frac{\partial H}{\partial u}\right)^0 = \lambda^0(t)$

5. $u^1(t) = u^0(t) - \left(\frac{\partial H}{\partial u}\right)^0 = -\frac{1}{2}\left[1 - \frac{(1 + 10t)^2}{121}\right]$ 。
