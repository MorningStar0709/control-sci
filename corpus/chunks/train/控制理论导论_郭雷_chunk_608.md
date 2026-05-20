$$
\left\{ \begin{array}{l} z _ {1} = x _ {1} - \sin (x _ {2}), \\ z _ {2} = \sin (x _ {2}). \end{array} \right.
$$

最后，系统(8.3.13)可在 $z$ 坐标下表示为

$$
\left\{ \begin{array}{l} \dot {z} _ {1} = u, \\ \dot {z} _ {2} = z _ {1} + z _ {2}, \\ y = z _ {2}. \end{array} \right.
$$

线性等价意味着系统本质上是一个线性系统。等价性研究揭示了线性系统的几何本质。实际上，更有用的是利用控制将非线性系统转换为一个线性系统。以下研究这个问题。

线性化问题要回答什么时候一个非线性系统能在一个坐标变换及一个正则状态反馈控制

$$u (x) = \alpha (x) + \beta (x) v \tag {8.3.14}$$

$(\beta (x)$ 可逆）下转化为一个线性系统.

定义8.3.3 系统(8.3.1)称为在 $x_0$ 点能线性化的，如果存在一个局部坐标变换 $z = z(x)$ 及 $z(x_0) = 0$ ，一个正则状态反馈控制(8.3.14)，使闭环系统能表示为

$$\dot {z} = A z + B v, \tag {8.3.15}$$

这里 $(A,B)$ 为完全能控的线性系统.

如果状态变换及反馈为全局的，则称为全局线性化.

记

$$\Delta_ {i} = \operatorname{span} \left\{\mathrm{ad} _ {f} ^ {s} g _ {j} \mid j = 1, \dots , m; s \leqslant i - 1 \right\}, \quad i = 1, 2, \dots .$$

定理8.3.2 系统(8.3.1)在 $x_0$ 能线性化，当且仅当存在 $x_0$ 的一个邻域 $U$ ，使得

(i) $\Delta_{i}(x), x \in U, i = 1, \cdots, n$ 为非奇异且对合的分布；

(ii) $\operatorname{rank}(\Delta_n)(x) = n, x \in U$ .

证明 (必要性) 一个显见的事实是：分布 $\Delta_{i}, i = 1, \dots, n$ ，反馈不变，即若令

$$\tilde {f} = f + g \alpha , \quad \tilde {g} = g \beta ,$$

则

$$\Delta_ {i} = \operatorname{span} \left\{\mathrm{ad} _ {\bar {f}} ^ {s} \bar {g} _ {j} \mid j = 1, \dots , m; s \leqslant i - 1 \right\}.$$

设 $T$ 为微分同胚，则有

$$T _ {*} (\tilde {f}) = T _ {*} (f) + T _ {*} (g) \alpha = A z,T _ {*} (\tilde {g}) = T _ {*} (g) \beta = B.$$

那么显然 (i) 和 (ii) 对 $T_{*}(\Delta_{i})$ 成立，于是对 $\Delta_{i}$ 也成立.

(充分性) 选择 $n$ 个线性无关向量场 (这里 $X_{i}^{j} := \mathrm{ad}_{f}^{j} g_{i}$ )

$$
\left[ \begin{array}{c c c c c c c c c} X _ {1} ^ {0} & \dots & X _ {1} ^ {k _ {1}} & X _ {1} ^ {k _ {1} + 1} & \dots & X _ {1} ^ {k _ {2}} & \dots & X _ {1} ^ {k _ {s - 1} + 1} & \dots & X _ {1} ^ {k _ {s}} \\ \vdots & & & \vdots & & & & \vdots & & \\ \vdots & & & \vdots & & & & X _ {m _ {s}} ^ {k _ {s - 1} + 1} & \dots & X _ {m _ {s}} ^ {k _ {s}} \\ \vdots & & & \vdots & & & & \\ \vdots & & & X _ {m _ {2}} ^ {k _ {1} + 1} & \dots & X _ {m _ {2}} ^ {k _ {2}} \\ \vdots & & & & & \\ X _ {m} ^ {0} & \dots & X _ {m} ^ {k _ {1}} \end{array} \right], \tag {8.3.16}
$$

这里的前 $t$ 列向量场为

$$\Delta_ {t} = \operatorname{span} \left\{\operatorname{ad} _ {f} ^ {s} g _ {j} \mid s < t, j = 1, \dots , m \right\}, \quad t = 1, \dots , k _ {s}$$

的基．注意，为长短顺序的需要， $g_{1},\cdots,g_{m}$ 可能需要重排顺序．记 $k_{0}=0$ 及 $d_{i}=k_{i}-k_{i-1}, i=1,\cdots,s$ ，我们定义一族分布为

$$\Delta_ {j} ^ {i} = \operatorname{span} \left\{\mathrm{ad} _ {f} ^ {k} y _ {t} \mid k < k _ {i - 1} + j, t = 1, \dots , m \right\}.$$

因此 $\Delta_j^i$ 由式(8.3.16)的前 $i - 1$ 块及第 $i$ 块的前 $j$ 列向量场生成，也就是说
