$$\left(\Delta_ {1}, \dots , \Delta_ {k _ {s}}\right) = \left(\Delta_ {1} ^ {1}, \dots , \Delta_ {d _ {1}} ^ {1}, \dots , \Delta_ {1} ^ {s}, \dots , \Delta_ {d _ {s}} ^ {s}\right).$$

$\Delta_{i}$ 的正交余分布记作 $\Omega_{k_{n} + 1 - i}$ . 于是可得一个余分布序列

$$\Omega_ {1}, \dots , \Omega_ {k _ {s}},$$

这里 $i$ 个元素是 $\{\Delta_t\}$ 序列中最后 $i$ 个元素的正交余向量场。相应于 $\{\Delta_j^i\}$ ，对偶序列的元素用双重指标记为

$$\{\Omega_ {1}, \dots , \Omega_ {k _ {s}} \} = \{\Omega_ {1} ^ {1}, \dots , \Omega_ {d _ {s}} ^ {1}, \dots , \Omega_ {1} ^ {2}, \dots , \Omega_ {d _ {s - 1}} ^ {2}, \dots , \Omega_ {1} ^ {s}, \dots , \Omega_ {d _ {1}} ^ {s} \}.$$

那么

$$\Omega_ {j} ^ {i} = \left(\Delta_ {d _ {s + 1 - i} + 1 - j} ^ {s + 1 - i}\right) ^ {\perp}.$$

现在 $\Delta_{d_{s}}^{s}$ 为对合分布，且余维数为 $m_{s}$ ，由 Frobenius 定理，存在光滑函数 $z_{1}, \cdots, z_{m_{s}}$ ，使得

$$\Omega_ {1} ^ {1} = \operatorname{span} \left\{\mathrm{d} z _ {1}, \dots , \mathrm{d} z _ {m _ {s}} \right\}.$$

于是可知

$$
D _ {s} := \left[ \begin{array}{c} \mathrm{d} z _ {1} ^ {1} \\ \vdots \\ \mathrm{d} z _ {m _ {s}} ^ {1} \end{array} \right] [ \mathrm{ad} _ {f} ^ {k _ {s} - 1} g _ {1} \dots \mathrm{ad} _ {f} ^ {k _ {s} - 1} g _ {m _ {s}} ] \tag {8.3.17}
$$

非奇异. 下面证明

$$\mathrm{d} L _ {f} ^ {k} z _ {j}, \quad j = 1, \dots , m _ {s}; k = 1, \dots , k _ {s} - 1$$

线性无关. 类似于式 (8.3.11) 的证明, 我们可以证明下面的公式:

$$
\left\langle L _ {f} ^ {k} \omega , g \right\rangle = \sum_ {i = 1} ^ {k} (- 1) ^ {i} \left[ \begin{array}{l} k \\ i \end{array} \right] L _ {f} ^ {k - i} \left\langle \omega , \mathrm{ad} _ {f} ^ {i} g \right\rangle . \tag {8.3.18}
$$

现在假定

$$\sum_ {i = 1} ^ {k _ {s} - 1} \sum_ {j = 1} ^ {m _ {s}} c _ {j} ^ {i} \mathrm{d} L _ {f} ^ {i} z _ {j} = 0.$$

利用式 (8.3.18), 可得到

$$
\begin{array}{l} \left\langle \sum_ {i = 1} ^ {k _ {s} - 1} \sum_ {j = 1} ^ {m _ {s}} c _ {j} ^ {i} \mathrm{d} L _ {f} ^ {i} z _ {j}, [ g _ {1}, \dots , g _ {m} ] \right\rangle \\ = \left[ c _ {1} ^ {k _ {s} - 1} \quad \dots \quad c _ {m _ {s}} ^ {k _ {s} - 1} \right] \left\langle \left[ \begin{array}{c} \mathrm{d} z _ {1} ^ {1} \\ \vdots \\ \mathrm{d} z _ {m _ {s}} ^ {1} \end{array} \right] \left[ \mathrm{ad} _ {f} ^ {k _ {s} - 1} g _ {1} \quad \dots \quad \mathrm{ad} _ {f} ^ {k _ {s} - 1} g _ {m _ {s}} \right] \right\rangle = 0. \\ \end{array}
$$

因此 $c_{1}^{k_{s}-1}=\cdots=c_{m_{s}}^{k_{s}-1}=0$ 。下面考察

$$\left\langle \sum_ {i = 1} ^ {k _ {s} - 2} \sum_ {j = 1} ^ {m _ {s}} c _ {j} ^ {i} \mathrm{d} L _ {f} ^ {i} z _ {j}, [ \operatorname{ad} _ {f} g _ {1}, \dots , \operatorname{ad} _ {f} g _ {m} ] \right\rangle = 0.$$
