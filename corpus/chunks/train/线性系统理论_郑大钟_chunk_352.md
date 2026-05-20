$$A _ {c} = A _ {c} ^ {o} - B _ {c} ^ {o} D _ {h c} ^ {- 1} D _ {l c}, \quad B _ {c} = B _ {c} ^ {o} D _ {h c} ^ {- 1}, \quad C _ {c} = \bar {N} _ {l c} \tag {9.195}$$

这里， $D_{bc}$ 和 $D_{lc}$ 为 $D_{L}(s)$ 的列次系数矩阵和低次系数矩阵， $\overline{N}_{lc}$ 为 $I_q$ 的系数矩阵，而核实现 $(A_c^o, B_c^o, C_c^o)$ 如(9.112)所示。并且， $(A_c, B_c, C_c)$ 具有如下的形式

$$
A _ {c} = \underbrace {\left[ \begin{array}{c c c c c c c c c} * & \cdots & * & * & \cdots & * \\ 1 & 0 & & & & & & & \\ & \ddots & \ddots & & & 0 & & & \\ & & 1 & 0 & & & & & \\ \hline * & \cdots & * & & \ddots & & & & \\ & 0 & & & \ddots & & & & \\ \hline & & & & & \ddots & & \\ & \vdots & & & & & \vdots \\ & \vdots & \ddots & & & & 1 & 0 \\ \hline k _ {1} \end{array} \right]} _ {k _ {1}} \underbrace {\left[ \begin{array}{c c c c c c c c c} * & \cdots & * \\ 1 & 0 \\ & \ddots & \ddots \\ & & 1 & 0 \\ \hline k _ {q} \end{array} \right]} _ {k _ {q}} B _ {c} = \underbrace {\left[ \begin{array}{c} * \cdots * \\ 0 \\ \hline \vdots \\ \hline * \cdots * \\ 0 \\ q \end{array} \right]} _ {k _ {q}}

C _ {c} = \left[ \begin{array}{l l l l} 0 & \dots & 0 & 1 \\ \hline & & & \\ & & \ddots & \\ & & & k _ {1} \\ \hline & & & k _ {q} \end{array} \right] \tag {9.196}
$$

② $A_{ob}$ 和 $C_{ob}$ 具有如下的形式:

$$
A _ {o b} = \underbrace {\left[ \begin{array}{c c c c c c c c c} 0 & 1 & & & & & & & \\ & \ddots & \ddots & & & & & & \\ & & 0 & 1 & & 0 & & & \\ * & \cdots & * & * & \cdots & * & & & \\ \hline & & & & & & & & \\ & 0 & & & \ddots & & & \\ * & \cdots & * & & & & & & \\ \hline & & & & \ddots & & & \\ \vdots & & & & \boxed {0} & 1 \\ \vdots & & & & \ddots & \ddots \\ * & \cdots & * \end{array} \right] \Bigg \}} _ {k _ {1}} C _ {o b} = \underbrace {\left[ \begin{array}{c c c c} 1 & 0 \cdots 0 \\ \hline & \ddots & \\ k _ {1} & \ddots & \\ 1 & 0 \cdots 0 \end{array} \right]} _ {k _ {q}} \tag {9.197}
$$

③ 把常数矩阵 $D_{bc}^{-1}D_{lc}$ 分块化，每个块阵的维数为 $1 \times k_{j}$ ，设第 $(i, j)$ 个分块阵为

$$\eta_ {i j} = [ \eta_ {i} ^ {(j)} \dots \dots \eta_ {k _ {j}} ^ {(i j)} ] \tag {9.198}$$

而将其元的排列顺序颠倒后的分块阵表为

$$\eta_ {i j} ^ {*} = \left[ \eta_ {k j} ^ {(i j)} \dots \dots \eta_ {1} ^ {(i j)} \right] \tag {9.199}$$

则 $A_{ob}$ 的第 $(i, j)$ 个分块阵中的\*行即等同于行一 $\eta_{ij0}^{*}$
