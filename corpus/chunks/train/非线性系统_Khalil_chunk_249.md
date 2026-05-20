时,定理8.5的所有假设全局满足,可得原点是全局指数稳定的。熟悉线性系统理论的读者会发现矩阵 $W(t,t+\delta)$ 是矩阵对 $(A(t),C(t))$ 的可观测性Gram矩阵,不等式 $W(t,t+\delta)\geqslant kI$ 是由 $(A(t),C(t))$ 的一致可观测性给出的。通过对本例和例4.21的比较可知,定理8.5允许我们用较弱的要求 $Q(t)=C^{\mathrm{T}}(t)C(t)$ 代替式(4.28)对矩阵 $Q(t)$ 为正定的要求,其中矩阵对 $(A(t),C(t))$ 是一致可观测的。

如例 8.11, 定理 8.4 和定理 8.5 及在线性系统中的应用广泛用于自适应控制系统的分析①。我们已在 1.2.6 节中分析了一个自适应控制系统的例子。

例8.12 在1.2.6节中我们看到了一个参考模型自适应控制系统的闭环方程，其中被控对象为 $\dot{y}_p = a_p y_p + k_p u$ ，参考模型为 $\dot{y}_m = a_m y_m + k_m r$ ，闭环方程由下式给出：

$$\dot {e} _ {o} = a _ {m} e _ {o} + k _ {p} \phi_ {1} r (t) + k _ {p} \phi_ {2} [ e _ {o} + y _ {m} (t) ]\dot {\phi} _ {1} = - \gamma e _ {o} r (t)\dot {\phi} _ {2} = - \gamma e _ {o} [ e _ {o} + y _ {m} (t) ]$$

其中 $\gamma > 0$ 是自适应控制增益， $e_0 = y_p - y_m$ 是输出误差， $\phi_1$ 和 $\phi_2$ 是参数误差。假设 $k_p > 0$ ，当

然参考模型必须有 $a_{m} < 0$ 。进一步假设 $r(t)$ 是分段连续且有界的，以

$$V = \frac {1}{2} \left[ \frac {e _ {o} ^ {2}}{k _ {p}} + \frac {1}{\gamma} (\phi_ {1} ^ {2} + \phi_ {2} ^ {2}) \right]$$

作为备选李雅普诺夫函数,可得

$$\dot {V} = \frac {a _ {m}}{k _ {p}} e _ {o} ^ {2} + e _ {o} (\phi_ {1} r + \phi_ {2} e _ {o} + \phi_ {2} y _ {m}) - \phi_ {1} e _ {o} r - \phi_ {2} e _ {o} (e _ {o} + y _ {m}) = \frac {a _ {m}}{k _ {p}} e _ {o} ^ {2} \leqslant 0$$

应用定理8.4可得，对于任意 $c > 0$ ，当所有初始状态属于集合 $\{V\leqslant c\}$ 时，所有状态变量对所有 $t\geqslant t_0$ 都有界，且 $\lim_{t\to \infty}e_0(t) = 0$ 。这说明设备的输出 $y_{p}$ 跟踪希望的输出 $y_{m}$ ，但没有说明参数误差 $\phi_{1}$ 和 $\phi_{2}$ 都收敛于零。事实上，它们可能不收敛于零。例如， $r$ 和 $y_{m}$ 是非零恒定信号，则闭环系统将有一个平衡子空间 $\{e_0 = 0,\phi_2 = (a_m / k_m)\phi_1\}$ ，这清楚地说明，一般情况下 $\phi_{1}$ 和 $\phi_{2}$ 并不收敛于零。为推出 $\phi_{1}$ 和 $\phi_{2}$ 收敛于零的条件，应用定理8.5将得到原点 $(e_0 = 0,\phi_1 = 0,\phi_2 = 0)$ 一致渐近稳定的条件。因为已经证明所有状态变量都是有界的，所以可将闭环系统表示为线性时变系统

$$
\dot {x} = \left[ \begin{array}{c c c} {{a _ {m}}} & {{k _ {p} r (t)}} & {{k _ {p} y _ {p} (t)}} \\ {{- \gamma r (t)}} & {{0}} & {{0}} \\ {{- \gamma y _ {p} (t)}} & {{0}} & {{0}} \end{array} \right] x, \qquad \text {其中} x = \left[ \begin{array}{c} {{e _ {o}}} \\ {{\phi_ {1}}} \\ {{\phi_ {2}}} \end{array} \right]
$$

假设参考信号 $r(t)$ 有一个稳态值 $r_{ss}(t)$ ，即 $\lim_{t\to \infty}[r(t) - r_{ss}(t)] = 0$ ，则有 $\lim_{t\to \infty}[y_m(t) - y_{ss}(t)] = 0$ ，其中 $y_{ss}(t)$ 是参考模型的稳态响应。以上极限及 $\lim_{t\to \infty}e_0(t) = 0$ 表明线性系统可表示为 $\dot{x} = [A(t) + B(t)]x$

其中

$$
A (t) = \left[ \begin{array}{c c c} {a _ {m}} & {k _ {p} r _ {\mathrm{ss}} (t)} & {k _ {p} y _ {\mathrm{ss}} (t)} \\ {- \gamma r _ {\mathrm{ss}} (t)} & 0 & 0 \\ {- \gamma y _ {\mathrm{ss}} (t)} & 0 & 0 \end{array} \right], \quad \lim _ {t \to \infty} B (t) = 0
$$
