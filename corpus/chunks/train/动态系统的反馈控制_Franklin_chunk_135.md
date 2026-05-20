# 例 3.11 部分分式展开：单实根

假设已经计算 $Y(s)$ :

$$Y (s) = \frac {(s + 2) (s + 4)}{s (s + 1) (s + 3)}$$

求 $y(t)$ 。

解答。根据部分分式展开，记 $Y(s)$ 为

$$Y (s) = \frac {C _ {1}}{s} + \frac {C _ {2}}{s + 1} + \frac {C _ {3}}{s + 3}$$

用消去法得

$$C _ {1} = \frac {(s + 2) (s + 4)}{(s + 1) (s + 3)} \Big | _ {s = 0} = \frac {8}{3} \tag {106}$$

以此类推，有

$$C _ {2} = \frac {(s + 2) (s + 4)}{s (s + 3)} \Big | _ {s = - 1} = - \frac {3}{2}$$

和

$$C _ {3} = \frac {(s + 2) (s + 4)}{s (s + 1)} \Big | _ {s = - 3} = - \frac {1}{6}$$

通过将部分分式相加检验所得结果的正确性，证明能够还原为原函数。对各部分分式查表后可得：

$$y (t) = \frac {8}{3} 1 (t) - \frac {3}{2} \mathrm{e} ^ {- t} 1 (t) - \frac {1}{6} \mathrm{e} ^ {- 3 t} 1 (t)$$

部分分式展开可用 Matlab 中的 residue 计算，Matlab 语句如下。

$$
\begin{array}{l l} \text {num = conv([1 2],[1 4]);} & \% \text {form numerator polynomial} \\ \text {den = conv([1 1 0],[1 3]);} & \% \text {form denominator polynomial} \\ [ r, p, k ] = \text {residue(num,den);} & \% \text {compute the residues} \end{array}
$$

由此得以下结果

$$r = [ - 0. 1 6 6 7 - 1. 5 0 0 0 2. 6 6 6 7 ] ^ {\prime}; \quad p = [ - 3 - 1 0 ] ^ {\prime}; \quad k = [ ];$$

该结果与手算结果一样。注意，Matlab 中 conv 函数常用于两个多项式相乘（函数的自变量为多项式系数）。
