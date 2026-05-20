分别为 $p \times p$ 和 $p \times q$ 的多项式矩阵。但是， $T^{-1}(s)F(s)$ 和 $T^{-1}(s)H(s)$ 只是形式上的有理分式矩阵，实质上仍然是多项式矩阵，所以以它们为传递函数矩阵的补偿器在物理上仍然是不能实现的。此外，在引入(11.135)的表达式后，观测器一控制器型状态反馈系统的结构图就可由图11.10进一步化成为图11.11的形式。

解决补偿器结构的可实现性问题 我们将从图11.11的结构图出发，分成两步来解决补偿器的物理可实现性问题。首先，将矩阵 $H(s)$ 用 $D_{L}(s)$ 相除可得

$$H (s) = L (s) D _ {L} (s) + N _ {y} (s) \tag {11.136}$$

其中 $N_{y}(s)$ 的列次数小于 $D_{L}(s)$ 的列次数。对应地，将 $F(s)$ 表示为

$$F (s) = - L (s) N _ {L} (s) + N _ {u} (s) \tag {11.137}$$

再由 $G_{o}(s) = N(s)D^{-1}(s) = D_{L}^{-1}(s)N_{L}(s)$ 可导出

$$N _ {L} (s) D (s) - D _ {L} (s) N (s) = 0 \tag {11.138}$$

而由(11.134)，并注意到 $\hat{\pmb{u}} (s) = D(s)\hat{\pmb{\zeta}} (s)$ 和 $\hat{\pmb{y}} (s) = N(s)\hat{\pmb{\zeta}} (s)$ ，又可导出

$$F (s) D (s) + H (s) N (s) = T (s) M (s) \tag {11.139}$$

现将(11.138)和(11.139)联合,那么可得到

$$
\left[ \begin{array}{c c} F (s) & H (s) \\ N _ {L} (s) & - D _ {L} (s) \end{array} \right] \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} T (s) M (s) \\ 0 \end{array} \right] \tag {11.140}
$$

进而,对上式作如下的运算:

$$
\left[ \begin{array}{c c} I & L (s) \\ \mathbf {0} & I \end{array} \right] \left[ \begin{array}{c c} F (s) & H (s) \\ N _ {L} (s) & - D _ {L} (s) \end{array} \right] \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c c} I & L (s) \\ \mathbf {0} & I \end{array} \right] \left[ \begin{array}{c} T (s) M (s) \\ \mathbf {0} \end{array} \right] \tag {11.141}
$$

则注意到式(11.136)和(11.137)的同时，有

$$
\left[ \begin{array}{c c} N _ {u} (s) & N _ {y} (s) \\ N _ {L} (s) & - D _ {L} (s) \end{array} \right] \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} T (s) M (s) \\ 0 \end{array} \right] \tag {11.142}
$$

并且，可由此导出补偿器的传递特性 $M(s)$ 的一个新的表达式为

$$M (s) = T ^ {- 1} (s) N _ {u} (s) D (s) + T ^ {- 1} (s) N _ {y} (s) N (s) \tag {11.143}$$

而相应地可导出反馈输入的一个新表达式为：

$$
\begin{array}{l} M (s) \hat {\zeta} (s) = T ^ {- 1} (s) N _ {u} (s) D (s) \hat {\zeta} (s) + T ^ {- 1} (s) N _ {y} (s) N (s) \hat {\zeta} (s) \\ = T ^ {- 1} (s) N _ {u} (s) \hat {\boldsymbol {u}} (s) + T ^ {- 1} (s) N _ {y} (s) \hat {\boldsymbol {y}} (s) \tag {11.144} \\ \end{array}
$$

这表明，在经过上述的处理后，图 11.11 的观测器—控制器型状态反馈系统可再化成为图 11.12 所示的结构图形式。

![](image/ef5913e77c5a58ec071cc9b6bb9c4a4d79892bdd947e4e5bb367e0bb95317c8d.jpg)

<details>
<summary>flowchart</summary>
