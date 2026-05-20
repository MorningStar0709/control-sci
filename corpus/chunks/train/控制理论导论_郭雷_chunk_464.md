显然，如果系统(6.7.1)是 $L^2$ -稳定的，即对于任意输入 $u \in L^2$ ，系统的输出响应 $y \in L^2$ ，那么不等式(6.7.2)对于任意给定的 $T > 0$ 成立，意味着该系统作为输入信号空间到输出信号空间的算子 $\Gamma: L^2 \to L^2$ 的 $L^2$ 诱导范数小于 $\gamma$ ，即

$$\| \Gamma \| = \sup _ {u \in L _ {2}} \frac {\| y \| _ {2}}{\| u \| _ {2}} \leqslant \gamma .$$

因此，上述定义所描述的是更为一般意义下的系统对输入信号的增益。对于那些无法定义 $L^2$ 诱导范数的系统，如果系统在充分大的有限时间区间 $[0, T]$ 内，满足增益不等式

$$\frac {\| y \| _ {T}}{\| u \| _ {T}} \leqslant \gamma ,$$

那么至少从工程意义上该系统的信号传递特征与 $L^2$ 诱导范数所描述的特征相类似.

与定义 6.7.1 密切相关的是所谓的耗散性概念 [14,19].

定义 6.7.2 考虑系统 (6.7.1). 若存在半正定函数 $V(x)(V(0)=0)$ 使得沿该系统的状态轨迹，如下耗散不等式成立：

$$\dot {V} = \frac {\mathrm{d} V}{\mathrm{d} t} \leqslant \frac {1}{2} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right), \quad \forall t \geqslant 0, \forall u, \tag {6.7.3}$$

则称该系统是 $\gamma-$ 耗散的，而半正定函数 $V(x)$ 称为能量存储函数，简称存储函数.

如果系统 (6.7.1) 是 $\gamma$ -耗散的，那么当 $x(0) = 0$ 时，考虑到存储函数的半正定性，将耗散不等式两边求积分，不难得到

$$\| y \| _ {T} ^ {2} \leqslant \| y \| _ {T} ^ {2} + 2 V (x (T)) \leqslant \gamma^ {2} \| u \| _ {T} ^ {2}, \quad \forall u. \tag {6.7.4}$$

该系统具有小于 $\gamma$ 的 $L_{2}$ 增益，实际上，在一定的条件下，可以证明反之亦然.

在介绍这一命题之前，我们先介绍 $\gamma-$ 耗散性的等价条件.

定理 6.7.1 系统 (6.7.1) 是 $\gamma-$ 耗散的充分必要条件是存在可微的半正定函数 $V(x)$ ，使得如下 Hamilton-Jacobi 不等式成立：

$$\frac {\partial V}{\partial x} f (x) + \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} g (x) g ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} + \frac {1}{2} h ^ {\mathrm{T}} (x) h (x) \leqslant 0, \quad \forall x, \tag {6.7.5}$$

这里，我们采用记号 $\frac{\partial^{\mathrm{T}}V}{\partial x}$ 表示 $\left(\frac{\partial V}{\partial x}\right)^{\mathrm{T}}$

证明 充分性. 利用不等式 (6.7.5), 得

$$
\begin{array}{l} \dot {V} = \frac {\partial V}{\partial x} (f (x) + g (x) u) \\ \leqslant - \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} g (x) g ^ {T} (x) \frac {\partial^ {T} V}{\partial x} - \frac {1}{2} h ^ {T} (x) h (x) + \frac {\partial V}{\partial x} g (x) u \\ = \frac {1}{2} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) - \frac {1}{2} \left\| \gamma^ {- 1} g ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} - \gamma u \right\| ^ {2} \\ \leqslant \frac {1}{2} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right). \tag {6.7.6} \\ \end{array}
$$

必要性. 如果该系统是 $\gamma$ -耗散的, 那么由耗散不等式得

$$\dot {V} = \frac {\partial V}{\partial x} (f (x) + g (x) u) \leqslant \frac {1}{2} (\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}), \quad \forall u. \tag {6.7.7}$$

于是
