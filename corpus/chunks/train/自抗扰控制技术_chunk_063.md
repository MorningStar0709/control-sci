这个引理是说,如果 $x(t)$ 趋于零,那么足够压缩其时间尺度 $\tau=\frac{t}{r}, r>1$ ,可以使它在有限时间区间上的积分值足够小.

例如， $x(t)=\mathrm{e}^{-t}$ 是趋于零的函数。现在把现时的时间t的尺度压缩r倍，即 $t=r\tau$ ，那么 $z(r,\tau)=x(r\tau)=\mathrm{e}^{-r\tau}$ 。显然 $z(r,\tau)=\mathrm{e}^{-r\tau}$ 的收敛速度加快了很多，从而使它在有限区间上的积分值变的很小。对 $\gamma=1/2,1,2$ 的情形如图2.3.5所示。

![](image/d6754b4ca3555d79cf428ba9709690a643f37fa85c150c5c727acb89a5ac09e8.jpg)

<details>
<summary>line</summary>

| x | e^-2+ | e^-3+ | e^-4+ |
| --- | --- | --- | --- |
| 0 | 0.9 | 0.9 | 0.9 |
| 2 | 0.5 | 0.4 | 0.3 |
| 4 | 0.3 | 0.2 | 0.15 |
| 6 | 0.2 | 0.15 | 0.1 |
| 8 | 0.15 | 0.1 | 0.08 |
| 10 | 0.1 | 0.08 | 0.05 |
</details>

图2.3.5

引理2 若系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) \end{array} \right. \tag {2.3.17}
$$

的任意解都满足: $x_{1}(t)\rightarrow0,x_{2}(t)\rightarrow0(t\rightarrow0)$ ，则对任意给定的常数c，系统

$$
\left\{ \begin{array}{l} \dot {z} _ {1} = z _ {2} \\ \dot {z} _ {2} = r ^ {2} f \left(z _ {1} - c, \frac {z _ {2}}{r}\right) \end{array} \right. \tag {2.3.18}
$$

的解 $z_{1}(r,t)$ ，对任意 $T > 0$ ，都满足

$$\lim _ {r \rightarrow \infty} \int_ {0} ^ {T} | z _ {1} (r, \tau) - c | \mathrm{d} \tau = 0 \tag {2.3.19}$$

引理3 如果两个有界可积函数 $v(t)$ 和 $v'(t)$ 在任意有限区间上，按某种测度充分接近，如满足

$$\int_ {0} ^ {T} | v (t) - v ^ {\prime} (t) | \mathrm{d} t < \mathrm{e} ^ {L (1 + T) T} \varepsilon / T, \forall T > 0 \tag {2.3.20}$$

那么两个初值问题

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1} - v (t), x _ {2}) \end{array} \right.,

\left\{ \begin{array}{l l} \dot {x} _ {1} ^ {\prime} = x _ {2} ^ {\prime}, & x _ {1} ^ {\prime} (0) = x _ {1} (0) \\ \dot {x} _ {2} ^ {\prime} = f (x _ {1} ^ {\prime} - v ^ {\prime} (t), x _ {2} ^ {\prime}), & x _ {2} ^ {\prime} (0) = x _ {2} (0) \end{array} \right. \tag {2.3.21}
$$

的解 $x_{1}(t)$ 和 $x_1'(t)$ 将在这个区间上满足

$$\int_ {0} ^ {T} \mid x _ {1} (t) - x _ {1} ^ {\prime} (t) \mid \mathrm{d} t < \varepsilon$$

引理 4 在引理 3 的条件下,两个初值问题

$$
\left\{ \begin{array}{l l} \dot {z} _ {1} = z _ {2}, & z _ {1} (0) = x _ {1} ^ {0} \\ \dot {z} _ {2} = r ^ {2} f \left(z _ {1} - v (t), \frac {z _ {2}}{r}\right), & z _ {2} (0) = r x _ {2} ^ {0} \end{array} \right. \tag {2.3.22}

\left\{ \begin{array}{l l} \dot {z} _ {1} ^ {\prime} = z _ {2} ^ {\prime}, & z _ {1} ^ {\prime} (0) = z _ {1} (0) \\ \dot {z} _ {2} ^ {\prime} = r ^ {2} f \left(z _ {1} ^ {\prime} - v ^ {\prime} (t), \frac {z _ {2} ^ {\prime}}{r}\right), & z _ {2} ^ {\prime} (0) = z _ {2} (0) \end{array} \right.
$$

的解 $z_{1}(r,t)$ 和 $z_1'(r,t)$ ，对任意 $T > 0$ ，将满足
