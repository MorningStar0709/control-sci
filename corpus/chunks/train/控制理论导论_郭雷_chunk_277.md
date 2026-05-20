# 4.1 概率论的一般概念

早在 17 世纪, 欧洲数学家已开始用可能性分析来解决赌博中的一些问题, 但概率论的真正历史始于 Bernoulli (1713) 及 De Moivre (1730) 的极限定理. 到 19 世纪末, Chebyshev, Markov, Lyapunov 及 20 世纪 Lévy, Khinchin 建立大数法则, 中心极限定理, 把分析概率发展到一个新水平. 但直到 1933 年 Kolmogorov 建立概率论的公理化体系, 概率论基于集合论、测度论的严密理论基础才得以奠定.

这一节主要介绍基于集合论、测度论的概率论的基本概念。由于篇幅所限，有关实变函数论及测度论的一些基本事实不加证明，但都有明确交代，并辅以实例。有需要的读者，可看有关参考文献[5],[7],[10],[12].

可测函数、Lebesgue积分

设 $f(\cdot)$ 为定义在区间 $[a, b]$ 上的函数，在微积分中把区间 $[a, b]$ 分割

$$x _ {0} = a < x _ {1} < x _ {2} < \dots < x _ {n} = b,$$

并在 $[x_k, x_{k+1}]$ 中任取点 $\xi_k, k = 0, \cdots, n-1$ , 构成 Riemann 和

$$\sum_ {k = 0} ^ {n - 1} f (\xi_ {k}) (x _ {k + 1} - x _ {k}).$$

如果当 $\max_{0\leqslant k\leqslant n - 1}(x_{k + 1} - x_k)\longrightarrow 0$ 时， $\sum_{k = 0}^{n - 1}f(\xi_k)(x_{k + 1} - x_k)$ 有有穷极限，并且该极限既不依赖区间 $[a,b]$ 的分割也不依赖于点 $\xi_{k}$ 的选取，那么该极限就是Riemann积分 $\int_a^b f(x)\mathrm{d}x.$ 大家熟知对连续函数 $f(\cdot)$ 存在Riemann积分.

现在来看Dirichlet函数 $f(\cdot)$ .该函数定义在[0,1]上，在有理点取值为1，在无理点上取值为0.那么，当 $\xi_{k}$ 都取在无理点上时，Riemann和为0，而当 $\xi_{k}$ 都取在有理点上时，Riemann和为1，所以对Dirichlet函数Riemann积分不存在．这就自然地导致需要拓宽函数和积分的概念.

一个开区间 $(a,b)$ 的长度 b-a 称为它的测度，即 $\mu(a,b)=b-a$ 。设 $\Delta_{i}, i=0,1,\cdots$ 为互不相交的开区间列，那么 $\mu\left(\sum_{k=0}^{\infty}\Delta_{i}\right)=\sum_{k=0}^{\infty}\mu(\Delta_{i})$ 。

如果对任 $\cdots x \in G$ , 必可找到的一个小邻域 $\delta(x)$ 使 $\delta(x) \in G$ , 那么 $G$ 叫开集. 对任一开集 $G$ , 可用不相交区间列来覆盖它, 这个覆盖有测度. 这种覆盖测度的下确界叫开集 $G$ 的测度。设 $F$ 为有界集， $F \subset (a, b)$ ，用 $F^c$ 表示 $F$ 的余集，即 $F^c = \{x : x \notin F, \infty < x < \infty\}$ 。如果 $(a, b) \cap F^c$ 为开集，则 $F$ 称为闭集。符号 $\cap$ 表示交： $A \cap B = \{x : x \in A; x \in B\}$ 。

对开集定义了测度后，就可以定义闭集 $F$ 的测度

$$\mu F \stackrel {\mathrm{def}} {=} (b - a) - \mu ((a, b) \cap F ^ {c}).$$

上面已定义了集合 $A$ 的余集 $A^c$ , 定义了两个集合的交 $A \cap B$ , 还要定义并 $\cup$ 的运算: $A \cup B = \{x : x \in A \text{ 或 } x \in B\}$ .

设 B 是一个集合类，它具有以下性质：

(1) 它包含一切开区间，并且对可列次交、并运算及取余集都封闭；  
(2) 如果 $B_{1}$ 是任一具有上述性质 1 的集合类，则必有 $B \subset B_{1}$ ，那么 $B$ 中的集合叫 Borel 集， $B$ 叫 Borel $\sigma$ -代数。任一 Borel 集合 $B$ 可用不相交区间来覆盖它，那么 $B$ 的测度 $\mu B$ 定义为这类覆盖的测度的下确界。

测度为零的 Borel 集合 (零测集) 的子集不一定是 Borel 集合。我们把 B 的集合作一个扩充：把任一零测集的任一子集都归到集合类 B 中，并且经这样归并所得集合的测度仍定义为相应 Borel 集合的测度。把经过这样扩充后的集合类记为 L。L 中的集合叫 Lebesgue 可测集，或简称可测集。上面定义的 Lebesgue 可测集的测度叫 Lebesgue 测度，记为 $\lambda$ 。也就是说，对任一 Lebesgue 可测集 $\Lambda$ ，必可找到 Borel 集 A 及 B，使

$$A \subset \Lambda \subset B, \quad \text { 并且 } \quad \lambda (A) = \lambda (B).$$
