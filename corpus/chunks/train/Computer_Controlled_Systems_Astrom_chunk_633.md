# Innovation's Representations

Theorem 10.3 has some conceptually important consequences. It follows from the theorem that a process with rational spectral density can be represented as

$$y (k) = \sum_ {n = - \infty} ^ {k} h (k - n) e (n) \tag {10.21}$$

where e is discrete-time white noise and h is the impulse response that corresponds to the pulse-transfer function (10.19). The system has a stable inverse if the polynomial $B(z)$ has all its zeros inside the unit disc. This means that

$$e (k) = \sum_ {n = - \infty} ^ {k} g (k - n) y (n)$$

where g is the impulse response, which corresponds to the stable pulse-transfer function $A(z)/B(z)$ . It thus follows that the sequences $y(k), y(k-1), \ldots$ and $e(k), e(k - 1), \ldots$ are equivalent in the sense that one sequence can be calculated from the other.

![](image/bcfacda51ced83fd5325ac82cf541325078f298a7947e863ca525baf49081a09.jpg)

<details>
<summary>scatter</summary>

| Point Type | Real | Imaginary |
| --- | --- | --- |
| Circle | -2.0 | 0.0 |
| Circle | -0.5 | 0.0 |
| Cross | 0.5 | 0.5 |
| Cross | 1.0 | -1.0 |
| Cross | 1.0 | 1.0 |
</details>

Figure 10.7 Symmetry of the poles and zeros of the spectral-density function (10.20).

Now consider

$$
\begin{array}{l} y (k + 1) = \sum_ {n = - \infty} ^ {k + 1} h (k + 1 - n) e (n) = \sum_ {n = - \infty} ^ {k} h (k + 1 - n) e (n) + h (0) e (k + 1) \\ = \sum_ {n = - \infty} ^ {k} h (k + 1 - n) \sum_ {l = - \infty} ^ {k} g (n - l) y (l) + h (0) e (k + 1) \\ \end{array}
$$

The variable $y(k+1)$ can be written as the sum of two terms: One term is a linear function of $y(k), y(k-1), \ldots$ , and the other term is $h(0)e(k+1)$ . Thus $e(k+1)$ can be interpreted as the part of $y(k+1)$ that contains new information that is not available in the past values $y(k), y(k-1), \ldots$ . The stochastic process $e(k)$ is therefore called the innovations of the process $y(k)$ and the representation in (10.21) is called the innovation's representation of the process. This representation is important in connection with filtering and prediction problems. The term

$$\sum_ {n = - \infty} ^ {k} h (k + 1 - n) \sum_ {l = - \infty} ^ {n} g (n - l) y (l)$$

is in fact the best mean-square prediction of $y(k + 1)$ based on $y(k), y(k - 1), \ldots$ . This will be discussed in detail in Chapters 11 and 12.
