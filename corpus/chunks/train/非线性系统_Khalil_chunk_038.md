# 1.2.6 自适应控制

考虑由模型

$$\dot {y} _ {p} = a _ {p} y _ {p} + k _ {p} u$$

描述的一阶线性系统, u 是输入控制, $y_{p}$ 是测得的输出, 我们把这一系统看成设备。假设希望

得到一个闭环系统,其输入-输出特性由参考模型

$$\dot {y} _ {m} = a _ {m} y _ {m} + k _ {m} r$$

描述, r 是参考输入, 且选择的模型用 $y_{m}(t)$ 表示闭环系统希望得到的输出, 这一目的可由反馈控制 $u(t)=\theta_{1}^{*}r(t)+\theta_{2}^{*}y_{p}(t)$

达到。假设设备参数 $a_{p}$ 和 $k_{p}$ 已知， $k_{p} \neq 0$ ，且选择控制器参数 $\theta_{1}^{*}$ 和 $\theta_{2}^{*}$ 为

$$\theta_ {1} ^ {*} = \frac {k _ {m}}{k _ {p}} \quad \text {且} \quad \theta_ {2} ^ {*} = \frac {a _ {m} - a _ {p}}{k _ {p}}$$

当 $a_{p}$ 和 $k_{p}$ 已知时，可以考虑输入控制器

$$u (t) = \theta_ {1} (t) r (t) + \theta_ {2} (t) y _ {p} (t)$$

时变增益 $\theta_{1}(t)$ 和 $\theta_{2}(t)$ 运用已有数据，即 $r(\tau), y_{m}(\tau), y_{p}(\tau)$ 和 $u(\tau)$ 进行在线调节， $\tau < t$ 。自适应就是使 $\theta_{1}(t)$ 和 $\theta_{2}(t)$ 的值逐渐逼近标称值 $\theta_{1}^{*}$ 和 $\theta_{2}^{*}$ ，选择自适应准则应基于稳定性考虑，一个称为梯度算法①的准则是运用

$$
\begin{array}{l} \dot {\theta} _ {1} = - \gamma (y _ {p} - y _ {m}) r \\ \dot {\theta} _ {2} = - \gamma (y _ {p} - y _ {m}) y _ {p} \\ \end{array}
$$

其中， $\gamma$ 是正常数，决定自适应的速度。这一自适应控制定律假设 $k_{p}$ 的符号是已知的，而且不失一般性地取为正值。为写出描述满足自适应控制定律的闭环系统的状态模型，把输出误差 $e_{o}$ 和参数误差 $\phi_{1}$ 和 $\phi_{2}$ 定义为

$$e _ {o} = y _ {p} - y _ {m}, \quad \phi_ {1} = \theta_ {1} - \theta_ {1} ^ {*}, \quad \phi_ {2} = \theta_ {2} - \theta_ {2} ^ {*}$$

更为方便。利用 $\theta_{1}^{*}$ 和 $\theta_{2}^{*}$ 的定义，参考模型可写为

$$\dot {y} _ {m} = a _ {p} y _ {m} + k _ {p} (\theta_ {1} ^ {*} r + \theta_ {2} ^ {*} y _ {m})$$

另一方面,设备输出 $y_{p}$ 满足方程

$$\dot {y} _ {p} = a _ {p} y _ {p} + k _ {p} (\theta_ {1} r + \theta_ {2} y _ {p})$$

上面两式相减,可得到误差方程

$$
\begin{array}{l} \dot {e} _ {o} = a _ {p} e _ {o} + k _ {p} \left(\theta_ {1} - \theta_ {1} ^ {*}\right) r + k _ {p} \left(\theta_ {2} y _ {p} - \theta_ {2} ^ {*} y _ {m}\right) \\ = a _ {p} e _ {o} + k _ {p} \left(\theta_ {1} - \theta_ {1} ^ {*}\right) r + k _ {p} \left(\theta_ {2} y _ {p} - \theta_ {2} ^ {*} y _ {m} + \theta_ {2} ^ {*} y _ {p} - \theta_ {2} ^ {*} y _ {p}\right) \\ = (a _ {p} + k _ {p} \theta_ {2} ^ {*}) e _ {o} + k _ {p} (\theta_ {1} - \theta_ {1} ^ {*}) r + k _ {p} (\theta_ {2} - \theta_ {2} ^ {*}) y _ {p} \\ \end{array}
$$

这样,闭环系统就可由下面的非线性非自治三阶状态模型描述:

$$\dot {e} _ {o} = a _ {m} e _ {o} + k _ {p} \phi_ {1} r (t) + k _ {p} \phi_ {2} [ e _ {o} + y _ {m} (t) ] \tag {1.23}\dot {\phi} _ {1} = - \gamma e _ {o} r (t) \tag {1.24}\dot {\phi} _ {2} = - \gamma e _ {o} [ e _ {o} + y _ {m} (t) ] \tag {1.25}$$

这里用到方程 $\dot{\phi}_{i}(t)=\dot{\theta}_{i}(t)$ ，且把 $r(t)$ 和 $y_{m}(t)$ 写为时间的显函数，以强调系统的非自治特点，信号 $r(t)$ 和 $y_{m}(t)$ 是闭环系统的外部驱动输入。
