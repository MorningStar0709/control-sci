定理 5.1.6 (开映象定理) 设 X, Y 为两个 Banach 空间，A 为 X 到 Y 的一闭线性算子。如果 $\mathcal{R}(A)=Y$ ，则 A 把 $\mathcal{D}(A)$ 中的每个开子集映成 Y 中的开子集。特别当 A 是满射并一对一时， $A^{-1}\in\mathcal{L}(X,Y)$ 。

定理5.1.7(闭图像定理) 定义在整个Banach空间取值于另一个Banach空间的闭线性算子是有界的.

定理5.1.8（一致有界性定理或共鸣定理）设 $X, Y$ 为两个Banach空间，并设 $\{T_{\lambda} \mid \lambda \in \Lambda\}$ 是 $X$ 到 $Y$ 的一族有界线性算子，这里 $\Lambda$ 是某一指标集。如果

$$\sup \left\{\| T _ {\lambda} x \| \mid \lambda \in A \right\} < \infty , \quad \forall x \in X,$$

则 $\sup \left\{\| T_{\lambda}\| \mid \lambda \in \Lambda \right\} < \infty.$

定理5.1.9 设 $X, Y$ 为两个Banach空间，并设 $\{T_n\} \subset \mathcal{L}(X, Y)$ . 如果

(1) $\sup \left\{\| T_n x \| \mid n \geqslant 1 \right\} < \infty, \forall x \in X;$

(2) 存在一映射 $T: X \to Y$ 及 $X$ 的一稠子集 $M$ , 使得当 $n \to \infty$ 时

$$T _ {n} x \rightarrow T x, \quad \forall x \in M,$$

则 $T \in \mathcal{L}(X, Y)$ 并且 $\| T \| \leqslant \underline{\lim}\| T_n\|$ .

设 $X, Y$ 为两个 Banach 空间，而 $A: X \to Y$ 为一具有稠定义域 $\mathcal{D}(A)$ 的线性算子。我们按如下方式定义 $A$ 的伴随算子 $A^{*}$ ：

$$\langle x, A ^ {*} g \rangle = \langle A x, g \rangle , \quad \forall x \in \mathcal {D} (A), \forall g \in \mathcal {D} (A ^ {*}),$$

其中

$$\mathcal {D} (A ^ {*}) = \left\{g \in Y ^ {*} \mid \langle A x, g \rangle \text {在} \mathcal {D} (A) \text {上有界} \right\}.$$

特别对于 $A \in \mathcal{L}(X, Y)$ , 我们有

$$\langle A x, g \rangle = \langle x, A ^ {*} g \rangle , \quad \forall x \in X, \forall g \in Y ^ {*},$$

并且 $\| A^{*}\| = \| A\|$ . 任一线性稠定算子的伴随算子总是闭的.

定理 5.1.10 设 X, Y 为两个自反 Banach 空间，而 $A: X \rightarrow Y$ 为一闭稠定线性算子，则 $A^{*}$ 也是闭稠定的，并且 $A^{**} = A$ .

对于从 $X$ 到 $Y$ 的线性算子 $A$ , 我们记 $\mathcal{N}(A)$ 为 $A$ 的零空间

$$\mathcal {N} (A) = \left\{x \in \mathcal {D} (A) \mid A x = 0 \right\}.$$

对于赋范线性空间 $X$ 中的子集 $S$ , 定义 $S$ 的零化子为

$$S ^ {\perp} \stackrel {{\mathrm{def}}} {{=}} \left\{f \in X ^ {*} \mid \langle x, f \rangle = 0, \forall x \in S \right\},$$

而对于 $X^{*}$ 中的子集 $M \subset X^{*}$ , 类似地定义 $M$ 的零化子为

$${ } ^ { \perp } M \stackrel { \mathrm{def} } { = } \left\{ x \in X \mid \langle x , f \rangle = 0 , \forall f \in M \right\} .$$

定理5.1.11 设 $X, Y$ 为两个Banach空间，而 $A$ 为 $X$ 到 $Y$ 的闭稠定线性算子，则下列4个命题是彼此等价的：

(1) $\mathcal{R}(A)$ 是闭的；  
(2) $\mathcal{R}(A^{*})$ 是闭的；  
(3) $\mathcal{R}(A^{*}) = \mathcal{N}(A)^{\perp}$ ;   
(4) $\mathcal{R}(A) = {}^{\perp}\mathcal{N}(A^{*})$

下列几个定理在第 10 章研究能控性和能观测性之间的关系时是有用的.

定理5.1.12 设 $X, Y, Z$ 为三个Banach空间，并设 $F \in \mathcal{L}(Y, X), G \in \mathcal{L}(Z, X)$ . 那么
