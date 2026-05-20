$$
A _ {c o} = \left[ \begin{array}{c c c c c c c c c} 0 & & & * & & * \\ 1 & & 0 & \vdots & 0 & \vdots \\ & & 1 & * & & * \\ \hline & & & & & \\ \hline & & & * & & \\ & 0 & & \ddots & & \\ & & & * & & \\ \hline & & & & & \\ \hline & \vdots & & & & \boxed {0} \\ & \vdots & & & & 1 \\ & \vdots & & & & 1 \\ \hline l _ {1} \end{array} \right] \left\{ \begin{array}{l} l _ {1} \\ , B _ {c o} = \left[ \begin{array}{c c c} 1 & & \\ 0 & & \\ \vdots & & \\ 0 & & \\ - - - \ddots & \\ & 1 \\ & 0 \\ & \vdots \\ & 0 \end{array} \right] \end{array} \right\} l _ {p} \tag {9.176}
$$

② 把常数矩阵 $D_{lr}D_{hr}^{-1}$ 分块化，每个块阵的维数为 $l_{i} \times 1$ ，设第 $(i, j)$ 个分块阵为

$$
\beta_ {i j} = \left[ \begin{array}{c} \beta_ {1} ^ {(i j)} \\ \vdots \\ \beta_ {l i} ^ {(i j)} \end{array} \right] \tag {9.177}
$$

而将其元的排列顺序颠倒后的分块阵表为

$$
\boldsymbol {\beta} _ {i j} ^ {*} = \left[ \begin{array}{c} \beta_ {i i} ^ {(i j)} \\ \vdots \\ \beta_ {1} ^ {(i j)} \end{array} \right] \tag {9.178}
$$

则 $A_{co}$ 的第 $(i, j)$ 个分块阵中的\*列即等同于列一 $\beta_{ij0}^{*}$

证（1）先来证明(9.175)。为此，根据(9.166)和(9.173)，有

$$
\begin{array}{l} [ \boldsymbol {b} _ {1} A _ {c o} \boldsymbol {b} _ {1} \dots A _ {c o} ^ {l _ {1} - 1} \boldsymbol {b} _ {1} | \dots | \boldsymbol {b} _ {p} A _ {c o} \boldsymbol {b} _ {p} \dots A _ {c o} ^ {l _ {p} - 1} \boldsymbol {b} _ {p} ] = I _ {n} = \tilde {I} _ {n} \tilde {I} _ {n} \\ = \tilde {I} _ {n} [ \bar {b} _ {1} A _ {o} \bar {b} _ {1} \dots A _ {o} ^ {i _ {1} - 1} \bar {b} _ {1} | \dots | \bar {b} _ {p} A _ {o} \bar {b} _ {p} \dots A _ {\sigma} ^ {i _ {p} - 1} b _ {p} ] \\ = \left[ \tilde {I} _ {n} \tilde {b} _ {1} \tilde {I} _ {n} A _ {o} \tilde {I} _ {n} \tilde {I} _ {n} \tilde {b} _ {1} \dots \tilde {I} _ {n} A _ {o} ^ {i _ {1} - 1} \tilde {I} _ {n} \tilde {I} _ {n} \tilde {b} _ {1} \right| \dots \\ \left[ \tilde {I} _ {n} \bar {b} _ {p} \tilde {I} _ {n} A _ {o} \tilde {I} _ {n} \tilde {I} _ {n} \bar {b} _ {p} \dots \tilde {I} _ {n} A _ {p} ^ {\prime - 1} \tilde {I} _ {n} \tilde {I} _ {n} \bar {b} _ {p} \right] \tag {9.179} \\ \end{array}
$$

于是，由此即可定出

$$\pmb {b} _ {i} = \tilde {I} _ {n} \bar {\pmb {b}} _ {i} \text {即} B _ {c o} = \tilde {I} _ {n} B _ {o} \tag {9.180}A _ {c o} = \tilde {I} _ {s} A _ {o} \tilde {I} _ {s} \tag {9.181}$$

再据 $\hat{\mathbf{y}}(s)=N(s)\bar{\mathbf{y}}(s)$ ，可导出

$$
\begin{array}{l} C _ {c o} (s I - A _ {c o}) ^ {- 1} B _ {c o} = N (s) D ^ {- 1} (s) = N (s) C _ {o} (s I - A _ {o}) ^ {- 1} B _ {o} \\ = N (s) C _ {o} \tilde {I} _ {n} \tilde {I} _ {n} (s I - A _ {o}) ^ {- 1} \tilde {I} _ {n} \tilde {I} _ {n} B _ {o} \\ = N (s) C _ {o} \tilde {I} _ {n} (s I - A _ {c o}) ^ {- 1} B _ {c o} = \bar {N} (s) (s I - A _ {c o}) ^ {- 1} B _ {c o} \tag {9.182} \\ \end{array}
$$
