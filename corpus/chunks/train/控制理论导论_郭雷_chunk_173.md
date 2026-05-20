$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {X} + \boldsymbol {X} \boldsymbol {A} = - \boldsymbol {Q} \tag {2.4.35}$$

有正定对称解矩阵的充分必要条件是 A 为稳定矩阵.

证明 该定理的充分性部分的证明与定理2.4.15的证明完全相同，不再重复.

现证定理的必要性. 设线性矩阵方程 (2.4.35) 有正定对称解矩阵 $P$ . 于是标量函数 $W(x) \stackrel{\mathrm{def}}{=} x^{\mathrm{T}}Px$ 是 $\mathbb{R}^{n}$ 中的正定二次型. 容易推得

$$\dot {\boldsymbol {W}} (\boldsymbol {x} (t)) \mid_ {(2. 4. 3 2)} = \boldsymbol {x} (t) ^ {\mathrm{T}} [ \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} ] \boldsymbol {x} (t) = - \boldsymbol {x} (t) ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {x} (t).$$

因此 A 是稳定的.

线性矩阵方程 (2.4.35) 称为 Lyapunov 方程，其正定解可以表示成

$$P = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {Q} \mathrm{e} ^ {\boldsymbol {A} t} \mathrm{d} t. \tag {2.4.36}$$

定理 2.4.17 对于任意给定的非负定 $n \times n$ 矩阵 $Q = C^{T}C$ ，当 $Q_{0} = [C^{T}, A^{T}C^{T}, \cdots, (A^{T})^{n-1}C^{T}]$ 满秩时，线性矩阵代数方程

$$X \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} X = - \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {C} \tag {2.4.37}$$

有正定对称解矩阵的充分必要条件是 A 为稳定阵.

总结上面的结果可得，对于线性定常向量微分方程(2.4.32)，其零平衡解为渐近稳定的充分必要条件，或者说其系数矩阵为稳定阵的充分必要条件是下列彼此等价的条件之一成立：

(1) $A$ 的特征多项式的Hurwitz行列式皆为正(Routh-Hurwitz定理);  
(2) 线性定常微分方程 (2.4.32) 的任一非零解趋于零;  
(3) 对于任意给定的正定对称 $n \times n$ 矩阵 $\pmb{Q}$ , 线性矩阵代数方程 (2.4.35) 存在正定对称解矩阵;  
(4) 对于任意给定的非负定 $n \times n$ 对称矩阵 $\pmb{Q} = \pmb{C}^{\mathrm{T}}\pmb{C}$ , 当 $\pmb{Q}_0 = [\pmb{C}^{\mathrm{T}}, \pmb{A}^{\mathrm{T}}\pmb{C}^{\mathrm{T}}, \dots, (\pmb{A}^{\mathrm{T}})^{n-1}\pmb{C}^{\mathrm{T}}]$ 为非降秩阵时, 线性矩阵代数方程 (2.4.37) 存在正定对称解矩阵.

现在我们介绍稳定性的一次近似理论。这里主要讨论非线性微分方程(2.4.19)与其一次近似微分方程解的稳定性之间的关系。设 $A = \frac{\partial f}{\partial x}(0)$ 。称线性齐次定常微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x \tag {2.4.38}$$

为非线性定常微分方程 (2.4.19) 的一次近似微分方程.

下面根据非线性微分方程 (2.4.19) 的线性化微分方程 (2.4.38) 的零解的渐近稳定性及不稳定性等信息来判断它本身的零平衡解的稳定性.

定理2.4.18 如果线性定常微分方程(2.4.38)的零平衡解是渐近稳定的，则非线性定常微分方程(2.4.19)的零平衡解是局部渐近稳定的.

证明 依假设知微分方程 (2.4.38) 的系数矩阵 $A$ 的特征值皆具有负实部。于是存在正定二次型

$$\boldsymbol {W} (\boldsymbol {x}) = \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x}, \tag {2.4.39}$$

使得 $W(x)$ 沿方程(2.4.38)对时间 $\pmb{t}$ 的全导数满足
