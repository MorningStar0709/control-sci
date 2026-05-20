$$
\begin{array}{l} \left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{l} 2 h ^ {2} \\ - h \end{array} \right] u (1) + \left[ \begin{array}{l} h ^ {2} \\ - h \end{array} \right] u (0) = \\ \left[ \begin{array}{l l} 2 h ^ {2} & h ^ {2} \\ - h & - h \end{array} \right] \left[ \begin{array}{l} u (1) \\ u (0) \end{array} \right] \tag {2.7.16} \\ \end{array}
$$

因此 $G(2)$ 是以 $a_{+2} = \left[ \begin{array}{c}3h^2 r\\ -2hr \end{array} \right],b_{-2} = \left[ \begin{array}{c}h^2 r\\ 0 \end{array} \right],a_{-2} = \left[ \begin{array}{c} - 3h^2 r\\ 2hr \end{array} \right],b_{+2} =$ $\left[ \begin{array}{c} - h^2 r\\ 0 \end{array} \right]$ 为顶点的平行四边形．在线段 $a_{-2}b_{-2}$ 上的点的坐标为 $\left[ \begin{array}{cc}1 - 4\alpha h^2 r\\ 2\alpha hr \end{array} \right],0\leqslant \alpha \leqslant 1,\alpha = 1$ 时是点 $a_{-2},\alpha = 0$ 时是点 $b_{-2}$ .从这个点出发，取 $u = -r$ ，走一步的结果为

$$
\left[ \begin{array}{c} (1 - 4 \alpha) h ^ {2} r \\ 2 \alpha h r \end{array} \right] + h \left[ \begin{array}{c} 2 \alpha h r \\ - r \end{array} \right] = \left[ \begin{array}{c} (1 - 2 \alpha) h ^ {2} r \\ - (1 - 2 \alpha) h r \end{array} \right]
$$

这里， $\alpha$ 从0变到1画出的就是线段 $a_{-1}a_{+1}$ ，而这个线段就是等时区 $G(1)$ 。因此，线段 $a_{-2}b_{-2}$ 上的快速最优控制值应该是 $u = -r$ 。同理可知，线段 $a_{+2}b_{+2}$ 上的快速最优控制值应该是 $u = +r$ 。容易验证，在线段 $c_{-2}c_{+2}$ 上，取 $u = 0$ 就能到达线段 $a_{-1}a_{+1}$ ，即等时区 $G(1)$ ，因此线段 $c_{-2}c_{+2}$ 上的快速最优控制值应该是 u = 0. 实际上, 等时区 G(2) 的边界是由四条直线

$x_{1}+2hx_{2}=y+hx_{2}=+h^{2}r$ （线段 $a_{-2}b_{-2}$ 所在直线），

$x_{1}+2hx_{2}=y+hx_{2}=-h^{2}r$ （线段 $a_{+2}b_{+2}$ 所在直线），

$y = x_{1} + hx_{2} = +h^{2}r$ （线段 $a_{+2}b_{-2}$ 所在直线），

$y = x_{1} + hx_{2} = -h^{2}r$ (线段 $a_{-2}b_{+2}$ 所在直线)

所围成(图2.7.2). 对前两式除以 h 知, 等时区 $G(2)$ 是由两个线性函数所限定的区域:

$$\left| \frac {x _ {1} + 2 h x _ {2}}{h} \right| = \left| x _ {2} + \frac {y}{h} \right| \leqslant h r; | x _ {1} + h x _ {2} | = | y | \leqslant h ^ {2} r \tag {2.7.17}$$

![](image/abc180765818744d1acbb513c34ef1475fc24f2e226dea14828a3d7185cb6c92.jpg)

<details>
<summary>line</summary>

| x | y (y = h' r) | y (y = y = h') |
| --- | --- | --- |
| -0.5 | 0.6 | 0.4 |
| -0.25 | 0.4 | 0.2 |
| 0 | 0 | 0 |
| 0.25 | -0.2 | -0.2 |
| 0.5 | -0.6 | -0.4 |
</details>

图2.7.2

从表达式(2.7.16)解出 $u(0)$ ，得

$$u (0) = \frac {x _ {1} (0) + 2 h x _ {2} (0)}{h ^ {2}} = \frac {x _ {2} (0) + y (0) / h}{h},\left| x _ {2} (0) + \frac {y (0)}{h} \right| \leqslant h r, | y (0) | \leqslant h ^ {2} r$$

去掉初始时刻的标记“(0)”,又得
