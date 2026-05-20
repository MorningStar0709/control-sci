由定义可知，第二可数拓扑空间必定为第一可数拓扑空间.

例3.3.9 给定任一集合 $X$ .(1)定义 $\mathcal{T} = \{X,\varnothing \}$ .容易看出 $\pmb{T}$ 是一个拓扑.这个拓扑称为平凡拓扑．它是最粗的拓扑；

(2) 定义 $T = \{U \mid U \subset X\}$ . 那么 $T$ 包含 $X$ 所有的子集. 它显然也是 $X$ 上的一个拓扑. 这个拓扑称为离散拓扑. 它是最细的拓扑.

例3.3.10 在 $\mathbb{R}^n$ 中我们考虑所有的开球

$$B _ {r} (c) = \{x \in \mathbb {R} ^ {n} \mid \| x - c \| < r \}, \quad \forall c \in \mathbb {R} ^ {n}, r > 0,$$

记其为 $B$ 。注意到 $B$ 中有限个球的交可以表示成 $B$ 中一些球的并。基于这个事实不难看出， $B$ 中某些元素的所有可能的并集形成一个拓扑。这个拓扑是 $\mathbb{R}^n$ 中的普通拓扑，因为这个拓扑里的元素正是我们通常称为“开集”的那些东西。

上面得到的这个拓扑 $\pmb{T}$ , 称为由距离导出的拓扑, 因为那里的球是由距离导出的. 根据定义 $B$ 是 $\mathbb{R}^n$ 的一个拓扑基.

考虑一个子集 $B^{Q} \subset B$ , 它由有理数球心 (即球心的坐标均为有理数) 和有理数半径组成. 那么 $B^{Q}$ 是一个可数集. 并且容易看出, $B^{Q}$ 是 $\mathbb{R}^{n}$ 的一个拓扑基. 因此 $\mathbb{R}^{n}$ 及其普通拓扑是一个第二可数的拓扑空间.

不难证明，在有穷维赋范空间中所有的范数导出的拓扑都一样。这也就是通常说的有穷维空间上的任何两个范数都等价。

例3.3.11 考虑一个真多项式分式 (可看作线性系统的传递函数)

$$\frac {Q (s)}{P (s)} = \frac {q _ {n - 1} s ^ {n - 1} + q _ {n - 2} s ^ {n - 2} + \cdots + q _ {0}}{s ^ {n} + p _ {n - 1} s ^ {n - 1} + \cdots + p _ {0}}.$$

确定 $Q(s)$ 和 $P(s)$ 是否互质在控制论中十分重要。考虑系数集， $\{q_{n-1},\cdots,q_{0},p_{n-1},\cdots,p_{0}\}$ ，将其看作 $R^{2n}$ 中的一个点。可以证明，使 $Q(s)$ 与 $P(s)$ 互质的那些点形成一个开集。要证明这一点，记 $2n \times 2n$ 矩阵

$$
S = \left[ \begin{array}{c c c c c c} 1 & p _ {n - 1} & & \dots & p _ {0} & \\ 0 & 1 & p _ {n - 1} & \dots & & p _ {0} \\ & & \ddots & \dots & & \ddots \\ & & & 1 & p _ {n - 1} & \dots & p _ {0} \\ 0 & q _ {n - 1} & & \dots & q _ {0} & \\ & 0 & q _ {n - 1} & \dots & & q _ {0} \\ & & \ddots & \dots & & \ddots \\ & & & 0 & q _ {n - 1} & \dots & q _ {0} \end{array} \right].
$$

利用数学归纳法可以证明 $Q(s)$ 与 $P(s)$ 互质，当且仅当 $\operatorname{det}(S) \neq 0$ 。这就证明了我们的断言。

定义 3.3.7 设 M 为一拓扑空间， $A \subset M$ .

(1) $A$ 的闭包，记作 $\bar{A}$ 或 $\operatorname{cl}(A)$ ，定义为包含 $A$ 的最小闭集。它等价于

$$\overline {{{A}}} = \cap \{C \mid C \text {闭且} C \supset A \};$$

(2) $A$ 的内部，记作 $\operatorname{int}(A)$ ，是 $A$ 所包含的最大开集。它等价于

$$\operatorname{int} (A) = \cup \{U \mid U \text {开且} U \subset A \};$$

(3) $A$ 的边界，记作 $\operatorname{bd}(A)$ ，定义为

$$\operatorname{bd} (A) = \overline {{{A}}} \cap \overline {{{A ^ {c}}}};$$

(4) $A$ 称为 $M$ 的一个稠集，如果 $\overline{A} = M$ ;  
(5) $A$ 称为在 $M$ 中无处稠，如果 $\vec{A}$ 不包含任何非空开集.

例 3.3.12 考虑 $R^{1}$ 连同普通拓扑.

(1) 设 $A = [0, 1] \subset \mathbb{R}^1$ , 则 (i) $\overline{A} = [0, 1]$ ; (ii) $\operatorname{int}(A) = (0, 1)$ ; $\operatorname{bd}(A) = \{0, 1\}$ ;   
(2) 设 $Q$ 为有理数集，那么 $Q$ 在 $\mathbb{R}^1$ 中稠；  
(3) 设 $Z$ 为整数集，则 $Z$ 在 $\mathbb{R}^1$ 中无处稠.

命题3.3.2 设 $A \subset M$ . 那么
