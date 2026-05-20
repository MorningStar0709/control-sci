$$
\begin{array}{l} z ^ {(k + 1)} (t) = \sum_ {p} \sum_ {i _ {s p} ^ {p}, \dots , i _ {1} ^ {p}} \left\langle h _ {0} \right\rangle \frac {\mathrm{d}}{\mathrm{d} t} \left(u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s p} ^ {p}} ^ {\left(q _ {s p} ^ {p}\right)}\right) \\ + \sum \left\langle \left\langle \sum_ {p} \sum_ {i _ {i _ {p}} ^ {p}, \dots , i _ {1} ^ {p}} \left\langle h _ {0} \right\rangle \frac {\mathrm{d}}{\mathrm{d} t} \left(u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s p} ^ {p}} ^ {\left(q _ {s p} ^ {r}\right)}\right) \right\rangle \right\rangle \\ + \sum_ {p} \sum_ {i _ {s p + 1} ^ {p}, \dots , i _ {1} ^ {p}} \left\langle h _ {0} \right\rangle u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s p} ^ {p}} ^ {\left(q _ {s p} ^ {p}\right)} u _ {i _ {s p + 1} ^ {p}} ^ {\left(q _ {s p + 1} ^ {p}\right)} \\ + \sum \left\langle \left\langle \sum_ {p} \sum_ {i _ {s p + 1} ^ {p}, \dots , i _ {1} ^ {p}} \langle h _ {0} \rangle u _ {i _ {1} ^ {p}} ^ {(q _ {1} ^ {p})} \dots u _ {i _ {s p} ^ {p}} ^ {(q _ {s p} ^ {p})} u _ {i _ {s p + 1} ^ {p}} ^ {q _ {s p + 1} ^ {p}} \right\rangle \right\rangle . \\ \end{array}
$$

经简单整理即可看出， $z^{(k + 1)}(t)$ 仍有式(8.5.26)的形式，这证明了式(8.5.26)的正确性．由式(8.5.26)即可推出

$$
z ^ {(k)} (0) = \sum_ {p} \sum_ {i _ {s _ {p}} ^ {p}, \dots , i _ {1} ^ {p}} \left\langle h _ {0} \right\rangle u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s _ {p}} ^ {p}} ^ {\left(q _ {s _ {p}} ^ {p}\right)}, \tag {8.5.27}
\begin{array}{l} z ^ {(k + 1)} (0) = \sum_ {p} \sum_ {i _ {s p} ^ {p}, \dots , i _ {1} ^ {p}} \left\langle h _ {0} \right\rangle \frac {\mathrm{d}}{\mathrm{d} t} \left(u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s p} ^ {p}} ^ {\left(q _ {s p} ^ {p}\right)}\right) \\ + \sum_ {p} \sum_ {i _ {s p + 1} ^ {p}, i _ {s p} ^ {p}, \dots , i _ {1} ^ {p}} \left\langle h _ {0} \right\rangle u _ {i _ {1} ^ {p}} ^ {\left(q _ {1} ^ {p}\right)} \dots u _ {i _ {s p} ^ {p}} ^ {\left(q _ {s p} ^ {p}\right)} u _ {i _ {s p + 1} ^ {p}} ^ {\left(q _ {s p + 1} ^ {p}\right)}. \tag {8.5.28} \\ \end{array}
$$

比较式 (8.5.27) 和式 (8.5.28) 与式 (8.5.22) 和式 (8.5.23) 可知，如果 $z^{(k)}(0) = y^{(k)}(0)$ ，那么 $z^{(k+1)}(0) = y^{(k+1)}(0)$ . 但前面已经知道， $z^0(0) = y^0(0) = h(x_0), \dot{z}(0) = \dot{y}(0) = \sum_{j=0}^{m} L_{g_j} h(x_0) u_j$ . 因此

$$z ^ {(k)} (0) = y ^ {(k)} (0), \quad k \geqslant 0.$$

为保证 $z(t)$ 逐项求导的合法性，我们要证明 $z(t)$ 的收敛性及其各阶导数的一致绝对收敛性。先证明存在 $T > 0$ ，使 $z(t)$ 在 $0 \leqslant t \leqslant T$ 上一致绝对收敛。

令 $u_{1}=u_{2}=\cdots=u_{m}=1$ ，那么
