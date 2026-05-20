$$
F \triangleq \left[ \begin{array}{c} \boldsymbol {c} _ {1} A ^ {d _ {1} + 1} \\ \vdots \\ \boldsymbol {c} _ {p} A ^ {d} p ^ {+ 1} \end{array} \right] \tag {5.105}
$$

相应地，可导出闭环系统的传递函数矩阵为：

$$G _ {K L} (s) = C \left(s I - A + B E ^ {- 1} F\right) ^ {- 1} B E ^ {- 1} \tag {5.106}$$

再利用(5.92)，可将其第 $i$ 个行传递函数向量表示为：

$$\boldsymbol {g} _ {K L i} (s) = \frac {1}{\bar {\sigma} (s)} \left[ \boldsymbol {c} _ {i} B s ^ {n - 1} + \boldsymbol {c} _ {i} \bar {R} _ {n - 2} B s ^ {n - 2} + \dots + \boldsymbol {c} _ {i} \bar {R} _ {1} B s + \boldsymbol {c} _ {i} \bar {R} _ {0} B \right] L \tag {5.107}$$

进而，注意到 $\vec{d}_i = d_i$ ，且由特征量 $\vec{d}_i$ 的定义，可知上式中有：

$$\boldsymbol {c} _ {i} B L = 0, \boldsymbol {c} _ {i} \bar {R} _ {n - 2} B L = 0, \dots , \boldsymbol {c} _ {i} \bar {R} _ {n - d _ {i}} B L = 0 \tag {5.108}$$

或等价地有

$$\mathbf {c} _ {i} B L = \mathbf {0}, \mathbf {c} _ {i} (A - B K) B L = \mathbf {0}, \dots , \mathbf {c} _ {i} (A - B K) ^ {d _ {i} - 1} B L = \mathbf {0} \tag {5.109}$$

利用(5.109)和(5.94)，则还可定出(5.107)中剩下的其他各项为：

$$
\begin{array}{l} \mathbf {c} _ {i} \bar {R} _ {n - d _ {i} - 1} B L = \mathbf {c} _ {i} (A - B K) ^ {d _ {i}} B L + \bar {\alpha} _ {n - 1} \mathbf {c} _ {i} (A - B K) ^ {d _ {i} - 1} B L + \dots + \bar {\alpha} _ {n - d _ {i}} \mathbf {c} _ {i} B L \\ = c _ {i} (A - B K) ^ {d _ {i}} B L = \bar {E} _ {i} = E _ {i} L \\ \end{array}
\mathbf {c} _ {i} \bar {R} _ {n - d _ {i} - 2} B L = \mathbf {c} _ {i} (A - B K) ^ {d _ {i} + 1} B L + \bar {\alpha} _ {n - 1} \mathbf {c} _ {i} (A - B K) ^ {d _ {i}} B L+ \dots + \bar {a} _ {n - d _ {i} - 1} c _ {i} B L= \mathbf {c} _ {i} (A - B K) ^ {d _ {i} + 1} B L + \bar {\alpha} _ {n - 1} \mathbf {c} _ {i} (A - B K) ^ {d _ {i}} B L= \left[ c _ {i} A ^ {d _ {i}} (A - B K) \right] B L + \bar {a} _ {n - 1} E _ {i} L= \left[ c _ {i} A ^ {d _ {i} + 1} - c _ {i} A ^ {d _ {i}} B K \right] B L + \bar {\alpha} _ {n - 1} E _ {i} L= \left[ F _ {i} - E _ {i} E ^ {- 1} F \right] B L + a _ {n - 1} E _ {i} L= \left[ F _ {i} - (0 \dots 0, 1, 0 \dots 0) E E ^ {- 1} F \right] B L + a _ {n - 1} E _ {i} L= \left[ F _ {i} - F _ {i} \right] B L + \bar {\alpha} _ {n - 1} E _ {i} L= \bar {a} _ {n - 1} E _ {i} L\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet\boldsymbol {c} _ {i} \bar {R} _ {0} B L = \partial_ {d _ {i + 1}} E _ {i} L \tag {5.110}
$$

于是，将（5.108）和（5.110）代入（5.107），进一步得到：

$$\boldsymbol {g} _ {K L i} (s) = \frac {1}{\bar {\alpha} (s)} \left[ s ^ {n - d _ {i} - 1} + \bar {\alpha} _ {n - 1} s ^ {n - d _ {i} - 2} + \dots + \bar {\alpha} _ {d _ {i} + 1} \right] E _ {i} L \tag {5.111}$$

另一方面，根据凯莱-哈密顿定理，有

$$(A - B K) ^ {n} + \bar {a} _ {n - 1} (A - B K) ^ {n - 1} + \dots + \bar {a} _ {1} (A - B K) + \bar {a} _ {0} I = 0 \tag {5.112}$$

现将(5.112)等式两边乘以 $\mathbf{c}_i(A - BK)^{d_i}$ ，那么由于
