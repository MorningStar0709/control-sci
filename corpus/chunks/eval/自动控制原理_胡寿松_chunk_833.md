$$\boldsymbol {x} (t) = \mathrm{e} ^ {\boldsymbol {A t}} \boldsymbol {x} _ {0}, \quad \forall \boldsymbol {x} _ {0} \neq \boldsymbol {0} \tag {10-129}$$

将式(10-129)代入式(10-127)，可得

$$\boldsymbol {x} _ {0} ^ {\mathrm{T}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}}} \boldsymbol {D} \boldsymbol {D} ^ {\mathrm{T}} \mathrm{e} ^ {\boldsymbol {A} t} \boldsymbol {x} _ {0} = 0$$

式中 $DD^{T}=Q$ 。上式表明

$$\boldsymbol {D} ^ {\mathrm{T}} \mathrm{e} ^ {\boldsymbol {A t}} \boldsymbol {x} _ {0} = \boldsymbol {0}, \quad \forall \boldsymbol {x} _ {0} \neq \boldsymbol {0}$$

故 $D^{T}e^{A}$ 列相关，这与 $\{A,D\}$ 完全可观矛盾，反设不成立。

根据李雅普诺夫稳定性定理，系统(10-124)大范围渐近稳定。

对于以上主要结论,需作如下几点说明:

1) 在定理 10-21 中, 对系统(10-119)提出的可控性要求, 是为了保证最优解的存在。在有限时间调节器问题中, 对系统并无可控性要求, 因为式(10-120)的积分上限 $t_f$ 有限, 无论系统可控与否, 性能指标 $J$ 不会趋于无穷。但在 $t_f \to \infty$ 时, 当不可控状态不稳定, 且又包含于性能指标 $J$ 之中时, 便会使 $J \to \infty$ , 从而使最优解不存在。

例 10-13 设系统状态方程及初始条件为

$$\dot {x} _ {1} (t) = x _ {1} (t), \quad x _ {1} (0) = 1\dot {x} _ {2} (t) = x _ {2} (t) + u (t), \quad x _ {2} (0) = 0$$

性能指标

$$J = \frac {1}{2} \int_ {0} ^ {\infty} [ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) + u ^ {2} (t) ] \mathrm{d} t$$

试求最优控制 $u^{*}(t)$ 及最优性能指标 $J^{*}$ 。

解 本例为无限时间定常状态调节器问题。由题意，状态 $x_{1}(t)$ 显然不可控。因为系统矩阵及状态转移矩阵为

$$
\mathbf {A} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right], \quad \mathrm{e} ^ {\mathbf {A} t} = \mathcal {L} ^ {- 1} [ (\mathbf {s I} - \mathbf {A}) ^ {- 1} ] = \left[ \begin{array}{l l} \mathrm{e} ^ {t} & 0 \\ 0 & \mathrm{e} ^ {t} \end{array} \right]
$$

故系统的零输入响应

$$
\left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] = \mathrm{e} ^ {\boldsymbol {A} t} \boldsymbol {x} (0) = \left[ \begin{array}{l} \mathrm{e} ^ {t} \\ 0 \end{array} \right]
$$

显然

$$\lim _ {t \rightarrow \infty} x _ {1} (t) = \lim _ {t \rightarrow \infty} e ^ {t} \rightarrow \infty$$

性能指标

$$J = \frac {1}{2} \int_ {0} ^ {\infty} [ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) + u ^ {2} (t) ] \mathrm{d} t= \frac {1}{2} \int_ {0} ^ {\infty} \left[ x _ {1} ^ {2} (t) + x _ {2} ^ {2} (t) + u ^ {2} (t) \right] d t \rightarrow \infty$$

因而本例不存在最优解。
