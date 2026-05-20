# 5.5.1 终端时间有限的状态调节器问题

设系统状态方程为

$$\boldsymbol {X} (k + 1) = \boldsymbol {A} (k) \boldsymbol {X} (k) + \boldsymbol {B} (k) \boldsymbol {U} (k) \tag {5-52}\boldsymbol {X} (0) = \boldsymbol {X} _ {0}$$

二次型性能指标为

$$J = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} (N) \boldsymbol {P} (N) \boldsymbol {X} (N) + \frac {1}{2} \sum_ {k = 0} ^ {N - 1} [ \boldsymbol {X} ^ {\mathrm{T}} (k) \boldsymbol {Q} (k) \boldsymbol {X} (k) +\left. \boldsymbol {U} ^ {\mathrm{T}} (\boldsymbol {k}) \boldsymbol {R} (\boldsymbol {k}) \boldsymbol {U} (\boldsymbol {k}) \right] \tag {5-53}$$

$P(N)$ 、 $Q(k)$ 为半正定阵， $R(k)$ 为正定阵。要求寻找最优控制序列 $u(k)$ ，使J最小。

写出哈密顿函数

$$\boldsymbol {H} (k) = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} (k) \boldsymbol {Q} (k) \boldsymbol {X} (k) + \frac {1}{2} \boldsymbol {U} ^ {\mathrm{T}} (k) \boldsymbol {R} (k) \boldsymbol {U} (k) +\boldsymbol {\lambda} ^ {T} (k + 1) [ \boldsymbol {A} (k) \boldsymbol {X} (k) + \boldsymbol {B} (k) \boldsymbol {U} (k) ] \tag {5-54}$$

协态方程

$$\boldsymbol {\lambda} (k) = \frac {\partial \boldsymbol {H} (k)}{\partial \boldsymbol {X} (k)} = \boldsymbol {Q} (\dot {k}) \boldsymbol {X} (k) + \boldsymbol {A} ^ {\mathrm{T}} (k) \boldsymbol {\lambda} (k + 1) \tag {5-55}$$

横截条件为

$$
\begin{array}{l} \boldsymbol {\lambda} (N) = \frac {\partial \phi}{\partial \boldsymbol {X} (N)} = \frac {\partial}{\partial \boldsymbol {X} (N)} \left[ \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} (N) \boldsymbol {P} (N) \boldsymbol {X} (N) \right] \\ = \boldsymbol {P} (N) \boldsymbol {X} (N) \tag {5-56} \\ \end{array}
$$

控制方程为

$$\frac {\partial \boldsymbol {H} (k)}{\partial \boldsymbol {U} (k)} = \boldsymbol {R} (k) \boldsymbol {U} (k) + \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {\lambda} (k + 1) = \boldsymbol {0}\boldsymbol {U} (k) = - \boldsymbol {R} ^ {- 1} (k) \boldsymbol {B} ^ {\mathrm{T}} (k) \boldsymbol {\lambda} (k + 1) \tag {5-57}$$

假设

$$\boldsymbol {\lambda} (k) = \boldsymbol {K} (k) \boldsymbol {X} (k) \tag {5-58}$$

把式 $(5-58)$ 代入协态方程 $(5-55)$ 得

$$\boldsymbol {K} (k) \boldsymbol {X} (k) = \boldsymbol {Q} (k) \boldsymbol {X} (k) + \boldsymbol {A} ^ {\mathrm{T}} (k) \boldsymbol {K} (k + 1) \boldsymbol {X} (k + 1) \tag {5-59}$$

由状态方程 $(5-52)$ 和控制方程 $(5-57)$ 可得
