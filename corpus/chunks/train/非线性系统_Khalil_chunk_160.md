定义,其中当 t<0 时, $h(t)=0$ 。假设 $h\in\mathcal{L}_{1e}$ ,即对于每个 $\tau\in[0,\infty)$ ,有

$$\| h _ {\tau} \| _ {\mathcal {L} _ {1}} = \int_ {0} ^ {\infty} | h _ {\tau} (\sigma) | d \sigma = \int_ {0} ^ {\tau} | h (\sigma) | d \sigma < \infty$$

如果 $u \in \mathcal{L}_{\infty e}, \tau \geqslant t$ ，则

$$
\begin{array}{l} | y (t) | \leqslant \int_ {0} ^ {t} | h (t - \sigma) | | u (\sigma) | d \sigma \\ \leqslant \int_ {0} ^ {t} | h (t - \sigma) | d \sigma \sup _ {0 \leqslant \sigma \leqslant \tau} | u (\sigma) | = \int_ {0} ^ {t} | h (s) | d s \sup _ {0 \leqslant \sigma \leqslant \tau} | u (\sigma) | \\ \end{array}
$$

因而有

$$\| y _ {\tau} \| _ {\mathcal {L} _ {\infty}} \leqslant \| h _ {\tau} \| _ {\mathcal {L} _ {1}} \| u _ {\tau} \| _ {\mathcal {L} _ {\infty}}, \forall \tau \in [ 0, \infty)$$

此不等式与式(5.2)相似,又不完全相同,因为在式(5.2)中常数 $\gamma$ 与 $\tau$ 无关。虽然 $\| h_{\tau} \|_{\mathcal{L}_1}$ 对于每个有限的 $\tau$ 是有限的,但可能对于 $\tau$ 不是一致有界的。例如,对于 $h(t) = e^t$ ,有 $\| h_{\tau} \|_{\mathcal{L}_1} = (e^\tau - 1)$ ,它在 $\tau \in [0, \infty)$ 区间内是有限的,但对于 $\tau$ 不是一致有界的。如果 $h \in \mathcal{L}_1$ ,不等式(5.2)成立,即

$$\| h \| _ {\mathcal {L} _ {1}} = \int_ {0} ^ {\infty} | h (\sigma) | d \sigma < \infty$$

这样,不等式 $\|y_{\tau}\|_{L_{\infty}}\leqslant\|h\|_{L_{1}}\|u_{\tau}\|_{L_{\infty}},\quad\forall\tau\in[0,\infty)$

说明系统是有限增益 $\mathcal{L}_{\infty}$ 稳定的。条件 $\| h \|_{\mathcal{L}_1} < \infty$ 实际上保证了对于每个 $p \in [1, \infty)$ ，系统的有限增益 $\mathcal{L}_p$ 稳定性。首先考虑 $p = 1$ 的情况，当 $t \leqslant \tau < \infty$ 时，有

$$\int_ {0} ^ {\tau} | y (t) | d t = \int_ {0} ^ {\tau} \left| \int_ {0} ^ {t} h (t - \sigma) u (\sigma) d \sigma \right| d t \leqslant \int_ {0} ^ {\tau} \int_ {0} ^ {t} | h (t - \sigma) | | u (\sigma) | d \sigma d t$$

交换积分次序,得

$$\int_ {0} ^ {\tau} | y (t) | d t \leqslant \int_ {0} ^ {\tau} | u (\sigma) | \int_ {\sigma} ^ {\tau} | h (t - \sigma) | d t d \sigma \leqslant \int_ {0} ^ {\tau} | u (\sigma) | \| h \| _ {\mathcal {L} _ {1}} d \sigma \leqslant \| h \| _ {\mathcal {L} _ {1}} \| u _ {\tau} \| _ {\mathcal {L} _ {1}}$$

这样， $\| y_{\tau}\|_{\mathcal{L}_1}\leqslant \| h\|_{\mathcal{L}_1}\| u_\tau \|_{\mathcal{L}_1},\forall \tau \in [0,\infty)$

现在考虑 $p \in (1, \infty)$ 的情况，设 $q \in (1, \infty)$ 满足 $1/p + 1/q = 1$ 。当 $t \leqslant \tau < \infty$ 时，有
