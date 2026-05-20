$$
\begin{array}{l} B _ {1} (t) e _ {j} = B (t) = \left[ b _ {1} (t), b _ {2} (t), \dots , b _ {r} (t) \right], \\ B _ {2} (t) e _ {j} = - A (t) B _ {1} (t) e _ {j} + \dot {B} _ {1} (t) e _ {j} = - A (t) b _ {j} (t) + \dot {b} _ {j} (t), \\ \end{array}
$$

:

$$B _ {n} (t) e _ {j} = - A (t) B _ {n - 1} (t) e _ {j} + \dot {B} _ {n - 1} (t) e _ {j}, \quad j = 1, 2, \dots , r.$$

证明 假定存在某个 $j_0, \psi^{\mathrm{T}}(t)b_{j_0}(t)$ 在 $[t_1, t_2]$ 上有无穷多个零点。于是存在序列 $\{t_m^0\} \subset [t_1, t_2]$ ，使 $\lim_{m \to \infty} t_m^0 = \bar{t} \in [t_1, t_2]$ ，且 $\psi^{\mathrm{T}}(t_m^0)b_{j_0}(t_m^0) = 0, \forall m \geqslant 1$ 。利用 Rolle 定理和函数连续性不难得到

$$
\begin{array}{l} \psi^ {\mathrm{T}} (\bar {t}) B _ {1} (\bar {t}) e _ {j _ {0}} = \psi^ {\mathrm{T}} (\bar {t}) b _ {j _ {0}} (\bar {t}) = 0, \\ \psi^ {\mathrm{T}} (\bar {t}) B _ {2} (\bar {t}) e _ {j _ {0}} = \psi^ {\mathrm{T}} (\bar {t}) \left[ - A (\bar {t}) b _ {j _ {0}} (\bar {t}) + \dot {b} _ {j _ {0}} (\bar {t}) \right] = 0, \\ \psi^ {T} (\bar {t}) B _ {n} (\bar {t}) e _ {j _ {0}} = \psi^ {T} (\bar {t}) \left[ - A (\bar {t}) B _ {n - 1} (\bar {t}) e _ {j _ {0}} + \dot {B} _ {n - 1} (\bar {t}) e _ {j _ {0}} \right] = 0, \\ \end{array}
$$

:

即

$$\psi^ {\mathrm{T}} (\bar {t}) \left[ B _ {1} (\bar {t}) e _ {j _ {0}}, B _ {2} (\bar {t}) e _ {j _ {0}}, \dots , B _ {n} (\bar {t}) e _ {j _ {0}} \right] = 0.$$

由于 $\psi^{\mathrm{T}}(t) \neq 0$ ，故

$$\operatorname{rank} \left[ B _ {1} (\bar {t}) e _ {j _ {0}}, B _ {2} (\bar {t}) e _ {j _ {0}}, \dots , B _ {n} (\bar {t}) e _ {j _ {0}} \right] < n,$$

与式 (7.2.17) 矛盾，从而定理 7.2.2 结论正确.

现在考察定常情形，即 $A(t), B(t)$ 为常矩阵。这时状态方程为

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u, \\ x (t _ {0}) = x _ {0}. \end{array} \right. \tag {7.2.18}
$$

式 (7.2.18) 和式 (7.2.12), (7.2.13), (7.2.14) 一起就是线性定常快速控制问题。对于线性定常快速控制问题，相应的共轭向量值函数 $\psi(t)$ 和快速控制函数 $u^{*}(t)$ 分别为

$$\psi^ {\mathrm{T}} (t) = \mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {j} ^ {*} - t)}, \tag {7.2.19}u ^ {*} (t) = \operatorname{sign} \left[ B ^ {\mathrm{T}} \mathrm{e} ^ {A ^ {\mathrm{T}} \left(t _ {f} ^ {*} - t\right)} \mu \right], \tag {7.2.20}$$

其中 $\mu, t_f^*$ 待求.

定理 7.2.3 线性定常控制系统 (7.2.18) 为正则快速系统的充分必要条件是

$$\operatorname{rank} G _ {j} = \operatorname{rank} \left[ b _ {j} A b _ {j} \dots A ^ {(n - 1)} b _ {j} \right] = n, \quad \forall j = 1, \dots , r. \tag {7.2.21}$$

证明 充分性就是定理 (7.2.3) 的结论. 下证必要性. 事实上, 设方程 (7.2.18) 是正则快速系统. 如果存在某个 $j_0$ 满足

$$\operatorname{rank} \left[ b _ {j _ {0}}, A b _ {j _ {0}}, \dots , A ^ {(n - 1)} b _ {j _ {0}} \right] < n,$$

则存在某个常向量 $\alpha \neq 0$ ，使得
