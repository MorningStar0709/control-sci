# 基本不等式

设 $g(\cdot)$ 为 Borel 函数，即对任一 Borel 集 $\mathbf{B}, \{x : g(x) \in B\}$ 也是 Borel 集。若 $\xi$ 为随机变量，那么 $g(\xi)$ 也是随机变量。所以下面提到的随机变量的函数也是随机变量。

注意到当 $0 \leqslant a < b$ 时， $|\xi|^a \leqslant 1 + |\xi|^b$ ，所以当 $E|\xi|^b < \infty$ 时，必有 $E|\xi|^a < \infty$ 。也就是说，高阶绝对矩有穷时，低阶绝对矩也有穷。

$C_{r}$ -不等式 设 $\xi$ 和 $\eta$ 为随机变量，那么

$$E | \boldsymbol {\xi} + \boldsymbol {\eta} | ^ {r} \leqslant c _ {r} (E | \boldsymbol {\xi} | ^ {r} + E | \boldsymbol {\eta} | ^ {r}), \tag {4.1.14}$$

其中常数 $c_{r} = \left\{ \begin{array}{ll}1, & 0\leqslant r\leqslant 1,\\ 2^{r - 1}, & r > 1. \end{array} \right.$

证明 只要对 $a > 0, b > 0$ 证明下列初等不等式：

$$(a + b) ^ {r} \leqslant c _ {r} (a ^ {r} + b ^ {r}). \tag {4.1.15}$$

设 $r \geqslant 1$ . 考察函数

$$g (x) = (a + x) ^ {r} - 2 ^ {r - 1} \left(a ^ {r} + x ^ {r}\right).$$

求导得

$$g ^ {\prime} (x) = r (a + x) ^ {r - 1} - r 2 ^ {r - 1} x ^ {r - 1}.$$

那么

$$
g ^ {\prime} (x) \left\{ \begin{array}{l l} > 0, & x <   a, \\ = 0, & x = a, \\ <   0, & x > a. \end{array} \right.
$$

所以

$$g (b) \leqslant \max g (x) = g (a) = 0.$$

由此得式 (4.1.15).

设 $r < 1$ , 不失一般性可设 $b \geqslant a$ , 那么用 Taylor 展式知

$$(a + b) ^ {r} = b ^ {r} \left(1 + \frac {a}{b}\right) ^ {r} \leqslant b ^ {r} \left(1 + \left(\frac {a}{b}\right) ^ {r}\right),$$

由此也得式 (4.1.15). 由式 (4.1.15) 立即得到式 (4.1.14).

Hölder 不等式 设 $1 < p < \infty, 1 < q < \infty, \frac{1}{p} + \frac{1}{q} = 1$ , 若 $E|\xi|^p < \infty, E|\eta|^q < \infty$ , 那么

$$E | \xi \eta | \leqslant (E | \xi | ^ {p}) ^ {\frac {1}{p}} (E | \eta | ^ {q}) ^ {\frac {1}{q}}. \tag {4.1.16}$$

证明 如果 $E|\xi|^p = 0$ 或 $E|\eta|^q = 0$ , 则 $\xi \eta = 0$ a.s., (4.1.16) 显然. 所以只考虑 $E|\xi|^p \neq 0$ , $E|\eta|^q \neq 0$ .

由于 $\log x$ 为凹函数，所以当 $r + s = 1, r > 0, s > 0$ 时，有

$$\log (r x + s y) \geqslant r \log x + s \log y = \log x ^ {r} y ^ {s}.$$

在这个不等式中取

$$x = \frac {| \xi | ^ {p}}{E | \xi | ^ {p}}, \quad y = \frac {| \eta | ^ {q}}{E | \eta | ^ {q}}, \quad r = \frac {1}{p}, \quad s = \frac {1}{q},$$

就得到

$$\frac {| \xi |}{(E | \xi | ^ {p}) ^ {\frac {1}{p}}} \cdot \frac {| \eta |}{(E | \eta | ^ {q}) ^ {\frac {1}{q}}} \leqslant \frac {| \xi | ^ {p}}{p E | \xi | ^ {p}} + \frac {| \eta | ^ {q}}{q E | \eta | ^ {q}}.$$

对上式取期望后就得式 (4.1.16)

$$\frac {E | \xi \eta |}{(E | \xi | ^ {p}) ^ {\frac {1}{p}} (E | \eta | ^ {q}) ^ {\frac {1}{q}}} \leqslant \frac {1}{p} + \frac {1}{q} = 1.$$

注4.1.1 当 $p = q = 2$ 时，Hölder不等式也叫Schwarz不等式，

$$E | \xi \eta | \leqslant (E | \xi | ^ {2}) ^ {\frac {1}{2}} (E | \eta | ^ {2}) ^ {\frac {1}{2}}.$$

Minkowski 不等式 设 $r \geqslant 1$ , 那么
