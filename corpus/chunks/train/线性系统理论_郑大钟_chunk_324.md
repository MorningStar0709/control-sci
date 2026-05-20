$$\operatorname{rank} \bar {Q} _ {e} \geqslant n, \operatorname{rank} \bar {Q} _ {c} \geqslant n \tag {9.18}$$

而这和反设 $\dim (\overline{A}) < n$ 是相矛盾的。所以，反设不成立，即不存在维数比 $(A, B, C)$ 更小的实现。从而证明了 $(A, B, C)$ 为最小实现。充分性得证。这就完成了证明过程。

结论2 对给定传递函数矩阵 $G(s)$ ，其最小实现不是唯一的，但满足广义唯一性。即：设 $(A, B, C)$ 和 $(\overline{A}, \overline{B}, \overline{C})$ 为 $G(s)$ 的任意两个最小实现，则它们必是代数等价的，也就是存在非奇异常阵 $T$ 使成立

$$\bar {A} = T ^ {- 1} A T, \bar {B} = T ^ {- 1} B, \bar {C} = C T \tag {9.19}$$

证 已知 $(A, B, C)$ 和 $(\overline{A}, \overline{B}, \overline{C})$ 均为最小实现，因此由结论1知它们都是联合能控和能观测的，从而有

$$\operatorname{rank} Q _ {c} = \operatorname{rank} Q _ {o} = \operatorname{rank} \bar {Q} _ {c} = \operatorname{rank} \bar {Q} _ {o} = n \tag {9.20}$$

其中 $n = \dim(A) = \dim(\overline{A})$ 。并且，进而可知

$$\overline {{{Q}}} _ {c} \overline {{{Q}}} _ {o} ^ {T} \text {和} \overline {{{Q}}} _ {o} ^ {T} \overline {{{Q}}} _ {o} \text {为非奇异} \tag {9.21}$$

于是，根据等式

$$Q _ {o} Q _ {c} = \overline {{{{Q}}}} _ {o} \overline {{{{Q}}}} _ {c} \tag {9.22}$$

即可导出

$$\overline {{{Q}}} _ {c} = \left(\overline {{{Q}}} _ {o} ^ {T} \overline {{{Q}}} _ {o}\right) ^ {- 1} \overline {{{Q}}} _ {o} ^ {T} Q _ {o} Q _ {c} = \overline {{{T}}} Q _ {c} \tag {9.23}$$

和

$$\overline {{{Q}}} _ {o} = Q _ {o} Q _ {c} \overline {{{Q}}} _ {c} ^ {T} (\overline {{{Q}}} _ {c} \overline {{{Q}}} _ {c} ^ {T}) ^ {- 1} = Q _ {o} T \tag {9.24}$$

而且，由(9.20)可知，矩阵

$$\overline {{{T}}} = (\overline {{{Q}}} _ {o} ^ {T} \overline {{{Q}}} _ {o}) ^ {- 1} \overline {{{Q}}} _ {o} ^ {T} Q _ {o} \text {和} T = Q _ {c} \overline {{{Q}}} _ {c} ^ {T} (\overline {{{Q}}} _ {c} \overline {{{Q}}} _ {c} ^ {T}) ^ {- 1} \tag {9.25}$$

均为非奇异。再因

$$
\begin{array}{l} \bar {T} T = \left(\bar {Q} _ {o} ^ {T} \bar {Q} _ {o}\right) ^ {- 1} \bar {Q} _ {o} ^ {T} Q _ {o} Q _ {c} \bar {Q} _ {c} ^ {T} \left(\bar {Q} _ {c} \bar {Q} _ {c} ^ {T}\right) ^ {- 1} \\ = \left(\bar {Q} _ {o} ^ {T} \bar {Q} _ {o}\right) ^ {- 1} \bar {Q} _ {o} ^ {T} \bar {Q} _ {o} \cdot \bar {Q} _ {c} \bar {Q} _ {c} ^ {T} \left(\bar {Q} _ {c} \bar {Q} _ {c} ^ {T}\right) ^ {- 1} = I \tag {9.26} \\ \end{array}
$$

进一步，又有

$$\overline {{{T}}} = T ^ {- 1} \tag {9.27}$$

这样，分别由

$$\overline {{{Q}}} _ {c} = T ^ {- 1} Q _ {c} \text {和} \overline {{{Q}}} _ {o} = Q _ {o} T \tag {9.28}$$

等式两边的第1列块相等和第1行块相等，就可得到关系式：

$$\overline {{{B}}} = T ^ {- 1} B \text {和} \overline {{{C}}} = C T \tag {9.29}$$

再由等式(9.22)展开而可导出

$$C A ^ {k} B = \bar {C} \bar {A} ^ {k} \bar {B}, k = 0, 1, \dots \tag {9.30}$$

因而成立如下的等式
