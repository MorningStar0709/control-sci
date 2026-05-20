$$\mathrm{sysG2} = \mathrm{ss(A,B,C2,D)}[ \mathrm{ZER2}, \text {gain2} ] = \text {tzero(sysG2)}$$

得到

$$\mathrm{ZER} 2 = - 2. 0 0 0 0, \text { gain } 2 = 0. 6$$

将磁带在读/写头的位置作为输出时，执行下述语句：

$$
\mathrm{sysG3} = \mathrm{ss(A,B,C3,D)}[ \mathrm{ZER3}, \text {gain3} ] = \text {tzero(sysG3)}
\mathrm{ZER3} = \left[ \begin{array}{l} - 0. 9 0 0 0 0 + 0. 8 8 8 8 \mathrm{i} \\ - 0. 9 0 0 0 0 - 0. 8 8 8 8 \mathrm{i} \end{array} \right], \mathrm{gain3} = 0. 7 5
$$

我们注意到这些结果与前面用分子多项式 N3 求得的值是相同的。最后，当电压作为输出时，执行下面语句：

$$\mathrm{sysGT} = \mathrm{ss(A,B,CT,D)}[ \mathrm{ZERT}, \text {gainT} ] = \text {tzero(sysGT)}$$

可以得到

$$
\mathrm{ZERT} = \left[ \begin{array}{c} 0 \\ - 1. 9 9 9 9 \\ - 1. 0 0 0 0 \end{array} \right], \mathrm{gainT} = - 0. 1 5
$$

根据这些结果可以写出传递函数，例如，对位置 $x_{3}$ 的传递函数为

$$
\begin{array}{l} G (s) = \frac {X _ {3} (s)}{E _ {1} (s)} \\ = \frac {0 . 7 5 s ^ {2} + 1 . 3 5 s + 1 . 2}{s ^ {5} + 2 . 7 5 s ^ {4} + 3 . 2 2 s ^ {3} + 1 . 8 8 s ^ {2} + 0 . 4 1 8 s} \\ = \frac {0 . 7 5 (s + 0 . 9 \pm 0 . 8 8 8 8 \mathrm{j})}{s (s + 0 . 5 0 7) (s + 0 . 9 6 8) (s + 0 . 6 3 7 \pm 0 . 6 6 7 \mathrm{j})} \tag {7.66} \\ \end{array}
$$
