# (2) 矩阵范数

定义 若对任意矩阵 $A \in R^{m \times n}$ ，都有实数 $\|A\|$ 与之对应，且满足下面的范数公理：

① 正定性： $\|A\|\geqslant0$ ，当且仅当A=0时 $\|A\|=0$ ；  
② 齐次性: 对任何 $\lambda \in R, \| \lambda A \| = |\lambda| \| A \|$ ;  
③三角不等式:对任何 $A,B\in R^{m\times n}$ ，有

$$\| \mathbf {A} + \mathbf {B} \| \leqslant \| \mathbf {A} \| + \| \mathbf {B} \|$$

则称这个实数 $\parallel A \parallel$ 为矩阵 A 的范数。

矩阵范数可分为以下几种类型：

$$\| \mathbf {A} \| _ {\mathrm{V} _ {1}} = \sum_ {j = 1} ^ {m} \sum_ {i = 1} ^ {n} | a _ {i j} | \tag {7}$$

$\|A\|_{V_{\infty}}=\max_{i,j}|a_{ij}|$ （切比雪夫范数）

$$\| \mathbf {A} \| _ {\mathrm{V} _ {\mathrm{p}}} = (\sum_ {j = 1} ^ {m} \sum_ {i = 1} ^ {n} | a _ {i j} | ^ {p}) ^ {1 / p}, 1 \leqslant p \leqslant + \infty \tag {9}$$

当 $p = 2$ 时，称 $\| \mathbf{A}\|_{\mathrm{V}_2} = \| \mathbf{A}\|_{\mathrm{F}} = \left(\sum_{j = 1}^{m}\sum_{i = 1}^{n}|a_{ij}|^2\right)^{1 / 2}$ 为 $\mathbf{A}$ 的Frobenius范数，简称F-范数，是最常用的范数之一。

$$\| \mathbf {A} \| _ {\mathrm{F}} ^ {2} = \operatorname{tr} (\mathbf {A} ^ {\mathrm{T}} \mathbf {A}) = \sum_ {j = 1} ^ {m} \sum_ {i = 1} ^ {n} | a _ {i j} | ^ {2}. \tag {10}$$

F- 范数具有下列良好的性质：

① 设 $A \in R^{m \times n}, B \in R^{n \times l}$ ，则有

$$\| \mathbf {A} \| _ {\mathrm{F}} \leqslant \| \mathbf {A} \| _ {\mathrm{F}} \| \mathbf {B} \| _ {\mathrm{F}} \tag {11}$$

② 在矩阵空间 $R^{n \times n}$ 上的任意实函数，记为 $\|\cdot\|$ ，如果对所有的 $A, B \in R^{n \times n}, \lambda \in R$ ，都满足：

- $\| A \| \geqslant 0$ ，当且仅当 $A = 0$ 时，有 $\| A \| = 0$ ;  
• || λA || = |λ| || A || ;   
- $\| A + B \| \leqslant \| A \| + \| B \|$ ;   
- $\| AB \| \leqslant \| A \| \| B \|$ 。

则称 $\parallel\cdot\parallel$ 为相容的矩阵范数，或简称矩阵范数。显然，矩阵的 F- 范数是一种相容的矩阵范数。

根据 F- 范数的性质, 有

$$\operatorname{tr} \left[ \widetilde {\boldsymbol {x}} ^ {\mathrm{T}} (\boldsymbol {x} - \widetilde {\boldsymbol {x}}) \right] \leqslant \| \widetilde {\boldsymbol {x}} \| _ {\mathrm{F}} \| \boldsymbol {x} \| _ {\mathrm{F}} - \| \widetilde {\boldsymbol {x}} \| _ {\mathrm{F}} ^ {2} \tag {12}$$
