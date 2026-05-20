# (4) 终值定理

如果函数 $e(t)$ 的 z 变换为 $E(z)$ ，函数序列 $e(nT)$ 为有限值 $(n=0,1,2,\cdots)$ ，且极限 $\lim_{n\to\infty}e(nT)$ 存在，则函数序列的终值

$$\lim _ {n \to \infty} e (n T) = \lim _ {z \to 1} (z - 1) E (z) \tag {7-31}$$

证明 由 z 变换线性定理,有

$$\mathcal {L} [ e (t + T) ] - \mathcal {L} [ e (t) ] = \sum_ {n = 0} ^ {\infty} \{e [ (n + 1) T ] - e (n T) \} z ^ {- n}$$

由平移定理

$$\mathcal {L} [ e (t + T) ] = z E (z) - z e (0)$$

于是 $(z - 1)E(z) - ze(0) = \sum_{n=0}^{\infty}\{e[(n+1)T] - e(nT)\} z^{-n}$

上式两边取 $z \to 1$ 时的极限，得

$$
\begin{array}{l} \lim _ {z \rightarrow 1} (z - 1) E (z) - e (0) = \lim _ {z \rightarrow 1} \sum_ {n = 0} ^ {\infty} \{e [ (n + 1) T ] - e (n T) \} z ^ {- n} \\ = \sum_ {n = 0} ^ {\infty} \left\{e [ (n + 1) T ] - e (n T) \right\} \\ \end{array}
$$

当取 n=N 为有限项时，上式右端可写为

$$\sum_ {n = 0} ^ {N} \{e [ (n + 1) T ] - e (n T) \} = e [ (N + 1) T ] - e (0)$$

令 $N\to \infty$ ，有

$$
\begin{array}{l} \sum_ {n = 0} ^ {\infty} \{e [ (n + 1) T ] - e (n T) ] = \lim _ {N \rightarrow \infty} \{e [ (N + 1) T ] - e (0) \} \\ = \lim _ {n \rightarrow \infty} e (n T) - e (0) \\ \end{array}
$$

所以 $\lim_{n\to \infty}e(nT) = \lim_{z\to 1}(z - 1)E(z)$

z 变换的终值定理形式亦可表示为

$$e (\infty) = \lim _ {n \rightarrow \infty} e (n T) = \lim _ {z \rightarrow 1} (1 - z ^ {- 1}) E (z) \tag {7-32}$$

读者不妨自行论证。在离散系统分析中，常采用终值定理求取系统输出序列的终值误差，或称稳态误差。

例7-10 设 $z$ 变换函数为

$$E (z) = \frac {0 . 7 9 2 z ^ {2}}{(z - 1) (z ^ {2} - 0 . 4 1 6 z + 0 . 2 0 8)}$$

试利用终值定理确定 $e(nT)$ 的终值。

解 由终值定理(7-31)得

$$
\begin{array}{l} e _ {s} (\infty) = \lim _ {z \rightarrow 1} (z - 1) \cdot \frac {0 . 7 9 2 z ^ {2}}{(z - 1) (z ^ {2} - 0 . 4 1 6 z + 0 . 2 0 8)} \\ = \lim _ {z \rightarrow 1} \frac {0 . 7 9 2 z ^ {2}}{z ^ {2} - 0 . 4 1 6 z + 0 . 2 0 8} = 1 \\ \end{array}
$$
