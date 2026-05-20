![](image/cd98ac734b3f6680f6ccaa4e8512d2a2667be8ba592b68d63c114f82c72b7d52.jpg)

<details>
<summary>text_image</summary>

y
0
1 x
</details>

(a)

![](image/cf11bbfc509c0a20198d67d233de719b865043ff6457330cd34c00f944676ba7.jpg)

<details>
<summary>text_image</summary>

y
0 1 x
</details>

(b)

![](image/336b9de66d91895ed80b4c5f57efdad84ddae6656c995fe9188d65c310969dad.jpg)

<details>
<summary>text_image</summary>

y
0 1 x
</details>

(c)

![](image/320f1d2aa848b3d608fab5a99d168b5145d63998a0313f2ba40b8b35e93dbeff.jpg)

<details>
<summary>text_image</summary>

y
0
1 x
</details>

(d)   
图3.3.2 不同距离下的球

距离空间的一个点列 $\{x_{n}\}$ 称为Cauchy列，如果任给 $\varepsilon >0$ ，存在 $N$ ，使

$$d (x _ {m}, x _ {n}) < \varepsilon , \quad \forall m, n > N.$$

$\{x_{n}\}$ 收敛于点 $x$ ，如果任给 $\varepsilon >0$ ，存在 $N$ ，使 $d(x_{n},x) <   \varepsilon ,\forall n > N.$

定义3.3.4 一个距离空间 $M$ 是完备的，如果每一个Cauchy列 $\{x_{n}\}$ 收敛于一个点 $x\in M$

例3.3.7 (1) $\mathbb{R}^n$ 在普通距离 $d_{1}, d_{2}, d_{\infty}, d_{P}$ 下都是一个完备距离空间；

(2) 设 $C[a, b]$ 为 $[a, b]$ 上连续函数空间。容易证明，若 $C[a, b]$ 赋以例3.3.4中的距离，则它不完备。

下面讨论一般拓扑空间.

定义 3.3.5 给定一个集合 X 及其一个子集族 T.

(1) $(X, T)$ 称为一个拓扑空间，如果 $\pmb{T}$ 满足以下条件：

T1: $X \in \mathcal{T}, \varnothing \in \mathcal{T}$ ,

T2: 如果 $U_{\lambda} \in T, \forall \lambda \in \Lambda$ , 则 $\bigcup_{\lambda \in \Lambda} U_{\lambda} \in T$ ,

T3: 如果 $U_{i} \in T, i = 1, \cdots, n,$ 那么 $\bigcap_{i=1}^{n} U_{i} \in T;$

(2) 一个元素 $U \in T$ 称为一个开集。它的余集，记作 $U^c$ ，称为一个闭集；  
(3) 给定一个点 $x \in X$ , 一个子集 $N$ 称为 $x$ 的一个邻域, 如果存在一个开集 $U$ 使得 $x \in U \subset N$ ;  
(4) 设 $B \subset T, B$ 称为一个拓扑基如果对任意 $U \in T, U$ 可以表示为 $B$ 中的元素的并；  
(5) 一个集合 $\{N_{\lambda} \mid \lambda \in \Lambda\}$ 称为 $x$ 的邻域基，如果对 $x$ 的任一邻域 $N$ 都存在 $N_{\lambda}$ 使 $x \in N_{\lambda} \subset N$ .

实际上给定一个集合 $M$ ，设 $B$ 为 $M$ 的一个子集族， $B$ 能够成为 $M$ 上某一个拓扑的拓扑基，当且仅当 (1) $\cup \{V \mid V \in B\} = M$ ；(2) $B$ 中有限多个元素的交可以表示为 $B$ 中某些元素的并。 $M$ 上的以 $B$ 为其拓扑基的拓扑 $T$ ，称为由 $B$ 生成的拓扑。

例3.3.8 某大学所有的研究生集合记作 $S$ 。设 $M$ 为男生集合， $F$ 为女生集合， $C_i, i = 1,2,3$ 为 $i$ 年级学生集合。给定一个子集族 $B_0 = \{M, F, C_1\}$ ，记由 $B_0$ 生成的最小拓扑为 $T$ 。那么

(1) $\pmb{T}$ 的一个拓扑基是

$$\{A _ {1} = M \cap C _ {1}, A _ {2} = F \cap C _ {1}, A _ {3} = M \cap (C _ {2} \cup C _ {3}), A _ {4} = F \cap (C _ {2} \cup C _ {3}) \};$$

(2) 在拓扑 $\mathcal{T}$ 下， $C_1$ 是一个开集， $C_1$ 也是一个闭集； $C_2$ 既不开也不闭；

(3) 设 $x$ 是一个二年级男生. $x$ 的邻域基包含单个集合 $\{A_4\}$ . 当然 $x$ 的邻域基不唯一. 例如, $\{A_4, M\}$ 也是一个邻域基.

定义3.3.6 (1) 一个拓扑空间称为第二可数的，如果它有一个可数拓扑基；

(2) 一个拓扑空间称为第一可数的，如果对任一点 $x \in X$ 都有一个可数邻域基.
