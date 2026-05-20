$$
\begin{array}{l} | y (t) | \leqslant \int_ {0} ^ {t} | h (t - \sigma) | | u (\sigma) | d \sigma \\ = \int_ {0} ^ {t} | h (t - \sigma) | ^ {1 / q} | h (t - \sigma) | ^ {1 / p} | u (\sigma) | d \sigma \\ \leqslant \left(\int_ {0} ^ {t} | h (t - \sigma) | d \sigma\right) ^ {1 / q} \left(\int_ {0} ^ {t} | h (t - \sigma) | | u (\sigma) | ^ {p} d \sigma\right) ^ {1 / p} \\ \leqslant \left(\| h _ {\tau} \| _ {\mathcal {L} _ {1}}\right) ^ {1 / q} \left(\int_ {0} ^ {t} | h (t - \sigma) | | u (\sigma) | ^ {p} d \sigma\right) ^ {1 / p} \\ \end{array}
$$

其中第二个不等式应用了 Hölder 不等式①, 这样,

$$
\begin{array}{l} \left(\| y _ {\tau} \| _ {\mathcal {L} _ {p}}\right) ^ {p} = \int_ {0} ^ {\tau} | y (t) | ^ {p} d t \\ \leqslant \int_ {0} ^ {\tau} \left(\left\| h _ {\tau} \right\| _ {\mathcal {L} _ {1}}\right) ^ {p / q} \left(\int_ {0} ^ {t} | h (t - \sigma) | | u (\sigma) | ^ {p} d \sigma\right) d t \\ = \left(\| h _ {\tau} \| _ {\mathcal {L} _ {1}}\right) ^ {p / q} \int_ {0} ^ {\tau} \int_ {0} ^ {t} | h (t - \sigma) | | u (\sigma) | ^ {p} d \sigma d t \\ \end{array}
$$

交换积分次序,得

$$
\begin{array}{l} \left(\| y _ {\tau} \| _ {\mathcal {L} _ {p}}\right) ^ {p} \leqslant \left(\| h _ {\tau} \| _ {\mathcal {L} _ {1}}\right) ^ {p / q} \int_ {0} ^ {\tau} | u (\sigma) | ^ {p} \int_ {\sigma} ^ {\tau} | h (t - \sigma) | d t d \sigma \\ \leqslant \left(\| h _ {\tau} \| _ {\mathcal {L} _ {1}}\right) ^ {p / q} \| h _ {\tau} \| _ {\mathcal {L} _ {1}} \left(\| u _ {\tau} \| _ {\mathcal {L} _ {p}}\right) ^ {p} = \left(\| h _ {\tau} \| _ {\mathcal {L} _ {1}}\right) ^ {p} \left(\| u _ {\tau} \| _ {\mathcal {L} _ {p}}\right) ^ {p} \\ \end{array}
$$

因此 $\| y_{\tau}\|_{\mathcal{L}_p}\leqslant \| h\|_{\mathcal{L}_1}\| u_\tau \| \mathcal{L}_p$

综上所述,如果 $\|h\|_{L_{1}}<\infty$ , 则对于每个 $p\in[1,\infty)$ , 因果卷积算子是有限增益 $L_{p}$ 稳定的, 且当 $\gamma=\|h\|_{L_{1}},\beta=0$ 时, 式(5.2)成立。

定义5.1的缺点是没有明显地要求不等式(5.1)和不等式(5.2)对所有输入空间 $\mathcal{L}^m$ 的信号都成立。这对于输入-输出关系只定义在输入空间子集上的系统是不适用的。下例将对这一点进行研究并给出小信号 $\mathcal{L}$ 稳定性的定义。

例5.3 考虑非线性单输入-单输出系统

$$y = \tan u$$

只有当输入信号满足 $|u(t)| < \frac{\pi}{2}, \forall t \geqslant 0$

时, 输出 $y(t)$ 才有定义。这样, 按照定义 5.1, 系统就不是 $L_{\infty}$ 稳定的。但如果把 $u(t)$ 限制为

$$| u | \leqslant r < \frac {\pi}{2}$$

则有 $|y|\leqslant \left(\frac{\tan r}{r}\right)|u|$

且系统满足不等式 $\| y\|_{\mathcal{L}_p}\leqslant \left(\frac{\tan r}{r}\right)\| u\|_{\mathcal{L}_p}$
