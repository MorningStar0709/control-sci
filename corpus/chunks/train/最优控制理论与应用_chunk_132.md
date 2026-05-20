这种方法的缺点是：（1）第一次估计 $\boldsymbol{\lambda}(t_{0})$ 很困难。（2）终端值对 $\dot{\boldsymbol{\lambda}}(t_{0})$ 非常敏感时， $\hat{\boldsymbol{Z}}(t_{\mathrm{f}})$ 与 $\boldsymbol{Z}(t_{\mathrm{f}})$ 相差很大，线性关系（7-70）不成立。（3）敏感矩阵难于确定得很精确，对它求逆的运算也容易引入误差。

例7-3 系统状态方程为

$$\dot {x} _ {1} = x _ {2} \quad x _ {1} (0) = - 5 \tag {7-75}\dot {x} _ {2} = - x _ {1} + 1. 4 x _ {2} - 0. 1 4 x _ {2} ^ {3} + 4 u \quad x _ {2} (0) = - 5 \tag {7-76}$$

性能指标为

$$J (u) = \int_ {0} ^ {0. 1} \left(x _ {1} ^ {2} + u ^ {2}\right) \mathrm{d} t \tag {7-77}$$

用边界迭代法寻找 $u(t)$ ，使 $J(u)$ 最小。

解 因终端 $x_{1}(0.1), x_{2}(0.1)$ 自由，故

$$\lambda_ {1} (0. 1) = \lambda_ {2} (0. 1) = 0$$

设 $\lambda_1(t_0)$ 和 $\lambda_2(t_0)$ 的初始估计值为 0，迭代结果见表 7-1。可见在第 7 次迭代时， $\lambda_1(t_f), \lambda_2(t_f)$ 已为 0，满足了边界条件。

表7-1

<table><tr><td>迭代次数</td><td>1</td><td>2</td><td>4</td><td>7</td><td>10</td></tr><tr><td> $\lambda_{1}(t_{0})$ </td><td>-1.050 00</td><td>-1.041 87</td><td>-1.044 01</td><td>-1.044 13</td><td>-1.044 13</td></tr><tr><td> $\lambda_{2}(t_{0})$ </td><td>-0.050 00</td><td>-0.044 15</td><td>-0.041 40</td><td>-0.041 14</td><td>-0.041 40</td></tr><tr><td> $\lambda_{1}(t_{f})$ </td><td>-0.007 11</td><td>0.001 83</td><td>0.000 13</td><td>0.000 00</td><td>0.000 00</td></tr><tr><td> $\lambda_{2}(t_{f})$ </td><td>-0.015 89</td><td>-0.005 66</td><td>0.000 00</td><td>0.000 00</td><td>0.000 00</td></tr></table>

（二）拟线性化法 这个方法的特点是用迭代算法来改善对正则方程解的估计，使它逐步逼近正则方程的精确解。和前面一样，将正则方程写成：

$$
\dot {\boldsymbol {Y}} = \boldsymbol {g} (\boldsymbol {Y}, t) \tag {7-78}
\mathbf {Y} \triangleq \left[ \begin{array}{l} X \\ \lambda \end{array} \right] \tag {7-79}
$$

设已知 n 个初始条件 $X(t_{0}) = X_{0}$ 和 n 个终端条件 $\lambda(t_{\mathrm{f}}) = \lambda_{\mathrm{f}}$ 。拟线性化法将非线性两点边值问题转化为线性两点边值问题，因此变得容易求解。

设在迭代的第 $K$ 步获得近似解 $\pmb{Y}^K (t)$ ，将正则方程(7-78)在 $\pmb{Y}^{K}(t)$ 展开，保留一次项，可得到 $K + 1$ 步的近似解 $\pmb{Y}^{K + 1}$ ，有

$$\dot {\boldsymbol {Y}} ^ {K + 1} = g \left(\boldsymbol {Y} ^ {K}, t\right) + \left(\frac {\partial g}{\partial \boldsymbol {Y}}\right) _ {K} \left(\boldsymbol {Y} ^ {K + 1} - \boldsymbol {Y} ^ {K}\right) K = 0, 1, \dots (7 - 8 0)$$

满足给定边界条件
