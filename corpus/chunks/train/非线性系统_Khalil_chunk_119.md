$$\| g (x) \| _ {2} < \gamma \| x \| _ {2}, \quad \forall \| x \| _ {2} < r$$

因此， $\dot{V} (x) <   - x^{\mathrm{T}}Qx + 2\gamma \| P\|_{2}\| x\|_{2}^{2},\quad \forall \| x\|_{2} <   r$

但是， $x^{\mathrm{T}}Qx\geqslant \lambda_{\min}(Q)\| x\| _2^2$

其中 $\lambda_{\min}(\cdot)$ 表示矩阵的最小特征值。注意,由于 Q 是对称且正定的,所以 $\lambda_{\min}(Q)$ 为正实数,因此

$$\dot {V} (x) < - [ \lambda_ {\min} (Q) - 2 \gamma \| P \| _ {2} ] \| x \| _ {2} ^ {2}, \forall \| x \| _ {2} < r$$

选择 $\gamma < (1/2)\lambda_{\min}(Q) / \|P\|_2$ ，以保证 $\dot{V}(x)$ 负定。由定理4.1可知，原点是渐近稳定的。为了证明定理的第二条，先考虑 $A$ 在虚轴上没有特征值的特例。如果 $A$ 的特征值集中到右半开平面为一组，左半开平面为一组，那么存在一个满秩矩阵 $T$ ，满足①

$$
T A T ^ {- 1} = \left[ \begin{array}{c c} - A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right]
$$

其中 $A_{1}$ 和 $A_{2}$ 都为赫尔维茨矩阵。设

$$
z = T x = \left[ \begin{array}{l} z _ {1} \\ z _ {2} \end{array} \right]
$$

z 的分块与 $A_{1}$ 和 $A_{2}$ 的维数一致。进行变量代换 z = Tx，则系统

$$\dot {x} = A x + g (x)$$

转换为 $\dot{z}_1 = -A_1z_1 + g_1(z)$

$$\dot {z} _ {2} = A _ {2} z _ {2} + g _ {2} (z)$$

其中对于任意 $\gamma > 0$ ，存在 $r > 0$ ，对函数 $g_{i}(z)$ 有

$$\| g _ {i} (z) \| _ {2} < \gamma \| z \| _ {2}, \forall \| z \| _ {2} \leqslant r, i = 1, 2$$

在 z 坐标系中, 原点 z=0 是系统的一个平衡点。显然, 与 z=0 有关的稳定性性质对于 x 坐标系的平衡点 x=0 都适用, 这是因为 T 是非奇异矩阵 $^{②}$ 。为了证明原点是非稳定的, 可以运用定理 4.3。基本按照例 4.7 构造函数 $V(z)$ , 只是用向量代替了例 4.7 中的标量。设 $Q_{1}$ 和 $Q_{2}$ 分别是与 $A_{1}$ 和 $A_{2}$ 维数相同的正定对称矩阵。由于 $A_{1}$ 和 $A_{2}$ 是赫尔维茨矩阵, 由定理 4.6 可知李

雅普诺夫方程 $P_{i}A_{i} + A_{i}^{\mathrm{T}}P_{i} = -Q_{i},\quad i = 1,2$

有唯一的正定解 $P_{1}$ 和 $P_{2}$ 。设

$$
V (z) = z _ {1} ^ {\mathrm{T}} P _ {1} z _ {1} - z _ {2} ^ {\mathrm{T}} P _ {2} z _ {2} = z ^ {\mathrm{T}} \left[ \begin{array}{c c} {{P _ {1}}} & {{0}} \\ {{0}} & {{- P _ {2}}} \end{array} \right] z
$$

在子空间 $z_{2}=0$ 内, 对于任意靠近原点的点有 $V(z)>0$ 。设

$$U = \{z \in R ^ {n} | \| z \| _ {2} \leqslant r \text {和} V (z) > 0 \}$$

在 U 内， $\dot{V}(z)=-z_{1}^{\mathrm{T}}(P_{1}A_{1}+A_{1}^{\mathrm{T}}P_{1})z_{1}+2z_{1}^{\mathrm{T}}P_{1}g_{1}(z)$

$$
- z _ {2} ^ {\mathrm{T}} \left(P _ {2} A _ {2} + A _ {2} ^ {\mathrm{T}} P _ {2}\right) z _ {2} - 2 z _ {2} ^ {\mathrm{T}} P _ {2} g _ {2} (z)
= z _ {1} ^ {\mathrm{T}} Q _ {1} z _ {1} + z _ {2} ^ {\mathrm{T}} Q _ {2} z _ {2} + 2 z ^ {\mathrm{T}} \left[ \begin{array}{c} P _ {1} g _ {1} (z) \\ - P _ {2} g _ {2} (z) \end{array} \right]
\geqslant \lambda_ {\min} (Q _ {1}) \| z _ {1} \| _ {2} ^ {2} + \lambda_ {\min} (Q _ {2}) \| z _ {2} \| _ {2} ^ {2}- 2 \| z \| _ {2} \sqrt {\| P _ {1} \| _ {2} ^ {2} \| g _ {1} (z) \| _ {2} ^ {2} + \| P _ {2} \| _ {2} ^ {2} \| g _ {2} (z) \| _ {2} ^ {2}}> \quad (\alpha - 2 \sqrt {2} \beta \gamma) \| z \| _ {2} ^ {2}
$$
