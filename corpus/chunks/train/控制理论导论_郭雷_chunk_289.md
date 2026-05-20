# 收敛性及收敛定理

设 $\{\xi_k\}$ 为随机变量序列.

以概率 1 或 a.s. 收敛 设除了一个可能的零概率集外, 对一切 $\omega \in \Omega$ , $\xi_k(\omega) \xrightarrow{k \to \infty} \xi(\omega)$ , 那么叫 $\xi_k$ a.s. (以概率 1) 收敛到 $\xi$ .

$\xi_{k}$ 收敛到有穷的 $\xi$ 的 $\omega$ 集为

$$[ \xi_ {k} \rightarrow \xi ] = \bigcap_ {j = 1} ^ {\infty} \bigcup_ {k = 1} ^ {\infty} \bigcap_ {s = 1} ^ {\infty} \left[ | \xi_ {k + s} - \xi | < \frac {1}{j} \right], \tag {4.1.19}$$

它是可测集．和实数列一样， $\xi_{k}$ 收敛到 $\xi$ ，等价于 $\xi_{k}$ Cauchy 收敛．Cauchy 收敛的 $\omega$ 集为

$$\bigcap_ {s = 1} ^ {\infty} \left[ \xi_ {k + s} - \xi_ {k} \rightarrow 0 \right] = \bigcap_ {j = 1} ^ {\infty} \bigcup_ {k = 1} ^ {\infty} \bigcap_ {s = 1} ^ {\infty} \left[ | \xi_ {k + s} - \xi_ {k} | < \frac {1}{j} \right], \tag {4.1.20}$$

显然它也是可测集.

随机变量 $\xi_{k}\rightarrow \xi <  \infty$ a.s.的充分必要条件是对任意 $\epsilon >0,$

$$P \bigcup_ {s = 1} ^ {\infty} \left[ | \xi_ {k + s} - \xi | \geqslant \epsilon \right] \underset {k \rightarrow \infty} {\longrightarrow} 0, \tag {4.1.21}$$

$\{\xi_k\}$ a.s. Cauchy 收敛的充分必要条件是对任意 $\epsilon > 0$ ,

$$P \bigcup_ {s = 1} ^ {\infty} \left[\left| \xi_ {k + s} - \xi_ {k} \right| \geqslant \epsilon \right] \underset {k \rightarrow \infty} {\longrightarrow} 0.$$

依概率收敛 如果对任意 $\epsilon > 0$

$$P [ | \xi_ {k + s} - \xi | \geqslant \epsilon ] \underset {k \rightarrow \infty} {\longrightarrow} 0, \tag {4.1.22}$$

那么称 $\xi_{k}$ 依概率收敛到 $\xi$ , 记作 $\xi_{k} \xrightarrow[k \to \infty]{P} \xi$ . 它等价于 $\xi_{k}$ 依概率相互收敛

$$P [ | \xi_ {k + s} - \xi_ {k} | \geqslant \epsilon ] \underset {k \to \infty} {\longrightarrow} 0, \quad \text {对} s \text {一致}.$$

比较式 (4.1.21) 及式 (4.1.22) 可看出， $\xi_{k}$ a.s. 收敛到 $\xi$ ，包含 $\xi_{k}$ 依概率收敛到 $\xi$ .

均方收敛 如果 $E|\xi_k - \xi|^2 \underset{k \to \infty}{\longrightarrow} 0$ ，则称 $\xi_k$ 均方收敛到 $\xi$ .

由 Chebyshev 不等式知

$$P [ | \xi_ {k} - \xi | ^ {p} \geqslant \epsilon ] \leqslant \frac {E | \xi_ {k} - \xi | ^ {p}}{\epsilon^ {p}}, \quad p > 0.$$

所以均方收敛包含依概率收敛 (我们在上面已定义了).

依分布收敛 如果在 $\xi$ 的分布函数 $F_{\xi}(\cdot)$ 的所有连续点 $x$ 上， $\xi_k$ 的分布函数 $F_{\xi_k}(x) \underset{k \to \infty}{\longrightarrow} F_{\xi}(x)$ ，那么称 $\xi_k$ 依分布收敛到 $\xi$ ，或 $\xi_k$ 弱收敛到 $\xi$ 。

设 $\xi_{k} \xrightarrow[k \to \infty]{P} \xi$ , 那么 $\xi_{k} \xrightarrow[k \to \infty]{w} \xi$ .

为证此点，设 $x$ 为 $\xi$ 的分布函数 $F_{\xi}(\cdot)$ 的连续点.

由于

$$[ \xi < x ^ {\prime} ] = [ \xi_ {k} < x, \xi < x ^ {\prime} ] \cup [ \xi_ {k} \geqslant x, \xi < x ^ {\prime} ] \subset [ \xi_ {k} < x ] \cup [ \xi_ {k} \geqslant x, \xi < x ^ {\prime} ],$$

所以当 $x' < x$ 时，就有
