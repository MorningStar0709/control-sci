# 8.3 线性化

给定一个仿射非线性系统

$$\dot {x} = f (x) + \sum_ {i = 1} ^ {m} g _ {i} (x) u _ {i} := f (x) + g (x) u, \quad x \in \mathbb {R} ^ {n}, u \in \mathbb {R} ^ {m}, \tag {8.3.1}$$

这里 $f(x_0) = 0$

定义8.3.1 称系统(8.3.1)在平衡点 $x_0$ 邻域等价于一个线性系统，如果存在一个(局部)坐标卡 $(U,z),z(x_0) = 0$ 使得系统(8.3.1)可(局部)表示为

$$\dot {z} = A z + \sum_ {i = 1} ^ {m} b _ {i} u _ {i} := A z + B u, \quad z \in U, u \in \mathbb {R} ^ {m}, \tag {8.3.2}$$

这里 $(A, B)$ 是一个完全能控对.

首先考虑局部线性等价问题.

定理8.3.1 系统(8.3.1)在平衡点 $x_0$ 邻域局部等价于一个线性系统，当且仅当

(i) $\operatorname{rank}\left\{\mathrm{ad}_f^k g_i(x_0) \mid 1 \leqslant i \leqslant m; 0 \leqslant k \leqslant n - 1\right\} = n;$

(ii) 存在 $x_0$ 的一个邻域 $U$ , 使得

$$\left[ \mathrm{ad} _ {f} ^ {s} g _ {i}, \mathrm{ad} _ {f} ^ {t} g _ {j} \right] = 0, \quad 1 \leqslant i, j \leqslant m; 0 \leqslant s, t \leqslant n.$$

证明 (必要性) 设存在坐标变换 $T: x \mapsto z$ , 使得

$$T _ {*} (f) = A z, \quad T _ {*} (g _ {i}) = b _ {i}, \quad i = 1, \dots , m.$$

由于系统 (8.3.2) 完全能控，简单计算可知

$$\mathrm{ad} _ {T _ {*} (f)} ^ {k} T _ {*} (g _ {i}) = (- 1) ^ {k} A ^ {k} b _ {i}. \tag {8.3.3}$$

而一个微分同胚不影响 Lie 括号，即

$$T _ {*} [ f, g ] = \left[ T _ {*} (f), T _ {*} (g) \right].$$

因此由式 (8.3.3) 可知 (i) 和 (ii) 成立.

(充分性) 由 (i), 存在 $n$ 个线性无关向量场

$$X _ {i} ^ {k + 1} = \operatorname{ad} _ {f} ^ {k} g _ {i}, \quad i = 1, \dots , m; k = 0, 1, \dots , n _ {i} - 1,$$

$\left(\sum_{i=1}^{m} n_i = n\right)$ , 它们在 $x_0$ 的一个邻域 $U$ 中线性无关. 选择一个局部坐标

$$z = \left\{z _ {1} ^ {1}, \dots , z _ {n _ {1}} ^ {1}, \dots , z _ {1} ^ {m}, \dots , z _ {n _ {m}} ^ {m} \right\} \in \mathbb {R} ^ {n},$$

并构造一个映射 $F: z \mapsto U$

$$F (z) = \phi_ {z _ {1} ^ {1}} ^ {X _ {1} ^ {1}} \circ \dots \phi_ {z _ {n _ {1}} ^ {1}} ^ {X _ {n _ {1}} ^ {1}} \dots \phi_ {z _ {1} ^ {m}} ^ {X _ {1} ^ {m}} \circ \dots \phi_ {z _ {n _ {m}} ^ {m}} ^ {X _ {n _ {m}} ^ {m}} (x _ {0}). \tag {8.3.4}$$

设 $p = F(z)$ . 利用引理3.8.2, (ii) 表明

$$\frac {\partial F}{\partial z _ {k} ^ {i}} (p) = X _ {k} ^ {i} (p), \quad i = 1, \dots , m; k = 1, \dots , n _ {i}.$$

因此在局部坐标 $z$ 下有

$$
\begin{array}{l} \left[ F _ {*} ^ {- 1} \left(X _ {1} ^ {1}\right), \dots , F _ {*} ^ {- 1} \left(X _ {n _ {1}} ^ {1}\right), \dots , F _ {*} ^ {- 1} \left(X _ {1} ^ {m}\right), \dots , F _ {*} ^ {- 1} \left(X _ {n _ {m}} ^ {m}\right) \right] \\ = \left(J _ {F}\right) ^ {- 1} \circ \left[ X _ {1} ^ {1}, \dots , X _ {n _ {1}} ^ {1}, \dots , X _ {1} ^ {m}, \dots , X _ {n _ {m}} ^ {1} \right] \circ F \\ = I. \\ \end{array}
$$

为记号简单，我们仍用 f 及 $g_{i}$ 表示它们在新坐标 z 下的形式，即 $F_{*}^{-1}(f)$ 和 $F_{*}^{-1}(g_{i})$ . 令 $n^{i}=n_{1}+n_{2}+\cdots+n_{i}$ ，记

$$\delta_ {i} = [ 0, \dots , 0, 1, 0, \dots , 0 ] ^ {\mathrm{T}} \in \mathbb {R} ^ {n}.$$

其中第 $i$ 个元为1.那么
