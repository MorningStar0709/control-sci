$$\dot {\boldsymbol {W}} (\boldsymbol {x}) \mid_ {(2. 4. 3 8)} = \boldsymbol {x} ^ {\mathbf {T}} (\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A}) \boldsymbol {x} = - \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {x},$$

其中 $P$ 为正定对称矩阵，因此我们得到

$$\dot {\boldsymbol {W}} (\boldsymbol {x}) \mid_ {(2. 4. 1 9)} = x ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A}) x + O (| x | ^ {2}) = - x ^ {\mathrm{T}} x + O (| x | ^ {2}).$$

因此在 $x = 0$ 某邻域内， $\dot{W}(x)|_{(2.4.19)}$ 是负定的。根据定理2.4.8, 非线性微分方程 (2.4.19) 的零平衡是局部渐近稳定的。

定理 2.4.19 $^{[12]}$ 如果线性定常微分方程 (2.4.38) 的系数矩阵 A 的特征值中至少有一个的实部大于零，则非线性定常微分方程 (2.4.19) 的零平衡解是不稳定的。

当 $\pmb{A}$ 有一个零特征值，而它其余的特征值皆具有的负实部时，我们称这种情况为第一临界情况；而当 $\pmb{A}$ 具有一对共轭的纯虚特征值、其余特征值皆具有负实部时，我们称为第二临界情况。不管是第一临界情况还是第二临界情况，非线性微分方程 (2.4.19) 的平衡解的稳定性问题不能由它的一次近似微分方程决定，而必须同时考虑它的高次近似。下面仅举一个例子说明。

例2.4.5 考察非线性二维向量微分方程

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} x \\ y \end{array} \right] = \left[ \begin{array}{l l} 0 & - 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l} x \\ y \end{array} \right] + \left[ \begin{array}{l} a x ^ {3} \\ a y ^ {3} \end{array} \right], \tag {2.4.40}
$$

其线性部分的系数矩阵 $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ 的特征方程为 $\lambda^{2} + 1 = 0$ ，它的解为 $\lambda = \pm \sqrt{-1}$ .

取 $W(x,y) = \frac{1}{2} (x^2 +y^2)$ 计算 $W(x,y)$ 沿微分方程(2.4.40)对 $t$ 的全导数得

$$\dot {W} (x, y) \mid_ {(2. 4. 4 0)} = a (x ^ {4} + y ^ {4}).$$

当 $a < 0$ 时， $\dot{W}(x, y) \big|_{(2.4.40)}$ 为负定，微分方程的平衡解渐近稳定；当 $a = 0$ 时，微分方程的零平衡解稳定；当 $a > 0$ 时，有 $\dot{W}(x, y) \big|_{(2.4.40)} > 0$ ，微分方程的零平衡解不稳定。

可见，对于非线性微分方程，当它的线性部分的系数矩阵的特征值为零或为纯虚数时，要判别其平衡解的稳定性还必须考察其更高阶部分的性质。对此问题本节不作进一步研究，有兴趣的读者可参阅文献[6],[13],[16].

微分方程全局稳定性是稳定性理论中的重要问题，但不易研究。这里主要介绍 Krasovskii 定理 和平面 Jacobi 猜想。

下面先给出一个用 Lyapunov 函数刻画的全局渐近稳定性的定理.

定理2.4.20 如果存在径向无界的正定函数 $W(x)$ , 使得 $\dot{W}(x)|_{(2.4.19)}$ 负定, 则式 (2.4.19) 的平衡解 $x = 0$ 全局渐近稳定.

定理2.4.20的证明与定理2.4.8的证明类似，这里略去.

假设微分方程 (2.4.19) 中 $f(\cdot): \mathbb{R}^n \to \mathbb{R}^n$ 连续可微，并记

$$\boldsymbol {M} _ {f} (x) = \frac {\partial f}{\partial x} (x) + \left(\frac {\partial f}{\partial x} (x)\right) ^ {\mathrm{T}}. \tag {2.4.41}$$

命题2.4.4 考察微分方程(2.4.19). 如果 $\forall x \in \mathbb{R}^n$ , $M_f(x)$ 为正定 (负定) 矩阵, 则在 $\mathbb{R}^n$ 内非线性微分方程 (2.4.19) 只有唯一的零平衡解, 即

$$f (x) \neq 0, \forall x \in \mathbb {R} ^ {n}, x \neq 0.$$

证明 设 $x^{*} \in \mathbb{R}^{n}, f(x^{*}) = 0$ ，则有
