# (4) 梯形隶属函数

梯形曲线可由4个参数 $a, b, c, d$ 确定，即

$$
f (x, a, b, c, d) = \left\{ \begin{array}{l l} 0 & x \leqslant a \\ \frac {x - a}{b - a} & a \leqslant x \leqslant b \\ 1 & b \leqslant x \leqslant c \\ \frac {d - x}{d - c} & c \leqslant x \leqslant d \\ 0 & x \geqslant d \end{array} \right. \tag {3.23}
$$

式中，参数 $a$ 和 $d$ 确定梯形的“脚”，而参数 $b$ 和 $c$ 确定梯形的“肩膀”。Matlab表示为trapmf $(\mathrm{x},[\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{d}])$ 。
