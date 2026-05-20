# 10.3.3 轨迹追踪

本节将解释 10.3.2 节末尾提出的问题, 设计 $u(t)$ 使得系统的状态稳定在一个非零的目标值 $z_{d}$ 。此时要求控制量 $u(t)$ (即动态系统的输入) 承担两个功能:

第一，改变系统的平衡点位置到 $z_{d}$ 。

第二，令 $z_{d}$ 成为一个稳定的平衡点。

首先引入误差，令

$$
\boldsymbol {e} (t) = \boldsymbol {z} _ {\mathrm{d}} - \boldsymbol {z} (t) = \left[ \begin{array}{l} z _ {1 \mathrm{d}} - z _ {1} (t) \\ z _ {2 \mathrm{d}} - z _ {2} (t) \end{array} \right] = \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] \tag {10.3.19}
$$

此时的设计目标就变成了：①令 $e(t)$ 的平衡点为 $e_{f} = [0,0]$ ；② $e_{f} = [0,0]$ 是稳定的平衡点。

![](image/81235e70a4f7dbac9f5f8a190c6437be74a729504bf0f7c6bfeeb66fbd49435c.jpg)

假设目标值 $z_{1\mathrm{d}}$ 和 $z_{2\mathrm{d}}$ 都是常数（或者变化缓慢），因此 $\frac{\mathrm{dz}_{1\mathrm{d}}}{\mathrm{dt}} = \frac{\mathrm{dz}_{2\mathrm{d}}}{\mathrm{dt}} = 0$ 。可得

$$
\frac {\mathrm{d} \boldsymbol {e} (t)}{\mathrm{d} t} = \frac {\mathrm{d} z _ {\mathrm{d}}}{\mathrm{d} t} - \frac {\mathrm{d} z (t)}{\mathrm{d} t} = - \frac {\mathrm{d} z (t)}{\mathrm{d} t} = - \boldsymbol {A} z (t) - \boldsymbol {B u} (t) \tag {10.3.20}
$$

将式(10.3.19)和 $A=\begin{bmatrix}0&1\\ \frac{g}{d}&0\end{bmatrix},B=\begin{bmatrix}0\\ 1\end{bmatrix}$ 代入(10.3.20)，得到

$$
\begin{array}{l} \frac {\mathrm{d} \boldsymbol {e} (t)}{\mathrm{d} t} = - \boldsymbol {A} \left(\boldsymbol {z} _ {\mathrm{d}} - \boldsymbol {e} (t)\right) - \boldsymbol {B u} (t) = \boldsymbol {A e} (t) - \boldsymbol {A z} _ {\mathrm{d}} - \boldsymbol {B u} (t) \\ \Rightarrow \frac {\mathrm{d} e (t)}{\mathrm{d} t} = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] - \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] \left[ \begin{array}{l} z _ {1 d} \\ z _ {2 d} \end{array} \right] - \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u (t) \tag {10.3.21} \\ \end{array}
$$

展开得到

$$
\frac {\mathrm{d} e _ {1} (t)}{\mathrm{d} t} = e _ {2} (t) - z _ {2 \mathrm{d}} \tag {10.3.22a}
$$

$$
\frac {\mathrm{d} e _ {2} (t)}{\mathrm{d} t} = \frac {g}{d} e _ {1} (t) - \frac {g}{d} z _ {1 \mathrm{d}} - u (t) \tag {10.3.22b}
$$

观察式(10.3.22)可以发现,本例中 $e_{2}(t)$ 的平衡点是无法通过输入改变的,因为无论 $u(t)$ 如何选择,都无法作用在式(10.3.22a)上,当式(10.3.22a)中的 $\frac{\mathrm{d}e_{1}(t)}{\mathrm{d}t}=0$ 时,平衡点 $e_{2\mathrm{f}}\equiv z_{2\mathrm{d}}$ ,这说明只有在 $z_{2\mathrm{d}}=0$ 时,误差的平衡点 $e_{2\mathrm{f}}=0$ ,意味着状态变量 $z_{2}(t)$ 的唯一平衡点为0。
