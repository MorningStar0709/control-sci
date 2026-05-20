$$
\begin{array}{l} e _ {\mathrm{ss}} = \lim _ {t \rightarrow \infty} e (t) = \lim _ {s \rightarrow 0} s E (s) = \lim _ {s \rightarrow 0} \frac {(s + a) R (s)}{s + a + a C (s)} \\ = \lim _ {s \rightarrow 0} \frac {(s + a) \frac {r}{s}}{s + a + a K _ {\mathrm{P}}} = \lim _ {s \rightarrow 0} \frac {(s + a) r}{s + a + a C (s)} = \frac {a r}{a + a \lim _ {s \rightarrow 0} C (s)} \\ = \frac {r}{1 + \lim _ {s \rightarrow 0} C (s)} \tag {7.3.10} \\ \end{array}
$$

根据式(7.3.10)，如果希望消除稳态误差（即令 $e_{ss}=0$ ），则 $\frac{r}{1+\lim_{s\to0}C(s)}$ 的分母要无穷大，即 $\lim_{s\to0}C(s)=\infty$ 。为此，一个很自然的做法就是令 $C(s)=\frac{1}{s}$ 。在使用中令 $C(s)=\frac{K_1}{s}$ ，其中， $K_1$ 被称为积分增益（Integral Gain），可以根据不同的要求进行调节。此时，系统控制量的拉普拉斯变换为

$$U (s) = C (s) E (s) = \frac {K _ {1}}{s} E (s) \tag {7.3.11a}$$

其对应的时域表达为

$$u (t) = K _ {1} \int_ {0} ^ {t} e (t) \mathrm{d} t \tag {7.3.11b}$$

以上就是积分控制器的动机与推导过程,使用积分控制可以有效地消除稳态误差。将 $C(s)=\frac{K_{1}}{s}$ 代入式(7.3.3)中,得到

$$X (s) = \frac {a \frac {r}{s} C (s)}{s + a + a C (s)} = \frac {a \frac {r}{s} \frac {K _ {\mathrm{I}}}{s}}{s + a + a \frac {K _ {\mathrm{I}}}{s}} = \frac {r}{s} \frac {a K _ {\mathrm{I}}}{s ^ {2} + a s + a K _ {\mathrm{I}}}\Rightarrow \left(s ^ {2} + a s + a K _ {\mathrm{I}}\right) X (s) = \frac {a K _ {\mathrm{I}} r}{s} \tag {7.3.12}$$

对式 $(7.3.12)$ 等号两边进行拉普拉斯逆变换,可得

$$\mathcal {L} ^ {- 1} \left[ \left(s ^ {2} + a s + a K _ {1}\right) X (s) \right] = \mathcal {L} ^ {- 1} \left[ \frac {a K _ {1} r}{s} \right]\Rightarrow \frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + a \frac {\mathrm{d} x (t)}{\mathrm{d} t} + a K _ {1} x (t) = a K _ {1} r \tag {7.3.13}$$

式(7.3.13)说明在引入积分控制器之后,原始的一阶系统变成了二阶系统,式(7.3.13)对应了二阶系统的阶跃响应。类比第5章中二阶系统的一般形式,得到此二阶系统的阻尼比 $\zeta$ 和固有频率 $\omega_{n}$ 为

$$
\left\{ \begin{array}{l} 2 \zeta \omega_ {\mathrm{n}} = a \\ \omega_ {\mathrm{n}} ^ {2} = a K _ {1} \end{array} \Rightarrow \left\{ \begin{array}{l} \zeta = \frac {a}{2 \sqrt {a K _ {1}}} \\ \omega_ {\mathrm{n}} = \sqrt {a K _ {1}} \end{array} \right. \right. \tag {7.3.14}
$$

正如 5.4.1 节所介绍的,此时的控制器设计就像是在设计一个“看不见”的弹簧质量阻尼系统,通过改变控制参数来调节此系统的固有频率和阻尼比。

例如，将式(7.3.14)代入式(5.4.3)中，可以得到上升时间为

$$T _ {\mathrm{r}} = \frac {\pi - \varphi}{\omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}}} = \frac {\pi - \varphi}{\sqrt {a K _ {1}} \sqrt {1 - \frac {a}{4 K _ {1}}}} = \frac {\pi - \varphi}{\sqrt {a K _ {1} - \frac {a ^ {2}}{4}}} \tag {7.3.15a}$$

式(7.3.15a)说明 $K_{1}$ 的增加将导致 $T_{r}$ 的下降, 加快系统的响应速度。将式(7.3.14)代入式(5.4.7)中, 得到最大超调量为
