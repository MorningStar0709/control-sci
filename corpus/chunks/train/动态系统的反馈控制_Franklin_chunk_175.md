# 3.6.1 有界输入有界输出稳定性

如果系统的每个有界输入对应一个有界输出(不管系统内部发生什么)，则称该系统具有有界输入有界输出(BIBO)稳定性。当系统响应由卷积给出时，则可判定系统的特性。如果系统输入为 $u(t)$ ，输出为 $y(t)$ ，脉冲响应为 $h(t)$ ，那么有

$$y (t) = \int_ {- \infty} ^ {+ \infty} h (\tau) u (t - \tau) \mathrm{d} t \tag {3.83}$$

如果输入 $u(t)$ 是有界的，则存在一个常数 $M$ ，使得 $\vert u\vert \leqslant M < \infty$ ，且输出界限为

$$
\begin{array}{l} | y | = \left| \int h u d \tau \right| \\ \leqslant \int | h | | u | d \tau \\ \leqslant M \int_ {- \infty} ^ {+ \infty} | h (\tau) | \mathrm{d} \tau \\ \end{array}
$$

因此，如果 $\int_{-\infty}^{+\infty}|h|\mathrm{d}\tau$ 是有界的，那么输出也是有界的。

换句话说，假设积分不是有界的，如果 $h(\tau) > 0$ ，则有界输入 $u(t - \tau) = +1$ ，如果 $h(\tau) <   0$ ，则 $u(t - \tau) = -1$ ，在这种情况下，有

$$y (t) = \int_ {- \infty} ^ {+ \infty} | h (\tau) | \mathrm{d} \tau \tag {3.84}$$

输出是无界的。我们可得出结论

当且仅当积分

$$\int_ {- \infty} ^ {+ \infty} | h (\tau) | \mathrm{d} \tau < + \infty$$

时，具有脉冲响应 $h(t)$ 的系统具有有界输入有界输出 (BIBO) 稳定性。
