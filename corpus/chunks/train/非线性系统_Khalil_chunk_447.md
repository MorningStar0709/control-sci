$$\dot {x} = f (x) + G (x) \alpha (x) + G (x) \beta (x) v \tag {14.75}y = h (x) \tag {14.76}$$

满足定理 14.4 的条件, 就可以用 $v = -\phi(y)$ 全局稳定原点, 这里 v 为输入, y 为输出。利用反馈将非无源系统转化为无源系统, 称为反馈无源化 $^{①}$ 。

例14.16 一个 $m$ 连杆机器人的非线性动力学方程为

$$M (q) \ddot {q} + C (q, \dot {q}) \dot {q} + D \dot {q} + g (q) = u$$

其中 q 是广义坐标中的 m 维向量, 表示相应连杆位置, u 是 m 维控制输入, $M(q)$ 是对所有 $q \in R^{m}$ 都正定的对称惯量矩阵, $C(q, \dot{q}) \dot{q}$ 一项代表离心力和科里奥利力, 矩阵 C 的特性是使得 M - 2C 对于所有 $q, \dot{q} \in R^{m}$ 都为斜对称矩阵, 其中 M 是 $M(q)$ 对 t 的全微分, $D\dot{q}$ —项表示黏滞阻尼,其中 D 是半正定对称矩阵, $g(q)$ 代表重力,由 $g(q)=\left[\partial P(q)/\partial q\right]^{\mathrm{T}}$ 给出,其中 $P(q)$ 是由重力引起的所有连杆的总势能。现在考虑设计状态反馈控制律的调节问题,使 q 渐近跟踪常数参考信号 $q_{r}$ 。设 $e=q-q_{r}$ ,则 e 满足微分方程

$$M (q) \ddot {e} + C (q, \dot {q}) \dot {e} + D \dot {e} + g (q) = u$$

我们的目标是在 $(e = 0, \dot{e} = 0)$ 处稳定系统，但这个点不是开环平衡点。设

$$u = g (q) - K _ {p} e + v$$

其中 $K_{p}$ 是正定对称矩阵， $v$ 是待选择的附加控制分量，将 $u$ 代入 $\ddot{e}$ 方程，得

$$M (q) \ddot {e} + C (q, \dot {q}) \dot {e} + D \dot {e} + K _ {p} e = v$$

取 $V = \frac{1}{2} \dot{e}^{\mathrm{T}} M(q) \dot{e} + \frac{1}{2} e^{\mathrm{T}} K_{p} e$

作为备选存储函数, 函数 V 是正定的, 且其导数满足

$$
\begin{array}{l} \dot {V} = \dot {e} ^ {\mathrm{T}} M \ddot {e} + \frac {1}{2} \dot {e} ^ {\mathrm{T}} \dot {M} \dot {e} + e ^ {\mathrm{T}} K _ {p} \dot {e} \\ = \frac {1}{2} \dot {e} ^ {\mathrm{T}} (\dot {M} - 2 C) \dot {e} - \dot {e} ^ {\mathrm{T}} D \dot {e} - \dot {e} ^ {\mathrm{T}} K _ {p} e + \dot {e} ^ {\mathrm{T}} v + e ^ {\mathrm{T}} K _ {p} \dot {e} \\ \leqslant \dot {e} ^ {\mathrm{T}} v \\ \end{array}
$$

把输出定义为 $y = \dot{e}$ ，可看出输入为 $v$ ，输出为 $y$ 的系统是无源的， $V$ 为存储函数。注意，把反馈分量 $g(q) - K_p e$ 无源化的作用是给势能一个新的表达式，即 $(1/2)e^T K_p e$ ，在 $e = 0$ 处有唯一的极小值，动能与该势能之和即为存储函数。当 $v = 0$ 时，有

$$y (t) \equiv 0 \Leftrightarrow \dot {e} (t) \equiv 0 \Rightarrow \ddot {e} (t) \equiv 0 \Rightarrow K _ {p} e (t) \equiv 0 \Rightarrow e (t) \equiv 0$$

说明系统是零状态可观测的,因此取控制 $v = -\phi(\dot{e})$ , 可使系统达到全局稳定, 其中任意函数 $\phi$ 对于所有 $y \neq 0$ , 满足 $\phi(0) = 0, y^{\mathrm{T}} \phi(y) > 0$ 。选择 $v = -K_{d} \dot{e}, K_{d}$ 是正定对称阵, 可得控制律 $u = g(q) - K_{p}(q - q_{r}) - K_{d} \dot{q}$

上式是附加一个重力补偿项的经典 PD 控制器。

一类服从反馈无源化(feedback passivation)的系统是无源系统的级联,该无源系统的无激励动力学方程在原点处有一个稳定平衡点。考虑系统

$$\dot {z} = f _ {a} (z) + F (z, y) y \tag {14.77}\dot {x} = f (x) + G (x) u \tag {14.78}y = h (x) \tag {14.79}$$
