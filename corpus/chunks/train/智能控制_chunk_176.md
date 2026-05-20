# 5. 模糊决策

模糊控制器的输出为误差向量和模糊关系的合成,即

$$\pmb {u} = \pmb {e} \circ \pmb {R}$$

当误差 e 为 NB 时, e = [1.0 0.5 0 0 0 0 0 0], 控制器输出为

$$
\begin{array}{r l} \boldsymbol {u} & = \boldsymbol {e} \circ \boldsymbol {R} = [ 1 \quad 0. 5 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 ] \circ \left[ \begin{array}{c c c c c c c c c} 1. 0 & 0. 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0. 5 & 0. 5 & 0. 5 & 0. 5 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0. 5 & 1. 0 & 0. 5 & 0. 5 & 0. 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0. 5 & 1. 0 & 0. 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0. 5 & 0. 5 & 0. 5 & 1. 0 & 0. 5 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0. 5 & 0. 5 & 0. 5 & 0. 5 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0. 5 & 1. 0 \end{array} \right] \\ & = [ 1 \quad 0. 5 \quad 0. 5 \quad 0. 5 \quad 0 \quad 0 \quad 0 \quad 0 \quad 0 ] \end{array}
$$
