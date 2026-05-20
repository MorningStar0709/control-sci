因为 $(A^r)_{ij} = \sum_{k=1}^{n}(A)_{ik}(A^{r-1})_{kj}$ , 所以只要对 $r$ 进行归纳, 定理 11.2.1 的证明便不难得到, 这里略去.

极大代数上的方阵如果其每行每列只有一个元素为0.而其余元素均为 $\varepsilon$ ，则称为该矩阵为置换阵，每个置换阵都可逆，并且其逆矩阵等于其转置.

定理11.2.2 设 $A \in D^{n \times n}, G(A)$ 含 $\omega$ 个强连通支, 则存在置换阵 $P \in D^{n \times n}$ , 使得

$$
P A P ^ {- 1} = \left[ \begin{array}{c c c c} A _ {1} & A _ {1 2} & \dots & A _ {1 \omega} \\ \phi & A _ {2} & \dots & A _ {2 \omega} \\ \vdots & \vdots & & \vdots \\ \phi & \phi & \dots & A _ {\omega} \end{array} \right], \tag {11.2.2}
$$

其中 $A_{1}, A_{2}, \cdots, A_{\omega}$ 都是不可约的，它们对应 $G(A)$ 的 $\omega$ 个强连通支， $\phi$ 是每个元素均为 $\varepsilon$ 的阵.

证明是用图论方法，详略．本节以上内容主要引自文献[10].

下面介绍双子代数的基础知识，

1972 年数学家 Kuntzmann 引入了 Dioid(双子) 一词, Gondran 等 $^{[21]}$ 研究了双子上的线性代数. 双子是既包含格又包含域作为特例的一种代数结构.

一个双子 $(\mathcal{D}, *, \oplus)$ 是一个具有二元运算“\*”，“ $\oplus$ ”的集合，满足以下运算律：

(1) 结合律: 对任意的 $a, b, c \in \mathcal{D}$ , 有 $(a \oplus b) \oplus c = a \oplus (b \oplus c), (a * b) * c = a * (b * c)$ ;

(2) 加法交换律：对任意的 $a, b \in \mathcal{D}$ ，有 $a \oplus b = b \oplus a$ ;

(3) 分配律：对任意的 $a, b, c \in \mathcal{D}$ ，有 $(a \oplus b) * c = (a * c) \oplus (b * c), c * (a \oplus b) = (c * a) \oplus (c * b)$ ;

(4) 有零元与幺元：对任意 $a \in \mathcal{D}$ ，存在 $\varepsilon \in \mathcal{D}$ ，满足 $a \oplus \varepsilon = a$ 并存在 $e \in D$ ，满足 $a * e = e * a = a$ ;

(5) 零元吸收律：对任意 $a \in \mathcal{D}$ 有 $a * \varepsilon = \varepsilon * a = \varepsilon$ ;

(6) 加法幂等律：对任意 $a \in \mathcal{D}$ 有 $a \oplus a = a$ .

文献[21]综述了双子的上线性代数理论，包括线性相关与无关，双行列式，双子上与Cayley-Hamilton定理对应的结果等。总的来说，这一理论还不够成熟，成为线性系统几何方法发展的一个障碍。

下面介绍极大极小函数的基础知识，主要引自文献[20],[22],[25].

定义11.2.1 一个极大极小式 $f$ 是按如下法则形成的式子：

$$f := x _ {1}, x _ {2}, \dots , x _ {n} | f + a | f \wedge f | f \vee f |, \tag {11.2.3}$$

其中 $\vee$ 表示取极大， $\wedge$ 表示取极小， $x_{1}, x_{2}, \cdots, x_{n}$ 是变量，而 $a \in \mathbb{R}$ 是参量，|是法则间的分隔号。特别是，仅含 $\vee$ 和 $+$ 的式子称为单极大式，而仅含 $\wedge$ 和 $+$ 的式子称为单极小式。

定义 11.2.2 n 维极大极小函数是指函数 $F(\mathbf{x}) : \mathbb{R}^{n} \to \mathbb{R}^{n}$ ，其中每个分量 $F(\mathbf{x})_{i} : \mathbb{R}^{n} \to \mathbb{R}$ 是 n 个变量 $x_{1}, x_{2}, \cdots, x_{n}$ 的一个极大极小式， $1 \leqslant i \leqslant n$ ，这里 x 为列向量： $(x_{1}, \cdots, x_{n})^{\mathrm{T}}$ 。如果 $F(\mathbf{x})_{i}, 1 \leqslant i \leqslant n$ 都是单极大式，则 $F(\mathbf{x})$ 称为单极大函数，也称为极大函数。极大极小函数有时简记为 F。

设 $\lambda \in \mathbb{R},\mathbf{x},y\in \mathbb{R}^n$ ，记 $\leqslant$ 是通常的偏序

$$\mathbf {x} \leqslant \mathbf {y} \Longleftrightarrow x _ {i} \leqslant y _ {i}, 1 \leqslant i \leqslant n.$$

规定
