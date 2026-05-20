# 5.3 线性算子半群

设 $A$ 是一 $n \times n$ 复矩阵，在 $\mathbb{C}^n$ 中考虑如下常微分方程：

$$\frac {\mathrm{d} x (t)}{\mathrm{d} t} = A x (t), \qquad x (0) = x _ {0}, \tag {5.3.1}$$

其中 $x \in \mathbb{C}^n$ . 熟知方程 (5.3.1) 的解可以表示成

$$x (t) = \mathrm{e} ^ {A t} x _ {0}, \quad t \geqslant 0. \tag {5.3.2}$$

现在我们在某个函数空间中考虑方程 (5.3.1), 当然这时 $A$ 表示该函数空间中一线性算子. 例如, 当 $A$ 表示有界区域 $\Omega \subset \mathbb{R}^n$ 上带某些边界条件的椭圆算子, 那么方程 (5.3.1) 就是一抛物方程. 在这种情形下, 人们仍然指望 $\mathrm{e}^{At} x_0$ 是方程 (5.3.1) 的解. 但是, 现在的问题要复杂得多. 如果问题 (5.3.1) 满足所谓的 Hadamard 适定条件: 对于任意初始数据 $x_0 \in \mathcal{D}(A)$ , 方程 (5.3.1) 有唯一解 $x(t), t \geqslant 0$ , 并且 $x(t)$ 连续地依赖于初始数据 $x_0$ , 那么我们可以定义一族线性算子 $T(t), t \geqslant 0$ ,

$$T (t) x _ {0} = x (t), \quad x _ {0} \in \mathcal {D} (A).$$

从解 $x(t)$ 的唯一性可知 $T(t)$ 有如下半群性质：

$$T (t + s) = T (t) T (s), \quad \forall t, s \geqslant 0.$$

其次，由 $T(t)x_0$ 对 $x_0$ 的连续依赖性可知 $T(t)$ 对于每一 $t \geqslant 0$ 是有界的。最后我们希望 $x(t)$ 关于 $t$ 有强连续性，即

$$\lim _ {t \downarrow 0} T (t) x _ {0} = x _ {0}, \quad \forall x _ {0} \in \mathcal {D} (A).$$
