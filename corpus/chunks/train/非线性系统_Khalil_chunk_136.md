$$\leqslant \int_ {t} ^ {t + \delta} 2 \| \phi (\tau ; t, x) \| _ {2} \| \phi_ {x} (\tau ; t, x) \| _ {2} d \tau\leqslant \int_ {t} ^ {t + \delta} 2 k e ^ {- \lambda (\tau - t)} e ^ {L (\tau - t)} d \tau \| x \| _ {2}= \frac {2 k}{(\lambda - L)} [ 1 - e ^ {- (\lambda - L) \delta} ] \| x \| _ {2}$$

这样, 当 $c_{4}=\frac{2k}{(\lambda-L)}[1-e^{-(\lambda-L)\delta}]$

时， $V(t,x)$ 满足定理的最后一个不等式。如果所有假设都全局成立，则显然可选择 $r_{0}$ 任意大。如果系统是自治的，那么 $\phi(\tau;t,x)$ 仅与 $(\tau-t)$ 有关，即

$$\phi (\tau ; t, x) = \psi (\tau - t; x)$$

于是 $V(t,x) = \int_{t}^{t + \delta}\psi^{\mathrm{T}}(\tau -t;x)\psi (\tau -t;x)d\tau = \int_0^\delta \psi^{\mathrm{T}}(s;x)\psi (s;x)ds$

即 $V(t,x)$ 与 t 无关。

在定理 4.13 中看到, 如果在原点线性化的非线性系统有一个指数稳定平衡点, 那么原点就是非线性系统的指数稳定平衡点。我们将用定理 4.14 证明线性化的指数稳定性是原点指数稳定性的充要条件。

定理4.15 设 $x = 0$ 是非线性系统 $\dot{x} = f(t,x)$

的平衡点,其中 $f:[0,\infty)\times D\to R^{n}$ 连续可微, $D=\{x\in R^{n}\mid\|x\|_{2}<r\}$ ,雅可比矩阵 $\left[\partial f/\partial x\right]$ 在 D 上有界,是利普希茨矩阵,且对 t 一致。设

$$A (t) = \left. \frac {\partial f}{\partial x} (t, x) \right| _ {x = 0}$$

那么，当且仅当 $x = 0$ 是线性系统 $\dot{x} = A(t)x$

的指数稳定平衡点时,它也是非线性系统的指数稳定平衡点。

证明:定理中的“当”部分的证明与定理4.13相同,为了证明“仅当”部分,把线性系统写成

$$\dot {x} = f (t, x) - [ f (t, x) - A (t) x ] = f (t, x) - g (t, x)$$

回顾前面的定理 4.13, 可知

$$\| g (t, x) \| _ {2} \leqslant L \| x \| _ {2} ^ {2}, \forall x \in D, \forall t \geqslant 0$$

由于原点是非线性系统的指数稳定平衡点,因此存在正常数 $k, \lambda$ 和 c,使

$$\| x (t) \| _ {2} \leqslant k \| x (t _ {0}) \| _ {2} e ^ {- \lambda (t - t _ {0})}, \forall t \geqslant t _ {0} \geqslant 0, \forall \| x (t _ {0}) \| _ {2} < c$$

选择 $r_0 < \min \{c, r/k\}$ ，则定理4.14的所有条件都得到满足。设 $V(t, x)$ 是定理4.14给出的函数，用其作为线性系统的备选李雅普诺夫函数，有

$$
\begin{array}{l} \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} A (t) x = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) - \frac {\partial V}{\partial x} g (t, x) \\ \leqslant - c _ {3} \| x \| _ {2} ^ {2} + c _ {4} L \| x \| _ {2} ^ {3} \\ <   - \left(c _ {3} - c _ {4} L \rho\right) \| x \| _ {2} ^ {2}, \quad \forall \| x \| _ {2} <   \rho \\ \end{array}
$$

选择 $\rho < \min \{r_0, c_3 / (c_4L)\}$ 保证了当 $\|x\|_2 < \rho$ 时， $\dot{V}(t,x)$ 负定。因此，当 $\|x\|_2 < \rho$ 时满足定理4.10的所有条件，从而得出结论：对于线性系统，原点是指数稳定平衡点。

推论4.3 设 $x = 0$ 是非线性系统 $\dot{x} = f(x)$ 的平衡点, 其中 $f(x)$ 在 $x = 0$ 的某个邻域内连续可微, 设 $A = [\partial f / \partial x](0)$ 。那么, 当且仅当 $A$ 是赫尔维茨矩阵时, $x = 0$ 是非线性系统的指数稳定平衡点。

例 4.23 设有一阶系统 $\dot{x} = -x^{3}$ 。由例 4.14 已知原点是渐近稳定的，但在原点线性化后得到的线性系统 $\dot{x} = 0$ ，其矩阵 A 不是赫尔维茨矩阵。根据推论 4.3，可知原点不是指数稳定的。
