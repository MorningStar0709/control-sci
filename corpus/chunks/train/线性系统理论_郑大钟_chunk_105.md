这表明 $\operatorname{rank} \bar{Q}_{\mu} = \operatorname{rank} Q_{\mu} = n$ ，而

$$\overline {{{b}}} _ {1}, \overline {{{A}}} \overline {{{b}}} _ {1}, \dots , \overline {{{A}}} ^ {\mu_ {1} - 1} \overline {{{b}}} _ {1}; \dots ; \overline {{{b}}} _ {r}, \overline {{{A}}} \overline {{{b}}} _ {r}, \dots , \overline {{{A}}} ^ {\mu_ {r} - 1} \overline {{{b}}} _ {r}$$

为 $\bar{Q}_{n}$ 中按上述方式搜索得到 $n$ 个线性无关列。从而，证得能控性指数和能控性指数集在线性非奇异变换下保持不变。

能控性指数 $\mu$ 在线性定常系统的综合中具有重要的用处。详细的阐述可参见第 5 章和第 11 章的有关内容。

线性时变系统的能控性判据 现推广讨论线性时变系统,其状态方程为

$$\dot {x} = A (t) x + B (t) u, x \left(t _ {0}\right) = x _ {0}, t, t _ {0} \in J \tag {3.63}$$

其中，x 为 n 维状态向量，u 为 p 维输入向量，J 为时间定义区间， $A(t)$ 和 $B(t)$ 为 $n \times n$ 和 $n \times p$ 的时变矩阵且满足解的存在唯一性条件。

结论1[格拉姆矩阵判据] 线性时变系统(3.63)在时刻 $t_0$ 为完全能控的充分必要条件是，存在一个有限时刻 $t_1 \in J, t_2 > t_0$ ，使如下定义的格拉姆矩阵

$$W _ {c} \left[ t _ {0}, t _ {1} \right] \triangleq \int_ {t _ {0}} ^ {t _ {1}} \Phi \left(t _ {0}, t\right) B (t) B ^ {T} (t) \Phi^ {T} \left(t _ {0}, t\right) d t \tag {3.64}$$

为非奇异,其中 $\Phi(\cdot,\cdot)$ 为系统(3.63)的状态转移矩阵。

证 充分性可采用构造性方法来证明,其中取控制 $u(t)$ 为:

$$\boldsymbol {u} (t) = - B ^ {T} (t) \Phi^ {T} \left(t _ {0}, t\right) W _ {c} ^ {- 1} \left[ t _ {0}, t _ {1} \right] x _ {0} \tag {3.65}$$

则利用状态运动的表达式和能控性定义即可证得在(3.64)条件下系统在时刻 $t_{0}$ 能控，具体推证过程同于定常系统的格拉姆矩阵判据。必要性可采用反证法来证明，具体推证过程也和定常情况时相类同，此略。证明完成。

应当指出，尽管格拉姆矩阵判据有着简单的形式，但因求解时变系统的状态转移矩阵十分困难，所以它在实际中是很难应用的，而只具有理论上的意义。为了使能直接根据 $A(t)$ 和 $B(t)$ 来判断系统的能控性，下面给出一个充分条件。

结论2[秩判据] 设 $A(t)$ 和 $B(t)$ 是 $(n - 1)$ 阶连续可微的，则线性时变系统(3.63)在时刻 $t_0$ 为完全能控的一个充分条件是，存在一个有限时刻 $t_1 \in J, t_1 > t_0$ ，使成立

$$\operatorname{rank} \left[ M _ {0} (t _ {1}) \mid M _ {1} (t _ {1}) \mid \dots \mid M _ {n - 1} (t _ {1}) \right] = n \tag {3.66}$$

其中

$$M _ {0} (t) = B (t)M _ {1} (t) = - A (t) M _ {0} (t) + \frac {d}{d t} M _ {0} (t)M _ {2} (t) = - A (t) M _ {1} (t) + \frac {d}{d t} M _ {1} (t) \tag {3.67}\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet \quad \bulletM _ {n - 1} (t) = - A (t) M _ {n - 2} (t) + \frac {d}{d t} M _ {n - 2} (t)$$

证 分成四点来证明：

(1) 考虑到 $\Phi(t_{0}, t_{1})B(t_{1}) = \Phi(t_{0}, t_{1})M_{0}(t_{1})$ ，且定义

$$\frac {\partial}{\partial t _ {1}} \left[ \Phi (t _ {0}, t _ {1}) B (t _ {1}) \right] = \left[ \frac {\partial}{\partial t} \Phi (t _ {0}, t) B (t) \right] _ {t = t _ {1}}$$

则有
