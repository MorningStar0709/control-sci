$$\{A _ {2}, B _ {2} \} \text { 能控 } \Longleftrightarrow \{s I - A _ {2}, B _ {2} \} \text { 左互质 } \Longleftrightarrow \{s I - A _ {1}, B _ {1} \} \text { 左互质 }\Leftrightarrow \left\{A _ {1}, B _ {1} \right\} \text {能控} \tag {10.134}\{A _ {2}, C _ {2} \} \text {能观测} \Longleftrightarrow \{s I - A _ {2}, C _ {2} \} \text {右互质} \Longleftrightarrow \{s I - A _ {1}, C _ {1} \} \text {右互质}\Leftrightarrow \left\{A _ {1}, C _ {1} \right\} \text {能观测} \tag {10.135}$$

从而，证明了能控性和能观测性在严格系统等价变换下保持不变。至此，证明完成。

结论5 两个状态空间描述 $(A_{1}, B_{1}, C_{1}, E_{1}(p))$ 和 $(A_{2}, B_{2}, C_{2}, E_{2}(p))$ 是代数等价的，当且仅当它们的系统矩阵

$$
S _ {1} (s) = \left[ \begin{array}{c c} s I - A _ {1} & B _ {1} \\ - C _ {1} & E _ {1} (s) \end{array} \right] \text {和} S _ {2} (s) = \left[ \begin{array}{c c} s I - A _ {2} & B _ {2} \\ - C _ {2} & E _ {2} (s) \end{array} \right] \tag {10.136}
$$

是严格系统等价的。

证 必要性：已知代数等价，证明严格系统等价。

由 $(A_{1}, B_{1}, C_{1}, E_{1}(p))$ 和 $(A_{2}, B_{2}, C_{2}, E_{2}(p))$ 代数等价可知，必存在可逆常数矩阵 $T$ ，使成立

$$A _ {2} = T A _ {1} T ^ {- 1}, B _ {2} = T B _ {1}, C _ {2} = C _ {1} T ^ {- 1}, E _ {2} (p) = E _ {1} (p) \tag {10.137}$$

由此，即可导出

$$
\begin{array}{l} \left[ \begin{array}{c c} s I - A _ {2} & B _ {2} \\ - C _ {2} & E _ {2} (s) \end{array} \right] = \left[ \begin{array}{c c} s I - T A _ {1} T ^ {- 1} & T B _ {1} \\ - C _ {1} T ^ {- 1} & E _ {1} (s) \end{array} \right] \\ = \left[ \begin{array}{l l} T & 0 \\ 0 & I \end{array} \right] \left[ \begin{array}{c c} s I - A _ {1} & B _ {1} \\ - C _ {1} & E _ {1} (s) \end{array} \right] \left[ \begin{array}{l l} T ^ {- 1} & 0 \\ 0 & I \end{array} \right] \tag {10.138} \\ \end{array}
$$

注意到上式的最后等式右边的矩阵中，最左和最右的矩阵均为单模阵，所以根据定义即知， $S_{2}(s)$ 和 $S_{1}(s)$ 为严格系统等价。必要性得证。

充分性：已知严格系统等价，证明代数等价。

已知 $S_{2}(s)$ 严格等价于 $S_{1}(s)$ ，故由结论1知两者具有相同的传递函数矩阵，从而成立

$$E _ {2} (p) = E _ {1} (p) \tag {10.139}$$

再由(10.107)可导出

$$
\left[ \begin{array}{l l} U (s) & 0 \\ X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c} s I - A _ {1} & B _ {1} \\ - C _ {1} & E _ {1} (s) \end{array} \right] = \left[ \begin{array}{c c} s I - A _ {2} & B _ {2} \\ - C _ {2} & E _ {2} (s) \end{array} \right] \left[ \begin{array}{c c} \bar {V} (s) & \bar {Y} (s) \\ 0 & I _ {p} \end{array} \right] \tag {10.140}
$$

其中， $\bar{V}(s)=V^{-1}(s)$ ， $\bar{Y}(s)=-V^{-1}(s)Y(s)$ 。这样，由(10.140)可得到

$$U (s) \left(s I - A _ {1}\right) = \left(s I - A _ {2}\right) \bar {V} (s) \tag {10.141}$$

考虑到一般地说 $(sI - A_2)^{-1}U(s)$ 不是严格真的，所以采用矩阵除法，可导出

$$U (s) = \left(s I - A _ {2}\right) \bar {U} (s) + T \tag {10.142}$$

其中 $T$ 为常数矩阵。将(10.142)代入(10.141)，可以得到
