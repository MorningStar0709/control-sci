# 3.3 解的可微性和灵敏度方程

假设对于所有 $(t, x, \lambda) \in [t_0, t_1] \times R^n \times R^p, f(t, x, \lambda)$ 对于 $(t, x, \lambda)$ 连续，且对于 $x$ 和 $\lambda$ 有一阶偏导数，设 $\lambda_0$ 是 $\lambda$ 的一个标称值，并假设标称状态方程

$$\dot {x} = f (t, x, \lambda_ {0}), \qquad x (t _ {0}) = x _ {0}$$

在 $[t_0, t_1]$ 上有唯一解 $x(t, \lambda_0)$ 。由定理3.5可知，当所有 $\lambda$ 足够接近 $\lambda_0$ ，即 $\| \lambda - \lambda_0\|$ 足够小时，状态方程 $\dot{x} = f(t, x, \lambda), \quad x(t_0) = x_0$

在 $[t_0, t_1]$ 上有唯一解 $x(t, \lambda)$ ，该解接近于标称解 $x(t, \lambda_0)$ 。 $f$ 对于 $x$ 和 $\lambda$ 的连续可微性是指附加性质，即解 $x(t, \lambda)$ 对于 $\lambda_0$ 附近的 $\lambda$ 是可微的，为说明这一点，取

$$x (t, \lambda) = x _ {0} + \int_ {t _ {0}} ^ {t} f (s, x (s, \lambda), \lambda) d s$$

求对 $\lambda$ 的偏导数, 可得

$$x _ {\lambda} (t, \lambda) = \int_ {t _ {0}} ^ {t} \left[ \frac {\partial f}{\partial x} (s, x (s, \lambda), \lambda) x _ {\lambda} (s, \lambda) + \frac {\partial f}{\partial \lambda} (s, x (s, \lambda), \lambda) \right] d s$$

其中 $x_{\lambda}(t,\lambda) = [\partial x(t,\lambda) / \partial \lambda ],[\partial x_0 / \partial \lambda ] = 0$ ，因为 $x_0$ 与 $\lambda$ 无关。对 $t$ 求微分，即可看出 $x_{\lambda}(t,\lambda)$ 满足微分方程

$$\frac {\partial}{\partial t} x _ {\lambda} (t, \lambda) = A (t, \lambda) x _ {\lambda} (t, \lambda) + B (t, \lambda), \quad x _ {\lambda} (t _ {0}, \lambda) = 0 \tag {3.4}$$

其中， $A(t,\lambda) = \frac{\partial f(t,x,\lambda)}{\partial x}\Big|_{x = x(t,\lambda)},\quad B(t,\lambda) = \frac{\partial f(t,x,\lambda)}{\partial\lambda}\Big|_{x = x(t,\lambda)}$

当 $\lambda$ 足够接近 $\lambda_0$ 时，矩阵 $A(t, \lambda)$ 和 $B(t, \lambda)$ 在 $[t_0, t_1]$ 上有定义，因此 $x_{\lambda}(t, \lambda)$ 也定义在同一区间。在 $\lambda = \lambda_0$ 处，式(3.4)的右边仅与标称解 $x(t, \lambda_0)$ 有关。设 $S(t) = x_{\lambda}(t, \lambda_0)$ ，那么

$S(t)$ 就是方程

$$\dot {S} (t) = A \left(t, \lambda_ {0}\right) S (t) + B \left(t, \lambda_ {0}\right), \quad S \left(t _ {0}\right) = 0 \tag {3.5}$$

的唯一解。函数 $S(t)$ 称为灵敏度函数，式(3.5)称为灵敏度方程。灵敏度函数给出解受参数变化影响的一阶估值，也可用于当 $\lambda$ 足够接近标称值 $\lambda_0$ 时逼近系统方程的解。当 $\| \lambda - \lambda_0 \|$ 较小时， $x(t, \lambda)$ 可在标称解 $x(t, \lambda_0)$ 附近按泰勒级数展开，得

$$x (t, \lambda) = x (t, \lambda_ {0}) + S (t) (\lambda - \lambda_ {0}) + \mathrm{高阶项}$$

忽略高阶项, 解 $x(t, \lambda)$ 可由

$$x (t, \lambda) \approx x (t, \lambda_ {0}) + S (t) (\lambda - \lambda_ {0}) \tag {3.6}$$

近似。这里不去验证这个近似值，在第10章讨论扰动理论时验证。式(3.6)的意义是，知道标称解和灵敏度函数，就足以逼近在以 $\lambda_{0}$ 为中心的小球内对所有 $\lambda$ 值的解。

计算灵敏度函数 $S(t)$ 的步骤可总结如下：
