# 5）正弦函数

考虑下列正弦函数：

$$
f (t) = \left\{ \begin{array}{l l} 0, & t <   0 \\ A \sin \omega t, & t \geqslant 0 \end{array} \right.
$$

式中， $A$ 和 $\omega$ 为常数。由于

$$\sin \omega t = \frac {1}{2 \mathrm{j}} (\mathrm{e} ^ {\mathrm{j} \omega t} - \mathrm{e} ^ {- \mathrm{j} \omega t})$$

故正弦函数的拉普拉斯变换为

$$
\begin{array}{l} F (s) = \mathscr {L} [ A \sin \omega t ] = \frac {A}{2 \mathrm{j}} \int_ {0} ^ {\infty} \left(\mathrm{e} ^ {\mathrm{j} \omega t} - \mathrm{e} ^ {- \mathrm{j} \omega t}\right) \mathrm{e} ^ {- s t} \mathrm{d} t \\ = \frac {A}{2 \mathrm{j}} \left(\frac {1}{s - \mathrm{j} \omega} - \frac {1}{s + \mathrm{j} \omega}\right) = \frac {A \omega}{s ^ {2} + \omega^ {2}} \\ \end{array}
$$

类似地， $A\cos \omega t$ 的拉普拉斯变换可导出为

$$F (s) = \mathscr {L} [ A \cos \omega t ] = \frac {A s}{s ^ {2} + \omega^ {2}}$$
