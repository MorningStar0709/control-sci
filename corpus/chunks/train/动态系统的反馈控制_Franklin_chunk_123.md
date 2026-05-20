# 例 3.10 正弦函数的拉普拉斯变换

求正弦函数的拉普拉斯变换。

解答。再一次利用式(3.32)，可得

$$\mathcal {L} (\sin (\omega t)) = \int_ {0} ^ {+ \infty} (\sin (\omega t)) \mathrm{e} ^ {- s t} \mathrm{d} t \tag {3.35}$$

如果我们将 www.fpe7e.com 的附录 WA 中的式(WA.34)，

$$\sin (\omega t) = \frac {\mathrm{e} ^ {\mathrm{j} \omega t} - \mathrm{e} ^ {- \mathrm{j} \omega t}}{2 \mathrm{j}}$$

代入式 $(3.35)$ ，得到

$$
\begin{array}{l} \mathcal {L} \left\{\sin (\omega t)\right) = \int_ {0} ^ {+ \infty} \left(\frac {\mathrm{e} ^ {\mathrm{j} \omega t} - \mathrm{e} ^ {- \mathrm{j} \omega t}}{2 \mathrm{j}}\right) \mathrm{e} ^ {- s t} \mathrm{d} t \\ = \frac {1}{2 \mathrm{j}} \int_ {0} ^ {+ \infty} \left(\mathrm{e} ^ {(\mathrm{j} \omega - s) t} - \mathrm{e} ^ {- (\mathrm{j} \omega + s) t}\right) \mathrm{d} t \\ = \frac {1}{2 \mathrm{j}} \left[ \frac {1}{\mathrm{j} \omega - s} \mathrm{e} ^ {(\mathrm{j} \omega - s) t} - \frac {1}{\mathrm{j} \omega + s} \mathrm{e} ^ {- (\mathrm{j} \omega + s) t} \right] \Bigg | _ {0} ^ {+ \infty} \\ = \frac {\omega}{s ^ {2} + \omega^ {2}}, \quad \mathrm{Re} (s) > 0 \\ \end{array}
$$

然后，可以扩展拉普拉斯变换的有效范围到除了极点 $s=\pm j\omega$ 以外的整个 s 平面（见附录 A）。

附录 A 中表 A.2 给出了基本时间函数的拉普拉斯变换。表中每一条都如例 3.8 到例 3.10 所示的那样，可直接应用拉普拉斯变换的定义式(3.32)得到。
