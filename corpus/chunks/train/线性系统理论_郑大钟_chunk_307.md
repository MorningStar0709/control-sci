$$
\left\{ \begin{array}{l} \sigma_ {1} (\alpha) = v _ {a} ^ {(1)} (G) \\ \sigma_ {2} (\alpha) = v _ {a} ^ {(2)} (G) - v _ {a} ^ {(1)} (G) \\ \dots \dots \\ \sigma_ {r} (\alpha) = v _ {a} ^ {(r)} (G) - v _ {a} ^ {(r - 1)} (G) \end{array} \right. \tag {8.61}
$$

证 先将 $G(s)$ 的史密斯-麦克米伦形表为

$$
M (s) = \left[ \begin{array}{c c c} (s - \alpha) ^ {\sigma_ {1} (\alpha)} \frac {\bar {\varepsilon} _ {1} (s)}{\bar {\psi} _ {1} (s)} & & \\ & (s - \alpha) ^ {\sigma_ {2} (\alpha)} \frac {\bar {\varepsilon} _ {2} (s)}{\bar {\psi} _ {2} (s)} & \\ & & \ddots & \\ & & (s - \alpha) ^ {\sigma_ {r} (\alpha)} \frac {\bar {\varepsilon} _ {r} (s)}{\bar {\psi} _ {r} (s)} \\ \hline 0 & & 0 \end{array} \right] \tag {8.62}
$$

其中， $\{\varepsilon_i(s), \bar{\psi}_i(s)\}$ 为互质，且 $\varepsilon_i(s)$ 和 $\bar{\psi}_i(s)$ 均不能为 $(s - \alpha)$ 除尽。则根据定义式(8.44)和结论1，就可导出

$$
\left\{ \begin{array}{l} v _ {a} ^ {(1)} (G) = v _ {a} ^ {(1)} (M) = \sigma_ {1} (\alpha) \\ v _ {a} ^ {(2)} (G) = v _ {a} ^ {(2)} (M) = \sigma_ {1} (\alpha) + \sigma_ {2} (\alpha) \\ \dots \dots \\ v _ {a} ^ {(r - 1)} (G) = v _ {a} ^ {(r - 1)} (M) = \sigma_ {1} (\alpha) + \sigma_ {2} (\alpha) + \dots + \sigma_ {r - 1} (\alpha) \\ v _ {a} ^ {(r)} (G) = v _ {a} ^ {(r)} (M) = \sigma_ {1} (\alpha) + \sigma_ {2} (\alpha) + \dots + \sigma_ {r} (\alpha) \end{array} \right. \tag {8.63}
$$

将(8.63)改写之即可得到(8.61)。从而证明完成。

不难看出,利用结论3,可以无需通过单模变换,而是通过计算各阶评价值,就可直接由给定传递函数矩阵 $G(s)$ 来定出其史密斯-麦克米伦形 $M(s)$ 。在很多情况下,这无疑是一种比较简便的算法。

例 给定传递函数矩阵 $G(s)$ 如下:

$$
G (s) = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & \frac {s}{(s + 2) ^ {2}} \\ \frac {- s}{(s + 2) ^ {2}} & \frac {- s}{(s + 2) ^ {2}} \end{array} \right]
$$

前面已经求出， $G(s)$ 的评价值为：

$$\nu_ {0} ^ {(1)} (G) = 1, \quad \nu_ {- 1} ^ {(1)} (G) = - 2, \quad \nu_ {- 2} ^ {(1)} (G) = - 2\nu_ {0} ^ {(2)} (G) = 3, \cdot \nu_ {- 1} ^ {(2)} (G) = - 2, \quad \nu_ {- 2} ^ {(2)} (G) = - 3$$

于是，首先根据(8.61)来求出 $s = 0, -1, -2$ 处的结构指数：

$$\sigma_ {1} (0) = v _ {0} ^ {(1)} (G) = 1, \quad \sigma_ {2} (0) = v _ {0} ^ {(2)} (G) - v _ {0} ^ {(1)} (G) = 2\sigma_ {1} (- 1) = v _ {- 1} ^ {(1)} (G) = - 2, \quad \sigma_ {2} (- 1) = v _ {- 1} ^ {(2)} (G) - v _ {- 1} ^ {(1)} (G) = 0\sigma_ {1} (- 2) = v _ {- 2} ^ {(1)} (G) = - 2, \quad \sigma_ {2} (- 2) = v _ {- 2} ^ {(2)} (G) - v _ {- 2} ^ {(1)} (G) = - 1$$

然后，就即可定出给定 $G(s)$ 的史密斯-麦克米伦形 $M(s)$ 为：

$$
M (s) = \left[ \begin{array}{l l} s & \\ & s ^ {2} \end{array} \right] \left[ \begin{array}{l l} (s + 1) ^ {- 2} & \\ & 1 \end{array} \right] \left[ \begin{array}{l l} (s + 2) ^ {- 2} & \\ & (s + 2) ^ {- 1} \end{array} \right]
