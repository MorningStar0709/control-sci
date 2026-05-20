# 12.6 习题

12.1 考虑例 12.2 中的闭环系统, 假设 a = c = 0, $\delta = \pi/4$ , b = 0, $k_{1} = 2.5$ , $k_{2} = 1$ 。求系统的李雅普诺夫函数并用它估计吸引区。

12.2 对下列系统,利用线性化

(a) 设计一个状态反馈控制器实现在原点的稳定。  
(b) 设计一个输出反馈控制器实现在原点的稳定。

(1) $\left\{ \begin{array}{l} \dot{x}_1 = x_1 + x_2 \\ \dot{x}_2 = 3x_1^2 x_2 + x_1 + u \\ y = -x_1^3 + x_2 \end{array} \right.$   
(2) $\left\{ \begin{array}{l} \dot{x}_1 = x_1 + x_2 \\ \dot{x}_2 = x_1x_2^2 - x_1 + x_3 \\ \dot{x}_3 = u \\ y = -x_1^3 + x_2 \end{array} \right.$   
(3) $\left\{ \begin{array}{l} \dot{x}_1 = -x_1 + x_2 \\ \dot{x}_2 = x_1 - x_2 - x_1x_3 + u \\ \dot{x}_3 = x_1 + x_1x_2 - 2x_3 \\ y = x_1 \end{array} \right.$

12.3 设 $\mathcal{A} = \left[ \begin{array}{ll} A & 0 \\ C & 0 \end{array} \right], \quad \mathcal{B} = \left[ \begin{array}{l} B \\ 0 \end{array} \right]$

其中 A, B 和 C 满足秩条件(12.23)。证明(A, B)是可控的(或可稳定的)，当且仅当(A, B)是可控的(或可稳定的)。

12.4 利用数值数据: a = 10, b = 0.1 和 c = 10, 考虑例 12.2 中的单摆

(a) 假设 $\theta$ 是可测的, 而 $\dot{\theta}$ 是不可测的, 利用线性化, 设计一个输出反馈积分控制器, 使单摆在角度 $\theta = \delta$ 处稳定。  
(b) 假设 $\theta$ 和 $\dot{\theta}$ 都是可测的, 设计一个增益分配状态反馈积分控制器, 使角度 $\theta$ 跟踪参考角度 $\theta_{r}$ , 并通过计算机仿真讨论增益分配控制器的性能。  
(c) 假设 $\theta$ 是可测的, 而 $\dot{\theta}$ 是不可测的, 设计一个基于观测器的增益分配积分控制器, 使角度 $\theta$ 跟踪参考角度 $\theta_{r}$ , 并通过计算机仿真讨论增益分配控制器的性能。

12.5 考虑线性系统

$$\dot {x} = A (\alpha) x + B (\alpha) u$$

其中 $A(\alpha)$ 和 $B(\alpha)$ 为常向量 $\alpha$ 的连续可微函数， $\alpha \in \Gamma$ 为 $R^m$ 的紧子集，设 $W(\alpha)$ 是可控制性 Gram 矩阵，定义为

$$W (\alpha) = \int_ {0} ^ {\tau} \exp [ - A (\alpha) \sigma ] B (\alpha) B ^ {\mathrm{T}} (\alpha) \exp [ - A ^ {\mathrm{T}} (\alpha) \sigma ] d \sigma$$

其中 $\tau > 0$ ，且与 $\alpha$ 无关，假设 $(A, B)$ 是关于 $\alpha$ 一致可控的，则存在与 $\alpha$ 无关的正常数 $c_{1}$ 和 $c_{2}$ ，使得

$$c _ {1} I \leqslant W (\alpha) \leqslant c _ {2} I, \quad \forall \alpha \in \Gamma$$

设 $Q(\alpha) = \int_0^\tau e^{-2c\sigma}\exp [-A(\alpha)\sigma ]B(\alpha)B^{\mathrm{T}}(\alpha)\exp [-A^{\mathrm{T}}(\alpha)\sigma ]d\sigma ,\quad c > 0$

(a) 证明 $c_{1}e^{-2c\tau}I \leqslant Q(\alpha) \leqslant c_{2}I, \quad \forall \alpha \in \Gamma$

(b) 设 $u = -K(\alpha)x \stackrel{\mathrm{def}}{=} -\frac{1}{2} B^{\mathrm{T}}(\alpha)P(\alpha)x$

其中 $P(\alpha) = Q^{-1}(\alpha)$ ，将 $V = x^{\mathrm{T}}P(\alpha)x$ 作为

$$\dot {x} = [ A (\alpha) - B (\alpha) K (\alpha) ] x$$

的备选李雅普诺夫函数,证明 $\dot{V} \leqslant -2cV$ 。

(c) 证明对于所有 $\alpha \in \Gamma, [A(\alpha) - B(\alpha)K(\alpha)]$ 是关于 $\alpha$ 一致赫尔维茨的。

12.6 证明由(12.50)定义的 $P(\alpha)$ 是非奇异的并满足式(12.51)。
