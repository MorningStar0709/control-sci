$$(X \cdot Y) \cdot Z = X \cdot (Y \cdot Z), \quad \forall X, Y, Z \in V,$$

那它就称为一个结合代数.

如果乘法还是交换的，即如下 A3 成立：

A3. (交换律)

$$X \cdot Y = Y \cdot X, \quad \forall X, Y \in V, \tag {3.2.4}$$

则它称为一个交换代数.

一个代数显然是一个环，因此，代数结构的性质几乎平行于环的性质。我们简略地说明如下：

定义 3.2.7 给定两个代数 V, W.

(1) $V$ 的一个子空间 $M \subset V$ 称为 $V$ 的一个子代数，如果对于同一个乘法运算 $M$ 构成一个代数；

(2) $V$ 的一个子代数 $M$ 称为 $V$ 的一个理想，如果

$$X \cdot Z \in M, \quad Z \cdot Y \in M, \quad \forall X, Y \in V, \quad Z \in M; \tag {3.2.5}$$

(3) 一个线性映射 $F: V \to W$ 称为一个代数同态，如果

$$F (X \cdot Y) = F (X) \cdot F (Y); \tag {3.2.6}$$

(4) 一个代数同态 $F: V \to W$ 称为代数同构，如果它是一对一且映上的.

例3.2.4 (1) 令 $M_{n}$ 为 $n \times n$ 矩阵集合，依标准矩阵加法，乘法以及数乘，它构成一个代数。这个代数是结合的，但不是交换的，它有单位元 $I_{n}$ ；

(2) 记 $U_{n} \subset M_{n}$ 为上三角矩阵集合。那么，容易证明 $U_{n}$ 是 $M_{n}$ 的一个子代数；

(3) 设 $M_{n}$ 连同普通模为一Banach空间，这里模为

$$\| \boldsymbol {A} \| = \sqrt {\max \left\{\lambda \in \sigma \left(\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {A}\right) \right\}},$$

它称为一个 Banach 代数. 这时 $\sigma(\cdot)$ 为特征值集合;

(4) 设 $[\cdot, \cdot]$ 在 $M_{n}$ 上定义一个乘法如下：

$$[ \boldsymbol {A}, \boldsymbol {B} ] = \boldsymbol {A B} - \boldsymbol {B A}. \tag {3.2.7}$$

容易证明， $M_{n}$ 在这个乘法下是一个代数，它称为一个Lie代数。它不是结合的，也没有单位元。

Lie 代数在非线性控制理论的研究中十分重要. 本节的其余部分都将用来讨论它.

定义 3.2.8 一个代数 V 带上乘法 $\left[\cdot,\cdot\right]:V\times V\rightarrow V$ ，构成一个 Lie 代数，如果它满足

L1. (反对称)

$$[ X, Y ] = - [ Y, X ], \quad \forall X, Y \in V. \tag {3.2.8}$$

L2. (Jacobi 等式)

$$[ X, [ Y, Z ] ] + [ Y, [ Z, X ] ] + [ Z, [ X, Y ] ] = 0, \quad \forall X, Y, Z \in V. \tag {3.2.9}$$

[·,·] 称为 Lie 括号.

例 3.2.5 (1) 回忆例 3.1.1 中的一般线性代数 $\mathrm{gl}(n,\mathbb{R})$ . 我们定义两个矩阵的 Lie 括号运算为式 (3.2.7). 那么, 容易检验它满足式 (3.2.8)\~(3.2.9). 因此, $\mathrm{gl}(n,\mathbb{R})$ 是一个 Lie 代数;

(2) 在 $\mathbb{R}^3$ 中令 $\{I, J, K\}$ 分别为 $x, y,$ 及 $z$ 轴的单位向量。则它们构成标准基。设 $X, Y$ 为两个向量，表示为 $X = x_1 I + x_2 J + x_3 K$ 及 $Y = y_1 I + y_2 J + y_3 K$ 。那么，它们的叉积定义为

$$
\boldsymbol {X} \times \boldsymbol {Y} = \det \left[ \begin{array}{l l l} \boldsymbol {I} & \boldsymbol {J} & \boldsymbol {K} \\ x _ {1} & x _ {2} & x _ {3} \\ y _ {1} & y _ {2} & y _ {3} \end{array} \right]. \tag {3.2.10}
$$

容易检验， $\mathbb{R}^3$ 在这种义积下是一个 Lie 代数；

(3) 设 $f(x), g(x) \in \mathbb{R}^n$ , 这里, 自变量 $x \in \mathbb{R}^n$ . 它们称为 $\mathbb{R}^n$ 上的向量场. (我们将在后面给予严格的定义.) 现在, 我们形式地定义两个 $\mathbb{R}^n$ 上的向量场的 Lie 括号为

$$[ f (x), g (x) ] = \frac {\partial g}{\partial x} f (x) - \frac {\partial f}{\partial x} g (x). \tag {3.2.11}$$

$\mathbb{R}^n$ 上的向量场依式 (3.2.11) 定义的 Lie 括号为一 Lie 代数。我们将检验工作留给读者。
