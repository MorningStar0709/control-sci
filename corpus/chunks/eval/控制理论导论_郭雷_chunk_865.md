本节将结束对极大代数上一般线性系统 $(A, B, C)$ 的讨论。在结束前，准备对稳定性以外的其他两个问题作简单论述，这就是几何方法与实现理论。

对应于几何方法中的能控性子空间, 我们在 11.5 节中引入了分别能达子模等, 并得到了系统的标准结构. 这些应是 DEDS 几何方法的一部分, 相对容易. 我们也引入了 $[1, N]$ 上的能达子模, 研究了其维数等, 这方面还很不成熟, 数学工具有待完善, 是较为困难的方向. 几何方法中另一重要概念是 $(A, B)$ - 不变子空间. 下面介绍相关的一些探索. 首先引入 $(A, B)$ - 不变子模概念.

定义 11.7.3 设 V 是 $D^{1 \times n}$ 中的一个子模。若有 $V A \subset V$ ，则称 V 为 A 不变子模；若有 K 使 $\mathcal{V}(A \oplus KB) \subset \mathcal{V}$ ，则称 V 为 $(A, B)$ -不变子模。若含于 ker C 的所有 $(A, B)$ -不变子模都包含在一个含于 ker C 的 $(A, B)$ -不变子模 $V^{*}$ 中，则称 $V^{*}$ 为含于 ker C 的最大 $(A, B)$ -不变子模。

显然， $A$ 不变子模一定是 $(A,B)$ - 不变子模，只要取 $K = \phi$ 但反之则不然.

例 11.7.2 令 V 是 $v_{1} = [2, 1]$ , $v_{2} = [1, 2]$ 生成的子模， $A = \begin{bmatrix} 0 & 1 \\ -2 & 4 \end{bmatrix}$ , B = [2, 2], 则 $v_{1}A = [2, 5]$ , $v_{2}A = [1, 6]$ , V A $\not\subset V$ , 所以 V 不是 A 不变子模。但存在 $K = [1, 1]$ , $A \oplus KB = \begin{bmatrix} 3 & 3 \\ 3 & 4 \end{bmatrix}$ , $v_{1}(A \oplus KB) = [5, 5]$ , $v_{2}(A \oplus KB) = [5, 6]$ , 所以

$$\mathcal {V} (\boldsymbol {A} \oplus \boldsymbol {K B}) \subset \mathcal {V},$$

$\nu$ 是 $(A, B)$ - 不变子模.

上例说明，在 $D$ -模中 $(A, B)$ -不变子模概念确实与 $A$ 不变子模概念不同。由于 $D$ 上有限生成模的结构与几何形态已足够复杂，所以对 $(A, B)$ -不变子模的一般性研究也是复杂与困难的。但是在几何方法中讨论干扰解耦问题 (DDP) 时，用的是 $\mathcal{V}^*$ ，这种子模结构简单而清楚，我们来一步步弄清楚它。下面引理说明有一类 $(A, B)$ -不变子模一定是 $A$ 不变子模。

引理11.7.1 记 $x^{r} = \{[\phi X_{r}] \mid X_{r} \in D^{1 \times r}, [\phi X_{r}] \in D^{1 \times n}, 1 \leqslant r \leqslant n\}$ , 那么当且仅当

$$
\boldsymbol {A} = \left[ \begin{array}{c c} \boldsymbol {A} _ {1} & \boldsymbol {A} _ {1 2} \\ \phi & \boldsymbol {A} _ {2} \end{array} \right], \quad \boldsymbol {A} _ {2} \in D ^ {r \times r}, \quad \boldsymbol {A} \in D ^ {n \times n} \tag {11.7.2}
$$

时 $x^r$ 是 $\pmb{A}$ 不变子模，且也是 $(\pmb {A},\pmb {B})$ - 不变子模.

证明 充分性. 式 (11.7.2) 成立时, 易验证 $x^r A \subset x^r$ ; 取 $\pmb{K} = \phi$ , 易知 $x^r(A \oplus KB) \subset x^r$ .

必要性. 若 $A \oplus KB$ 不具有类似式 (11.7.2) 的形式, 则左下角的非 $\varepsilon$ 元必然使某个 $X \in x^r$ , 但是 $X(A \oplus KB) \notin x^r$ , 矛盾. (类似可证式 (11.7.2) 是 $x^r$ 为 $A$ 不变子模的必要条件.) 再由 $D$ 中 $a \oplus b = \varepsilon \Longrightarrow a = \varepsilon, b = \varepsilon$ , 所以 $A \oplus KB$ 具有式 (11.7.2) 形式导致 $A$ 与 $KB$ 都有式 (11.7.2) 的形式.

以上引理说明 $X_{r}$ 的分量取 $D$ 中任意值，其他分量为 $\varepsilon$ 而形成的子模（相当于 $n$ 维欧氏空间中 $r$ 个标准正交基形成的 $r$ 维子空间），当其为 $(A, B)$ -不变子模时，一定是 $A$ 不变子模。这是由于 $D$ 中 $a \oplus b = \varepsilon \Longrightarrow a = \varepsilon, b = \varepsilon$ 。极大代数加法 $\oplus$ 没有逆运算的上述特点，使找 $\gamma^{*}$ 变得容易了，它就是上限不能观测子模，见以下定理。
