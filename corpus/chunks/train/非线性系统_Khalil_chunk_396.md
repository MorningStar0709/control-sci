误差项 $\delta (x)$ 全局满足边界条件 $|\delta (x)|\leqslant k\| x\| _2 + \varepsilon$ ，其中

$$k = \left| \frac {\hat {a} c - a \hat {c}}{\hat {c}} \right| + \left| \frac {c - \hat {c}}{\hat {c}} \right| \sqrt {k _ {1} ^ {2} + k _ {2} ^ {2}}, \quad \varepsilon = \left| \frac {\hat {a} c - a \hat {c}}{\hat {c}} \right| | \sin \delta_ {1} |$$

常数 $k$ 和 $\varepsilon$ 是估计参数 $a$ 和 $c$ 时误差大小的测度。设

$$
P = \left[ \begin{array}{l l} p _ {1 1} & p _ {1 2} \\ p _ {1 2} & p _ {2 2} \end{array} \right]
$$

是李雅普诺夫方程 $P(A - BK) + (A - BK)^{\mathrm{T}}P = -I$ 的解。如果

$$k < \frac {1}{2 \sqrt {p _ {1 2} ^ {2} + p _ {2 2} ^ {2}}}$$

则系统的解全局毕竟有界,其界与 $\varepsilon$ 成比例。如果 $\sin\delta_{1}=0$ , 则上面 k 的边界能够保证原点的全局指数稳定性。

下面讨论一般的闭环系统(13.44)\~(13.45)。

引理 13.4 考虑闭环系统(13.44)\~(13.45)，其中 A-BK 是赫尔维茨矩阵

\- 如果对于所有 $z$ ，有 $\| \delta(z) \| \leqslant \varepsilon$ ，且 $\dot{\eta} = f_0(\eta, \xi)$ 是输入-状态稳定的，则状态 $z$ 全局最终有界，其界为 $\varepsilon$ 的 $\kappa$ 类函数。

\- 如果在 $z = 0$ 的某邻域内，对于足够小的 $k$ ，有 $\| \delta (z)\| \leqslant k\| z\|$ ，且 $\dot{\eta} = f_0(\eta ,0)$ 的原点是指数稳定的，则 $z = 0$ 是系统(13.44）\~（13.45）的指数稳定平衡点。

证明: 设 $V(\xi)=\xi^{\mathrm{T}}P\xi$ ，其中 $P=P^{T}>0$ 是李雅普诺夫方程 $P(A-BK)+(A-BK)^{\mathrm{T}}P=-I$ 的解，则

$$
\begin{array}{l} \dot {V} = \xi^ {\mathrm{T}} [ P (A - B K) + (A - B K) ^ {\mathrm{T}} P ] \xi + 2 \xi^ {\mathrm{T}} P B \delta (z) \\ \leqslant - \| \xi \| _ {2} ^ {2} + 2 \| P B \| _ {2} \| \xi \| _ {2} \| \delta (z) \| _ {2} \\ \end{array}
$$

如果 $\| \delta (z)\| _2\leqslant \varepsilon$ ，有

$$\dot {V} \leqslant - \| \xi \| _ {2} ^ {2} + 2 \varepsilon \| P B \| _ {2} \| \xi \| _ {2} \leqslant - \frac {1}{2} \| \xi \| _ {2} ^ {2}, \forall \| \xi \| _ {2} \geqslant 4 \varepsilon \| P B \| _ {2}$$

因此运用定理4.18可证明存在有限时间 $t_0$ 和一个正常数 $c$ ，使得

$$\| \xi (t) \| _ {2} \leqslant c \varepsilon , \quad \forall t \geqslant t _ {0}$$

由 $\dot{\eta} = f_0(\eta, \xi)$ 的输入-状态稳定性，有

$$\| \eta (t) \| _ {2} \leqslant \beta_ {0} (\| \eta (t _ {0}) \| _ {2}, t - t _ {0}) + \gamma_ {0} (\sup _ {t \geqslant t _ {0}} \| \xi (t) \| _ {2}) \leqslant \beta_ {0} (\| \eta (t _ {0}) \| _ {2}, t - t _ {0}) + \gamma_ {0} (c \varepsilon)$$

其中 $\beta_0$ 和 $\gamma_0$ 分别是 $\mathcal{KL}$ 类函数和 $\mathcal{K}$ 类函数。经过一段有限时间后， $\beta_0(\| \eta(t_0)\|_2, t - t_0)$ 满足 $\beta_0 \leqslant \varepsilon$ 。因此 $\| z(t)\|_2$ 是毕竟有界的，其界为 $c\varepsilon + \varepsilon + \gamma_0(c\varepsilon)$ ，为 $\varepsilon$ 的 $\mathcal{K}$ 类函数。为了证明引理的第二种情况，回顾定理4.14，在 $\eta = 0$ 的某个邻域内，存在李雅普诺夫函数 $V_1(\eta)$ ，使得
