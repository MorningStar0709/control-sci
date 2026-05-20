李雅普诺夫函数可用于检验矩阵 A 是否为赫尔维茨矩阵，并可作为另一种计算 A 的特征值的方法。首先选择一个正定矩阵 $Q(\text{如 } Q=I)$ ，然后解李雅普诺夫方程(4.12)求出 P。如果方程有一个正定解，则 A 是赫尔维茨矩阵，否则 A 就不是赫尔维茨矩阵。但通过解李雅普诺夫方程计算 A 的特征值时，在计算上并没有优势 $^{②}$ 。此外，特征值为线性系统响应提供了更直接的信息。我们对李雅普诺夫方程感兴趣 $^{③}$ ，不在于检验线性系统的稳定性，而在于对任何线性系统 $\dot{x}=Ax$ ，当 A 是赫尔维茨矩阵时，它提供了一种求李雅普诺夫函数的方法。当方程右边的 Ax 受到扰动时，无论是以 A 为系数的线性扰动还是非线性扰动，仅仅知道存在李雅普诺夫函数，就允许我们大致给出系统的一些结论。随着对李雅普诺夫法的进一步研究，这一优势将愈加明显。

现在回到非线性系统

$$\dot {x} = f (x) \tag {4.14}$$

其中， $f: D \to R^{n}$ 是从 $D \subset R^{n}$ 到 $R^{n}$ 的连续可微映射。假设原点 $x = 0$ 在 $D$ 内，且为系统的一个平衡点，即 $f(0) = 0$ 。根据均值定理

$$f _ {i} (x) = f _ {i} (0) + \frac {\partial f _ {i}}{\partial x} (z _ {i}) x$$

其中 $z_{i}$ 是连接 $x$ 与原点之间的线段上的一点。前面的等式对于任意一点 $x \in D$ 都成立，从而使连接 $x$ 到原点的线段全部在 $D$ 内。由 $f(0) = 0$ 可写出

$$f _ {i} (x) = \frac {\partial f _ {i}}{\partial x} (z _ {i}) x = \frac {\partial f _ {i}}{\partial x} (0) x + \left[ \frac {\partial f _ {i}}{\partial x} (z _ {i}) - \frac {\partial f _ {i}}{\partial x} (0) \right] x$$

因此 $f(x) = Ax + g(x)$

其中 $A = \frac{\partial f}{\partial x} (0),\qquad g_i(x) = \left[\frac{\partial f_i}{\partial x} (z_i) - \frac{\partial f_i}{\partial x} (0)\right]x$

函数 $g_{i}(x)$ 满足 $|g_{i}(x)| \leqslant \left\| \frac{\partial f_{i}}{\partial x} (z_{i}) - \frac{\partial f_{i}}{\partial x} (0) \right\| \| x\|$

根据 $[\partial f / \partial x]$ 的连续性可知， $\frac{\|g(x)\|}{\|x\|} \to 0$ ，当 $\|x\| \to 0$

这就是说在原点的一个小邻域内,可以用对系统在原点的线性化方程

$$\dot {x} = A x, \quad \text {其中} \quad A = \frac {\partial f}{\partial x} (0)$$

近似表示非线性系统(4.14)。

下一个定理给出了一些条件,在此条件下可大致得出这样的结论:当原点是非线性系统的平衡点时,其稳定性可以通过研究线性系统在该平衡点的稳定性得出。

定理4.7 设 $x = 0$ 是非线性系统 $\dot{x} = f(x)$

的一个平衡点,其中 $f:D\rightarrow R^{n}$ 是连续可微的,且D为原点的一个邻域。设

$$A = \left. \frac {\partial f}{\partial x} (x) \right| _ {x = 0}$$

那么，

1. 如果 A 的所有特征值都满足 $Re \lambda_{i} < 0$ ，则原点是渐近稳定的。  
2. 如果 A 至少有一个特征值满足 $Re \lambda_{i} > 0$ ，则原点是不稳定的。

证明:为了证明第一条,设 A 是赫尔维茨矩阵。那么根据定理 4.6 可知,对于任何正定对称矩阵 Q,李雅普诺夫方程(4.12)的解 P 都是正定的。以 $V(x)=x^{T}Px$ 作为非线性系统的备选李雅普诺夫函数,则 $V(x)$ 沿系统轨线的导数为

$$
\begin{array}{l} \dot {V} (x) = x ^ {\mathrm{T}} P f (x) + f ^ {\mathrm{T}} (x) P x \\ = x ^ {T} P [ A x + g (x) ] + \left[ x ^ {T} A ^ {T} + g ^ {T} (x) \right] P x \\ = x ^ {T} \left(P A + A ^ {T} P\right) x + 2 x ^ {T} P g (x) \\ = - x ^ {T} Q x + 2 x ^ {T} P g (x) \\ \end{array}
$$

上式右边的第一项是负定的,而第二项(一般)是不定的。函数 $g(x)$ 满足

$$\frac {\| g (x) \| _ {2}}{\| x \| _ {2}} \to 0 \quad \text {当} \| x \| _ {2} \to 0$$

因此,对于任意 $\gamma > 0$ , 存在 r > 0, 使
