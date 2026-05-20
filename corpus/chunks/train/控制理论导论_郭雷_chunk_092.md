$$
\left[ \begin{array}{l l} \boldsymbol {B} _ {c c} & \boldsymbol {R} \end{array} \right] = \left[ \begin{array}{c} \boldsymbol {h} ^ {\mathrm{T}} \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} \\ \vdots \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} a _ {0} & r _ {0} \\ a _ {1} & r _ {1} \\ \vdots & \vdots \\ a _ {\nu_ {0} - 2} & r _ {\nu_ {0} - 2} \end{array} \right];
$$

(10) 计算

$$\boldsymbol {A} _ {c} = \boldsymbol {T} - R b h ^ {\mathrm{T}}, \quad \boldsymbol {F} _ {c} = z h ^ {\mathrm{T}}, \quad \boldsymbol {F} _ {0} = z e ^ {\mathrm{T}} + H _ {1}.$$

定理 1.6.4 设定常线性系统 (1.6.1) 完全能控且完全能观测，并且它的能控指数为 $\mu_{0}$ ，那么对任意给定的含有 $n + \mu_{0} - 1$ 个复数的对称集合 A，都存在一个动态输出反馈控制规律 (1.6.20)，使得闭环系统 (1.6.21) 的极点集合为 A，其中 $A_{c}$ ， $B_{c}$ ， $F_{c}$ 和 $F_{0}$ 分别是 $(\mu_{0} - 1) \times (\mu_{0} - 1)$ ， $(\mu_{0} - 1) \times m$ ， $r \times (\mu_{0} - 1)$ 和 $r \times m$ 常值矩阵。

从定理 1.6.3 和 1.6.4 可以看出，由能控指数和能观测指数决定的动态输出反馈控制规律的动态阶数是不相同的，一个为 $\mu_{0}-1$ 阶的，一个为 $\nu_{0}-1$ 阶的。它们是系统 (1.6.1) 的一类动态补偿器的阶数。
