对于三个矩阵 $\pmb{A} \in \mathbb{C}^{m \times n}, \pmb{B} \in \mathbb{C}^{n \times p}, \pmb{C} \in \mathbb{C}^{p \times q}$ , 有

$$V _ {r} (\boldsymbol {A B C}) = (\boldsymbol {A} \otimes \boldsymbol {C} ^ {\mathrm{T}}) V _ {r} (\boldsymbol {B}), \tag {1.1.4}V _ {c} (\boldsymbol {A B C}) = \left(\boldsymbol {C} ^ {\mathrm{T}} \otimes \boldsymbol {A}\right) V _ {c} (\boldsymbol {B}). \tag {1.1.5}$$

矩阵求逆公式 有时用分块矩阵求逆的方法求 $A^{-1}$ 是比较方便的。若 $\pmb{A}$ 是一个 $n_1 + n_2$ 阶分块三角形矩阵

$$
\pmb {A} = \left[ \begin{array}{c c} {\pmb {A} _ {1 1}} & {\pmb {A} _ {1 2}} \\ {0} & {\pmb {A} _ {2 2}} \end{array} \right] \quad \text {或} \quad \pmb {A} = \left[ \begin{array}{c c} {\pmb {A} _ {1 1}} & {0} \\ {\pmb {A} _ {2 1}} & {\pmb {A} _ {2 2}} \end{array} \right],
$$

其中 $A_{11} \in \mathbb{C}^{n_1 \times n_1}, A_{22} \in \mathbb{C}^{n_2 \times n_2}$ .

当 $A_{11}^{-1}, A_{22}^{-1}$ 存在时，有

$$
\pmb {A} ^ {- 1} = \left[ \begin{array}{c c} {\pmb {A} _ {1 1} ^ {- 1}} & {- \pmb {A} _ {1 1} ^ {- 1} \pmb {A} _ {1 2} \pmb {A} _ {2 2} ^ {- 1}} \\ {0} & {\pmb {A} _ {2 2} ^ {- 1}} \end{array} \right], \quad \text {或} \quad \pmb {A} ^ {- 1} = \left[ \begin{array}{c c} {\pmb {A} _ {1 1} ^ {- 1}} & {0} \\ {- \pmb {A} _ {2 2} ^ {- 1} \pmb {A} _ {2 1} \pmb {A} _ {1 1} ^ {- 1}} & {\pmb {A} _ {2 2} ^ {- 1}} \end{array} \right].
$$

容易验证 $AA^{-1}=A^{-1}A=I.$

当 $\pmb{A}$ 不是分块三角形矩阵 $A = \left[ \begin{array}{ll}A_{11} & A_{12}\\ A_{21} & A_{22} \end{array} \right]$ ，且 $A_{11}^{-1},A_{22}^{-1}$ 存在时，容易验证

$$
\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c} \boldsymbol {I} _ {n _ {1}} & 0 \\ \boldsymbol {A} _ {2 1} \boldsymbol {A} _ {1 1} ^ {- 1} & \boldsymbol {I} _ {n _ {2}} \end{array} \right] \left[ \begin{array}{c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} \\ 0 & \boldsymbol {A} _ {2 2} ^ {- 1} - \boldsymbol {A} _ {2 1} \boldsymbol {A} _ {1 1} ^ {- 1} \boldsymbol {A} _ {1 2} \end{array} \right] \\ = \left[ \begin{array}{c c} I _ {n _ {1}} & A _ {1 2} A _ {2 2} ^ {- 1} \\ 0 & I _ {n _ {2}} \end{array} \right] \left[ \begin{array}{c c} A _ {1 1} - A _ {1 2} A _ {2 2} ^ {- 1} A _ {2 1} & 0 \\ A _ {2 1} & A _ {2 2} ^ {- 1} \end{array} \right]. \\ \end{array}
$$

利用分块三角形矩阵求逆公式可得
