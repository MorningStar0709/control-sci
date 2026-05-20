$$\mathbf {w} ^ {1} \wedge \mathbf {w} ^ {2} = \frac {1}{2} (\mathbf {w} ^ {1} + \mathbf {w} ^ {2} - (\mathbf {w} ^ {1} - \mathbf {w} ^ {2}) _ {+})$$

这里对于向量 $\mathbf{w},\mathbf{w}_{+}$ 表示各分量取绝对值形成的向量．因为 $(\mathbf{w}^{1} - \mathbf{w}^{2})_{+}$ 是连续的，因此 $\mathbf{w}^1\vee \mathbf{w}^2$ 和 $\mathbf{w}^1\wedge \mathbf{w}^2$ 是连续的．用归纳法可得 $\chi (F\vee BK)$ 是连续的．

当状态分量 $x_{i}$ 能达时，总可作状态反馈 $\pmb{K}$ ，使 $x_{i}$ 经过输入点 $u$ 形成新的含 $K$ 中元 $k_{i}$ 为弧重的 $r$ 色自回路，这回路均重随 $k_{i} \to +\infty$ 而 $\to +\infty$ 。对 $|I|$ 种颜色均如此。当 $k_{i}$ 充分小时，新回路对 $\mu_{i}(A_{r})$ 不起作用。若 $x_{i}$ 不能达，则至少有一种颜色 $r_{0}$ ，对任意 $\pmb{K}$ ，其 $\mu_{i}(A_{r_{0}})$ 不变，而 $\mu_{i}(F) \leqslant \mu_{i}(A_{r_{0}})$ 。再应用定理11.10.5，就证明了以下定理：

定理 11.10.6 $^{[25]}$ 系统 (11.10.6) 的周期时间 (广义特征值) 分量 $\mu_{i}(F \vee BK)$ 能在 $[\mu_{i}(F), +\infty)$ 中任意配置的充要条件是 $x_{i}$ 为 $(F, B, C)$ 的能达分量.

类似地，对输出反馈，相应的充要条件是 $x_{i}$ 为能达能观测分量.

由于 K 中元的耦合作用， $G^{*}(F \vee BK)$ 中凝点的数目 $\omega'$ 可 $\leqslant G^{*}(F)$ 中凝点的数目 $\omega$ ，当取 < 号时称为合并配置，取 = 号时称为不合并配置。使 $\omega' = 1$ (即全部合并) 的能配置的充要条件是系统能达；文献 [25] 把它推广到部分合并的情况。对于不合并配置，当且仅当系统能达时，能找到适当的 K，使对每个 $i, 1 \leqslant i \leqslant n, \mu_{i}(F \vee BK)$ 能在 $[\mu_{i}(F), +\infty)$ 中任意配置，且 $\omega' = \omega$ 。

以上各类配置中， $\omega$ 个 $\mu_{i}$ 相互之间可以是不独立的，有某种依赖关系，这就没有发挥配置的最大潜力，也不能与传统线性系统中的极点配置完全对应。因此需要考虑以下比不合并配置更进一步的独立配置问题。

定义 11.10.7 向量集 $\Delta \in \mathbb{R}^{\omega}$ , 称为系统 $S$ 的 (状态反馈下的周期时间) 配置域, 是指对于任意向量 $z \in \Delta$ , 能找到 $K$ 使 $F \vee BK$ 的周期时间为 $z$ . 若 $\Delta$ 包含 $\mathbb{R}^{\omega}$ 中一个的球心为 $M = [m_1, m_2, \cdots, m_\omega]$ , 半径为 $N$ 的 $\omega$ 维球, 这里 $N$ 为先取定的充分大的正常数, $m_1, m_2, \cdots, m_\omega$ 均为由 $N$ 确定的充分大的正常数, 则称 $\Delta$ 为 $\omega$ 维的. 若系统 $S$ 的配置域 $\Delta$ 为 $\omega$ 维的, 则称系统 $S$ 的周期时间能用状态反馈 (独立) 配置.

定理11.10.7 系统 $S$ 的周期时间能用状态反馈（独立）配置的充要条件是存在一个标准序，使得在 $G^{*}(S)$ 中以下条件成立：

(1) 恰有 $\omega$ 条弧 $u_{i}X_{i}, 1 \leqslant x \leqslant \omega$ :

(2) 没有弧 $u_{i}X_{j}, 1 \leqslant j \leqslant i \leqslant \omega$ :

(3) 对每个 $i$ , 存在一种色 $r(i)$ , 使得当 $j > i$ 时, 从 $X_{j}$ 到 $X_{i}$ 无 $r(i)$ 色路.

以上定理的证明相当困难，需要较大篇幅，因此略去。当 $F$ 退化为一个阵 $\pmb{A}$ 时，上述条件(3)由标准序定义自然满足，这时定理11.10.7与定理11.6.2一致。

用定理 11.2.5 中 F 的对偶表达式可建立非自治极大极小系统：

$$
\left\{ \begin{array}{l} \boldsymbol {x} (k + 1) = \vee_ {\overline {{r}} \in J} (\overline {{A}} _ {\overline {{r}}} \boldsymbol {x} (k)) \wedge B \boldsymbol {u} (k), \\ \boldsymbol {y} (k) = C \boldsymbol {x} (k), \end{array} \right.
$$
