$$
\begin{array}{l} \Delta (t, x, v) = \delta (t, x, - E ^ {- 1} (x) L (x) \left(f _ {b} (\eta , \xi) - (\partial \phi / \partial \eta) f _ {a} (\eta , \xi)\right) + E ^ {- 1} (x) v) \\ + [ I - G (x) L (x) ] \left[ f _ {b} (\eta , \xi) - (\partial \phi / \partial \eta) f _ {a} (\eta , \xi) \right] \\ \end{array}
$$

的第 $i$ 个分量， $g_{i}$ 为 $G$ 的第 $i$ 个对角元素。假设 $\Delta_i / g_i$ 满足不等式

$$\left| \frac {\Delta_ {i} (t , x , v)}{g _ {i} (x)} \right| \leqslant \varrho (x) + \kappa_ {0} \| v \| _ {\infty}, \quad \forall (t, x, v) \in [ 0, \infty) \times D \times R ^ {p}, \forall 1 \leqslant i \leqslant p \tag {14.10}$$

其中 $\varrho(x) \geqslant 0$ （一个连续函数）和 $\kappa_0 \in [0,1)$ 已知。接下来利用式(14.10)的估计，设计 $v$ ，迫使 $s$ 指向流形 $s = 0$ 。以 $V_i = (1/2)s_i^2$ 作为方程(14.9)的备选李雅普诺夫函数，可得

$$\dot {V} _ {i} = s _ {i} \dot {s} _ {i} = s _ {i} g _ {i} (x) v _ {i} + s _ {i} \Delta_ {i} (t, x, v) \leqslant g _ {i} (x) \left\{s _ {i} v _ {i} + | s _ {i} | [ \varrho (x) + \kappa_ {0} \| v \| _ {\infty} ] \right\}$$

取 $^{②}$

$$v _ {i} = - \beta (x) \operatorname{sgn} \left(s _ {i}\right), \quad 1 \leqslant i \leqslant p \tag {14.11}$$

其中

$$\beta (x) \geqslant \frac {\varrho (x)}{1 - \kappa_ {0}} + \beta_ {0}, \quad \forall x \in D \tag {14.12}$$

且 $\beta_0 > 0$ ，则

$$
\begin{array}{l} \dot {V} _ {i} \leqslant g _ {i} (x) [ - \beta (x) + \varrho (x) + \kappa_ {0} \beta (x) ] | s _ {i} | = g _ {i} (x) [ - (1 - \kappa_ {0}) \beta (x) + \varrho (x) ] | s _ {i} | \\ \leqslant g _ {i} (x) \left[ - \varrho (x) - \left(1 - \kappa_ {0}\right) \beta_ {0} + \varrho (x) \right] \left| s _ {i} \right| \leqslant - g _ {0} \beta_ {0} \left(1 - \kappa_ {0}\right) \left| s _ {i} \right| \\ \end{array}
$$

不等式 $\dot{V}_{i}\leqslant-g_{0}\beta_{0}(1-\kappa_{0})|s_{i}|$ 保证了所有始于流形 s=0 之外的轨线都能在有限时间内到达流形，而已在流形上的轨线不会离开它。

滑模稳定控制器的设计步骤可归纳为以下几步：

\- 设计滑动流形 $\xi = \phi (\eta)$ ，以稳定降阶系统(14.6)。

- 把控制 $u$ 取为 $u = E^{-1}\{-\hat{G}^{-1}[f_b - (\partial \phi / \partial \eta)f_a] + v\}$ 或 $u = E^{-1}v$ 。  
- 估计式(14.10)中的 $\varrho(x)$ 和 $\kappa_0$ ，其中 $\Delta$ 的计算取决于上一步的选择。  
- 选取 $\beta(x)$ 满足式(14.12)，并按式(14.11)选取切换(不连续)控制 $v$ 。

上述步骤显示模型阶数降低了,因为主要设计任务是对降阶系统(14.6)进行的。滑模控制的主要特征在于其对匹配的不确定性的鲁棒性。在到达阶段,只要 $\beta(x)$ 满足不等式(14.12),迫使轨线向滑动流形运动并保持在流形上的任务,就由切换控制(14.11)实现。从式(14.10)可以看出, $\varrho(x)$ 是不确定性大小的度量,由于不需要 $\varrho(x)$ 取得很小,因此切换控制器可以处理相当大的不确定项,实际中只受到控制信号幅度的限制。在滑动阶段,系统的运动由方程(14.6)决定,与不确定项 G 和 $\delta$ 无关。
