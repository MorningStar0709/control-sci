$$
H (s, t) = \left\{ \begin{array}{l l} H _ {1} (2 s, t), & 0 \leqslant s \leqslant 1 / 2, \\ H _ {2} (2 s - 1, t), & 1 / 2 \leqslant s \leqslant 1. \end{array} \right.
$$

这个映射是连续的，因为

$$H _ {1} (1, t) = f _ {1} (1) = g _ {1} (0) = H _ {2} (0, t).$$

由定义有

$$H (s, 0) = f _ {1} \circ g _ {1}, \quad H (s, 1) = f _ {2} \circ g _ {2},$$

而且

$$
\left\{ \begin{array}{l} H (0, t) = H _ {1} (0, t) = f _ {1} (0) = f _ {2} (0) = f _ {1} \circ g _ {1} (0) = f _ {1} \circ g _ {2} (0), \\ H (1, t) = H _ {2} (1, t) = g _ {1} (1) = g _ {2} (1) = f _ {1} \circ g _ {1} (1) = f _ {2} \circ g _ {2} (1). \end{array} \right.
$$

因此 $f_{1} \circ g_{1} \sim f_{2} \circ g_{2}$ .

上述引理说明我们可以定义路径的等价类之间的乘法如下：

$$[ f ] [ g ] \stackrel {\text { def }} {=} [ f \circ g ]. \tag {3.4.4}$$

定义3.4.4 一个路径 $f$ 称为一个环路，如果 $f(0) = f(1) = x$ 。点 $x$ 称为基点。

下一步，我们要证明根据式(3.4.4)定义的等价类乘法，使环路的等价类形成一个群．以下的三个引理分别证明群的结合律，单位元和逆元.

引理3.4.2 设 $\alpha(s), \beta(s)$ 和 $\gamma(s)$ 为依次头尾相接的三个路径, 即, $\alpha(1) = \beta(0)$ 及 $\beta(1) = \gamma(0)$ . 那么 $([ \alpha][\beta])[\gamma] = [\alpha]([\beta][\gamma]).$

证明 我们只需证明 $(\alpha \circ \beta) \circ \gamma \simeq_{(\{0\}, \{1\})} \alpha \circ (\beta \circ \gamma)$ . 根据定义，有

$$
(\alpha \circ \beta) \circ \gamma (s) = \left\{ \begin{array}{l l} \alpha (4 s), & 0 \leqslant s \leqslant 1 / 4, \\ \beta (4 s - 1), & 1 / 4 \leqslant s \leqslant 1 / 2, \\ \gamma (2 s - 1), & 1 / 2 \leqslant s \leqslant 1. \end{array} \right.
$$

且

$$
\alpha \circ (\beta \circ \gamma) (s) = \left\{ \begin{array}{l l} \alpha (2 s), & 0 \leqslant s \leqslant 1 / 2, \\ \beta (4 s - 2), & 1 / 2 \leqslant s \leqslant 3 / 4, \\ \gamma (4 s - 3), & 3 / 4 \leqslant s \leqslant 1. \end{array} \right.
$$

定义两路径的同伦为

$$
H (s, t) = \left\{ \begin{array}{l l} \alpha \left(\frac {4 s}{1 + t}\right), & 4 s - 1 \leqslant t \leqslant 1, \\ \beta (4 s - t - 1), & 4 s - 2 \leqslant t \leqslant 4 s - 1, \\ \gamma \left(\frac {4 s - t - 2}{2 - t}\right), & 0 \leqslant t \leqslant 4 s - 2. \end{array} \right.
$$

请读者自行检验 $H(s,t)$ 是连续的且固定两个端点（对 $t = 0$ 及 $t = 1$ ）.

为方便起见，记 $e_x$ 为基点为 $x$ 的单点路径，即 $e_x(t) = x, \forall t \in [0,1]$ .

引理3.4.3 设 $\alpha(s)$ 为一路径， $\alpha(0) = x$ 且 $\alpha(1) = y$ . 那么

$$[ e _ {x} ] [ \alpha ] = [ \alpha ] = [ \alpha ] [ e _ {y} ].$$

证明 我们证明第一等式. 第二个等式可类似地证明. 因此只要证 $e_x \circ \alpha \simeq (\{0\}, \{1\}) \alpha$ 即可. 构造一个同伦如下:

$$
H (s, t) = \left\{ \begin{array}{l l} x, & 0 \leqslant t \leqslant 1 - 2 s, \\ \alpha \left(\frac {2 s + t - 1}{t + 1}\right), & 1 - 2 s \leqslant t \leqslant 1. \end{array} \right.
$$

那么
