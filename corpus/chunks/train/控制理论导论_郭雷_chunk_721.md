$$L _ {t} (z) u _ {t} = R _ {t} (z) \left\{y _ {t} ^ {*} - y _ {t} \right\}. \tag {9.6.28}$$

定理9.6.2 对系统(9.6.1)，上述定义的自适应极点配置控制律(9.6.28)是稳定的，即

$$\lim _ {T \rightarrow \infty} \frac {1}{T} \sum_ {t = 1} ^ {T} (y _ {t} ^ {2} + u _ {t} ^ {2}) < \infty , \quad \text { a.s. }$$

证明 定义

$$v _ {t} = A _ {t} (z) y _ {t} - B _ {t} (z) u _ {t},$$

易见

$$v _ {t} = w _ {t} + \tilde {\theta} _ {t} ^ {T} \phi_ {t}, \quad (\tilde {\theta} _ {t} \stackrel {{\text { def }}} {{=}} \theta - \hat {\theta} _ {t}).$$

由于多项式 $A_{t}(z), B_{t}(z), L_{t}(z)$ 及 $R_{t}(z)$ 的系数是收敛的，利用上式及式 (9.6.27)\~式 (9.6.28)，经简单运算可得

$$
\begin{array}{l} A ^ {*} (z) y _ {t} = \left[ A _ {t} (z) L _ {t} (z) + B _ {t} (z) R _ {t} (z) \right] y _ {t} \\ = L _ {t} (z) \left[ A _ {t} (z) y _ {t} \right] + B _ {t} (z) \left[ R _ {t} (z) y _ {t} \right] + o \left(\max _ {0 \leqslant i \leqslant 2 n} \{| y _ {t - i} | \}\right) \\ = L _ {t} (z) \left[ B _ {t} (z) u _ {t} + v _ {t} \right] + B _ {t} (z) \left[ R _ {t} (z) y _ {t} ^ {*} - L _ {t} (z) u _ {t} \right] + o \left(\max _ {0 \leqslant i \leqslant 2 n} \{| y _ {t - i} | \}\right) \\ = L _ {t} (z) v _ {t} + \left[ B _ {t} (z) R _ {t} (z) \right] y _ {t} ^ {*} + o \left(\max _ {0 \leqslant i \leqslant 2 n} \left\{\left| y _ {t - i} \right| + \left| u _ {t - i} \right| \right\}\right). \\ \end{array}
$$

类似地，有

$$A ^ {*} (z) u _ {t} = - R _ {t} (z) v _ {t} + [ A _ {t} (z) R _ {t} (z) ] y _ {t} ^ {*} + o \left(\max _ {0 \leqslant i \leqslant 2 n} \{| y _ {t - i} | + | u _ {t - i} | \}\right).$$

于是利用引理9.6.1及 $A^{*}(z)$ 的稳定性易见

$$\sum_ {i = 1} ^ {t} (y _ {i} ^ {2} + u _ {i} ^ {2}) = O (t) + o (r _ {t}).$$

此式意味着 $r_t = O(t)$ ，故稳定性成立。证毕。

由于 $\{\hat{\theta}_t\}$ 不一定收敛到真实的 $\theta$ ，系统的闭环方程不一定渐近与理想的方程(9.6.7)相等，因此我们用“衰减激励”方法设计“最优”的控制器。

设 $\{\epsilon_i\}$ 是有界的 i.i.d. 序列，它与 $\{w_i, \eta_i\}$ 独立，且具有零均值及单位方差。设 $u_t^0$ 定义为

$$L _ {t} (z) u _ {t} ^ {0} = R _ {t} (z) \{y _ {t} ^ {*} - y _ {t} \}, \tag {9.6.29}$$

其中 $L_{t}(z)$ 与 $R_{t}(z)$ 及由式(9.6.27)所定义．于是可定义系统的实际输入为

$$u _ {t} = u _ {t} ^ {0} + \frac {\epsilon_ {t}}{t ^ {\frac {\epsilon}{2}}}, \quad \epsilon \in \left(0, \frac {1}{2 n}\right). \tag {9.6.30}$$

定理 9.6.3 对系统 (9.6.1), 若适应控制由式 (9.6.30) 所定义, 则闭环系统在下列意义下是最优的:

$$\frac {1}{T} \sum_ {t = 1} ^ {T} [ A ^ {*} (z) y _ {t} - L (z) w _ {t} - B (z) R (z) y _ {t} ^ {*} ] ^ {2} \longrightarrow 0, \quad \text { a.s. } \quad T \to \infty .$$
