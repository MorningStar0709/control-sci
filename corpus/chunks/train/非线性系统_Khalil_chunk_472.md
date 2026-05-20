(e) 对速度控制, 假设 $\omega_{r}(t)$ , $\dot{\omega}_{r}(t)$ 和 $T_{o}(t)$ 是有界的, 适当选择 s 和 $\varepsilon$ , 设计一个形如 $i_{q} = -I_{q} \operatorname{sat}(s/\varepsilon)$ 的滑模控制器。给出控制器正常工作的条件, 并估计跟踪误差的最终边界。

(f) 除前述假设外, 另设 $\omega_r(t)$ 满足 $\lim_{t \to \infty} \omega_r(t) = \overline{\omega}_r$ 和 $\lim_{t \to \infty} \dot{\omega}_r(t) = 0$ , 而且希望在 $T_o$ 是常数时, 实现零稳态误差。利用积分控制, 适当选择 $s$ 和 $\varepsilon$ , 设计一个形如$i_{q} = -I_{q} \text{ sat}(s/\varepsilon)$ 的滑模控制器。给出控制器正常工作的条件，并验证其实现零稳态误差。

(g) 转子磁通可测的假设实际上不成立,应用中一般用观测器

$$\dot {\hat {\lambda}} _ {a} = - \frac {\hat {R} _ {r}}{L _ {r}} \hat {\lambda} _ {a} - p \omega \hat {\lambda} _ {b} + \frac {\hat {R} _ {r} M}{L _ {r}} i _ {a}, \quad \dot {\hat {\lambda}} _ {b} = - \frac {\hat {R} _ {r}}{L _ {r}} \hat {\lambda} _ {b} + p \omega \hat {\lambda} _ {a} + \frac {\hat {R} _ {r} M}{L _ {r}} i _ {b}$$

估计磁通,其中 $\hat{R}_{r}$ 是 $R_{r}$ 的标称值(或估计值)。场方向角 $\rho$ 和磁通幅值 $\lambda_{d}$ 可由 $\rho=\arctan(\hat{\lambda}_{b}/\hat{\lambda}_{a})$ 和 $\lambda_{d}=\sqrt{\hat{\lambda}_{a}^{2}+\hat{\lambda}_{b}^{2}}$ 计算, $i_{d}$ 和 $i_{q}$ 由式(14.117)定义,其中 $\rho$ 采用新的定义。为写出整个系统的状态模型,把磁通估计误差 $e_{d}$ 和 $e_{q}$ 定义为

$$
\left[ \begin{array}{l} e _ {d} \\ e _ {q} \end{array} \right] = \left[ \begin{array}{c c} \cos \rho & \sin \rho \\ - \sin \rho & \cos \rho \end{array} \right] \left[ \begin{array}{l} \hat {\lambda} _ {a} - \lambda_ {a} \\ \hat {\lambda} _ {b} - \lambda_ {b} \end{array} \right] \tag {14.119}
$$

以 $\omega, \lambda_d, \rho, e_d$ 和 $e_q$ 作为状态变量，证明整个系统的状态模型可表示为

$$J \dot {\omega} = k _ {t} \left(\lambda_ {d} i _ {q} + e _ {q} i _ {d} - e _ {d} i _ {q}\right) - T _ {L}\dot {\lambda} _ {d} = - \frac {\hat {R} _ {r}}{L _ {r}} \lambda_ {d} + \frac {\hat {R} _ {r} M}{L _ {r}} i _ {d}\dot {\rho} = p \omega + \frac {\hat {R} _ {r} M i _ {q}}{L _ {r} \lambda_ {d}}\dot {e} _ {d} = - \frac {R _ {r}}{L _ {r}} e _ {d} + \frac {\hat {R} _ {r} M i _ {q}}{L _ {r} \lambda_ {d}} e _ {q} + \left(\frac {\hat {R} _ {r} - R _ {r}}{L _ {r}}\right) (M i _ {d} - \lambda_ {d})\dot {e} _ {q} = - \frac {\hat {R} _ {r} M i _ {q}}{L _ {r} \lambda_ {d}} e _ {d} - \frac {R _ {r}}{L _ {r}} e _ {q} + \left(\frac {\hat {R} _ {r} - R _ {r}}{L _ {r}}\right) M i _ {q}$$

(h) 验证如果 $I_{d} > \lambda_{r} / M$ 和 $0 < \lambda_{d}(0) < \lambda_{r}$ , 磁通控制 (14.118) 仍把 $\lambda_{d}$ 调节到 $\lambda_{r}$ 。进一步证明 $|M i_{d}(t) - \lambda_{d}(t)| \leqslant (1 + k M)[M I_{d} - \lambda_{d}(0)] \exp[-(\hat{R}_{r} / \hat{L}_{r}) t]$
