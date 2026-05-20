向量场为 $V_{F}, V_{H}$ . 那么这两个Hamilton向量场的Lie括号为

$$V _ {\{F, H \}} = - [ V _ {F}, V _ {H} ] = [ V _ {H}, V _ {F} ].$$

设 $x = [x^1, \dots, x^m]$ 是 $M$ 上的局部坐标. 基底的 Poisson 括号

$$J ^ {i j} (x) = \{x ^ {i}, x ^ {j} \}, \quad i, j = 1, \dots , m.$$

称为 Poisson 流形 $M$ 相对于给定坐标的结构函数，它唯一决定了 Poisson 结构本身。为方便起见，将结构函数排成 $m \times m$ 矩阵 $J(x)$ ，称为 $M$ 的结构矩阵。于是 Poisson 括号在局部坐标下可表示为

$$\{F, H \} = \mathrm{d} F J (x) \nabla H (x).$$

命题 3.12.4 设 $J(x)=(J^{ij}(x))$ 为 $x=(x^{1},\cdots,x^{m})$ 的 $m\times m$ 矩阵，定义在一个开集 $M\subset R^{m}$ 上。那么 $J(x)$ 是定义于 M 上的 Poisson 括号 $\{F,H\}=dFJ\nabla H$ ，当且仅当它满足条件：

PB1. (反对称)

$$J ^ {i j} (x) = - J ^ {j i} (x), \quad i, j = 1, \dots , m.$$

PB2. (Jacobi 等式)

$$\sum_ {l = 1} ^ {m} \left\{J ^ {i l} \partial_ {l} J ^ {j k} + J ^ {k l} \partial_ {l} J ^ {i j} + J ^ {j l} \partial_ {l} J ^ {k i} \right\} = 0, \quad i, j, k = 1, \dots , m, \forall x \in M.$$

命题3.12.5 设 $M$ 为一Poisson流形， $x \in M$ 。那么存在唯一的线性映射

$$\pi = \pi | _ {x}: T ^ {*} M | _ {x} \rightarrow T M | _ {x},$$

使对任何实值函数 $H \in C^r(M)$ , 有

$$\pi (d H (x)) = V _ {H} | _ {x}.$$

定义3.12.6 设 $M$ 为一Poisson流形， $x \in M$ . $M$ 在 $x$ 点的秩定为线性映射 $\pi|_x: T^* M|_x \to TM|_x$ 的秩.

命题 3.12.6 一个 Poisson 流形在任意一点的秩均为偶数.

定义3.12.7 设 $M$ 和 $N$ 为Poisson流形，一个Poisson映射 $\phi : M \to N$ 定义为使Poisson括号不变的映射，即

$$\{F \phi , H \phi \} _ {M} = \{F, H \} _ {N} \phi , \quad \forall F, H \in C ^ {r} (N).$$

命题3.12.7 设 $M$ 为一Poisson流形， $X_H$ 为一Hamilton向量场。那么对每一个 $t, \phi_t^{X_H}: M \to M$ 决定了一个从 $M$ 到自身的Poisson映射。

推论3.12.1 如果 $X_{H}$ 为Poisson流形 $M$ 上的一个Hamilton向量场，那么 $M$ 在 $\phi_t^{X_H}(x)$ 上的秩对任何 $t\in \mathbb{R}$ 均等于 $M$ 在 $x$ 的秩.

下面是推广的 Darboux 定理.

定理3.12.3(Darboux定理) 设 $M$ 为一 $m$ 维Poisson流形，且有定常秩 $2n \leqslant m$ 。那么在任一点 $x_0 \in M$ 存在一个局部坐标，

$$(p, q, z) = (p ^ {1}, \dots , p ^ {n}, q ^ {1}, \dots , q ^ {n}, z ^ {1}, \dots , z ^ {l}), \quad 2 n + l = m,$$

使得 Poisson 括号可表示为

$$\{F, H \} = \sum_ {i = 1} ^ {n} \left(\frac {\partial F}{\partial q ^ {i}} \frac {\partial H}{\partial p ^ {i}} - \frac {\partial F}{\partial p ^ {i}} \frac {\partial H}{\partial q ^ {i}}\right),$$

而 $z^{1},\cdots,z^{l}$ 称为 Casimir 函数.
