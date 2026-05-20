(2) 在(8.33)给出的 $M_{\alpha}(s)$ 中, 当结构指数 $\sigma_{i}(\alpha)$ 为正整数时表示 $G(s)$ 在 $s = \alpha$ 处有零点, 当 $\sigma_{i}(\alpha)$ 为负整数时表示 $G(s)$ 在 $s = \alpha$ 处有极点, 而 $\sigma_{i}(\alpha)$ 为零时则表示 $G(s)$ 在 $s = \alpha$ 上既无零点也没有极点。因此, 从 $\sigma_{i}(\alpha)$ 的为正或为负, 就可直接判断 $G(s)$ 在 $\alpha$ 处结构特性的属性。

(3) 根据 $G(s)$ 在 $s = \alpha$ 处的整个结构指数 $\{\sigma_{1}(\alpha), \sigma_{2}(\alpha), \cdots, \sigma_{r}(\alpha)\}$ ，就可以确定出 $G(s)$ 在 $s = \alpha$ 处极点的总重数和零点的总重数：

$G(s)$ 在 $s = \alpha$ 处极点的重数 $=\{\sigma_{1}(\alpha), \sigma_{2}(\alpha), \cdots, \sigma_{r}(\alpha)\}$ 中的负指数之和取绝对值 (8.35)

$G(s)$ 在 $s = \alpha$ 处零点的重数 $=\{\sigma_{1}(\alpha), \sigma_{2}(\alpha), \cdots, \sigma_{r}(\alpha)\}$ 中的正指数之和 (8.36)

（4）由于结构指数 $\{\sigma_i(\alpha)\}$ ， $\forall \alpha \in S_{sp}$ ，完全刻划了传递函数矩阵 $G(s)$ 的极点和零点的特性，因此通常可利用其来表达 $G(s)$ 的史密斯-麦克米伦形 $M(s)$ ：

$$
M (s) = \left[ \begin{array}{c c} \prod_ {a} \operatorname{diag} \{(s - a) ^ {\sigma_ {1} (a)}, \dots , (s - a) ^ {\sigma_ {r} (a)} \} & 0 \\ \hline 0 & 0 \end{array} \right] \tag {8.37}
$$

所以，一旦 $G(s)$ 的所有极点和零点集被确定，那么在定出 $S_{sp}$ 中各位置点处的结构指数后，就可由(8.37)来导出 $G(s)$ 的史密斯-麦克米伦形 $M(s)$ 。从而，提供了确定史密斯-麦克米伦形的一种新方法。
