$$
\begin{array}{r l} \widetilde {A} & = \left[ \begin{array}{c c c c c c c c} \lambda_ {1} & 1 & & & & \\ & \ddots & \ddots & 1 & & \\ & & \ddots & \ddots & & \\ & & & \lambda_ {1} & & \\ & & & & \ddots & \\ & & & & & \ddots \\ & & & & & \mu_ {1} \\ & & & & & \mu_ {p} \\ \tilde {c} & = [ f _ {1 \mu_ {1}} \dots f _ {1 1} ] \dots i f _ {p \mu_ {2}} \dots f _ {p 1} ] \\ \end{array} \right] \left\{ \begin{array}{l} \mu_ {1} \\ , \\ \tilde {b} = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \\ - \\ \vdots \\ \vdots \\ - \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \end{array} \right\} \mu_ {1} \\ & = \left[ \begin{array}{c} \mu_ {p} \\ \mu_ {p} \\ \mu_ {p} \end{array} \right] \end{array}
$$

其中 $\lambda_{i}(i=1,2,\cdots,p)$ 可以是实数或共轭复数。

证 将 $(\tilde{A}, \tilde{b}, \tilde{c})$ 改写为

$$
\tilde {A} = \left[ \begin{array}{c c c} A _ {1} & & \\ & \ddots & \\ & & A _ {p} \end{array} \right], \tilde {b} = \left[ \begin{array}{c} b _ {1} \\ \vdots \\ b _ {p} \end{array} \right], \tilde {c} = [ c _ {1}, \dots , c _ {p} ] \tag {9.64}
$$

其中

$$
A _ {i} = \left[ \begin{array}{c c c c} \lambda_ {i} & 1 & & \\ & \ddots & \ddots & \\ & & \ddots & 1 \\ & & & \lambda_ {i} \end{array} \right], \quad b _ {i} = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right], \quad c _ {i} = [ f _ {i, p _ {i}}, \dots , f _ {i i} ] \tag {9.65}
$$

于是，由(9.64)即可导出

$$
\begin{array}{l} \tilde {c} (s I - \widetilde {A}) ^ {- 1} \tilde {b} = [ c _ {1}, \dots , c _ {p} ] \left[ \begin{array}{c c c} (s I - A _ {1}) ^ {- 1} & & \\ & \ddots & \\ & & (s I - A _ {p}) ^ {- 1} \end{array} \right] \left[ \begin{array}{c} b _ {1} \\ \vdots \\ b _ {p} \end{array} \right] \\ = \sum_ {i = 1} ^ {p} c _ {i} (s I - A _ {i}) ^ {- 1} b _ {i} \tag {9.66} \\ \end{array}
$$

而由(9.65)，则可导出
