在虚部方程中， $\omega = 0$ 显然不是欲求之解，因此根轨迹与虚轴交点坐标应为 $\omega = \pm 1.1$ 。将所得 $\omega$ 值代入实部方程，立即解出 $K^{*} = 8.16$ 。所得结果与劳斯表法完全一样。整个系统概略根轨迹如图4-12所示。

根据以上介绍的七个法则,不难绘出系统的概略根轨迹。为了便于查阅,所有绘制法则统一归纳在表 4-1 之中。

表 4-1 根轨迹图绘制法则

<table><tr><td>序号</td><td>内容</td><td>法则</td></tr><tr><td>法则1</td><td>根轨迹的起点和终点</td><td>根轨迹起于开环极点(包括无限极点),终于开环零点(包括无限零点)</td></tr><tr><td>法则2</td><td>根轨迹的分支数,对称性和连续性</td><td>根轨迹的分支数等于开环极点数n(n&gt;m),或开环零点数m(m&gt;n)根轨迹对称于实轴</td></tr><tr><td>法则3</td><td>根轨迹的渐近线</td><td>n-m条渐近线与实轴的交角和交点为 $\varphi_{a} - \frac{(2k+1)\pi}{n-m}\quad (k=0,1,\cdots,n-m-1)$  $\sigma_{a} = \frac{\sum\limits_{i=1}^{n}p_{i} - \sum\limits_{j=1}^{m}z_{j}}{n-m}$ </td></tr><tr><td>法则4</td><td>根轨迹在实轴上的分布</td><td>实轴上某一区域,若其右方开环实数零、极点个数之和为奇数,则该区域必是根轨迹</td></tr><tr><td>法则5</td><td>根轨迹的分离点与分离角</td><td>l条根轨迹分支相遇,其分离点坐标由 $\sum\limits_{j=1}^{m}\frac{1}{d-z_{j}} - \sum\limits_{i=1}^{n}\frac{1}{d-p_{i}}$ 确定;分离角等于(2k+1) $\pi/l$ </td></tr><tr><td>法则6</td><td>根轨迹的起始角与终止角</td><td>起始角: $\theta_{p_{i}} = (2k+1)\pi + (\sum\limits_{j=1}^{m}\varphi_{z_{j}p_{i}} - \sum\limits_{\substack{j=1 \\ (j\neq i)}}^{n}\theta_{p_{j}p_{i}})$ 终止角: $\varphi_{z_{i}} = (2k+1)\pi - (\sum\limits_{\substack{j=1 \\ (j\neq i)}}^{m}\varphi_{z_{j}z_{i}} - \sum\limits_{i=1}^{n}\theta_{p_{j}z_{i}})$ </td></tr><tr><td>法则7</td><td>根轨迹与虚轴的交点</td><td>根轨迹与虚轴交点的K*值和ω值,可利用劳斯判据确定</td></tr><tr><td>法则8</td><td>根之和</td><td> $\sum\limits_{i=1}^{n}s_{i} = \sum\limits_{i=1}^{n}p_{i}$ </td></tr></table>

法则8 根之和。系统的闭环特征方程在 $n > m$ 的一般情况下，可以有不同形式的表示

$$
\begin{array}{l} \prod_ {i = 1} ^ {n} (s - p _ {i}) + K ^ {*} \prod_ {j = 1} ^ {m} (s - z _ {j}) = s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}. \\ = \prod_ {i = 1} ^ {n} (s - s _ {i}) = s ^ {n} + (- \sum_ {i = 1} ^ {n} s _ {i}) s ^ {n - 1} + \dots + \prod_ {i = 1} ^ {n} (- s _ {i}) \\ = 0 \\ \end{array}
$$

式中， $s_{i}$ 为闭环特征根。

当 $n - m \geqslant 2$ 时，特征方程第二项系数与 $K^{*}$ 无关，无论 $K^{*}$ 取何值，开环 $n$ 个极点之和总是等于闭环特征方程 $n$ 个根之和

$$\sum_ {i = 1} ^ {n} s _ {i} = \sum_ {i = 1} ^ {n} p _ {i}$$

在开环极点确定的情况下,这是一个不变的常数。所以,当开环增益 K 增大时,若闭环某些根在 s 平面上向左移动,则另一部分根必向右移动。

法则8对判断根轨迹的走向是很有用的。
