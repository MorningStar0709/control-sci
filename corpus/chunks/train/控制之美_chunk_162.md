$$
G (s) = \frac {N (s)}{D (s)} = \frac {(s - s _ {z 1}) (s - s _ {z 2}) \cdots (s - s _ {z m})}{(s - s _ {\mathrm{p} 1}) (s - s _ {\mathrm{p} 2}) \cdots (s - s _ {\mathrm{p} n})}, \quad n > m \tag {9.2.5}
$$

其中， $N(s)$ 和 $D(s)$ 代表传递函数 $G(s)$ 的分子和分母多项式。 $s_{z1}, s_{z2}, \cdots, s_{zm}$ 说明传递函数共含有 m 个零点； $s_{p1}, s_{p2}, \cdots, s_{pn}$ 表示传递函数共含有 n 个极点。此时系统的输出为

$$
X (s) = U (s) G (s) = \frac {A \omega_ {\mathrm{i}} + B s}{(s + \mathrm{j} \omega_ {\mathrm{i}}) (s - \mathrm{j} \omega_ {\mathrm{i}})} \frac {N (s)}{D (s)} \tag {9.2.6a}
$$

对其使用分式分解法可得

$$
\begin{array}{l} X (s) = \frac {A \omega_ {\mathrm{i}} + B s}{(s + \mathrm{j} \omega_ {\mathrm{i}}) (s - \mathrm{j} \omega_ {\mathrm{i}})} \frac {N (s)}{D (s)} \\ = \frac {A \omega_ {\mathrm{i}} + B s}{(s + \mathrm{j} \omega_ {\mathrm{i}}) (s - \mathrm{j} \omega_ {\mathrm{i}})} \frac {N (s)}{(s - s _ {\mathrm{p} 1}) (s - s _ {\mathrm{p} 2}) \cdots (s - s _ {\mathrm{p} n})} \\ = \frac {K _ {1}}{s + \mathrm{j} \omega_ {\mathrm{i}}} + \frac {K _ {2}}{s - \mathrm{j} \omega_ {\mathrm{i}}} + \frac {C _ {1}}{s - s _ {\mathrm{p} 1}} + \frac {C _ {2}}{s - s _ {\mathrm{p} 2}} + \dots + \frac {C _ {n}}{s - s _ {\mathrm{p} n}} \tag {9.2.6b} \\ \end{array}
$$

对式 $(9.2.6b)$ 进行拉普拉斯逆变换,可得

$$
\begin{array}{l} x (t) = \mathcal {L} ^ {- 1} [ X (s) ] = \mathcal {L} ^ {- 1} \left[ \frac {K _ {1}}{s + j \omega_ {i}} + \frac {K _ {2}}{s - j \omega_ {i}} + \frac {C _ {1}}{s - s _ {p 1}} + \frac {C _ {2}}{s - s _ {p 2}} + \dots + \frac {C _ {n}}{s - s _ {p n}} \right] \\ = K _ {1} \mathrm{e} ^ {- \mathrm{j} \omega_ {\mathrm{i}} t} + K _ {2} \mathrm{e} ^ {\mathrm{j} \omega_ {\mathrm{i}} t} + C _ {1} \mathrm{e} ^ {s _ {\mathrm{p} 1} t} + C _ {2} \mathrm{e} ^ {s _ {\mathrm{p} 2} t} + \dots + C _ {n} \mathrm{e} ^ {s _ {\mathrm{p} n} t} \tag {9.2.7} \\ \end{array}
$$

根据前面几章的分析, 当传递函数 $G(s)$ 的极点 $s_{p1}, s_{p2}, \cdots, s_{pn}$ 的实部都小于 0 时, $C_{1}e^{s_{p1}t}, C_{2}e^{s_{p2}t}, \cdots, C_{n}e^{s_{pn}t}$ 会随着时间 t 的增加而趋于 0。也只有在这种情况下, 系统的频率响应分析才有意义, 否则系统的输出将无穷大。此时, 系统的稳态输出为

$$
x _ {\mathrm{ss}} (t) = K _ {1} \mathrm{e} ^ {- \mathrm{j} \omega_ {\mathrm{i}} t} + K _ {2} \mathrm{e} ^ {\mathrm{j} \omega_ {\mathrm{i}} t} \tag {9.2.8}
$$

下面求 $K_{1}$ 和 $K_{2}$ 。根据式(9.2.6b)，得到
