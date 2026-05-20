现在假设 $G(s)$ 是正实赫尔维茨矩阵，回顾 $\{A, B, C, D\}$ 是 $G(s)$ 的最小实现，根据引理C.5，存在一个 $r \times p$ 传递函数矩阵 $V(s)$ ，满足式(C.39)。设 $\{F, G, H, J\}$ 是 $V(s)$ 的最小实现，因为 $V(s)$ 是赫尔维茨矩阵，故矩阵 $F$ 是赫尔维茨的。容易看出， $\{-F^{\mathrm{T}}, H^{\mathrm{T}}, -G^{\mathrm{T}}, J^{\mathrm{T}}\}$ 是 $V^{\mathrm{T}}(-s)$ 的最小实现，因此

$$
\left\{\mathcal {A} _ {1}, \mathcal {B} _ {1}, \mathcal {C} _ {1}, \mathcal {D} _ {1} \right\} = \left\{\left[ \begin{array}{c c} F & 0 \\ H ^ {\mathrm{T}} H & - F ^ {\mathrm{T}} \end{array} \right], \left[ \begin{array}{c} G \\ H ^ {\mathrm{T}} J \end{array} \right], \left[ \begin{array}{c c} J ^ {\mathrm{T}} H & - G ^ {\mathrm{T}} \end{array} \right], J ^ {\mathrm{T}} J \right\}
$$

是级联的 $V^{\mathrm{T}}(-s)V(s)$ 的实现,通过检验可控性和可观测性,并利用当 $\mathrm{Re}[s]>0$ 时秩 $V(s)=r$ 的性质,可看出该实现是最小实现。下面说明可控性检测 $^{①}$ ,可观测性检测与之相似。由

$$
\begin{array}{l} \left[ \begin{array}{c c} I & 0 \\ H (s I - F) ^ {- 1} & I \end{array} \right] \left[ \begin{array}{c c} s I - F & G \\ - H & J \end{array} \right] = \left[ \begin{array}{c c} s I - F & G \\ 0 & H (s I - F) ^ {- 1} G + J \end{array} \right] \\ = \left[ \begin{array}{c c} s I - F & G \\ 0 & V (s) \end{array} \right] \\ \end{array}
$$

可看出 $\operatorname{rank} V(s) = r, \forall \operatorname{Re}[s] > 0 \Leftrightarrow \operatorname{rank}\left[ \begin{array}{cc} sI - F & G \\ -H & J \end{array} \right] = n_F + r, \forall \operatorname{Re}[s] > 0$

其中 $n_{F}$ 是 $F$ 的维数。下面通过反证法证明 $(\mathcal{A}_1,\mathcal{B}_1)$ 的可控性。假设 $(\mathcal{A}_1,\mathcal{B}_1)$ 是不可控的，则存在一个复数 $\lambda$ 和一个向量 $\omega \in C^{n_F + r}$ ，将其分为 $n_F$ 和 $r$ 子向量，使

$$(w _ {1} ^ {*}) ^ {\mathrm{T}} F + (w _ {2} ^ {*}) ^ {\mathrm{T}} H ^ {\mathrm{T}} H = \lambda (w _ {1} ^ {*}) ^ {\mathrm{T}} \tag {C.40}- (w _ {2} ^ {*}) ^ {\mathrm{T}} F ^ {\mathrm{T}} = \lambda (w _ {2} ^ {*}) ^ {\mathrm{T}} \tag {C.41}(w _ {1} ^ {*}) ^ {\mathrm{T}} G + (w _ {2} ^ {*}) ^ {\mathrm{T}} H ^ {\mathrm{T}} J = 0 \tag {C.42}$$

方程(C.41)说明 $\operatorname{Re}[\lambda] > 0$ ，因为 $F$ 是赫尔维茨的。方程(C.40)和方程(C.42)说明

$$
\left[ \begin{array}{l l} (w _ {1} ^ {*}) ^ {\mathrm{T}} & (w _ {2} ^ {*}) ^ {\mathrm{T}} H ^ {\mathrm{T}} \end{array} \right] \left[ \begin{array}{c c} \lambda I - F & G \\ - H & J \end{array} \right] = 0 \Rightarrow \operatorname{rank} V (\lambda) <   r
$$

这与当 $\operatorname{Re}[s]>0$ 时，秩 $V(s)=r$ 相矛盾，所以 $(\mathcal{A}_{1},\mathcal{B}_{1})$ 是可控的。

考虑李雅普诺夫方程

$$K F + F ^ {\mathrm{T}} K = - H ^ {\mathrm{T}} H$$

由于矩阵对 $(F,H)$ 是可观测的,则存在唯一的正定解K,该结果已在习题4.22中证明。利用相似变换
