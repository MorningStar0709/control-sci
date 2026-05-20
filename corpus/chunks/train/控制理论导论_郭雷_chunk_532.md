# 奇异快速控制

如上所述，本书仅涉及当(7.2.6)式中某个 $q_{j_0}(x^* (t),\psi (t),t)$ 在 $[t_1,t_2]\subset [t_0,t_f]$ 中恒为零的奇异快速控制．虽然在此奇异区间上，不能从“极大条件”

$$H (x ^ {*} (t), u ^ {*} (t), \psi (t), t) \geqslant H (x ^ {*} (t), u, \psi (t), t), \quad \forall u \in \mathbb {U} _ {r}$$

确定出使 $H(x^{*}(t), u, \psi(t), t)$ 达到极大 $u^{*}(t)$ 的信息，但这并不意味着快速控制函数一定不存在。因此需要寻找另外的必要条件。下面为说明寻找的思路并简化记号，仅以单输入 $(u \in \mathbb{R}^1)$ 定常仿射非线性系统为例。

考察单输入仿射非线性系统快速控制问题

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + b (x) u, \\ x (t _ {0}) = x _ {0} \in \mathbb {R} ^ {n}, \end{array} \right. \tag {7.2.39}
| u | \leqslant 1, \tag {7.2.40}\boldsymbol {x} (t _ {f}) = 0, \tag {7.2.41}J [ u (\cdot) ] = \int_ {t _ {0}} ^ {t _ {f}} \mathrm{d} t = t _ {f} - t _ {0}. \tag {7.2.42}
$$

式 (7.2.39) 和式 (7.2.42) 的 Hamilton 函数 $H(x, u, \psi)$ 为

$$H (x, u, \psi) = - 1 + \psi^ {\mathrm{T}} (t) f (x) + \psi^ {\mathrm{T}} (t) b (x) u.$$

记 $\psi = [\psi_{1}, \psi_{2}, \cdots, \psi_{n}]^{T}$ , $f(x) = [f_{1}(x), f_{2}(x), \cdots, f_{n}(x)]^{T}$ 及

$$
\begin{array}{l} \alpha (\psi , x) = \psi^ {\mathrm{T}} f (x) = \sum_ {i = 1} ^ {n} \psi_ {i} f _ {i} (x), \\ \beta (\psi , x) = \psi^ {\mathrm{T}} b (x) = \sum_ {i = 1} ^ {n} \psi_ {i} b _ {i} (x), \\ \end{array}
$$

于是有

$$H (x, u, \psi) = - 1 + \alpha (\psi , x) + \beta (\psi , x) u. \tag {7.2.43}$$

根据极大值原理，沿最优解 $(x^{*}(t), u^{*}(t))$ 有 $H(x^{*}(t), u^{*}(t), \psi(t)) \equiv 0$ 。为简化书写，去掉“\*”，即有

$$\alpha (\psi (t), x (t)) + \beta (\psi (t), x (t)) u (t) \equiv 1, \tag {7.2.44}$$

而 $\psi(t)=[\psi_{1}(t),\psi_{2}(t),\cdots,\psi_{n}(t)]$ 满足

$$
\left\{ \begin{array}{l} \dot {\psi} _ {k} (t) = - \sum_ {i = 1} ^ {n} \psi_ {i} (t) \frac {\partial f _ {i} (x (t))}{\partial x _ {k}} - u (t) \sum_ {i = 1} ^ {n} \psi_ {i} (t) \frac {\partial b _ {i} (x (t))}{\partial x _ {k}}, \\ \psi_ {k} (t _ {f}) = \mu_ {k}, \quad k = 1, 2, \dots , n. \end{array} \right. \tag {7.2.45}
$$

当存在某个时间区间 $[t_1, t_2] \subset [t_0, t_f]$ 使得

$$\beta (t) \stackrel {\mathrm{def}} {=} \beta (\psi (t), x (t)) = \sum_ {i = 1} ^ {n} \psi_ {i} (t) b _ {i} (x (t)) = 0, \qquad \forall t \in [ t _ {1}, t _ {2} ] \tag {7.2.46}$$

时，符号函数 $\operatorname{sign} \beta(t)$ 无意义。此时满足控制约束 (7.2.40) 的任一控制函数皆满足极大条件，即不能从极大条件确定出一个或有限个 $u$ 。使式 (7.2.44) 和式 (7.2.46) 成立的控制 $u(t)$ 和相应的轨线 $x(t)$ 分别称为奇异快速控制和奇异轨线。下面探讨奇异快速控制满足的必要条件。由式 (7.2.44) 和式 (7.2.46) 知

$$\alpha (t) \stackrel {\mathrm{def}} {=} \alpha (\psi (t), x (t)) = \sum_ {i = 1} ^ {n} \psi_ {i} (t) f _ {i} (x (t)) = 1, \qquad \forall t \in [ t _ {1}, t _ {2} ]. \tag {7.2.47}$$
