为使证明简单，不妨假设 $\pmb{A}$ 是循环矩阵，否则由引理1.6.1知，存在矩阵 $\pmb{H}$ ，使得 $A + BHC$ 是循环的，同时保持系统的能控性和能观测性不变。

由于 $(A, B)$ 完全能控，并且 $A$ 是循环矩阵，因此必有向量 $b \in \operatorname{Image}(B)$ ，使得 $b$ 是 $A$ 的生成元，从而有 $(A, b)$ 完全能控 [1.15].

任取 $(\nu_0 - 1) \times (\nu_0 - 1)$ 循环矩阵 $E$ , 以及向量 $g, h \in \mathbb{R}^{\nu_0 - 1}$ , 使得

$$\boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {g} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {E} \boldsymbol {g} = \dots = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {E} ^ {\nu_ {0} - 3} \boldsymbol {g} = 0, \quad \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {E} ^ {\nu_ {0} - 2} \boldsymbol {g} = 1.$$

容易检验，矩阵对

$$
\left(\left[ \begin{array}{c c} \boldsymbol {A} & \boldsymbol {b h} ^ {\mathrm{T}} \\ 0 & \boldsymbol {E} \end{array} \right], \left[ \begin{array}{c} 0 \\ \boldsymbol {g} \end{array} \right]\right)
$$

是完全能控的．根据定理1.6.1，必存在向量 $\pmb{a}\in \mathbb{R}^n$ 和 $\pmb {v}\in \mathbb{R}^{\nu_0 - 1}$ ，使得

$$
\sigma \left(\left[ \begin{array}{c c} A & b h ^ {T} \\ g a ^ {T} & E + g v ^ {T} \end{array} \right]\right) = \Lambda .
$$

因为 $b \in \operatorname{Image}(B)$ , 所以存在向量 $z$ , 使得 $b = Bz$ . 令 $F_c = zh^T$ , 这里 $F_c$ 为 $r \times (\nu_0 - 1)$ 矩阵. 于是 $bh^T = BF_c$ .

为了寻找所要求的矩阵，只需求 $(\nu_0 - 1) \times m$ 矩阵 $B_{c}, (\nu_0 - 1) \times (\nu_0 - 1)$ 矩阵 $A_{c}$ 和向量 $a \in \operatorname{Image}(C^{\mathrm{T}})$ ，使得矩阵

$$
\left[ \begin{array}{c c} {{A}} & {{b h ^ {\mathrm{T}}}} \\ {{g a ^ {\mathrm{T}}}} & {{E + g v ^ {\mathrm{T}}}} \end{array} \right] \text {与} \left[ \begin{array}{c c} {{A + b d ^ {\mathrm{T}}}} & {{b h ^ {\mathrm{T}}}} \\ {{B _ {c} C}} & {{A _ {c}}} \end{array} \right]
$$

相似．如果有 $(\nu_0 - 1) \times n$ 矩阵 $\pmb{R}$ ，使得

$$
\left[ \begin{array}{c c} {\boldsymbol {A}} & {\boldsymbol {b h ^ {\mathrm{T}}}} \\ {\boldsymbol {g a ^ {\mathrm{T}}}} & {\boldsymbol {E + g v ^ {\mathrm{T}}}} \end{array} \right] \left[ \begin{array}{c c} {\boldsymbol {I _ {n}}} & 0 \\ {\boldsymbol {R}} & {\boldsymbol {I _ {\nu_ {0} - 1}}} \end{array} \right] = \left[ \begin{array}{c c} {\boldsymbol {I _ {n}}} & 0 \\ {\boldsymbol {R}} & {\boldsymbol {I _ {\nu_ {0} - 1}}} \end{array} \right] \left[ \begin{array}{c c} {\boldsymbol {A + b d ^ {\mathrm{T}}}} & {\boldsymbol {b h ^ {\mathrm{T}}}} \\ {\boldsymbol {B _ {c} C}} & {\boldsymbol {A _ {c}}} \end{array} \right],
$$

那么问题也就解决了．而上述等式成立的一个充分条件是
