# 5.4 镇定问题: 可镇定条件和算法

状态反馈的镇定问题 对于线性定常受控系统

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \quad \boldsymbol {x} \in \mathcal {R} ^ {n}, \boldsymbol {u} \in \mathcal {R} ^ {p} \tag {5.67}$$

如果可以找到状态反馈控制律

$$\boldsymbol {u} = - K \boldsymbol {x} + \boldsymbol {v}, \quad \boldsymbol {v} \text {为参考输入} \tag {5.68}$$

使得通过反馈构成的闭环系统

$$\boldsymbol {x} = (A - B K) \boldsymbol {x} + B \boldsymbol {v} \tag {5.69}$$

是渐近稳定的，也即其特征值均具有负实部，则称系统（5.67）实现了状态反馈镇定。实质上，镇定问题是极点配置问题的一类特殊情况。在镇定问题中，综合的目标不是要使闭环系统的极点严格地配置到任意指定的一组位置上，而是使其配置于复数平面的左半开平面上，因此这类问题属于极点区域配置问题。利用这一特点，可以很容易由极点配置问题的讨论结果，导出镇定问题的相应结论。

可镇定条件 依据极点配置的基本定理可知,如果系统 $\{A, B\}$ 为能控,则必存在状态反馈增益矩阵 K,使得 $(A - BK)$ 的全部特征值配置到任意指定的一组位置上。当然,这也包含了使 $\operatorname{Re}\lambda_{i}(A - BK) < 0, i = 1, 2, \cdots, n$ 。因此, $\{A, B\}$ 为能控是系统 (5.67) 可由状态反馈实现镇定的一个充分条件。状态反馈镇定的充分必要条件则由下述结论给出:

结论 线性定常系统(5.67)是由状态反馈可镇定的, 当且仅当其不能控部分是渐近稳定的。

证 由 $\{A, B\}$ 为不完全能控，则必可对其引入线性非奇异变换而进行结构分解：

$$
\bar {A} = P A P ^ {- 1} = \left[ \begin{array}{l l} \bar {A} _ {e} & \bar {A} _ {1 2} \\ 0 & \bar {A} _ {e} \end{array} \right], \quad \bar {B} = P B = \left[ \begin{array}{l} \bar {B} _ {e} \\ 0 \end{array} \right] \tag {5.70}
$$

并且对任意 $K = [K_1, K_2]$ 可导出 $\overline{K} = KP^{-1} = [\overline{K}_1, \overline{K}_2]$ 。于是，由此可得到

$$
\begin{array}{l} \det (s I - A + B K) = \det (s I - \bar {A} + \bar {B} \bar {K}) \\ = \det \left[ \begin{array}{c c} (s I - \bar {A} _ {e} + \bar {B} _ {c} \bar {K} _ {1}) & - \bar {A} _ {1 2} + \bar {B} _ {c} \bar {K} _ {2} \\ 0 & (s I - \bar {A} _ {e}) \end{array} \right] \\ = \det (s I - \bar {A} _ {c} + \bar {B} \bar {K} _ {1}) \det (s I - \bar {A} _ {c}) \tag {5.71} \\ \end{array}
$$

但知 $\{\overline{A}_c, \overline{B}_c\}$ 为能控，故必存在 $\overline{K}_1$ 使 $(\overline{A}_c - \overline{B}_c\overline{K}_1)$ 的特征值均具有负实部。从而，由(5.71)即知，存在 $K$ 使 $(A - BK)$ 的特征值均具有负实部，也即系统(5.67)为由状态反馈可镇定的充分必要条件，是不能控部分 $\overline{A}_s$ 的特征值均具有负实部。这样，就完成了证明。

算法 给定 $\{A, B\}$ ，且知其满足可镇定条件，则镇定问题中综合状态反馈增益矩阵 K 的计算可按下述步骤来进行：

第1步：对 $\{A, B\}$ 按能控性进行结构分解，导出 $\{\overline{A}_c, \overline{B}_c\}$ ，并求出变换阵 $P$ 。

第2步：对 $\{\overline{A}_e,\overline{B}_e\}$ 求出约当规范形：

$$
\tilde {A} _ {c} = Q ^ {- 1} \bar {A} _ {c} Q = \left[ \begin{array}{l l} \tilde {A} _ {1} & 0 \\ 0 & \tilde {A} _ {2} \end{array} \right], \quad \tilde {B} _ {c} = Q ^ {- 1} \bar {B} _ {c} = \left[ \begin{array}{l} \tilde {B} _ {1} \\ \tilde {B} _ {2} \end{array} \right]
$$
