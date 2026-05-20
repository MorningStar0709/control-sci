其中 $\omega$ 是转子的转速， $T_{L}$ 是负载力矩， $\lambda_{a}$ 和 $\lambda_{b}$ 是转子磁通量向量的分量， $i_{a}$ 和 $i_{b}$ 是定子电流向量的分量， $L_{r}$ 和 $M$ 是转子的自感和互感， $R_{r}$ 是转子的电阻， $J$ 是转动惯量， $p$ 是电极对的数量， $k_{t}$ 是正常数。负载力矩 $T_{L}$ 可取为 $T_{L} = T_{o} + \phi(\omega)$ ，其中 $\phi \in [0, \infty]$ 是局部利普希茨函数，表示摩擦力产生的负载模型，而 $T_{o}$ 表示的是与速度无关的负载模型，电流 $i_{a}$ 和 $i_{b}$ 是控制变量。我们想要设计一个反馈控制，在有未知负载力矩时，使速度 $\omega$ 跟踪参考速度 $\omega_{r}$ 。本习题通过把方程变换到以场为方向的坐标系中进行设计，这种变换把一个控制问题分解为两个独立的控制问题，一个是速度控制，另一个是转子磁通控制，该变换应在线运用，且要求转子磁通可测。首先假设转子磁通量已测得，然后利用观测器估计该磁通，并分析磁通由其估计值代替时的控制性能。分析时要考虑转子电阻的不确定性，因为在电机工作时，电阻值随温度的变化相当大。

(a) 设 $\rho$ 是转子磁通向量的角度, $\lambda_{d}$ 是其幅值, 即 $\rho = \arctan (\lambda_{b} / \lambda_{a}), \lambda_{d} = \sqrt{\lambda_{a}^{2} + \lambda_{b}^{2}}$ , 用 $\lambda_{d}$ 和 $\rho$ 代替 $\lambda_{a}$ 和 $\lambda_{b}$ 作为状态变量, 并将 $i_{a}$ 和 $i_{b}$ 转换为 $i_{d}$ 和 $i_{q}$ 。 $i_{d}$ 和 $i_{q}$ 定义为

$$
\left[ \begin{array}{l} i _ {d} \\ i _ {q} \end{array} \right] = \left[ \begin{array}{c c} \cos \rho & \sin \rho \\ - \sin \rho & \cos \rho \end{array} \right] \left[ \begin{array}{l} i _ {a} \\ i _ {b} \end{array} \right] \tag {14.117}
$$

上式说明电机可由状态模型表示为

$$J \dot {\omega} = k _ {t} \lambda_ {d} i _ {q} - T _ {L}, \quad \dot {\lambda} _ {d} = - \frac {R _ {r}}{L _ {r}} \lambda_ {d} + \frac {R _ {r} M}{L _ {r}} i _ {d}, \quad \dot {\rho} = p \omega + \frac {R _ {r} M i _ {q}}{L _ {r} \lambda_ {d}}$$

其中 $\lambda_{d}>0$ 。

(b) 上述模型中前两个方程与 $\rho$ 无关, 因此要设计对 $i_{d}$ 和 $i_{q}$ 的反馈控制, 可以从状态方程中消去 $\rho$ 。但仍需要 $\rho$ 由式(14.117)给出的反变换计算 $i_{a}$ 和 $i_{b}$ 。证明: 对常数 $\omega, i_{q}$ 和 $\lambda_{d}, \rho$ 是无界的, 并解释为什么对一个无界的 $\rho$ 不会有问题。

(c) 注意到电机产生的力矩与 $\lambda_{d}i_{q}$ 成正比, 因此可首先通过用控制输入 $i_{d}$ , 把 $\lambda_{d}$ 调节到期望的常数磁通 $\lambda_{r}$ , 以控制速度。然后可假设 $\lambda_{d} = \lambda_{r}$ , 设计 $i_{q}$ 。如果磁通环路的动态变化比速度环路的动态变化快得多, 可以证明该假设是合理的①。这部分习题设计一个磁通控制, 证明 $i_{d} = (\lambda_{r}/M) - k(\lambda_{d} - \lambda_{r})$ 实现所期望的调节, $k \geqslant 0$ 。

(d) 由于电流 $i_a$ 和 $i_b$ 必须限制为某一最大值, 因此在设计中, 要假设 $i_d$ 和 $i_q$ 限制为 $I_d$ 和 $I_q$ 。证明如果 $I_d > \lambda_r / M, 0 < \lambda_d(0) < \lambda_r$ , 则在饱和控制

$$i _ {d} = I _ {d} \mathrm{sat} \left(\frac {\lambda_ {r} / M - k (\lambda_ {d} - \lambda_ {r})}{I _ {d}}\right) \tag {14.118}$$

下, $\lambda_{d}(t)$ 从 $\lambda_{d}(0)$ 到 $\lambda_{r}$ 单调变化,估计稳定时间(settling time)。
