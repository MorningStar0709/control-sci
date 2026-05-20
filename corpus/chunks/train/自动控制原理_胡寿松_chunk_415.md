# (1) 线性定理

若 $E_{1}(z) = \mathcal{X}[e_{1}(t)], E_{2}(z) = \mathcal{X}[e_{2}(t)], a$ 为常数，则

$$\mathcal {L} \big [ e _ {1} (t) \pm e _ {2} (t) \big ] = E _ {1} (z) \pm E _ {2} (z) \tag {7-26}\mathcal {L} [ a e (t) ] = a E (z) \tag {7-27}$$

其中， $E(z)=\mathcal{L}[e(t)]$ 。

证明 由 $z$ 变换定义

$$
\begin{array}{l} \mathcal {L} [ e _ {1} (t) \pm e _ {2} (t) ] = \sum_ {n = 0} ^ {\infty} [ e _ {1} (n T) \pm e _ {2} (n T) ] z ^ {- n} \\ = \sum_ {n = 0} ^ {\infty} e _ {1} (n T) z ^ {- n} \pm \sum_ {n = 0} ^ {\infty} e _ {2} (n T) z ^ {- n} = E _ {1} (z) \pm E _ {2} (z) \\ \end{array}
$$

以及 $\mathcal{L}[ae(t)] = a\sum_{n=0}^{\infty}e(nT)z^{-n} = aE(z)$

式(7-26)和式(7-27)表明，z变换是一种线性变换，其变换过程满足齐次性与均匀性。
