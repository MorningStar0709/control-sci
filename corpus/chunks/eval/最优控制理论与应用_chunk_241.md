# 4. 鲁棒干扰抑制问题。

设被控对象由状态方程

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \Delta \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {1} \boldsymbol {w} + \boldsymbol {B} _ {2} \boldsymbol {u}$$

描述。其中，u 表示控制输入，w 表示有界干扰，且对于任意的 T > 0 是平方可积的。假设不确定性函数向量 $\Delta A$ 属于某一给定的集合 $\Omega$ 。

试设计适当的反馈控制律 u = Kx，使得 x = 0 是系统的渐进稳定平衡点；同时，当有干扰 w 作用时，尽可能减少由干扰引起的状态调节误差。（提示：选择如下的性能准则：

$$
\begin{array}{l} \max _ {\Delta A \in \Omega} \int_ {0} ^ {T} [ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q} \boldsymbol {x} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} \boldsymbol {u} (t) ] \mathrm{d} t \\ \leqslant \gamma^ {2} \int_ {0} ^ {T} w ^ {\mathrm{T}} (t) w (t) \mathrm{d} t, \forall w (t) \in L _ {2} [ 0, T) \\ \end{array}
$$

其中 $\gamma > 0$ 表示系统的干扰抑制能力, $Q > 0$ , $R \geqslant 0$ 分别为加权阵, 不难找到 $M, N$ , 使得 $Q = M^{\mathrm{T}}M$ , $R = N^{\mathrm{T}}N$ , 定义性能评价信号 $z = \begin{bmatrix} Mx \\ Nu \end{bmatrix} = \begin{bmatrix} M \\ 0 \end{bmatrix} x + \begin{bmatrix} 0 \\ N \end{bmatrix} u$ , 由此得到性能准则:

$$\int_ {0} ^ {T} \boldsymbol {z} ^ {\mathrm{T}} (t) \boldsymbol {z} (t) \mathrm{d} t \leqslant \gamma^ {2} \int_ {0} ^ {T} \boldsymbol {w} ^ {\mathrm{T}} (t) \boldsymbol {w} (t) \mathrm{d} t, \forall \boldsymbol {w} (t) \in L _ {2} [ 0, T)$$

由此通过本章所介绍的线性定常系统 $H_{\infty}$ 最优控制问题的求解方法进行求解。）
