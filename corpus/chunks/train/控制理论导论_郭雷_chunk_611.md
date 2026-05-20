$$
\left\{ \begin{array}{l l} \dot {z} _ {1} ^ {i} & = z _ {2} ^ {i}, \\ & \vdots \\ \dot {z} _ {r _ {i - 1}} ^ {i} & = z _ {r _ {i}} ^ {i}, \\ \dot {z} _ {r _ {i}} ^ {i} & = L _ {f} ^ {r _ {i}} z _ {1} ^ {i} + L _ {g} L _ {f} ^ {r _ {i} - 1} z _ {1} ^ {i} u, \quad i = 1, \dots , s. \end{array} \right. \tag {8.3.21}
$$

令

$$
D = \left[ \begin{array}{c} L _ {g} L _ {f} ^ {r _ {1} - 1} z _ {1} ^ {1} \\ L _ {g} L _ {f} ^ {r _ {2} - 1} z _ {1} ^ {2} \\ \vdots \\ L _ {g} L _ {f} ^ {r _ {s} - 1} z _ {1} ^ {s} \end{array} \right], \quad F = \left[ \begin{array}{c} L _ {f} ^ {r _ {1}} z _ {1} ^ {1} \\ L _ {f} ^ {r _ {2}} z _ {1} ^ {2} \\ \vdots \\ L _ {f} ^ {r _ {s}} z _ {1} ^ {s} \end{array} \right].
$$

类似前面的讨论，不难证明 $D$ 是非奇异的。然后定义一个 $n \times m$ 矩阵 $E$

$$E = \langle f, g \rangle ,$$

其中

$$
f = \left[ \begin{array}{c} \mathrm{d} z _ {1} ^ {1} \\ \vdots \\ \mathrm{d} L _ {f} ^ {r _ {1} - 1} z _ {1} ^ {1} \\ \vdots \\ \mathrm{d} z _ {1} ^ {s} \\ \vdots \\ \mathrm{d} L _ {f} ^ {r _ {s} - 1} z _ {1} ^ {s} \end{array} \right],
$$

则 $\operatorname{rank}(E) = m$ . 这是因为头 $n$ 个1-形式线性无关. 作为一般约定, $g_1, \cdots, g_m$ 也线性无关. 现在正好 $E$ 中仅有的 $m$ 个非零行形成 $D$ , 故 $\operatorname{rank}(D) = m$ .

采用如下控制：

$$u = - D ^ {- 1} F + \dot {D} ^ {- 1} v,$$

则系统 (8.3.21) 变为

$$
\left\{ \begin{array}{l l} \dot {z} _ {1} ^ {i} & = z _ {2} ^ {i}, \\ & \vdots \\ \dot {z} _ {r _ {i - 1}} ^ {i} & = z _ {r _ {i}} ^ {i}, \\ \dot {z} _ {r _ {i}} ^ {i} & = v ^ {i}, \quad i = 1, \dots , s, \end{array} \right. \tag {8.3.22}
$$

这里 $v^i$ 是 $\pmb{v}$ 的一个如下的分割：

$$
v ^ {1} = \left[ \begin{array}{c} v _ {1} \\ \vdots \\ v _ {m _ {s}} \end{array} \right], \quad v ^ {2} = \left[ \begin{array}{c} v _ {m _ {s} + 1} \\ \vdots \\ v _ {m _ {s - 1}} \end{array} \right], \quad \dots , \quad v ^ {s} = \left[ \begin{array}{c} v _ {m _ {2} + 1} \\ \vdots \\ v _ {m _ {1}} \end{array} \right],
$$

而系统 (8.3.22) 是一个完全能控线性系统.

注8.3.2 由以上证明可知，如果

$$\operatorname{rank} \left(\Delta_ {i + 1} - \Delta_ {i}\right) = \operatorname{rank} \left(\Delta_ {i} - \Delta_ {i - 1}\right),$$

则 $\Delta_{i}$ 的对合性可由 $\Delta_{i+1}$ 的对合性保证. 因此在定理 8.3.2 中 $\Delta_{i}, i = 1, \cdots, n$ 的对合性条件可用以下的对合性条件代替

$$\operatorname{rank} \left(\Delta_ {i + 1} - \Delta_ {i}\right) < \operatorname{rank} \left(\Delta_ {i} - \Delta_ {i - 1}\right).$$

(记 $\Delta_{0}:=\{0\}$ )

考虑一个单输入系统．显然如果 $\operatorname{rank}(\Delta_n) = n$ ，则

$$\operatorname{rank} \left(\Delta_ {k}\right) = k, \quad k = 1, \dots , n.$$

而且利用以上注释，如果 $\Delta_{n-1}$ 对合，则所有的 $\Delta_{k}, k = 1, \cdots, n$ 均对合。因此我们有如下推论。

推论8.3.1 系统(8.3.1)当 $m = 1$ 时在 $x_0$ 可线性化，当且仅当存在一个邻域 $U$ ，使得

(i) $\forall x \in U, \Delta_{n-1}(x)$ 是对合；  
(ii) $\operatorname{rank}(\Delta_n)(x) = n, \forall x \in U$ .
