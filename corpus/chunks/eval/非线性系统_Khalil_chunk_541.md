# C. 21 证明定理 13.1

证明中用到了14.3节介绍的Lie括号和对合分布的概念以及完全可积性的概念。一个在 $D$ 上由 $f_{1},\dots ,f_{k}$ 产生的非奇异分布 $\Delta$ 是完全可积的，如果对于每个 $x_0\in D$ ，存在 $x_0$ 的一个邻域 $N$ 和 $n - k$ 个实值光滑函数 $h_1(x),\dots ,h_{n - k}(x)$ ，满足

$$\frac {\partial h _ {j}}{\partial x} f _ {i} (x) = 0, \quad \forall 1 \leqslant i \leqslant k, \quad 1 \leqslant j \leqslant n - k$$

且对于所有 $x \in D$ ，行向量 $dh_{1}(x), \cdots, d_{n-k}(x)$ 是线性无关的，其中

$$d h (x) = \frac {\partial h}{\partial x} = \left[ \frac {\partial h}{\partial x _ {1}}, \dots , \frac {\partial h}{\partial x _ {n}} \right]$$

称为 $h$ 的微分。微分几何学中的一个重要结论是 Frobenius 定理①，该定理说明非奇异分布是完全可积的，当且仅当它是对合的。

首先给出并证明两个基本引理。

引理C.8 对于所有 $x \in D$ 以及所有整数 $k$ 和 $j$ , 当 $k \geqslant 0$ 和 $0 \leqslant j \leqslant \rho - k - 1$ 时, 有

$$
L _ {a d _ {f} ^ {j} g} L _ {f} ^ {k} h (x) = \left\{ \begin{array}{l l} 0, & 0 \leqslant j + k <   \rho - 1 \\ (- 1) ^ {j} L _ {g} L _ {f} ^ {\rho - 1} h (x) \neq 0, & j + k = \rho - 1 \end{array} \right. \tag {C.92}
$$

◇

证明:对j用归纳法证明该引理。根据相对阶的定义,当j=0时,式(C.92)成立。现在假设对于某个j,式(C.92)成立,证明对于 $j+1$ ,式(C.92)也成立。回顾雅可比恒等式(见习题13.8)

$$L _ {[ f, \beta ]} \lambda (x) = L _ {f} L _ {\beta} \lambda (x) - L _ {\beta} L _ {f} \lambda (x)$$

其中 $\lambda$ 为任意实值函数， $f$ 和 $\beta$ 为任意向量场。取 $\lambda = L_f^k h, \beta = ad_f^j g$ ，得

$$L _ {a d _ {f} ^ {j + 1} g} L _ {f} ^ {k} h (x) = L _ {[ f, a d _ {f} ^ {j} g ]} L _ {f} ^ {k} h (x) = L _ {f} L _ {a d _ {f} ^ {j} g} L _ {f} ^ {k} h (x) - L _ {a d _ {f} ^ {j} g} L _ {f} ^ {k + 1} h (x)$$

注意,由于 $j+k+1\leqslant\rho-1\Rightarrow j+k<\rho-1\Rightarrow L_{f}L_{ad_{f}^{j}g}L_{f}^{k}h(x)=0$

故右边第一项为零。此外假设式(C.92)对于j成立,有

$$
L _ {a d _ {f} ^ {j} g} L _ {f} ^ {k + 1} h (x) = \left\{ \begin{array}{l l} 0, & 0 \leqslant j + k + 1 <   \rho - 1 \\ (- 1) ^ {j} L _ {g} L _ {f} ^ {\rho - 1} h (x) \neq 0, & j + k + 1 = \rho - 1 \end{array} \right.
$$

因此 $L_{ad_f^{j + 1}g}L_f^k h(x) = \left\{ \begin{array}{ll}0, & 0\leqslant j + k + 1 <   \rho -1\\ (-1)^{j + 1}L_gL_f^{\rho -1}h(x)\neq 0, & j + k + 1 = \rho -1 \end{array} \right.$

证毕。

引理 C.9 对于所有 $x \in D$ ，有

- 行向量 $dh(x), dL_f h(x), \cdots, dL_f^{\rho - 1}h(x)$ 是线性无关的；  
- 列向量 $g(x), ad_{f}g(x), \cdots, ad_{f}^{\rho - 1}g(x)$ 是线性无关的。

证明:我们有

$$
\left[ \begin{array}{c} d h (x) \\ \vdots \\ d L _ {f} ^ {\rho - 1} h (x) \end{array} \right] \left[ \begin{array}{l l l} g (x) & \dots & a d _ {f} ^ {\rho - 1} g (x) \end{array} \right] =
