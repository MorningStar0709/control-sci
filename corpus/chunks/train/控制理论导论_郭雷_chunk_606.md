注8.3.1 从以上的讨论可看出如果定理8.3.1的条件全局成立，且由式(8.3.4)定义的映射 $F: \mathbb{R}^n \to M$ 是一个全局微分同胚，则系统(8.3.1)全局等价于一个完全能控的线性系统。

下面考虑带输出的仿射非线性系统

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + \sum_ {i = 1} ^ {m} g _ {i} (x) u _ {i} := f (x) + g (x) u, \quad x \in \mathbb {R} ^ {n}, u \in \mathbb {R} ^ {m}, \\ y = h (x), \quad y \in \mathbb {R} ^ {p}, \end{array} \right. \tag {8.3.9}
$$

这里 $f(x_0) = 0, h(x_0) = 0.$

定义8.3.2 系统(8.3.9)在平衡点 $x_0$ 附近局部等价于一个线性系统，如果存在一个局部坐标卡 $(U,z),z(x_0) = 0$ 使系统(8.3.9)能表示为

$$
\left\{ \begin{array}{l} \dot {z} = A z + \sum_ {i = 1} ^ {m} b _ {i} u _ {i} := A z + B u, \quad z \in U, u \in \mathbb {R} ^ {m}, \\ y = C z, \end{array} \right. \tag {8.3.10}
$$

这里 $(A, B)$ 完全能控， $(C, A)$ 完全能观测.

考虑局部情况.

命题8.3.1 系统(8.3.9)在平衡点 $x_0$ 附近局部等价于一个线性系统，当且仅当

(i) $\operatorname{rank}\left\{\mathrm{ad}_f^k g_i(x_0)\mid 1\leqslant i\leqslant m;0\leqslant k\leqslant n - 1\right\} = n;$

(ii) $\operatorname{rank}\left\{\mathrm{d}L_f^k h_j(x_0)\mid 1\leqslant j\leqslant p;0\leqslant k\leqslant n - 1\right\} = n;$

(iii) 存在 $x_0$ 的一个邻域 $U$ ，使得

$$L _ {g _ {i}} L _ {f} ^ {s} L _ {g _ {j}} L _ {f} ^ {t} h (x) = 0, \quad x \in U, 1 \leqslant i, j \leqslant m, s, t \geqslant 0.$$

证明 (必要性) 设 $f$ 为一向量场, $h$ 为一光滑函数. 那么对任一微分同胚 $T$ , Lie 导数在以下意义下不变, 即

$$L _ {T _ {*} (f)} ((T ^ {- 1}) ^ {*} (h)) = (T ^ {- 1}) ^ {\mathrm{T}} * (L _ {f} (h)).$$

显见 (i), (ii) 和 (iii) 是必要的，因为对线性系统它们均成立.

(充分性) 我们先证明一个公式，这公式本身也很有用

$$L _ {\mathrm{ad} _ {f} ^ {k} g} h (x) = \sum_ {i = 0} ^ {k} (- 1) ^ {i} \binom {k} {i} L _ {f} ^ {k - i} L _ {g} L _ {f} ^ {i} h (x), \tag {8.3.11}$$

这里

$$\binom {k} {i} = \frac {k !}{i ! (k - i) !}.$$

它可由数学归纳法证明．对 k=0 显然成立．假定对 k=p 它成立，那么

$$L _ {\mathrm{ad} _ {f} ^ {p + 1} g} h (x) = L _ {f} L _ {\mathrm{ad} _ {f} ^ {p} g} h (x) - L _ {\mathrm{ad} _ {f} ^ {p} g} L _ {f} h (x).$$

利用式 (8.3.11) 及等式

$$\binom {p} {q} + \binom {p} {q + 1} = \binom {p + 1} {q + 1},$$

则可证明式 (8.3.11) 对 $p + 1$ 成立.

其次，我们断言存在 $x_0$ 的一个邻域 $U$ ，使得

$$L _ {[ \mathrm{ad} _ {f} ^ {s} g _ {i}, \mathrm{ad} _ {f} ^ {t} g _ {j} ]} L _ {f} ^ {k} h (x) = 0, \quad x \in U, 1 \leqslant i, j \leqslant m; 0 \leqslant s, t \leqslant n - 1; k \geqslant 0. \tag {8.3.12}$$

事实上，这可利用式 (8.3.11) 及条件 (iii) 得证.

由于式 (8.3.12) 等价于

$$\left\langle \mathrm{d} L _ {f} ^ {k} h (x), [ \mathrm{ad} _ {f} ^ {s} g _ {i}, \mathrm{ad} _ {f} ^ {t} g _ {j} ] \right\rangle = 0,$$

故由条件 (ii) 可得

$$\left[ \mathrm{ad} _ {f} ^ {s} g _ {i}, \mathrm{ad} _ {f} ^ {t} g _ {j} \right] = 0, \quad 1 \leqslant i, j \leqslant m, 0 \leqslant s, t \leqslant n - 1.$$

根据定理 8.3.1, 系统 (8.3.10) 可局部表示为
