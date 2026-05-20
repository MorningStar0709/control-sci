$$\lambda + \mathbf {x} := (\lambda + x _ {1}, \dots , \lambda + x _ {n}) ^ {T}.$$

定义范数

$$\| \mathbf {x} \| := \max _ {1 \leqslant i \leqslant n} | x _ {i} |.$$

对极大极小函数，有下面的基本性质：

定理 11.2.3 (1) 齐次性:

$$F (\lambda + \mathbf {x}) = \lambda + F (\mathbf {x}), \quad \forall \lambda \in \mathbb {R}, \mathbf {x} \in \mathbb {R} ^ {n}.$$

(2) 单调性:

$$F (\mathbf {x}) \leqslant F (\mathbf {y}), \quad \mathbf {x}, \mathbf {y} \in \mathbb {R} ^ {n}, \mathbf {x} \leqslant \mathbf {y}.$$

(3) 非膨胀性:

$$\| F (\mathbf {x}) - F (\mathbf {y}) \| \leqslant \| \mathbf {x} - \mathbf {y} \|, \quad \forall \mathbf {x}, \mathbf {y} \in \mathbb {R} ^ {n}.$$

定理11.2.4 (1) 如果 $F$ 和 $G$ 是两个 $n$ 维极大极小函数，那么 $F$ 与 $G$ 的复合也是一个 $n$ 维极大极小函数；

(2) 每个极大极小函数有合取和析取分解式.

以上两个定理证明不难，略去.

由定理 11.2.4(1), 对任何 $k \geqslant 0$ , $F^{k}(\mathbf{x})$ 是一极大极小函数. 一般地, 极大极小函数 $F(\mathbf{x})$ 不是压缩的. 当 $F(\mathbf{x})$ 是一个压缩函数时, 由压缩映射定理, $F(\mathbf{x})$ 的动态行为是平凡的. 假定对 $R^{n}$ 中的某点 x, 极限向量

$$\lim _ {k \rightarrow + \infty} \frac {1}{k} F ^ {k} (\mathbf {x}) \tag {11.2.4}$$

存在, 则由定理 11.2.3(3), 上述极限对 $\mathbb{R}^n$ 中所有点都存在, 且有相同的 (向量) 值, 因而是唯一的. 在极大极小函数的应用中, 状态向量 $\mathbf{x}$ 常被视为某些事件发生的时间向量, 而向量 $F(\mathbf{x})$ 被视为后继事件发生的时间向量. 因此, 极限 (11.2.4) 可以认为是相邻事件间隔的平均时间向量. 事实上, 当 $k \to +\infty$ 时

$$\frac {F ^ {k} (\mathbf {x}) - F ^ {k - 1} (\mathbf {x}) + \cdots + F (\mathbf {x}) - \mathbf {x}}{k} = \frac {F ^ {k} (\mathbf {x}) - \mathbf {x}}{k}$$

的极限就是式 (11.2.4).

定义 11.2.3 假定 $F(\mathbf{x})$ 是一个极大极小函数，如果存在 $\mathbf{x} \in \mathbb{R}^n$ 使极限 (11.2.4) 存在，则称其为 $F(\mathbf{x})$ 的广义特征值（向量），也称为 $F(\mathbf{x})$ 的周期时间（向量），记为 $\chi(F)$ .

$F(\mathbf{x})$ 的每个分支可以分解为合取式

$$F _ {k} (\mathbf {x}) = (a _ {k 1} ^ {1} + x _ {1} \vee \dots \vee a _ {k n} ^ {1} + x _ {n}) \wedge \dots \wedge (a _ {k 1} ^ {l (k)} + x _ {1} \vee \dots \vee a _ {k n} ^ {l (k)} + x _ {n}) \tag {11.2.5}$$

其中 $1 \leqslant k \leqslant n, a_{kj}^i \in$ 极大代数 $D, l(k)$ 表示 $F_k(\mathbf{x})$ 中单极大式的个数。如果 $a_{kj}^i = -\infty$ ，则表示 $F_k(\mathbf{x})$ 的第 $i$ 个单极大式中没有 $x_j$ 项。在上式中写出项 $-\infty + x_j$ 仅为表述方便。选择 $a_{k1}^i, \cdots, a_{kn}^i, 1 \leqslant i \leqslant l(k), 1 \leqslant k \leqslant n$ 作为矩阵的第 $k$ 行而得的矩阵 $A$ 称为 $F(\mathbf{x})$ 的一个单极大射影。如果把 $F_k(\mathbf{x})$ 分解为析取式，类似地，可以得到 $F(\mathbf{x})$ 的单极小射影。 $F(\mathbf{x})$ 的单极大射影有 $\prod_{k=1}^{n} l(k)$ 个。

定义 11.2.4 设 $A \in D^{n \times n}$ , $G(A)$ 为按第二种定义的 A 的关联图，现定义 A 的周期时间（向量）为： $\mu(A) = [\mu_{1}(A), \cdots, \mu_{n}(A)]^{\mathrm{T}} \in \mathbb{R}^{n}$ ，其中
