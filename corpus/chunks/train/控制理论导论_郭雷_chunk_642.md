$$
\begin{array}{l} y (t) = h \left(x _ {0}\right) + \sum_ {k = 0} ^ {\infty} \sum_ {i _ {k}, \dots , i _ {0} = 0} ^ {m} L _ {g _ {i _ {0}}} \dots L _ {g _ {i _ {k}}} h \left(x _ {0}\right) \tag {8.5.21} \\ \times \int_ {0} ^ {t} d \xi_ {i _ {k}} \dots d \xi_ {i _ {0}}, \quad j = 1, \dots , p, 0 \leqslant t \leqslant T. \\ \end{array}
$$

证明 给定解析输入 $u_{1}, u_{2}, \cdots, u_{m}$ ，用 $z(t)$ 表示式 (8.5.19) 的右边。那么， $z(t)$ 及 $y(t)$ 均为解析函数。所以，只要证明式 (8.5.21) 的两边在 t = 0 处有相同的各阶导数，则它们的 Taylor 展开式一样。因此，在收敛域内，它们相等。这就是我们证明的思路。

先考虑 $y(t)$ ，由式(8.5.19)可知

$$y (0) = h \left(x _ {0}\right),\dot {y} (t) = \langle \mathrm{d} h, \dot {x} \rangle = \sum_ {i = 0} ^ {m} L g _ {i} h u _ {i},\dot {y} (0) = \sum_ {i = 0} ^ {m} L _ {g _ {i}} h \left(x _ {0}\right) u _ {i}.$$

为方便起见，引入记号

$$\sum_ {i _ {s}, \dots , i _ {1} = 0} ^ {m} L _ {g _ {i _ {s}}} L _ {g _ {i _ {s - 1}}} \dots L _ {g _ {i _ {1}}} h (x) u _ {i _ {1}} ^ {(q _ {1})} \dots u _ {i _ {s}} ^ {(q _ {s})} = \sum_ {i _ {s}, \dots , i _ {1}} \langle h \rangle u _ {i _ {1}} ^ {(q _ {1})} \dots u _ {i _ {s}} ^ {(q _ {s})}.$$

相应地，它在 $x_0$ 点值为

$$\sum_ {i _ {s}, \dots , i _ {1}} \langle h _ {0} \rangle u _ {i _ {1}} ^ {(q _ {1})} \dots u _ {i _ {s}} ^ {(q _ {s})}$$

假定

$$y ^ {(k)} (t) = \sum_ {p} \sum_ {i _ {s p} ^ {p}, \dots , i _ {1} ^ {p}} \langle h \rangle u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s p} ^ {p}} ^ {\left(q _ {s p} ^ {p}\right)}, \tag {8.5.22}$$

那么由式 (8.5.18) 可直接推出

$$
\begin{array}{l} y ^ {(k + 1)} (t) = \sum_ {p} \sum_ {i _ {s p} ^ {p}, \dots , i _ {1} ^ {p}} \langle h \rangle \frac {\mathrm{d}}{\mathrm{d} t} \left(u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s p} ^ {p}} ^ {\left(q _ {s p} ^ {p}\right)}\right) (3-20) \\ + \sum_ {p} \sum_ {i _ {s p + 1} ^ {p}, i _ {s p} ^ {p}, \dots , i _ {1} ^ {p}} \langle h \rangle u _ {i _ {1} ^ {p}} ^ {(q _ {1} ^ {p})} \dots u _ {i _ {s p} ^ {p}} ^ {(q _ {s p} ^ {p})} u _ {i _ {s p + 1} ^ {p}} ^ {(q _ {s p + 1} ^ {p})}. (8.5.23) \\ \end{array}
$$

注意，在式(8.5.22)中对 $p$ 求和仅表示有有限多个 $\sum_{p}$ 后的那种形式的项求和。由前面计算可知， $k = 1$ 时式(8.5.22)显见成立。另一方面，式(8.5.23)经简单整理即得式(8.5.22)的形式。由此可知，式(8.5.22)对一切 $k$ 成立。另外，式(8.5.23)也给出从 $y^{(k)}(t)$ 到 $y^{(k + 1)}(t)$ 的递推算法。

下面求 $z(t)$ 的各阶导数．为方便起见，记

$$\sum_ {k = 0} ^ {\infty} \sum_ {i _ {0}, \dots , i _ {k} = 0} ^ {m} L g _ {i _ {0}} L g _ {i _ {1}} \dots L g _ {i _ {k}} (\varphi (x)) \int_ {0} ^ {t} d \xi_ {i _ {k}} \dots d \xi_ {i _ {0}} = \sum \langle \langle \varphi (x) \rangle \rangle .$$

设级数 $z(t)$ 可逐项求导，则由式(8.5.21)可知
