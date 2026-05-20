# 10.3 连续对策

若 $u$ 与 $v$ 的选择为连续值时（即可有无限个对策），则有一个连续的支付函数 $L(u, v)$ ，而非离散的支付矩阵 $\pmb{L}_{ij}$ 。现在要找一对最优的 $(u^{*}, v^{*})$ ，使得

$$L (u ^ {*}, v) \leqslant L (u ^ {*}, v ^ {*}) \leqslant L (u, v ^ {*})$$

上式表明 $(u^{*}, v^{*})$ 是 $L$ 的一个鞍点，鞍点可用图10-4表示。 $L(u, v)$ 有鞍点的必要条件为

$$\frac {\partial L}{\partial u} = 0, \quad \frac {\partial L}{\partial v} = 0 \tag {10-17}\frac {\partial^ {2} L}{\partial u ^ {2}} \geqslant 0, \quad \frac {\partial^ {2} L}{\partial v ^ {2}} \leqslant 0$$

充分条件为

$$
\begin{array}{l} \frac {\partial L}{\partial u} = 0, \quad \frac {\partial L}{\partial v} = 0 \tag {10-18} \\ \frac {\partial^ {2} L}{\partial u ^ {2}} > 0, \quad \frac {\partial^ {2} L}{\partial v ^ {2}} <   0 \\ \end{array}
$$

![](image/f63dbb4b74bce50ad4c6642fc6f4a99efb952989388fc35cd8f6ea6ab77a83fa.jpg)

<details>
<summary>text_image</summary>

L
(u*,v*)
u
v
</details>

图10-4 连续对策的鞍点

例10-2 设对策的支付函数为

$$L (u, v) = \frac {1}{2} \left(u ^ {2} - v ^ {2}\right)- 1 \leqslant u \leqslant 1, \quad - 1 \leqslant v \leqslant 1$$

u 要选取策略使 L 最小, 而 v 则要使 L 最大, 求最优对策解, 即鞍点的值。
解

$$\frac {\partial L}{\partial u} = u = 0 \rightarrow u ^ {*} = 0\frac {\partial L}{\partial v} = - v = 0 \rightarrow v ^ {*} = 0$$

且，

$$\frac {\partial^ {2} L}{\partial u ^ {2}} = 1 > 0, \frac {\partial^ {2} L}{\partial v ^ {2}} = - 1 < 0$$

故 $(u^{*}, v^{*})$ 确实是 $L(u, v)$ 的鞍点。并且有

$$\max _ {v} \min _ {u} L (u, v) = \min _ {u} \max _ {v} L (u, v) = L \left(u ^ {*}, v ^ {*}\right) = 0$$

下面的支付函数

$$L (u, v) = u ^ {2} - 3 u v + 2 v ^ {2} \quad - 1 \leqslant u \leqslant 1, - 1 \leqslant v \leqslant 1$$

就不存在鞍点, 因为 $\frac{\partial^2 L}{\partial v^2} = 4 \neq 0$ 。(存在这种情形的原因是 $L(u, v)$ 中存在交叉积项 $3uv$ , 这使得 $L$ 不能分成二项, 一项仅与 $u$ 有关, 另一项仅与 $v$ 有关。)

对于不存在鞍点的情况,可以采用类似于矩阵对策中的概率混合对策。
