定理 11.5.2 $^{[10]}$ 系统 (11.5.2) 能达的充要条件是，与 A 中 “单块列”（设为第 r 块列，这列中仅有一块 $A_{r} \neq \phi$ . 其他 $A_{ir} = \phi$ ）对应的所有 $B_{r} \neq \phi$ . 能观测的充要条件是：与 A 中 “单块行”（设为第 s 块行，这行中仅有 $A_{s} \neq \phi$ , 其他 $A_{sj} \neq \phi$ ）对应的所有 $C_{s} \neq \phi$ .

W. M. Wonham 教授创建了线性多变量控制系统的几何方法。最近，文献[2]则探索了极大代数上 $(A, B, C)$ 的几何方法的数学工具，较难而不够成熟。我们沿着一条比较容易的路作些讨论，即以结构能达与能观测为基础。为此首先引入模的概念。

定义11.5.4 设 $D$ 为极大代数， $(M, \oplus)$ 是一个含零交换半群。如果存在一个 $D \times M \to M$ 的映射 $(a, X) \longmapsto aX$ (称为纯量乘法)，对于任意 $a, b \in D, X, Y \in M$ 满足

$$a (\boldsymbol {X} \oplus \boldsymbol {Y}) = a \boldsymbol {X} \oplus a \boldsymbol {Y},(a \oplus b) X = a X \oplus b X.(a \cdot b) X = a (b X),1 \cdot X = X, \quad 0 \cdot X = 0,$$

则称 $M$ 是 $D$ 上的模，简称 $D$ -模或模。设 $N$ 是 $M$ 的子集，如果 $N$ 是 $(M, \oplus)$ 的子半群，且 $N$ 在纯量乘法下封闭，即 $aX \in N, \forall a \in D, X \in N$ ，则称 $N$ 是 $M$ 的子模。这里 $D$ 中的 1,0 为通常的 0， $-\infty$ 。

我们用 $D^{n \times m}$ 表示 $D$ 上所有 $n$ 行 $m$ 列矩阵的集合。显然 $D^{1 \times n}$ 是 $D$ -模，这对应于传统线性系统理论中的 $n$ 维状态空间。能达与不能达子空间，能观测与不能观测子空间是线性多变量控制几何方法中的几个基本概念，DEDS中也可有与它们对应的几个子模概念。

下面先引入第二种能达，即分别能达的定义（后面将证明它与结构能达等价），然后引入分别能达子模等概念.

定义 11.5.5 设系统 (11.5.1) 中， $X(0) = [x_{1}(0), x_{2}(0), \cdots, x_{n}(0)] = \phi$ ，若对任意指定实数 $\tilde{x}_{i}$ ，存在输入列 $U_{i}(1), U_{i}(2), \cdots, U_{i}(k)$ ，使终态分量 $x_{i}(k) = \tilde{x}_{i}$ ，则称 $x_{i}$ 是分别能达的（对不同的 i，输入列 $U_{i}(1), U_{i}(2), \cdots, U_{i}(k)$ 可以不同，因此是“分别”能达分量），系统 (11.5.1) 的分别能达分量 $x_{i}$ 组成的向量集：

$$\{[ x _ {1}, x _ {2}, \dots , x _ {n} ] \mid x _ {i} \in D, \quad \text {对所有分别能达分量}; \quad x _ {i} = \varepsilon , \quad \text {对其他} i \}$$

称为系统 (11.5.1) 的所有分别能达子模，记为 $\mathcal{R}$ . $\mathcal{R} = D^{1 \times D}$ 时称系统 (11.5.1) 分别能达．系统 (11.5.1) 分别能达分量以外的分量称为不能达分量，所有不能达分量组成的向量集：

$$\{[ x _ {1}, x _ {2}, \dots , x _ {n} ] \mid x _ {i} \in D, \quad \text {对所有不能达分量}; \quad x _ {i} = \varepsilon , \quad \text {对其他} i \}$$

称为不能达子模，记为 $\mathcal{R}^{\perp}$

读者可自己验证： $\mathcal{R}$ 与 $\mathcal{R}^{\perp}$ 确实符合子模的定义.

引理 11.5.2 A 不可约时， $(A,B)$ 分别能达 $\Longrightarrow B \neq \phi$ .

记 $A^{*}=E_{n}\oplus A\oplus\cdots\oplus A^{n-1}$ ，其中 $E_{n}$ 为 $D^{n\times n}$ 中单位阵。 $A^{*}$ 有与式 (11.5.2) 中的 A 同样的分块结构。用 $A_{ij}^{*}$ 记 $A^{*}$ 的 i 行 j 列块。

定理11.5.3 设式(11.5.2)中仅 $B_{i_s} \neq \phi, 1 \leqslant s \leqslant \alpha, A^*$ 的 $i_s$ 块行中不等于 $\phi$ 的块与 $A_{i_s}^*$ 记为 $A_{i_{s}j_r}^*, 1 \leqslant r \leqslant \beta_s$ . 令

$$J = \bigcup_ {s = 1} ^ {\alpha} \left\{j _ {1}, j _ {2}, \dots , j _ {\beta_ {s}} \right\}.$$
