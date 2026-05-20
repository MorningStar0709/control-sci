再考虑到初等运算不影响史密斯意义下的等价性,所以进一步又可导出

$$
\left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ 0 & I \end{array} \right] \sim \left[ \begin{array}{c c} s I - A _ {c} & 0 \\ 0 & I \end{array} \right] \tag {9.136}

\left[ \begin{array}{c c} I & 0 \\ Y (s) & D (s) \end{array} \right] \stackrel {{\mathrm{s}}} {{\sim}} \left[ \begin{array}{c c} I & 0 \\ 0 & D (s) \end{array} \right] \tag {9.137}
$$

再由等价变换的传递性,所以由(9.135)—(9.137)就可得到

$$
\left[ \begin{array}{c c} s I - A _ {e} & \mathbf {0} \\ \mathbf {0} & I \end{array} \right] \stackrel {{s}} {{\sim}} \left[ \begin{array}{c c} I & \mathbf {0} \\ \mathbf {0} & D (s) \end{array} \right] \tag {9.138}
$$

这意味着,这两个多项式矩阵具有等同的不变多项式,也即成立

$$\det (s I - A _ {c}) \propto \det D (s) \tag {9.139}$$

其中， $\operatorname{det}(sI - A_c)$ 为首1多项式，而

$$\det D (s) = \left(\det D _ {b c}\right) s ^ {a} + L (s) \tag {9.140}$$

式中 $n = \sum_{i=1}^{p} k_i, L(s)$ 为次数小于 $n$ 的一个多项式。显然，由(9.140)可导出 $\operatorname{det} D(s)$ 的首1多项式为

$$\left(\det D _ {k c}\right) ^ {- 1} \det D (s) = s ^ {n} + \left(\det D _ {k c}\right) ^ {- 1} L (s) \tag {9.141}$$

于是,考虑到式(9.139)意味着两者具有相同的首1多项式,就可由(9.139)和(9.141)证得(9.123)。而(9.124)是(9.123)的直接推论。从而,就完成了证明。

性质 4 右 MFD 和其控制器形实现之间有着如下的关系式:

$$
\left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ - C _ {c} & 0 \end{array} \right] \stackrel {{s}} {{\sim}} \left[ \begin{array}{c c} I _ {n} & 0 \\ 0 & N (s) \end{array} \right] \tag {9.142}
$$

并且， $(A_{c}, B_{c}, C_{c})$ 为联合能控和能观测的一个充分条件是对所有 $s \in \mathcal{C} N(s)$ 为列满秩。

证（1）先证(9.142)。作如下的单模变换：

$$
\begin{array}{l} \left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ - C _ {c} & 0 \end{array} \right] \left[ \begin{array}{c c} X (s) & - \Psi (s) \\ Y (s) & D (s) \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ - C _ {c} X (s) & C _ {c} \Psi (s) \end{array} \right] \\ = \left[ \begin{array}{c c} I & 0 \\ - C _ {c} X (s) & N _ {l c} \Psi (s) \end{array} \right] \\ - \left[ \begin{array}{c c} I & 0 \\ - C _ {c} X (s) & N (s) \end{array} \right] \tag {9.143} \\ \end{array}
$$

于是，可得到

$$
\left[ \begin{array}{c c} s I - A _ {e} & B _ {e} \\ - C _ {e} & 0 \end{array} \right] \stackrel {{s}} {{\sim}} \left[ \begin{array}{c c} I & 0 \\ - C _ {e} X (s) & N (s) \end{array} \right] \tag {9.144}
$$

再对上式右边的多项式矩阵作初等运算,可进一步导出

$$
\left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ - C _ {c} & 0 \end{array} \right] \sim \left[ \begin{array}{c c} I & 0 \\ 0 & N (s) \end{array} \right] \tag {9.145}
$$

从而，就证得式(9.142)。

(2) 由(9.142)可知, 当按假定对所有 $s \in \mathcal{C} N(s)$ 为列满秩时, 必对所有 $s \in \mathcal{C}$
