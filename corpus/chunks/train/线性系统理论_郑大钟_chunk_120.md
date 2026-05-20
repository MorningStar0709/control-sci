$$
\begin{array}{l} P A _ {c} = A P = \left[ A e _ {1}, A e _ {2}, \dots , A e _ {n} \right] \\ = \left[ A ^ {n} \boldsymbol {b}, \dots , A ^ {1} \boldsymbol {b}, A \boldsymbol {b} \right] \left[ \begin{array}{c c c c c} 1 & & & & \\ & \ddots & & & \\ \alpha_ {n - 1} & & \ddots & & \\ \vdots & \ddots & & \ddots & \\ \alpha_ {1} & \dots & \alpha_ {n - 1} & 1 \end{array} \right] \tag {3.165} \\ \end{array}
$$

由此，并利用凯莱-哈密顿定理 $\alpha(A) = 0$ 和(3.162)，进一步得到

$$
\begin{array}{l} A e _ {1} = \left(A ^ {n} b + \alpha_ {n - 1} A ^ {n - 1} b + \dots + \alpha_ {1} A b + \alpha_ {0} b\right) - \alpha_ {0} b = - \alpha_ {0} e _ {s} \\ A e _ {2} = \left(A ^ {n - 1} b + \alpha_ {n - 1} A ^ {n - 2} b + \dots + \alpha_ {2} A b + \alpha_ {1} b\right) - \alpha_ {1} b = e _ {1} - \alpha_ {1} e _ {2} \\ \dots \tag {3.166} \\ \end{array}
A e _ {n - 1} = \left(A ^ {2} b + \alpha_ {n - 1} A b + \alpha_ {n - 2} b\right) - \alpha_ {n - 2} b = e _ {n - 2} - \alpha_ {n - 2} e _ {n}A e _ {s} = (A b + \alpha_ {s - 1} b) - \alpha_ {s - 1} b = e _ {s - 1} - \alpha_ {s - 1} e _ {s}
$$

于是，将(3.166)代入(3.165)，可有

$$
\begin{array}{l} P A _ {c} = \left[ - \alpha_ {0} e _ {n}, e _ {1} - \alpha_ {1} e _ {n}, \dots , e _ {n - 2} - \alpha_ {n - 2} e _ {n}, e _ {n - 1} - \alpha_ {n - 1} e _ {n} \right] \\ = \left[ e _ {1}, e _ {2}, \dots , e _ {s} \right] \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \ddots & & \\ \vdots & & & & \\ 0 & & & 1 & \\ - \alpha_ {0} & - \alpha_ {1} & \dots & - \alpha_ {s - 1} \end{array} \right] \tag {3.167} \\ \end{array}
$$

考虑到 $[e_1, e_2, \cdots, e_n] = P$ ，所以将上式左乘 $P^{-1}$ ，即导出了 $A_c$ 的表达式。

(ii) 推导 $b_{c}$ : 利用 $b_{c}=P^{-1}b$ 和 (3.162)，可导出

$$
P b _ {c} = b = e _ {n} = \left[ e _ {1}, e _ {2}, \dots , e _ {n} \right] \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] = P \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \tag {3.168}
$$

将上式左乘 $P^{-1}$ ，就得到 $\pmb{b}_c$ 的表达式。

(iii) 推导 $c_{c}$ : 利用 $c_{c}=cP$ 和 (3.162)，并注意到关系式 (3.161)，即得

$$
\begin{array}{l} \mathbf {c} _ {c} = \mathbf {c} P = \mathbf {c} [ A ^ {s - 1} \boldsymbol {b}, \dots , A \boldsymbol {b}, \boldsymbol {b} ] \left[ \begin{array}{c c c c c} 1 & & & & \\ & \ddots & & & \\ \alpha_ {s - 1} & & \ddots & & \\ \vdots & \ddots & & \ddots & \\ \alpha_ {1} & \dots \alpha_ {s - 1} & & 1 \end{array} \right] \\ = \left[ \beta_ {0}, \beta_ {1}, \dots , \beta_ {n - 1} \right] \tag {3.169} \\ \end{array}
$$

至此，就完成了证明。

例 给定能控的单输入-单输出线性定常系统为:
