# 2. 用共轭梯度法解最优控制问题

前面已说过,最优控制计算的直接法是用迭代方法逐步改善控制量 $u(t)$ ,使它最后满足哈密顿函数H取极小的必要条件。故梯度向量为

$$\boldsymbol {g} ^ {K} = \boldsymbol {g} ^ {K} (t) = \left(\frac {\partial H}{\partial \boldsymbol {u}}\right) _ {\boldsymbol {u} (t) = \boldsymbol {u} ^ {K} (t)} \triangleq \left(\frac {\partial H}{\partial \boldsymbol {u}}\right) _ {K} \tag {7-47}$$

这里梯度向量 $\boldsymbol{g}^{K}(t)$ 是时间的函数, 向量时间函数的内积定义为

$$\left(\boldsymbol {g} ^ {K} (t), \boldsymbol {g} ^ {K} (t)\right) \triangleq \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left(\boldsymbol {g} ^ {K} (t)\right) ^ {\mathrm{T}} \boldsymbol {g} ^ {K} (t) \mathrm{d} t = \left\| \boldsymbol {g} ^ {K} (t) \right\| ^ {2} (7 - 4 8)$$

除了这些以外,其他在形式上与求函数极值的共轭梯度法一样。

共轭梯度法求最优控制步骤为

(1) 设已求出第 K 步估计的控制函数 $\boldsymbol{u}^{K}(t)$ , $\boldsymbol{u}^{0}(t)$ 可任选。  
(2) 以 $X(t_0)$ 为初值, 从 $t_0$ 到 $t_f$ 积分状态方程, 得出状态轨迹 $\pmb{X}^K(t)$ 。  
(3) 以 $\pmb{\lambda}(t_{\mathrm{f}})$ 为终值, 从 $t_{\mathrm{f}}$ 到 $t_{0}$ 反向积分协态方程, 求得协态轨迹 $\pmb{\lambda}^K(t)$ 。

(4) 计算梯度向量 $g^{K}=\left(\frac{\partial H}{\partial u}\right)_{u=u^{K}}$

(5) 计算共轭系数

$$\beta^ {K} = \frac {\left\| \pmb {g} ^ {K} (t) \right\| ^ {2}}{\left\| \pmb {g} ^ {K - 1} (t) \right\| ^ {2}} K = 0 \text {时}, \quad \beta^ {0} = 0 \tag {7-49}$$

(6) 计算共轭梯度

$$\pmb {P} ^ {K} = - \pmb {g} ^ {K} + \beta^ {K} \pmb {P} ^ {K - 1} \quad K = 0 \text {时}, \pmb {P} ^ {0} = - \pmb {g} ^ {0} \tag {7-50}$$

(7) 计算控制函数

$$\boldsymbol {u} ^ {K + 1} (t) = \boldsymbol {u} ^ {K} (t) + \alpha^ {K} \boldsymbol {P} ^ {K} \tag {7-51}$$

用一维寻优决定 $\alpha^K$ ，即 $J = (\pmb{u}^K + \alpha^K\pmb{P}^K) = \min_{\alpha > 0} J(\pmb{u}^K + \alpha P^K)$ (7-52)

(8) 当满足下面的不等式

$$\left| \frac {J \left(\boldsymbol {u} ^ {K + 1}\right) - J \left(\boldsymbol {u} ^ {K}\right)}{J \left(\boldsymbol {u} ^ {K}\right)} \right| < \varepsilon \tag {7-53}$$

停止计算。否则令 $K = K + 1$ ，回到步骤2。

例7-2 设系统状态方程为

$$\dot {x} _ {1} = u \quad x _ {1} (0) = \frac {1}{2} \tag {7-54}\dot {x} _ {2} = (1 + u) x _ {1} + u + \frac {1}{2} u ^ {2} \quad x _ {2} (0) = 0 \tag {7-55}$$

性能指标

$$J = x _ {2} (1) \tag {7-56}$$

要求用共轭梯度法决定最优控制 $u(t)$ ，使 J 最小。

解 哈密顿函数为

$$H = \lambda_ {1} u + \lambda_ {2} \left[ (1 + u) x _ {1} + u + \frac {1}{2} u ^ {2} \right] \tag {7-57}$$

协态方程为

$$\dot {\lambda} _ {1} = - \frac {\partial H}{\partial x _ {1}} = - \lambda_ {2} (1 + u) \tag {7-58}\dot {\lambda} _ {2} = - \frac {\partial H}{\partial x _ {2}} = 0 \quad \therefore \lambda_ {2} (t) = c (\text {常数}) \tag {7-59}$$

由横截条件
