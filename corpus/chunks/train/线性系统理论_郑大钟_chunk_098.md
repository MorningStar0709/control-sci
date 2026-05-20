$$
\bar {x} _ {0} = - \int_ {0} ^ {t _ {1}} e ^ {- A t} B u (t) d t \tag {3.15}
\begin{array}{l} \left\| \boldsymbol {x} _ {0} \right\| ^ {2} = \bar {\boldsymbol {x}} _ {0} ^ {T} \bar {\boldsymbol {x}} _ {0} = \left[ - \int_ {0} ^ {t _ {1}} e ^ {- A t} B \boldsymbol {u} (t) d t \right] ^ {T} \bar {\boldsymbol {x}} _ {0} \\ = - \int_ {0} ^ {t _ {1}} u ^ {T} (t) B ^ {T} e ^ {- A ^ {T} t} \bar {x} _ {0} d t \tag {3.16} \\ \end{array}
$$

再利用(3.13)，则由(3.16)可得到

$$\| \boldsymbol {x} _ {0} \| ^ {2} = 0 \text {即} \bar {\boldsymbol {x}} _ {0} = \mathbf {0} \tag {3.17}$$

这表明， $\bar{x}_0 \neq 0$ 的假设是和已知系统完全能控相矛盾。因此，反设不成立，即 $W_c[0, t_1]$ 为非奇异。必要性得证。至此，证明完成。

不难看出,为了应用格拉姆矩阵判据,必须先计算矩阵指数函数 $e^{At}$ ,而这在 A 的维数 n 较大时并非易事。所以,这一判据主要用于理论分析中。下面利用其来导出如下的直接由 A 和 B 判断能控性的秩判据。

结论2 [秩判据] 线性定常系统（3.7）为完全能控的充分必要条件是

$$\operatorname{rank} [ B \mid A B \mid \dots \mid A ^ {n - 1} B ] = n \tag {3.18}$$

其中，n 为矩阵 A 的维数， $Q_{c} \triangleq [B \mid AB \mid \cdots \mid A^{n-1}B]$ 称为系统的能控性判别阵。

证 充分性：已知 $\operatorname{rank} Q_c = n$ ，欲证系统为完全能控。

采用反证法。反设系统为不完全能控，则据格拉姆矩阵判据知，如下的格拉姆矩阵

$$W _ {c} [ 0, t _ {1} ] = \int_ {0} ^ {t _ {1}} e ^ {- A t} B B ^ {T} e ^ {- A ^ {T} t} d t, \forall t _ {1} > 0 \tag {3.19}$$

为奇异,而这又意味着存在某个非零 n 维常向量 a 使成立

$$
\begin{array}{l} 0 = \boldsymbol {\alpha} ^ {T} W [ 0, t _ {1} ] \boldsymbol {\alpha} = \int_ {0} ^ {t _ {1}} \boldsymbol {\alpha} ^ {T} e ^ {- A t} B B ^ {T} e ^ {- A ^ {T} t} \boldsymbol {\alpha} d t \\ = \int_ {0} ^ {t _ {1}} \left[ \alpha^ {T} e ^ {- A t} B \right] \left[ \alpha^ {T} e ^ {- A t} B \right] ^ {T} d t \tag {3.20} \\ \end{array}
$$

显然，由此可以导出

$$\boldsymbol {a} ^ {T} e ^ {- A t} B = 0, \quad \forall t \in [ 0, t _ {1} ] \tag {3.21}$$

现将上式求导直至 $(n - 1)$ 次，再在所得结果中令 $t = 0$ ，那么又可得到

$$\boldsymbol {a} ^ {T} B = 0, \boldsymbol {a} ^ {T} A B = 0, \boldsymbol {a} ^ {T} A ^ {2} B = 0, \dots , \boldsymbol {a} ^ {T} A ^ {n - 1} B = 0 \tag {3.22}$$

进而，表上式为

$$\boldsymbol {a} ^ {T} [ B \mid A B \mid A ^ {2} B \mid \dots \mid A ^ {n - 1} B ] = \boldsymbol {a} ^ {T} Q _ {\bullet} = 0 \tag {3.23}$$

由于 $\alpha \neq 0$ ，所以上式意味着 $Q_{\epsilon}$ 为行线性相关，也即有 $\operatorname{rank} Q_{\epsilon} < n$ 。但这显然和已知 $\operatorname{rank} Q_{\epsilon} = n$ 相矛盾。所以，反设不成立，系统为完全能控。充分性得证。

必要性：已知系统完全能控，欲证 $\operatorname{rank} Q_{\varepsilon} = n_{0}$

采用反证法。反设 $\operatorname{rank} Q_{\bullet} < n$ ，这意味着 $Q_{\bullet}$ 为行线性相关，因此必存在一个非零 $n$ 维常向量 $\pmb{\alpha}$ 使成立

$$\alpha^ {T} Q _ {c} = \alpha^ {T} [ B | A B | \dots | A ^ {n - 1} B ] = 0 \tag {3.24}$$

考虑到问题的一般性，由上式成立又可导出

$$\alpha^ {T} A ^ {i} B = 0, \quad i = 0, 1, \dots , n - 1 \tag {3.25}$$
