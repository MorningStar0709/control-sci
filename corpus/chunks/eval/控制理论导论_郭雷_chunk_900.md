由定理 11.10.4, 仅需在 $R^w$ 中研究 $\chi(F)$ 的 $w$ 个不同分量。标准序与凝着色图工具揭示了 $F$ 的广义特征值的块状规律，这使许多问题得到简化。当下面研究‘极点’配置时，可类似于 11.6 节考虑块合并与不合并配置。白色图与标准形使 (结构) 能达能观测性的判据与系统的标准结构能描述为类似于 11.5 节中的形式，详见文献 [25]。

对于系统 $S$ 分别施加状态反馈

$$\boldsymbol {u} (k) = \boldsymbol {K} \boldsymbol {x} (k), \quad \boldsymbol {K} \in D ^ {q \times n}, \tag {11.10.5}$$

和输出反馈

$$\boldsymbol {u} (k) = \boldsymbol {K} \boldsymbol {y} (k), \quad \boldsymbol {K} \in D ^ {q \times p}.$$

则得到下面的闭环系统

$$
\left\{ \begin{array}{l} \boldsymbol {x} (k + 1) = F (\boldsymbol {x} (k)) \vee \boldsymbol {B K} (\boldsymbol {x} (k)) = \wedge_ {r \in I} (\boldsymbol {A} _ {r} \vee \boldsymbol {B K}) \boldsymbol {x} (k), \\ \boldsymbol {y} (k) = \boldsymbol {C x} (k) \end{array} \right. \tag {11.10.6}
$$

和

$$
\left\{ \begin{array}{l} \boldsymbol {x} (k + 1) = F (\boldsymbol {x} (k)) \vee B K C (\boldsymbol {x} (k)) = \wedge_ {r \in I} (\boldsymbol {A} _ {r} \vee B K C) \boldsymbol {x} (k), \\ \boldsymbol {y} (k) = C \boldsymbol {x} (k). \end{array} \right.
$$

类似于11.6节，可以研究与极点配置相对应的各类周期时间(即广义特征值)配置问题．我们主要论述状态反馈，关于输出反馈可得到对应的结果.

这里要指出与11.6节的一个不同处．对线性系统 $(A, B, C)$ ，是配置 $A \oplus BK$ 的不可约子阵，或合并后的不可约阵的特征值，与状态向量 $x$ 无关．对非线性系统 $(F, B, C), F$ 离不开 $x$ ，是配置 $\chi(F \vee BK)$ ，由定义它是状态向量的某种极限式，因而更复杂一些．

回忆11.6节中当 $\pmb{A}$ 不可约时，由于极大运算不能减小 $\pmb{A}$ 的特征值 $\lambda$ 。所以最大的配置范围是 $[\lambda, +\infty)$ 。为达到在这范围内用 $\pmb{K}$ 任意配置周期，最基本重要的性质是，被配置的周期为 $\pmb{K}$ 的元的连续单调增函数（且不取一个常数）。现在 $\chi(F \vee B K)$ 也有类似的基本性质。

定理 11.10.5 $^{[25]}$ 对任何状态反馈 (11.10.5), 系统 (11.10.6) 的周期时间 $\chi(F \vee BK)$ 是关于 K 中元的连续单调增函数.

证明 假设对系统施加状态反馈 $\pmb{u}(k) = \pmb{K}\pmb{x}(k)$ ，则在 $G(S)$ 中增加了一些从 $x_{i}$ 到 $u_{j}$ 的具有权重 $k_{ji}$ 的弧。由定理11.6.1，这种回路的均重是关于 $\pmb{K}$ 中元 $k_{ji}$ 的仿射函数。注意到 $\mathbb{R}^{q\times n} \cong \mathbb{R}^{qn}$ ，由对偶定理知闭环系统 $\chi(F \vee BK)$ 的周期时间是从 $\mathbb{R}^{qn}$ 到 $\mathbb{R}^n$ 的非线性函数，即

$$\chi (F \vee B K) = \wedge_ {r \in I} \mathbf {w} (\mathbf {k}, r)$$

这里 $\mathbf{k} \in \mathbb{R}^{nq}, \mathbf{w}(\cdot)$ 表示 $n$ 维列向量，它的每一个分量是一些仿射函数取极大。因为上述仿射函数的所有系数大于0，用归纳法我们可得

$$\chi (F \vee B K) \leqslant \chi (F \vee B K ^ {\prime}), \forall \mathbf {k}, \mathbf {k} ^ {\prime} \in R ^ {q n}, \mathbf {k} \leqslant \mathbf {k} ^ {\prime}.$$

于是， $\chi (F\vee BK)$ 是单调增加的．对于 $n$ 维列向量函数 $\mathbf{w}$

$$\mathbf {w} ^ {1} \vee \mathbf {w} ^ {2} = \frac {1}{2} (\mathbf {w} ^ {1} + \mathbf {w} ^ {2} + (\mathbf {w} ^ {1} - \mathbf {w} ^ {2}) _ {+})$$

和
