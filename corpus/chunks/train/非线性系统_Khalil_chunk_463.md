# 14.2 水下作业船偏航的简化模型为 $^{[60]}$

$$\ddot {\psi} + a \dot {\psi} | \dot {\psi} | = \tau$$

其中 $\psi$ 是航向改变角， $\tau$ 是归一化的力矩输入，a 是正参数，期望 $\psi$ 能够跟踪预定的轨线 $\psi_{r}(t)$ ，其中 $\psi_{r}(t)$ ， $\dot{\psi}_{r}(t)$ 和 $\ddot{\psi}_{r}(t)$ 都是 t 的有界函数，令 $\hat{a}=1$ 是 a 的归一化。

(a) 用 $x_{1}=\psi$ 和 $x_{2}=\dot{\psi}$ 作为状态变量, $u=\tau$ 作为控制输入, $y=\psi$ 作为输出, 求出系统模型。

(b) 证明这个系统是输入-输出线性化的。

(c) 设 $a=\hat{a}=1$ ，利用反馈线性化设计一个状态反馈控制器，实现全局渐近跟踪。

(d) 设 $|\hat{a} - a| \leqslant 0.01$ 和 $\psi_r(t) = \sin 2t$ , 证明 (c) 中设计的控制器能在容许偏差为$|\psi(t)-\psi_{r}(t)|\leqslant\delta_{1}$ 时实现渐近跟踪，并估计 $\delta_{1}$ 。另外，是否对所有初始状态都能保证这样的容许偏差？

(e) 设 $\left|\hat{a}-a\right|\leqslant k$ ，其中 k 是已知的，设计一个状态反馈控制器实现全局渐近跟踪，其容许偏差要满足 $\left|\psi(t)-\psi_{r}(t)\right|\leqslant0.01$ 。

14.3 (见文献[176])考虑受控范德波尔方程

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = - \omega^ {2} x _ {1} + \varepsilon \omega (1 - \mu^ {2} x _ {1} ^ {2}) x _ {2} u$$

其中 $\omega, \varepsilon$ 和 $\mu$ 是正常数, u 是控制输入。

(a) 证明当 u=1 时, 在曲面 $x_{1}^{2}+x_{2}^{2}/\omega^{2}=1/\mu^{2}$ 外, 存在一个稳定的极限环。当 u=-1 时, 在同一曲面外存在一个非稳定极限环。

(b) 设 $s = x_{1}^{2} + x_{2}^{2}/\omega^{2} - r^{2}$ ，其中 $r < 1/\mu$ 。证明把系统运动限制在 s = 0 曲面上，即 $s(t) \equiv 0$ 时，可得到一个多谐振荡器

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = - \omega^ {2} x _ {1}$$

产生频率为 $\omega$ ，幅度为 r 的正弦波。

(c) 设计一个状态反馈滑模控制器, 把带状区域 $\left|x_{1}\right|<1/\mu$ 内的所有轨线都驱动到流形 s=0 上, 并使其在该流形上滑动。

(d) 对系统在理想滑模控制下的响应及其连续逼近的响应进行仿真, 参数为 $\omega = \mu = \varepsilon = 1$ 。

14.4 考虑系统 $\dot{x}_1 = x_2 + ax_1\sin x_1,\quad \dot{x}_2 = bx_1x_2 + u$

其中 a 和 b 是未知常数,但已知其边界为 $\left|a-1\right|\leqslant1$ 和 $\left|b-1\right|\leqslant2$ ,应用滑模控制,设计一个连续全局稳定的状态反馈控制器。

14.5 一个悬挂点时变、有界且在水平方向加速的单摆,其运动方程为

$$m \ell \ddot {\theta} + m g \sin \theta + k \ell \dot {\theta} = T / \ell + m h (t) \cos \theta$$

其中 h 是水平加速度, T 是力矩输入, 其他变量与 1.2.1 节中的定义相同。假设

$$0. 9 \leqslant \ell \leqslant 1. 1, \quad 0. 5 \leqslant m \leqslant 1. 5, \quad 0 \leqslant k \leqslant 0. 2, \quad | h (t) | \leqslant 1$$

且 g=9.81。希望对任意初始条件 $\theta(0)$ 和 $\dot{\theta}(0)$ ，使单摆在 $\theta=0$ 处稳定。设计一个连续滑模状态反馈控制器，在 $|\theta|\leqslant0.01$ 和 $|\dot{\theta}|\leqslant0.01$ 时，实现毕竟有界。

14.6 （见文献[108]）考虑系统

$$\dot {x} _ {1} = x _ {1} x _ {2}, \quad \dot {x} _ {2} = x _ {1} + u$$

(a) 应用滑模控制,设计一个连续全局稳定的状态反馈控制器。

(b) 能通过反馈线性化使原点达到全局稳定吗?

14.7 考虑系统 $\dot{x}_{1} = -x_{1} + \tanh(x_{2}), \quad \dot{x}_{2} = x_{2} + x_{3}, \quad \dot{x}_{3} = u + \delta(x)$
