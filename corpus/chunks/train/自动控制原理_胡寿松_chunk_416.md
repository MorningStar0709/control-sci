# (2) 实数位移定理

实数位移定理又称平移定理。实数位移的含意，是指整个采样序列在时间轴上左右平移若干采样周期，其中向左平移为超前，向右平移为滞后。实数位移定理如下：

如果函数 $e(t)$ 是可拉氏变换的，其 $\pmb{z}$ 变换为 $E(z)$ ，则有

$$\mathcal {L} [ e (t - k T) ] = z ^ {- k} E (z) \tag {7-28}$$

以及 $\mathcal{L}[e(t + kT)] = z^k\Big[E(z) - \sum_{n=0}^{k-1}e(nT)z^{-n}\Big]$ (7-29)

其中 k 为正整数。

证明 由 $z$ 变换定义

$$\mathcal {L} [ e (t - k T) ] = \sum_ {n = 0} ^ {\infty} e (n T - k T) z ^ {- n} = z ^ {- k} \sum_ {n = 0} ^ {\infty} e [ (n - k) T ] z ^ {- (n - k)}$$

令 $m = n - k$ ，则有

$$\mathcal {L} [ e (t - k T) ] = z ^ {- k} \sum_ {m = - k} ^ {\infty} e (m T) z ^ {- m}$$

由于 $z$ 变换的单边性，当 $m < 0$ 时，有 $e(mT) = 0$ ，所以上式可写为

$$\mathcal {L} [ e (t - k T) ] = z ^ {- k} \sum_ {m = 0} ^ {\infty} e (m T) z ^ {- m}$$

再令 m=n，立即证得式(7-28)。

为了证明式(7-29)，取 $k = 1$ ，得

$$\mathcal {L} [ e (t + T) ] = \sum_ {n = 0} ^ {\infty} e (n T + T) z ^ {- n} = z \sum_ {n = 0} ^ {\infty} e [ (n + 1) T ] z ^ {- (n + 1)}$$

令 $m = n + 1$ ，上式可写为

$$
\begin{array}{l} \mathcal {L} [ e (t + T) ] = z \sum_ {m = 1} ^ {\infty} e (m T) z ^ {- m} = z \left[ \sum_ {m = 0} ^ {\infty} e (m T) z ^ {- m} - e (0) \right] \\ = z [ E (z) - e (0) ] \\ \end{array}
$$

取 $k = 2$ ，同理得

$$
\begin{array}{l} \mathcal {L} [ e (t + 2 T) ] = z ^ {2} \sum_ {m = 2} ^ {\infty} e (m T) z ^ {- m} = z ^ {2} \left[ \sum_ {m = 0} ^ {\infty} e (m T) z ^ {- m} - e (0) - z ^ {- 1} e (T) \right] \\ = z ^ {2} \left[ E (z) - \sum_ {n = 0} ^ {1} e (n T) z ^ {- n} \right] \\ \end{array}
$$

取 $k = k$ 时，必有

$$\mathcal {L} [ e (t + k T) ] = z ^ {k} \left[ E (z) - \sum_ {n = 0} ^ {k - 1} e (n T) z ^ {- n} \right]$$

在实数位移定理中，式(7-28)称为滞后定理；式(7-29)称为超前定理。显然可见，算子 $z$ 有明确的物理意义： $z^{-k}$ 代表时域中的滞后环节，它将采样信号滞后 $k$ 个采样周期；同理， $z^k$ 代表超前环节，它把采样信号超前 $k$ 个采样周期。但是， $z^k$ 仅用于运算，在物理系统中并不存在。

实数位移定理是一个重要定理,其作用相当于拉氏变换中的微分和积分定理。应用实数位移定理,可将描述离散系统的差分方程转换为 z 域的代数方程。有关差分方程的概念将在下节介绍。

例7-8 试用实数位移定理计算滞后一个采样周期的指数函数 $\mathrm{e}^{-a(t - T)}$ 的 $z$ 变换，其中 $a$ 为常数。

解 由式(7-28)

$$\mathcal {L} \left[ e ^ {- a (t - T)} \right] = z ^ {- 1} \mathcal {L} \left[ e ^ {- a t} \right] = z ^ {- 1} \cdot \frac {z}{z - e ^ {- a T}} = \frac {1}{z - e ^ {- a T}}$$
