定义5.1 如果存在定义在 $[0, \infty)$ 上的 $\kappa$ 类函数 $\alpha$ 和非负常数 $\beta$ , 对于所有 $u \in \mathcal{L}_e^m$ 和 $\tau \in [0, \infty)$

满足 $\| (Hu)_{\tau} \|_{\mathcal{L}} \leqslant \alpha (\| u_{\tau} \|_{\mathcal{L}}) + \beta$ (5.1)

则映射 $\mathcal{L}_e^m\to \mathcal{L}_e^q$ 是 $\mathcal{L}$ 稳定的。如果存在非负常数 $\gamma$ 和 $\beta$ ，对于所的 $u\in \mathcal{L}_e^m$ 和 $\tau \in [0,\infty)$

满足 $\| (Hu)_{\tau} \|_{\mathcal{L}} \leqslant \gamma \| u_{\tau} \|_{\mathcal{L}} + \beta$ (5.2)

则称该映射是有限增益L稳定的。

式(5.1)和式(5.2)中的常数 $\beta$ 称为偏项, 加在定义中是为了保证系统当 $u = 0$ 时, $Hu$ 不为零②。当不等式(5.2)成立时, 通常我们感兴趣的是对于最小的 $\gamma$ , 存在 $\beta$ 使式(5.2)成立。具有明确定义的 $\gamma$ 称为系统的增益。当存在 $\gamma \geqslant 0$ 满足不等式(5.2)时, 称系统的 $\mathcal{L}$ 增益小于或等于 $\gamma$ 。

对于因果L稳定系统,通过简单运算可以证明

$$u \in \mathcal {L} ^ {m} \Rightarrow H u \in \mathcal {L} ^ {q}$$

及 $\|Hu\|_{\mathcal{L}} \leqslant \alpha (\|u\|_{\mathcal{L}}) + \beta, \forall u \in \mathcal{L}^{m}$

对于因果有限增益L稳定系统,上述不等式应相应变为

$$\| H u \| _ {\mathcal {L}} \leqslant \gamma \| u \| _ {\mathcal {L}} + \beta , \forall u \in \mathcal {L} ^ {m}$$

对于有界输入-有界输出稳定性来说, $L_{\infty}$ 稳定性的定义是很常用的概念。也就是说,如果系统是 $L_{\infty}$ 稳定的,则对每个有界输入 $u(t)$ ,输出 $H u(t)$ 是有界的。

例 5.1 无记忆的,也可能是时变的函数 $h:[0,\infty)\times R\rightarrow R$ 可以看成算子 H, 它对于每个输入信号 $u(t)$ 赋予输出信号 $y(t)=h(t,u(t))$ 。我们用这一简单算子说明 L 稳定性的定义。设

$$h (u) = a + b \tanh c u = a + b \frac {e ^ {c u} - e ^ {- c u}}{e ^ {c u} + e ^ {- c u}}$$

其中 $a, b$ 和 $c$ 为非负常数。由

$$h ^ {\prime} (u) = \frac {4 b c}{\left(e ^ {c u} + e ^ {- c u}\right) ^ {2}} \leqslant b c, \forall u \in R$$

有 $|h(u)| \leqslant a + bc|u|, \forall u \in R$

因此， $H$ 是有限增益 $\mathcal{L}_{\infty}$ 稳定的，其中 $\gamma = bc, \beta = a$ 。进一步，如果 $a = 0$ ，则对于每个 $p \in [1, \infty)$ 有

$$\int_ {0} ^ {\infty} | h (u (t)) | ^ {p} d t \leqslant (b c) ^ {p} \int_ {0} ^ {\infty} | u (t) | ^ {p} d t$$

这样,对于每个 $p\in[1,\infty)$ ,算子H是有限增益 $L_{p}$ 稳定的,偏项为零,且 $\gamma=bc$ 。设h是时变函数,对于某个正常数a满足

$$| h (t, u) | \leqslant a | u |, \forall t \geqslant 0, \forall u \in R$$

则对于每个 $p \in [1, \infty)$ ，映射 $H$ 是有限增益 $\mathcal{L}_p$ 稳定的，偏项为零，且 $\gamma = a$ 。最后设

$$h (u) = u ^ {2}$$

由于 $\sup_{t\geqslant 0}|h(u(t))|\leqslant \left(\sup_{t\geqslant 0}|u(t)|\right)^2$

所以 $H$ 是 $\mathcal{L}_{\infty}$ 稳定的，偏项为零，且 $\alpha (r) = r^2$ 。但它不是有限增益 $\mathcal{L}_{\infty}$ 稳定的，因为对于所有 $u\in R$ ，函数 $h(u) = u^{2}$ 不以形如 $|h(u)|\leqslant \gamma |u| + \beta$ 的直线为界。

例 5.2 考虑一个单输入-单输出系统,由因果卷积运算

$$y (t) = \int_ {0} ^ {t} h (t - \sigma) u (\sigma) d \sigma$$
