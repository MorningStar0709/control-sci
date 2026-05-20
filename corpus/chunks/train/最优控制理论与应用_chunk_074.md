$$\delta J _ {\mathrm{a}} = \left[ \frac {\partial \theta^ {\mathrm{T}}}{\partial \boldsymbol {X} (N)} - \boldsymbol {\lambda} ^ {\mathrm{T}} (N) \right] \delta \boldsymbol {X} (N) + \boldsymbol {\lambda} ^ {\mathrm{T}} (0) \delta \boldsymbol {X} (0) +\sum_ {k = 0} ^ {N - 1} \left\{\left[ \left(\frac {\partial H (k)}{\partial \boldsymbol {X} (k)}\right) ^ {\mathrm{T}} - \boldsymbol {\lambda} ^ {\mathrm{T}} (k) \right] \delta \boldsymbol {X} (k) + \left(\frac {\partial \boldsymbol {H} (k)}{\partial \boldsymbol {U} (k)}\right) ^ {\mathrm{T}} \delta \boldsymbol {U} (k) \right\} \tag {4-94}$$

上式中 $H(k) = H(X, U, \lambda, k)$ 。由于初始条件 $X(0)$ 给定，故 $\delta X(0) = 0$ 。根据 $\delta J_{\mathrm{a}} = 0$ 以及 $\delta X(N), \delta X(k), \delta U(k)$ 的任意性，可推导出最优控制序列应满足的必要条件：

正则方程

$$\boldsymbol {\lambda} (k) = \frac {\partial H (k)}{\partial \boldsymbol {X} (k)} \quad k = 0, 1, \dots , N - 1 \tag {4-95}X (k + 1) = \frac {\partial H (k)}{\partial \lambda (k + 1)} \tag {4-96}$$

横截条件

$$\boldsymbol {\lambda} (N) = \frac {\partial \theta}{\partial \boldsymbol {X} (N)} = \frac {\partial \phi}{\partial \boldsymbol {X} (N)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {X} (N)} \boldsymbol {v} \tag {4-97}$$

控制方程

$$\frac {\partial H (k)}{\partial \boldsymbol {U} (k)} = \mathbf {0} \quad k = 0, 1, \dots , N - 1 \tag {4-98}$$

初始条件

$$\boldsymbol {X} (0) = \boldsymbol {X} _ {0} \tag {4-99}$$

所得结果与连续系统类似,但应注意协态方程(4-95)的右侧无负号。从上面的一组方程可知,已知初始条件 $X(0)=X_{0}$ ,又从横截条件可求出 $\lambda(N)$ ,这样得出了离散非线性两点边值问题,求解一般是困难的。

（2）控制向量有约束。这时 $\frac{\partial H(k)}{\partial U(k)} = 0$ 一般不成立。根据极小值原理，哈密顿函数在最优控制序列上取极小值，即

$$H \left[ \boldsymbol {X} ^ {*} (k), \boldsymbol {U} ^ {*} (k), \boldsymbol {\lambda} ^ {*} (k + 1), k \right] = \min _ {\boldsymbol {v} \in \Omega} \left[ \boldsymbol {X} ^ {*} (k), \boldsymbol {U} (k), \boldsymbol {\lambda} ^ {*} (k + 1), k \right]$$

例4-4 系统的状态方程为

$$x (k + 1) = x (k) + u (k) \quad x (0) = 1 \tag {4-100}$$

$u(k)$ 无约束，指标函数为

$$J (u) = \frac {1}{2} x ^ {2} (2) + \frac {1}{2} \sum_ {k = 0} ^ {1} u ^ {2} (k) \tag {4-101}$$

用离散极小值原理求最优控制 $u^{*}(0)$ 、 $u^{*}(1)$ ，使 J 取极小。

解 哈密顿函数为

$$H (k) = \frac {1}{2} u ^ {2} (k) + \lambda (k + 1) [ x (k) + u (k) ] \quad (4 - 1 0 2)$$

协态方程为

$$\lambda (k) = \frac {\partial H (k)}{\partial x (k)} = \lambda (k + 1) \tag {4-103}$$

即协态为常数。

横截条件为
