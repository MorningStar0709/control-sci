证明 由定理3.5.1, 如果 $F$ 的秩是定常的, 那么 $K = F^{-1}(e)$ 是 $G_{1}$ 的一个闭子流形, 其余维数为 $\operatorname{rank}(F)$ . 因此它是一个Lie子群. 因此我们只要证明 $F$ 的秩是定常值.

设 $a \in G_1$ 且 $b = F(a) \in G_2$ . 那么

$$F (x) = F (a) F \left(a ^ {- 1} x\right) = b F \left(a ^ {- 1} x\right) \stackrel {\text { def }} {=} L _ {b} F \left(a ^ {- 1} x\right),$$

这里 $L_{b}$ 是 $b$ 的左乘算子。显然 $L_{b}$ 是解析的，而且它的逆 $(L_{b})^{-1} = L_{b - 1}$ 也是解析的。因此它是一个微分同胚。于是有

$$\operatorname{rank} (F (x)) = \operatorname{rank} (F (a ^ {- 1} x)).$$

由于 $a \in G_1$ 是任意的，故 $\operatorname{rank}(F)$ 处处相等.

例 3.9.2 (1) 特殊线性群：令

$$\operatorname{SL} (n, \mathbb {R}) = \{\boldsymbol {A} \in \operatorname{GL} (n, \mathbb {R}) | \det (\boldsymbol {A}) = 1 \}.$$

$\mathbf{SL}(n,\mathbb{R})$ 称为特殊线性群，它是 $\operatorname{GL}(n,\mathbb{R})$ 的一个Lie子群；

(2) 正交群：令

$$O (n, \mathbb {R}) = \left\{\boldsymbol {A} \in \operatorname{GL} (n, \mathbb {R}) \mid \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {A} = \boldsymbol {I} \right\}.$$

$O(n,\mathbb{R})$ 称为正交群，它是 $\operatorname{GL}(n,\mathbb{R})$ 的一个Lie子群；

(3) $U$ 群：设

$$U (n, \mathbb {C}) = \{\boldsymbol {A} \in \operatorname{GL} (n, \mathbb {C}) \mid \overline {{{\boldsymbol {A}}}} ^ {\mathrm{T}} \boldsymbol {A} = \boldsymbol {I} \}.$$

$U(n,\mathbb{R})$ 称为一个 $U$ 群，它也是 $\operatorname{GL}(n,\mathbb{C})$ 的一个Lie子群；

(4) 辛群：记

$$
\boldsymbol {J} = \left[ \begin{array}{c c} 0 & \boldsymbol {I} _ {n} \\ - \boldsymbol {I} _ {n} & 0 \end{array} \right].
$$

定义

$$\operatorname{Sp} (2 n, \mathbb {R}) = \left\{\boldsymbol {A} \in \operatorname{GL} (2 n, \mathbb {R}) \mid \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {J} \boldsymbol {A} = \boldsymbol {J} \right\}.$$

$\operatorname{Sp}(2n, \mathbb{R})$ 称为辛群，它是 $\operatorname{GL}(2n, \mathbb{R})$ 的一个 Lie 子群.

上述几个结论的证明都是类似的. 这里仅详细讨论 $\operatorname{SL}(n, \mathbb{R})$ . 考虑 $F: \operatorname{GL}(n, \mathbb{R}) \to (\mathbb{R}^{+}, \times)$ , 定义为 $A \to F(A) = \det(A)$ . 显然 $F$ 是一个 Lie 群同态.

对任一 $\pmb{A} = [a_{ij}] \in \mathrm{GL}(n, \mathbb{R})$ ，记 $A^{ij}$ 为 $a_{ij}$ 的余子式。因为

$$F (A) = \sum_ {k = 1} ^ {n} (- 1) ^ {k - 1} a _ {1 k} \det (A ^ {1 k}) \neq 0,$$

故至少有一个 $k$ , 使得 $\operatorname{det}(A^{1k}) \neq 0$ . 因此

$$\frac {\partial F}{\partial a _ {1 k}} = (- 1) ^ {k - 1} \det (A ^ {1 k}) \neq 0,$$

这说明 $\operatorname{rank}(F) = 1$ 。由定理3.9.2可知 $\operatorname{SL}(n, \mathbb{R}) = \ker(F)$ 是 $\operatorname{GL}(n, G)$ 的维数为 $n^2 - 1$ 的Lie子群。
