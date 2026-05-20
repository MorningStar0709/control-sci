# 8.4 传递函数矩阵的评价值

从前几节的讨论中可以看出，传递函数矩阵的史密斯-麦克米伦形，对多变量系统的极点和零点的分析有重要的作用。这一节中，我们通过引入传递函数矩阵的评价值(Valuation)，来给出确定史密斯-麦克米伦形的一种简便方法。下面，将分成两种情况进行讨论。

传递函数矩阵在复数平面的有限处的评价值 首先，我们对标量传递函数 $g(s)$ 的评价值进行定义。给定传递函数 $g(s) = \bar{n}(s) / \bar{d}(s)$ ，如果可将其表示为

$$g (s) = (s - \zeta) ^ {\prime} \zeta \frac {n (s)}{d (s)} \tag {8.42}$$

其中， $\{d(s),n(s)\}$ 为互质，且 $n(s)$ 和 $d(s)$ 均不能为 $(s - \zeta)$ 整除，则就定义

$g(s)$ 在 $(s-\zeta)$ 即 $s=\zeta$ 处的评价值

$$= v _ {\zeta} (g) \triangleq v _ {\zeta} \tag {8.43}$$

不难看出，评价值 $v_{\zeta}$ 只能为包括零在内的正或负整数。如果所考虑的传递函数 $g(s) \equiv 0$ 则规定其评价值 $v_{\zeta}(g) = \infty$ 。现在，来推广定义传递函数矩阵 $G(s)$ 的评价值。令 $|G|$ 表示 $G(s)$ 的一个 $i \times i$ 子式，则规定

$$G (s) \text { 在 } s = \zeta \text { 处的第 } i \text { 阶评价值 } = v _ {\zeta} ^ {(i)} (G)\triangle \min \left\{\nu_ {\zeta} (| G | ^ {i}) \right\}, i = 1, 2, \dots , r \tag {8.44}$$

其中 $r = \mathrm{rank}G(s)$ 。

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & \frac {s}{(s + 2) ^ {2}} \\ \frac {- s}{(s + 2) ^ {2}} & \frac {- s}{(s + 2) ^ {2}} \end{array} \right]
$$

先定出其各阶子式:

$$\left| G \right| ^ {2} = \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}}, \frac {- s}{(s + 2) ^ {2}}, \frac {s}{(s + 2) ^ {2}}, \frac {- s}{(s + 2) ^ {2}}\left| G \right| ^ {2} = \frac {s ^ {3}}{(s + 1) ^ {2} (s + 2) ^ {3}}$$

随后，根据定义式(8.44)和(8.43)，即可定出：

$G(s)$ 在 $s = 0$ 的评价值为

$$\nu_ {0} ^ {(1)} (G) = \min \{1, 1, 1, 1 \} = 1v _ {0} ^ {(2)} (G) = 3$$

$G(s)$ 在 $s = -1$ 的评价值为

$$\nu_ {- 1} ^ {(1)} (G) = \min \{- 2, 0, 0, 0 \} = - 2\nu_ {- j} ^ {(2)} (G) = - 2$$

$G(s)$ 在 $s = -2$ 的评价值为

$$v _ {- 2} ^ {(1)} (G) = \min \{- 2, - 2, - 2, - 2 \} = - 2\nu_ {- 2} ^ {(1)} (G) = - 3$$

现在,我们进一步来指出传递函数矩阵在有限复数平面上的评价值的一些重要属性。

结论1 考虑多变量系统的传递函数矩阵 $G(s)$ ，令 $\operatorname{rank} G(s) = r$ ，且将其史密斯-麦克米伦形表为

$$
M (s) = U (s) G (s) V (s) = \left[ \begin{array}{c c} \prod M _ {a} (s) & 0 \\ - \frac {}{0} & 0 \end{array} \right] \tag {8.45}
$$

其中， $U(s)$ 和 $V(s)$ 为单模阵，而

$$M _ {a} (s) = \operatorname{diag} \left\{\left(s - \alpha\right) ^ {\sigma_ {1} (a)}, \dots , \left(s - \alpha\right) ^ {\sigma_ {r} (a)} \right\} \tag {8.46}$$

则对任一 $\pmb{\alpha} \in \mathcal{C}$ ，必定成立如下的关系式：

$$v _ {a} ^ {(i)} (G) = v _ {a} ^ {(i)} (M) = v _ {a} ^ {(i)} \left(M _ {a}\right), i = 1, 2, \dots , r \tag {8.47}$$
