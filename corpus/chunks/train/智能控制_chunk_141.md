# (5) 三角形隶属函数

三角形曲线的形状由3个参数 $a, b, c$ 确定，即

$$
f (x, a, b, c) = \left\{ \begin{array}{l l} 0 & x \leqslant a \\ \frac {x - a}{b - a} & a \leqslant x \leqslant b \\ \frac {c - x}{c - b} & b \leqslant x \leqslant c \\ 0 & x \geqslant c \end{array} \right. \tag {3.24}
$$

式中，参数 $a$ 和 $c$ 确定三角形的“脚”，而参数 $b$ 确定三角形的“峰”。Matlab表示为 $\operatorname{trimf}(\mathbf{x}, [\mathbf{a}, \mathbf{b}, \mathbf{c}])$ 。
