# 10.4.2 线性观测器设计

针对一个可观测的系统,可以设计一个线性观测器,通过系统的输出来观测(估计)状态变量。首先来看一个最直接、最简单的状态观测器,即

$$
\frac {\mathrm{d} \hat {z} (t)}{\mathrm{d} t} = A \hat {z} (t) + B u (t) \tag {10.4.3}
$$

其中, $\hat{z}(t)$ 代表估计值。这一观测器的核心理念是“猜”。式(10.4.3)中的观测器的状态空间方程和式(10.4.1a)中的动态系统一模一样。这意味着, 如果运气足够好, 在 $t = 0$ 时刻“猜”的状态变量的值是准确的, 即 $\hat{z}(0) = z(0)$ , 那么在未来通过式 (10.4.3) 所计算得到的估计值 $\hat{z}(t)$ 会和实际值 $z(t)$ 保持一致, 即 $\hat{z}(t) = z(t)$ 。但是, 如果在初始时刻猜得不准确 $\hat{z}(0) \neq z(0)$ , 未来估计的结果就将大相径庭, 更为严重的是, 如果使用一个不准确的估计值来指导设计控制器, 就有可能带来危害性的后果。因此, 为改善式 (10.4.3), 可以为其加上一个和输出有关的反馈, 令

$$
\frac {\mathrm{d} \hat {z} (t)}{\mathrm{d} t} = A \hat {z} (t) + B u (t) + L (y (t) - \hat {y} (t)) \tag {10.4.4a}
$$

$$
\hat {\mathbf {y}} (t) = \mathbf {C} \hat {\mathbf {z}} (t) + \mathbf {D u} (t) \tag {10.4.4b}
$$

其中, $\hat{\mathbf{y}}(t)$ 是根据估计值 $\hat{z}(t)$ 计算出的估计输出。因为输出 $\mathbf{y}(t)$ 是可测的, 所以可以利用它与估计输出 $\hat{\mathbf{y}}(t)$ 之间的差 (输出误差) 反馈到观测器式 (10.4.4a) 中, 这样就形成了一个闭环的观测器。式 (10.4.4) 被称为龙伯格观测器 (Luenberger Observer)。设计目标则是通过设计观测矩阵 $L$ , 使得 $\hat{z}(t)$ 随时间的增加趋近于 $z(t)$ 。首先将式 (10.4.4b) 代入式 (10.4.4a), 得到

$$
\begin{array}{l} \frac {\mathrm{d} \hat {z} (t)}{\mathrm{d} t} = A \hat {z} (t) + B u (t) + L (y (t) - C \hat {z} (t) - D u (t)) \\ = (\boldsymbol {A} - \boldsymbol {L C}) \hat {\boldsymbol {z}} (t) + (\boldsymbol {B} - \boldsymbol {L D}) \boldsymbol {u} (t) + \boldsymbol {L y} (t) \tag {10.4.5} \\ \end{array}
$$

式(10.4.5)通过输入 $u(t)$ 和输出 $y(t)$ 表示估计值 $\hat{z}(t)$ ，这两个值都是可知的。除此之外，式中不存在未知的变量，所以式(10.4.5)是线性观测器最终的表达式。

用式(10.4.1a)减去式(10.4.5)，得到

$$
\frac {\mathrm{d} (\boldsymbol {z} (t) - \hat {\boldsymbol {z}} (t))}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B} \boldsymbol {u} (t) - (\boldsymbol {A} - \boldsymbol {L C}) \hat {\boldsymbol {z}} (t) - (\boldsymbol {B} - \boldsymbol {L D}) \boldsymbol {u} (t) - \boldsymbol {L y} (t) \tag {10.4.6}
$$

将式(10.4.1b)代入式(10.4.6)，得到

$$
\begin{array}{l} \frac {\mathrm{d} (\boldsymbol {z} (t) - \hat {\boldsymbol {z}} (t))}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B} \boldsymbol {u} (t) - (\boldsymbol {A} - \boldsymbol {L C}) \hat {\boldsymbol {z}} (t) - (\boldsymbol {B} - \boldsymbol {L D}) \boldsymbol {u} (t) - \boldsymbol {L} (\boldsymbol {C z} (t) + \boldsymbol {D u} (t)) \\ = (\mathbf {A} - \mathbf {L C}) (\mathbf {z} (t) - \hat {\mathbf {z}} (t)) \tag {10.4.7} \\ \end{array}
$$

令 $\tilde{z}(t)=z(t)-\hat{z}(t)$ ，代表观测误差，代入式(10.4.7)可得

$$
\frac {\mathrm{d} \tilde {z} (t)}{\mathrm{d} t} = (\mathbf {A} - \mathbf {L C}) \tilde {z} (t) \tag {10.4.8}
$$

式(10.4.8)说明观测误差 $\tilde{z}(t)$ 的平衡点是[0]。根据前面的分析, 当矩阵 $(A - LC)$ 的特征值实部都为负数时, 其平衡点是稳定的。这意味着随着时间的增加, $\tilde{z}(t) \to 0$ , 即 $\hat{z}(t) \to z(t)$ 。因此, 当前设计的目标就是找到合适的 $L$ , 使得 $(A - LC)$ 的特征值实部都为负数。观测器设计的框图如图 10.4.1 所示, 其中被虚线圈起来的部分就是观测器, 即式(10.4.5)所表示的内容。它相当于在“后台”同步运行另一套动态系统, 而这个动态系统可以根据系统的输入 $u(t)$ 和输出 $y(t)$ 估计系统的状态值 $z(t)$ 。
