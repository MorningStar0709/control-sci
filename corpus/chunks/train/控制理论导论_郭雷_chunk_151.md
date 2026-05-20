定理2.2.13 假设 $f(t,x), \frac{\partial f(t,x)}{\partial x}$ 在 $\Omega_{n+1}$ 内连续。设微分方程(2.2.19)的以 $(t_0, x_0)$ 为初值的解 $\varphi(t; t_0, x_0)$ 在闭区间 $r_1 \leqslant t \leqslant r_2$ 上有定义，那么存在正数 $\sigma > 0$ ，使得当 $|\bar{t}_0 - t_0| < \sigma, |\bar{x}_0 - x_0| < \sigma$ 时，微分方程(2.2.19)的以 $(\bar{t}_0, \bar{x}_0)$ 为初值的解 $\varphi(t; \bar{t}_0, \bar{x}_0)$ 也在区间 $r_1 \leqslant t \leqslant r_2$ 上确定，且是 $(t, \bar{t}_0, \bar{x}_0)$ 的连续函数。

同理能够得到微分方程 (2.2.19) 的初值问题的解关于初值的可微性定理.

定理2.2.14 设微分方程(2.2.19)的右端函数满足定理2.2.13中的条件。如果微分方程(2.2.19)的以 $(t_0, x_0)$ 为初值的解 $\varphi(t; t_0, x_0)$ 在闭区间 $r_1 \leqslant t \leqslant r_2$ 上确定，那么必定存在正数 $\sigma_1 > 0$ ，使得当 $|\bar{t}_0 - t_0| < \sigma_1, |\bar{x}_0 - x_0| < \sigma_1$ 时，有

(1) $\varphi(t; \bar{t}_0, \bar{x}_0)$ 关于 $\bar{t}_0$ 和 $\bar{x}_0$ 的偏导数 $\frac{\partial \varphi(t; \bar{t}_0, \bar{x}_0)}{\partial \bar{t}_0}$ , $\frac{\partial \varphi(t; \bar{t}_0, \bar{x}_0)}{\partial \bar{x}_0}$ 存在;

(2) $\frac{\partial\varphi(t;\bar{t}_0,\bar{x}_0)}{\partial\bar{x}_0}$ 满足矩阵型变分方程

$$\dot {\boldsymbol {Z}} (t) = \frac {\partial f (t , \varphi (t ; \bar {t} _ {0} , \bar {x} _ {0}))}{\partial x} \boldsymbol {Z} (t) \tag {2.2.38}$$

和初始条件

$$\boldsymbol {Z} (\bar {t} _ {0}) = \boldsymbol {I} _ {n}, \tag {2.2.39}$$

这里 $I_{n}$ 为 $n \times n$ 单位方阵；而 $\frac{\partial \varphi(t; t_0, \bar{x}_0)}{\partial \bar{t}_0}$ 满足向量型变分方程

$$\dot {z} (t) = \frac {\partial f (t , \varphi (t ; \bar {t} _ {0} , \bar {x} _ {0}))}{\partial x} z (t) \tag {2.2.40}$$

和初始条件

$$z (t _ {0}) = - f (\bar {t} _ {0}, \bar {x} _ {0}); \tag {2.2.41}$$

(3) $\frac{\partial^2\varphi(t;\bar{t}_0,\bar{x}_0)}{\partial t\partial\bar{t}_0},\frac{\partial\varphi(t;\bar{t}_0,\bar{x}_0)}{\partial t\partial\bar{x}_0}$ 存在且连续.

注2.2.1 当微分方程(2.2.19)是标量方程时，可直接求得 $\frac{\partial\varphi(t;t_0,x_0)}{\partial t_0}$ 和 $\frac{\partial\varphi(t;t_0,x_0)}{\partial x_0}$ 的表示式如下：

$$\frac {\partial \varphi (t ; t _ {0} , x _ {0})}{\partial t _ {0}} = - f (t _ {0}, x _ {0}) \exp \left\{\int_ {t _ {0}} ^ {t} \frac {\partial f (s , \varphi (s ; t _ {0} , x _ {0}))}{\partial x} d s \right\},\frac {\partial \varphi (t ; t _ {0} , x _ {0})}{\partial x _ {0}} = \exp \left\{\int_ {t _ {0}} ^ {t} \frac {\partial f (s , \varphi (s ; t _ {0} , x _ {0}))}{\partial x} d s \right\}.$$

注2.2.2 用数学归纳法能够证明，如果微分方程(2.2.33)的右端连续向量值函数 $f(t, x; \mu)$ 具有关于 $(x, \mu)$ 的直到 $p(p$ 是大于1的整数)阶的连续偏导数，那么它的以 $(t_0, x_0)$ 为初值的解 $\varphi(t; \mu)$ 也具有关于参数 $\mu$ 的直到 $p$ 阶的连续偏导数.

注2.2.3 用数学归纳法能够证明，如果微分方程(2.2.19)右端的连续向量值函数 $f(t,x)$ 关于 $\pmb{x}$ 有直到 $\pmb{p}$ 阶的连续偏微商，关于 $\pmb{t}$ 有一阶连续偏微商，则它的以 $(t_0,x_0)$ 为初值的解 $\varphi (t;t_0,x_0)$ 必具有对 $x_0$ 的直到 $\pmb{p}$ 阶偏导数以及对 $t_0$ 求导一次对 $x_0$ 求导 $(p - 1)$ 次的混合偏微商.
