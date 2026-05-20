证明:首先证明对于任意常数 r>0, 存在一个常数 $b=b(r)>0$ , 使得当 $\omega(x(0))\leqslant r$ 时, 方程 (C.13) 的解对于所有 $t\geqslant0$ 都满足 $\omega(x(t))\leqslant b$ 。假设反过来不成立, 则存在一个方程 (C.13) 的解序列 $x^{(i)}(t)$ 及常数 $t_{i}$ , 使得 $\omega(x^{(i)}(0))\leqslant r(i=1,2,3,\cdots)$ 和 $\omega(x^{(i)}(t_{i}))>i(i=1,2,3,\cdots)$ 。设 $T^{*}$ 是所有 $T\geqslant0$ 的上确界, 使得对于所有 $t\in[0,T], x^{(i)}(t)(i=1,2,3,\cdots)$ 都是有限的, 即

$$T ^ {*} = \sup \{T \geqslant 0 \mid \lim _ {i \rightarrow \infty} \sup _ {0 \leqslant t \leqslant T} \left\{\max _ {0 \leqslant t \leqslant T} \left\{\omega (x ^ {(i)} (t)) \right\} < \infty \right\} \tag {C.16}$$

分别考虑 $T^{*} < \infty$ 和 $T^{*} = \infty$ 两种情况。当 $T^{*} < \infty$ 时，设 $\tau_{i}$ 是正常数序列，使得对于每个 $i \geqslant 1$

方程(C.13)的解满足

$$\omega (x (0)) \leqslant i \Rightarrow \omega (x (t)) \leqslant i + 1, \forall 0 \leqslant t \leqslant 2 \tau_ {i} \tag {C.17}$$

由于 $x(t)$ 的连续性, 因此该序列非空。我们总可以选择 $\tau_{i}$ 使得 $T^{*} > \tau_{1} > \tau_{2} > \cdots$ , 且 $\lim_{i \to \infty} \tau_{i} = 0$ 。设 $x^{(1,i)}(t)$ 是所有函数 $x^{(i)}(t)$ 中满足 $\omega(x^{(i)}(T^{*} - \tau_{1})) > 1$ 的序列, 则函数 $x^{(1,i)}(t)$ 形成一个无限序列。为了理解这一点, 设 $I_{1}$ 是所有不属于序列 $x^{(1,i)}(t)$ 的 $x^{(i)}(t)$ 中 i 构成的集合, 选择 $\tau_{1}$ , 使得

$$\omega \left(x ^ {(i)} (t)\right) \leqslant 2, \quad T ^ {*} - \tau_ {1} \leqslant t \leqslant T ^ {*} + \tau_ {1}, \forall i \in I \tag {C.18}$$

如果在序列 $x^{(1,i)}(t)$ 中，仅存在有限个函数 $x^{(i)}(t)$ ，那么由式(C.18)可知

$$\lim _ {i \rightarrow \infty} \sup \left\{\max _ {0 \leqslant t \leqslant T ^ {*} + \tau_ {1}} \left\{\omega \left(x ^ {(i)} (t)\right)\right\}\right\} < \infty \tag {C.19}$$

这与 $T^{*}$ 的定义式(C.16)相矛盾, 因此序列 $x^{(1,i)}(t)$ 是无限的。设 $x^{(2,i)}(t)$ 是所有函数 $x^{(1,i)}(t)$ 中满足 $\omega(x^{(1,i)}(T^{*}-\tau_{2}))>2$ 的序列, 重复前面的讨论可证明序列 $x^{(2,i)}(t)$ 也是无限的。重复进行上述步骤, 即可构造出一族子序列, 以序列 $\tilde{x}^{(i)}(t)$ 结束, 该序列满足

$$\omega \left(\tilde {x} ^ {(i)} \left(T ^ {*} - \tau_ {j}\right)\right) \geqslant j, \quad \forall j = 1, 2, 3, \dots , \quad \forall i = 1, 2, 3, \dots \tag {C.20}$$
