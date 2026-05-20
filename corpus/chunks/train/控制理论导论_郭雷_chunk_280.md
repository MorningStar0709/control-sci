# 集合、空间、测度

我们要把可测集、可测函数等概念，进一步推广到一般的空间中去.

设 $\Omega$ 为全空间，它的元素称为点，记作 $\omega$ 。用 $A, B, C$ 等表示点集。用 $\varnothing$ 表示空集。

和 $\mathbb{R}^1$ 类似，对 $\Omega$ 中的集合也可引进并 $\cup$ 、交 $\cap$ 及求余集的运算

$$A \cup B = \{\omega : \omega \in A \text {或} \omega \in B \}; \qquad A \cap B = \{\omega : \omega \in A, \omega \in B \};A ^ {c} = \varOmega \backslash A = \{\omega : \omega \in \varOmega \text {但} \omega \not \in A \}.$$

设 $\mathcal{F}$ 为一个集合类，即 $\mathcal{F}$ 中的元都是 $\Omega$ 中的集合，且满足以下条件：

(1) $\Omega \in \mathcal{F}$ , 即全空间也是 $\mathcal{F}$ 的元;  
(2) 若 $A \in \mathcal{F}$ , 则 $A^c \in \mathcal{F}$ , 即若 $A$ 是 $\mathcal{F}$ 的元, 则它的余集也是 $\mathcal{F}$ 的元;  
(3) 若 $A_{i} \in \mathcal{F}, i = 1,2,\dots$ , 则 $\bigcup_{i=1}^{\infty} A_{i} \in \mathcal{F}$ , 即 $\mathcal{F}$ 对求可列并封闭.

那么 $\mathcal{F}$ 叫 $\sigma$ -代数或 $\sigma$ -域，而 $(\Omega, \mathcal{F})$ 叫可测空间.

我们来证 $\bigcap_{i=1}^{\infty} A_i = \left( \bigcup_{i=1}^{\infty} A_i^c \right)^c$ , 也就是要证 $\left( \bigcap_{i=1}^{\infty} A_i \right)^c = \bigcup_{i=1}^{\infty} A_i^c$ .

设 $\omega \in$ 上式左端，即 $\omega$ 不属于 $\{A_i\}$ 的公共部分，也就是说 $\omega$ 至少不属于某个 $A_i$ ，即 $\omega \in A_i^c$ ，所以 $\omega \in$ 上式右端。反之，若 $\omega \in$ 上式右端，那么 $\omega$ 必属于某个 $A_i^c$ ，也就是 $\omega$ 不属于 $A_i$ ，那么 $\omega \notin \bigcap_{i=1}^{\infty} A_i$ ，所以 $\omega$ 属于上式左端。这样就证明上面集合之间的等式。

设 $\mathcal{F}$ 为 $\sigma$ -代数， $A_i \in \mathcal{F}, i = 1, 2, \cdots$ 。据条件 $2, A_i^c \in \mathcal{F}$ ，据条件 $3, \bigcup_{i=1}^{\infty} A_i^c \in \mathcal{F}$ ，又据条件 $2, \left( \bigcup_{i=1}^{\infty} A_i^c \right)^c \in \mathcal{F}$ 。所以 $\bigcap_{i=1}^{\infty} A_i \in \mathcal{F}$ 。这就是说 $\sigma$ -代数对可列个交也封闭。

有了 $\sigma$ -代数的概念后，我们回到上面定义的 Borel $\sigma$ -代数，它就是包含所有开区间的最小 $\sigma$ -代数.

设 $\{A_{n}\}$ 是可测集合序列 $A_{i} \in \mathcal{F}$ , 除了有穷个 $A_{i}$ 外, 属于其余所有 $A_{i}$ 的点 $\omega$ 构成 $\{A_{n}\}$ 的下确界

$$\liminf _ {n \to \infty} A _ {n} = \bigcup_ {n = 1} ^ {\infty} \bigcap_ {k = n} ^ {\infty} A _ {k}. \tag {4.1.3}$$

类似地，属于无穷多个 $A_{i}$ 的点构成 $\{A_i\}$ 的上确界

$$\limsup _ {n \to \infty} A _ {n} = \bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = n} ^ {\infty} A _ {k}. \tag {4.1.4}$$

显然， $\liminf_{n\to \infty}A_n\in \mathcal{F},\limsup_{n\to \infty}A_n\in \mathcal{F},$ 并且

$$\liminf _ {n \to \infty} A _ {n} \subset \limsup _ {n \to \infty} A _ {n}.$$

若两者相等，则称 $\{A_{n}\}$ 收敛

$$\lim _ {n \to \infty} A _ {n} = A (= \operatorname * {l i m i n f} _ {n \to \infty} A _ {n} = \operatorname * {l i m s u p} _ {n \to \infty} A _ {n}).$$
