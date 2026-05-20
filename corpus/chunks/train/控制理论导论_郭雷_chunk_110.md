$$\lim _ {t \rightarrow \infty} z (t) = 0.$$

定义 1.8.1 已知定常线性系统 (1.8.1) 和动态补偿器 (1.8.2). 如果这个动态补偿器使得闭环系统 (1.8.3) 是内部稳定的和输出调节的, 那么式 (1.8.2) 就叫做系统 (1.8.1) 的一个综合 (或无静差补偿器). 带有无静差补偿器的闭环系统叫做无静差系统, 或者叫做稳定的输出调节系统.

为分析输出调节系统的结构性质，令

$$
\boldsymbol {A} _ {L} = \left[ \begin{array}{c c} \boldsymbol {A} _ {1} + \boldsymbol {B} _ {1} \boldsymbol {F C} _ {1} & \boldsymbol {B} _ {1} \boldsymbol {F} _ {\mathrm{c}} \\ \boldsymbol {B} _ {\mathrm{c}} \boldsymbol {C} _ {1} & \boldsymbol {A} _ {\mathrm{c}} \end{array} \right], \quad \boldsymbol {B} _ {L} = \left[ \begin{array}{c} \boldsymbol {A} _ {3} + \boldsymbol {B} _ {1} \boldsymbol {F C} _ {2} \\ \boldsymbol {B} _ {\mathrm{c}} \boldsymbol {C} _ {2} \end{array} \right],

\boldsymbol {D} _ {L} = \left[ \begin{array}{l l} \boldsymbol {D} _ {1} & 0 \end{array} \right], \quad x _ {L} (t) = \left[ \begin{array}{l} x _ {1} (t) \\ x _ {c} (t) \end{array} \right],
$$

那么闭环系统 (1.8.3) 可写成

$$
\left\{ \begin{array}{l} \dot {x} _ {L} (t) = A _ {L} x _ {L} (t) + B _ {L} x _ {2} (t), \\ \dot {x} _ {2} (t) = A _ {2} x _ {2} (t), \\ z (t) = D _ {L} x _ {L} (t) + D _ {2} x _ {2} (t). \end{array} \right. \tag {1.8.4}
$$

假设 $\sigma(A_L) \subset \mathbb{C}^-$ , $\sigma(A_2) \subset \overline{\mathbb{C}}^+$ . 于是, 对系统 (1.8.4) 有如下一个重要引理:

引理 1.8.1(输出调节系统的结构定理) 已知系统 (1.8.4), 设 $\sigma(A_L) \subset \mathbb{C}^-$ , $\sigma(A_2) \subset \overline{\mathbb{C}}^+$ . 使系统 (1.8.4) 是输出调节的充分必要条件是, 存在一个 $(n_1 + l) \times n_2$ 阶常值矩阵 $V$ , 使得

$$\boldsymbol {A} _ {L} \boldsymbol {V} - \boldsymbol {V} \boldsymbol {A} _ {2} = \boldsymbol {B} _ {L}. \quad \boldsymbol {D} _ {L} \boldsymbol {V} = \boldsymbol {D} _ {2}. \tag {1.8.5}$$

证明 充分性. 假设存在相应的常值矩阵 V, 使得等式 (1.8.5) 成立. 令

$$\widehat {x} _ {L} = x _ {L} (t) + V x _ {2} (t).$$

将它代入系统 (1.8.4) 得出

$$\dot {\widehat {x}} _ {L} = A _ {L} \widehat {x} _ {L} (t), \quad z (t) = D _ {L} \widehat {x} _ {L} (t).$$

由于 $\sigma(A_L) \subset \mathbb{C}^-$ , 因此对任意 $\hat{x}_L(t_0)$ 都有

$$\lim _ {t \rightarrow \infty} \widehat {x} _ {L} (t) = 0,$$

从而对任意 $x_{20} = x_2(t_0)$ .有

$$\lim _ {t \rightarrow \infty} z (t) = 0,$$

根据定义，系统(1.8.4)是输出调节的.

必要性. 设系统 (1.8.4) 是输出调节的, 那么对任意 $x_{2}(t_{0}) = x_{20}$ 都有

$$\lim _ {t \to \infty} z (t) = 0. \tag {1.8.6}$$

另一方面，由于 $\sigma(A_L) \cap \sigma(A_2) = \varnothing$ 。其中 $\varnothing$ 表示空集。那么由定理 1.1.2 必存在唯一常值矩阵 $V$ ，使得

$$\boldsymbol {A} _ {L} \boldsymbol {V} - \boldsymbol {V} \boldsymbol {A} _ {2} = \boldsymbol {B} _ {L}.$$

令

$$\widehat {x} _ {L} = x _ {L} (t) + V x _ {2} (t),$$

于是有
