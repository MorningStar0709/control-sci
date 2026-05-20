# 4）斜坡函数

考虑下列斜坡函数：

$$
f (t) = \left\{ \begin{array}{l l} 0, & t <   0 \\ A t, & t \geqslant 0 \end{array} \right.
$$

式中， $A$ 为常数。

斜坡函数的拉普拉斯变换为

$$
\begin{array}{l} F (s) = \int_ {0} ^ {\infty} A t \mathrm{e} ^ {- s t} \mathrm{d} t = A t \frac {\mathrm{e} ^ {- s t}}{- s} \left| _ {0} ^ {\infty} - \int_ {0} ^ {\infty} \frac {A \mathrm{e} ^ {- s t}}{- s} \mathrm{d} t \right. \\ = \frac {A}{s} \int_ {0} ^ {\infty} \mathrm{e} ^ {- s t} \mathrm{d} t = \frac {A}{s ^ {2}} \\ \end{array}
$$
