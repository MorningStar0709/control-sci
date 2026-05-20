# 4.1 外部稳定性和内部稳定性

外部稳定性 考虑一个线性因果系统, 如果对应于一个有界的输入 $\alpha(t)$ , 即满足条件

$$\| \boldsymbol {u} (t) \| \leqslant k _ {1} < \infty , \quad \forall t \in [ t _ {0}, \infty) \tag {4.1}$$

的输入 $\boldsymbol{u}(t)$ ，所产生的输出 $\boldsymbol{y}(t)$ 也是有界的，即成立

$$\| \mathbf {y} (t) \| \leqslant k _ {2} < \infty , \quad \forall t \in [ t _ {0}, \infty) \tag {4.2}$$

则称此因果系统是外部稳定的，也即是有界输入-有界输出稳定的，并简称为 BIBO 稳定。应当指出，在讨论外部稳定性时，必须假定系统的初始条件为零；因为，只是在这种假定下，系统的输入-输出描述才是唯一的和有意义的。

线性系统的 BIBO 稳定性可根据其脉冲响应矩阵或传递函数矩阵来进行判别。下面，给出判别外部稳定性的一些常用的准则。

结论1[时变情况] 对于零初始条件的线性时变系统, 表 $G(t, \tau)$ 为其脉冲响应矩阵, 则系统为BIBO稳定的充分必要条件是, 存在一个有限常数 $k$ , 使对于一切 $t \in [t_0, \infty)$ , $G(t, \tau)$ 的每一个元 $g_{ij}(t, \tau)$ ( $i = 1, 2, \cdots, q$ ; $j = 1, 2, \cdots, p$ ) 均满足关系式

$$\int_ {t _ {0}} ^ {t} \left| g _ {i j} (t, \tau) \right| d \tau \leqslant k < \infty \tag {4.3}$$

证 分成两步来证明。首先，考虑 $p = q = 1$ 即单输入-单输出的情况。先证充分性：已知（4.3）成立，且任意输入 $u(t)$ 满足 $|u(t)| \leqslant k_1 < \infty, t \in [t_0, \infty)$ ，那么利用由脉冲响应函数 $g(t, \tau)$ 表示的输出 $y(t)$ 的表达式，就可得到

$$\left| y (t) \right| = \left| \int_ {t _ {0}} ^ {t} g (t, \tau) u (\tau) d \tau \right| \leqslant \int_ {t _ {0}} ^ {t} | g (t, \tau) | | u (\tau) | d \tau\leqslant k _ {1} \int_ {t _ {0}} ^ {t} | g (t, \tau) | d \tau \leqslant k _ {1} k = k _ {2} < \infty \tag {4.4}$$

从而由定义知系统为 BIBO 稳定。再证必要性：采用反证法，设存在某个 $t_{1} \in [t_{0}, \infty)$ 使

$$\int_ {t _ {0}} ^ {t _ {1}} | g (t, \tau) | d \tau = \infty \tag {4.5}$$

则定义如下的一个有界输入

$$
u (t) = \operatorname{sgn} g \left(t _ {1}, t\right) = \left\{ \begin{array}{c l} + 1, & \text {当} g \left(t _ {1}, t\right) > 0 \\ 0, & \text {当} g \left(t _ {1}, t\right) = 0 \\ - 1, & \text {当} g \left(t _ {1}, t\right) <   0 \end{array} \right. \tag {4.6}
$$

考察由它作用下所产生的输出 $y(t)$ ，易知

$$y \left(t _ {1}\right) = \int_ {t _ {0}} ^ {t _ {1}} g \left(t _ {1}, \tau\right) u (\tau) d \tau = \int_ {t _ {0}} ^ {t _ {1}} \left| g \left(t _ {1}, \tau\right) \right| d \tau = \infty \tag {4.7}$$

表明输出 $y(t)$ 为无界，而这是和已知系统为 BIBO 稳定相矛盾的。因此，反设不成立，即

$$\int_ {t _ {0}} ^ {t} | g (t, \tau) | d \tau \leqslant k < \infty , \quad \forall t \in [ t _ {0}, \infty) \tag {4.8}$$

进而，考虑多输入-多输出的情况。注意到此时系统输出 $y(t)$ 的分量 $y_{i}(t)$ 满足关系式
