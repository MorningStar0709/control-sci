# 3.1 群

群是研究动态系统（包括控制系统）对称性及不变性等的一个重要工具。有些控制系统，例如卫星姿态控制系统，它的状态空间就是一个群。

定义3.1.1 一个集合 $G$ 连同一种运算 $\otimes: G \times G \to G$ 称为群，如果它满足以下的条件：

G1: (结合律) 对任意的 $a, b, c \in G$

$$(a \otimes b) \otimes c = a \otimes (b \otimes c). \tag {3.1.1}$$

G2: (单位元) 存在一个元素 $e$ , 使得

$$g \otimes e = e \otimes g = g, \quad \forall g \in G. \tag {3.1.2}$$

这样的 e 称为单位元.

G3: (逆元) 对每一个 $g \in G$ 存在一个元素 $g^{-1}$ 称为 $g$ 的逆，使得

$$g \otimes g ^ {- 1} = g ^ {- 1} \otimes g = e. \tag {3.1.3}$$

一个群 $G$ 如果还满足

$$a \otimes b = b \otimes a, \qquad \forall a, b \in G, \tag {3.1.4}$$

则称 $G$ 为一个Abel群.

例 3.1.1 (1) C (复数集), R (实数集), Q (有理数集), Z (整数集) 连同普通加法 “+”, 均为群;

(2) $\mathbb{C} \setminus \{0\}$ , $\mathbb{R} \setminus \{0\}$ , $\mathbb{Q} \setminus \{0\}$ 连同普通乘法“ $\times$ ”, 均为群. $\mathbb{Z}$ 连同普通乘法“ $\times$ ”, 不是群, 因为如果 $z \neq \pm 1$ , 则 $z$ 在 $\mathbb{Z}$ 中没有逆;  
(3) 记 $\operatorname{gl}(n, \mathbb{C})$ , $(\operatorname{gl}(n, \mathbb{R}))$ 为 $n \times n$ 复 (实) 矩阵, 连同普通矩阵加法, $\operatorname{gl}(n, \mathbb{C})$ , $(\operatorname{gl}(n, \mathbb{R}))$ 是一个群, 它称为一般线性代数;  
(4) 记 $\operatorname{GL}(n, \mathbb{C})$ , $(\operatorname{GL}(n, \mathbb{R}))$ 为 $n \times n$ 可逆复 (实) 矩阵, 连同普通矩阵乘法, $\operatorname{GL}(n, \mathbb{C})$ , $(\operatorname{GL}(n, \mathbb{R}))$ 是一个群, 它称为一般线性群. 这个群不是 Abel 群.

例 3.1.2 给定集合 $Z_{n}=\{0,1,\cdots,n-1\}$ 及一种运算 $\oplus$ 定义如下：

$$a \oplus b \stackrel {\text { def }} {=} a + b (\mathrm{mod} n),$$

则 $\mathbb{Z}_n$ 为一个群，称为 $n$ 阶循环群。在这个群中0是单位元，它的逆是它自己。 $z \neq 0$ 的逆是 $n - z$ 。例如，在 $\mathbb{Z}_5$ 中： $3 \oplus 4 = 2; 4^{-1} = 1$ 等。

例 3.1.3 给定一个集合 $G_{n}=\{1,2,\cdots,n\}$ . 以所有 $G_{n}$ 上元素的排列作为集

如果，它们在 $x \in \mathbb{R}^{n}$ 时，它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可以得到第一个条件。它们可

$$\sigma_ {2} \otimes \sigma_ {1} = (3, 4, 5);$$

$(G,\otimes)$ 为一个群， $H\subset G$ 是它的一个子集，如果 $(H,\otimes)$ ， $G$ 的一个子群，记作 $H\in G$

集合 $g \otimes H \stackrel{\mathrm{def}}{=} \{g \otimes h \mid h \in H\}$ 称为 $H$ 的左 $g$ -陪集. $\left|h \in H\right\}$ 称为 $H$ 的右 $g$ -陪集；

一个正规子群，如果对任 $y \in \mathcal{O}$ 均有

$$g \otimes H = H \otimes g.$$
