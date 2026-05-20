$$\operatorname{def} H _ {2} (s) = 0, \quad \operatorname{def} G _ {1 1} (s) = 0 \tag {8.127}$$

而 $[W(s) - I]$ 和 $\left[ \begin{array}{c}I\\ W(s) \end{array} \right]$ 具有相同的极点和零点布局，所以又可导出

$$
\operatorname{def} [ W (s) - I ] = \operatorname{def} \left[ \begin{array}{c} I \\ W (s) \end{array} \right] \tag {8.128}
$$

由此，考虑到(8.127)和(8.128)的同时，就可由(8.125)和(8.126)导出

$$\operatorname{def} H (s) = \operatorname{def} G _ {1} (s) \tag {8.129}$$

将(8.129)代入(8.117)，就证明了：

$$\text { def } G _ {1} (s) = \sum_ {k = 1} ^ {\beta} v _ {k} \tag {8.130}$$

同理，也可证明得到

$$\text { def } G _ {2} (s) = \sum_ {l = 1} ^ {\eta} \mu_ {l} \tag {8.131}$$

③ 再将(8.130)和(8.131)代入(8.108)，即得

$$\text { def } G (s) = \sum_ {l = 1} ^ {\eta} \mu_ {l} + \sum_ {k = 1} ^ {\beta} v _ {k} \tag {8.132}$$

从而，证明了关系式(8.106)。于是证明完成。

下面,我们对上述结论进行如下的一些讨论:

（1）亏数的大小反映了传递函数矩阵的奇异程度。这表明，传递函数矩阵的奇异性，在结构特性上呈现为极点总个数与零点总个数之间的不匹配性。  
(2) 由式(8.106)可知,传递函数矩阵 $G(s)$ 的亏数 $\operatorname{def} G(s)$ 总是正整数。因此,当 $G(s)$ 为奇异时,必属于极点总个数多于零点总个数的情况。  
(3) 当且仅当 $G(s)$ 为方的和为非奇异时，有亏数 $\operatorname{def} G(s) = 0$ ，因而极点总个数等于零点总个数，即 $G(s)$ 可保持良好的结构性质(8.98)。
