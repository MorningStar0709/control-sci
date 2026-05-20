# THEOREM 2.8 Parseval's theorem

Let

$$H (q ^ {- 1}) = \sum_ {k = 0} ^ {\infty} h _ {k} q ^ {- k}G (q ^ {- 1}) = \sum_ {k = 0} ^ {\infty} g _ {k} q ^ {- k}$$

be two stable transfer functions, and let $e(t)$ be white noise of zero mean and covariance $\sigma^{2}$ . Then

$$\sigma^ {2} \sum_ {k = 0} ^ {\infty} h _ {k} g _ {k} = \frac {\sigma^ {2}}{2 \pi} \int_ {- \pi} ^ {\pi} H (e ^ {i \omega}) G (e ^ {i \omega}) d \omega$$

□

Remark. The left-hand side can be interpreted as $E\left(H(q^{-1})e(t)\cdot G(q^{-1})e(t)\right)$ , that is, the covariance of the two signals obtained by sending white noise through the transfer functions $H(q^{-1})$ and $G(q^{-1})$ .
