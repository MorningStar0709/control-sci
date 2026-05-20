其中 $\{\nu_{1},\nu_{2},\cdots,\nu_{\beta}\}$ 为 $G(s)$ 的左最小指数即左克罗内克尔指数， $\{\mu_{1},\mu_{2},\cdots,\mu_{\eta}\}$ 为 $G(s)$ 的右最小指数即右克罗内克尔指数，而 $\beta=q-r$ 和 $\eta=p-r$ 。

设 $\{h_{1}(s), h_{2}(s), \cdots, h_{\beta}(s)\}$ 为 $G_{1}(s)$ 的左零空间的一个最小多项式基，其次数为 $\{\bar{v}_{1}, \bar{v}_{2}, \cdots, \bar{v}_{\beta}\}$ 。由此，由最小多项式基的推论可知，矩阵

$$
H (s) = \left[ \begin{array}{c} \boldsymbol {h} _ {1} (s) \\ \vdots \\ \boldsymbol {h} _ {\beta} (s) \end{array} \right] \tag {8.113}
$$

为不可简约的和行既约的多项式基矩阵。于是，进而就有

$$H (s) G (s) = H (s) G _ {1} (s) G _ {2} (s) = \mathbf {0} \cdot G _ {2} (s) = \mathbf {0} \tag {8.114}$$

这表明， $H(s)$ 也是 $G(s)$ 的左零空间的最小多项式基矩阵，从而有

$$\left\{\bar {v} _ {1}, \bar {v} _ {2}, \dots , \bar {v} _ {\beta} \right\} = \left\{v _ {1}, v _ {2}, \dots , v _ {\beta} \right\} \tag {8.115}$$

现考虑多项式矩阵 $H(s)$ ，其行次数为 $v_{1} \leqslant v_{2} \leqslant \cdots \leqslant v_{\beta s}$ ，且由于其为不可简约和列既约的，所以通过推证可得：

$$v ^ {(1)} (H) = - v _ {1}, v ^ {(2)} (H) = - \left(v _ {1} + v _ {2}\right), \dots , v ^ {(r)} (H) = - \sum_ {k = 1} ^ {\beta} v _ {k} \tag {8.116}$$

从而可知

$$\text { def } H (s) = - \nu^ {(r)} (H) = \sum_ {k = 1} ^ {\beta} \nu_ {k} \tag {8.117}$$

再之, 因为 $G_{1}(s)$ 为列满秩, 故不妨表为

$$
G _ {1} (s) = \left[ \begin{array}{l} G _ {1 1} (s) \\ G _ {2 1} (s) \end{array} \right], G _ {1 1} (s) \text {为非奇异} \tag {8.118}
$$

而 $H(s)$ 为行满秩，类似地表为

于是，有 $H(s) = [H_1(s)\quad H_2(s)]$ ， $H_{2}(s)$ 为非奇异 (8.119)

$$
\begin{array}{l} H (s) G _ {1} (s) = - H _ {2} (s) \left[ - H _ {2} ^ {- 1} (s) H _ {1} (s) - I \right] \left[ \begin{array}{c} I \\ G _ {2 1} (s) G _ {1 1} ^ {- 1} (s) \end{array} \right] G _ {1 1} (s) \\ = - H _ {2} (s) \bar {H} (s) \bar {G} _ {1} (s) G _ {1 1} (s) = 0 \tag {8.120} \\ \end{array}
$$

其中

$$
\overline {{H}} (s) = \left[ - H _ {2} ^ {- 1} (s) H _ {1} (s) - I \right], \overline {{G}} _ {1} (s) = \left[ \begin{array}{c} I \\ G _ {2 1} (s) G _ {1 1} ^ {- 1} (s) \end{array} \right] \tag {8.121}
$$

进一步，从(8.120)又可导出

$$- H _ {2} ^ {- 1} (s) H _ {1} (s) = G _ {2 1} (s) G _ {1 1} ^ {- 1} (s) = W (s) \tag {8.122}$$

这样,就可将 $H(s)$ 和 $G_{1}(s)$ 分别表为

$$
H (s) = - H _ {2} (s) [ W (s) - I ] \tag {8.123}
G _ {1} (s) = \left[ \begin{array}{c} I \\ W (s) \end{array} \right] G _ {1 1} (s) \tag {8.124}
$$

从而，有

$$
\text { def } H (s) = \text { def } H _ {2} (s) + \text { def } [ W (s) - I ] \tag {8.125}
\operatorname{def} G _ {1} (s) = \operatorname{def} \left[ \begin{array}{c} I \\ W (s) \end{array} \right] + \operatorname{def} G _ {1 1} (s) \tag {8.126}
$$

考虑到 $H_{2}(s)$ 和 $G_{11}(s)$ 为非奇异，因此可得
