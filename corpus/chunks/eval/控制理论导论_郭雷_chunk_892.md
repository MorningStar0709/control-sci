令 $x = [\langle t \rangle, \langle t \rangle_{2}, \cdots, \langle t \rangle_{13}]^{T}$ . 则由上面式子可得矩阵 A. 热轧线可建模为

$$\boldsymbol {x} = \boldsymbol {A} \boldsymbol {x} \oplus \overline {{{\boldsymbol {v}}}},$$

其中 $\bar{v} = [\bar{u}, \bar{0}, \cdots, \bar{0}]^{T}$ . 由式 (11.9.3) 和式 (11.9.4) 可得 $\lambda = (2 \times 2 + 1) \times 2 + 1.5 = 11.5$ , 热轧线加工完 18 个工件的批周期为 $\bar{\lambda} = \max\{45, 6 \times 11.5\} = 69$ . 热轧机的最大利用率 $= \frac{18 \times (2 + 1.5)}{69} \approx 0.913$ .

上例不很复杂，但用这个例说明的建模与分析的方法可应用于很复杂的制造系统，在计算机的帮助下，可计算出生产周期等重要参数.

下面来研究系统 (11.9.2) 的控制. 在式 (11.9.2) 中引入控制项 $u$ , 得

$$\boldsymbol {x} = \boldsymbol {A} \boldsymbol {x} \oplus \boldsymbol {v} \oplus \boldsymbol {u} \stackrel {\text { def }} {=} \boldsymbol {A} \boldsymbol {x} \oplus \boldsymbol {I} _ {\mathrm{c}} \boldsymbol {y} \oplus \boldsymbol {v}. \tag {11.9.5}$$

其中

$$
(I _ {c}) _ {i j} = \left\{ \begin{array}{l l} {[ 0 ],} & {\quad \text {当} i = j, t _ {i} \in T _ {c},} \\ {[ \varepsilon ].} & {\quad \text {其他情形}.} \end{array} \right.
$$

[0] 和 $[\varepsilon]$ 分别是 $\langle F, \otimes \rangle$ 中的单位元与零元， $T_{c} \subseteq T$ 是控制变迁集， $t_{i} \in T_{c}$ 是控制变迁.

前几节论述了图论方法在 TEG 中的应用，本节进一步把图论方法用于 ETEG 中。前面曾给出了例 11.9.1 的 A 与 $G(A)$ 的关系，一般地可有如下定义：

定义11.9.4 对式(11.9.5)中的任意一个 $A \in F^{n \times n}$ . 都存在一个赋权有向图 $G(A)$ 与之对应, $A$ 的 $n$ 行位置 (或列位置) 在 $G(A)$ 中有 $n$ 个点与之对应. 当阵 $A$ 的第 $i$ 行第 $j$ 列元素 $(A)_{ij} \neq [\varepsilon]$ 时, 从点 $j$ 到点 $i$ 存在一条弧 $ji$ , 其权为 $(A)_{ij}$ ; 当 $(A)_{ij} = [\varepsilon]$ 时, 从点 $j$ 到点 $i$ 不存在弧. 图 $G(A)$ 称为阵 $A$ 的关联图.

与 TEG 不同，这里弧的权为算子，本身无法比较轻重， $(A^{k})_{ij}$ 只能对 j 到 i 长为 k 的所有路的权求和 $(\Sigma_{\oplus})$ ，而不是最重路。从 $i_{0}$ 到 $i_{k}$ 的路 $i_{0}i_{1}\cdots i_{k}$ 的权

$W(i_0i_1\dots i_k)$ 定义为弧的权的复合算子，用上述方法可计算出 $\pmb{A}^*$ ，即 $(\pmb{A}^{*})_{ij}$ 等于从 $j$ 到 $i$ 的所有路的权求和.

尽管 A 的元素无轻重之分，但根据 A 中元素 $\neq [\varepsilon]$ 或 $=[\varepsilon]$ ，仍可揭示出 $G(A)$ 中点与点是否有弧连接，即 ETEG 的变迁之间是否有一个位置连通。因而 ETEG 中与结构连通有关的本质特征可用图 $G(A)$ 为工具加以研究。

类似于11.2节，可引入强连通，凝图，不可约，标准形与序，强凝网等概念，详见文献[6].

对于 ETEG, 考虑带控制输入 $u$ 的模型 (11.9.5), 也可引入能达性的概念.

定义11.9.5 系统(11.9.5)对应的ETEG中，能与某输入分量 $y_{r_i}$ 连通的状态分量(即中间变迁) $x_{i}$ 称为能达的；否则，称为不能达的，当且仅当全部 $n$ 个分量 $x_{i}(1 \leqslant i \leqslant n)$ 均能达时，称系统能达.

系统 (11.9.5) 中的阵 $I_{c}$ 实质上与 TEG 中的阵 $\pmb{B}$ 作用类似.

定理11.9.4 (1) 在系统(11.9.5)的强凝网中，从 $u$ 出发，有路能达到的所有凝点对应的状态分量集合是系统(11.9.5)的全部能达状态分量；

(2) 系统 (11.9.5) 能达的充要条件是在 (11.9.5) 的强凝网中，从点 $u$ 到 $G^{*}(A)$ 的无进弧的凝点都有弧.
