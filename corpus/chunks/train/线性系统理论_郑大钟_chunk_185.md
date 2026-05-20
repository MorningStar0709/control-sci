$$\mathbf {c} _ {i} B L = \mathbf {0}\mathbf {c} _ {i} (A - B K) B L = \left(\mathbf {c} _ {i} A B\right) L - \left(\mathbf {c} _ {i} B\right) K B L = 0\mathbf {c} _ {i} (A - B K) ^ {2} B L = \left(\mathbf {c} _ {i} A ^ {2} B\right) L - \left(\mathbf {c} _ {i} B\right) K A B L - \left(\mathbf {c} _ {i} A B\right) K B L+ \left(\mathbf {c} _ {i} B\right) K B K B L = 0 \tag {5.99}\bullet \quad \bullet \quad \bullet \quad \bullet \quad \bullet\mathbf {c} _ {i} (A - B K) ^ {d _ {i} - 1} B L = \left(\mathbf {c} _ {i} A ^ {d _ {i} - 1} B\right) L - \left(\mathbf {c} _ {i} A ^ {d _ {i} - 2} B\right) K B L -\dots + \left(\mathbf {c} _ {i} B\right) K (B K) ^ {d _ {i} - 2} B L = 0$$

再由 $c_{i}A^{d_{i}}B \neq 0$ 和(5.98)，又可导出：

$$
\begin{array}{l} \mathbf {c} _ {i} (A - B K) ^ {d _ {i}} B L = \mathbf {c} _ {i} A ^ {d _ {i}} B L - \left(\mathbf {c} _ {i} A ^ {d _ {i} - 1} B\right) K B L - \left(\mathbf {c} _ {i} B\right) K A ^ {d _ {i} - 1} B L \\ - \dots - (- 1) ^ {d _ {i}} \left(\mathbf {c} _ {i} B\right) K (B K) ^ {d _ {i} - 1} B L \\ = \mathbf {c} _ {i} A ^ {d _ {i}} B L \tag {5.100} \\ \end{array}
$$

此外，因 $L$ 为非奇异，可知当 $\pmb{c}_iA^{d_i}B\neq 0$ 时上式将不为零。于是，根据 $\vec{d}_i$ 和 $\vec{E}_i$ 的定义，即可由(5.99)和(5.100)断言， $\vec{d}_i = d_i$ 和 $\vec{E}_i = E_iL$ 。从而，证明完成。

可解耦条件 在上述对传递函数矩阵的两个特征量所作的讨论的基础上，现在就可来给出受控系统(5.72)可用状态反馈和输入变换实现解耦的条件。

结论 线性定常受控系统 (5.72) 可采用状态反馈和输入变换即存在矩阵对 $\{L, K\}$ 进行解耦的充分必要条件, 是如下的 $p \times p$ 常阵

$$
E = \left[ \begin{array}{c} E _ {1} \\ \vdots \\ E _ {p} \end{array} \right] \tag {5.101}
$$

为非奇异。

证 必要性：已知对 $\{A, B, C\}$ 存在 $\{L, K\}$ 可实现解耦，即闭环系统的传递函数矩阵为

$$
G _ {K L} (s) = \left[ \begin{array}{c c c} \bar {g} _ {1 1} (s) & & \\ & \ddots & \\ & & \bar {g} _ {p p} (s) \end{array} \right], \quad \bar {g} _ {i i} (s) \neq 0 \tag {5.102}
$$

由此并利用(5.79)，可得

$$
\bar {E} = \left[\begin{array}{c}\bar {E} _ {1}\\\vdots\\\dot {\bar {E}} _ {p}\end{array}\right] = \left[\begin{array}{c}\lim _ {s \rightarrow \infty} s ^ {d _ {1} + 1} g _ {K L 1} (s)\\\vdots\\\lim _ {s \rightarrow \infty} s ^ {d _ {p} + 1} g _ {K L p} (s)\end{array}\right] = \left[\begin{array}{c c c}\lim _ {s \rightarrow \infty} s ^ {d _ {1} + 1} \bar {g} _ {1 1} (s)&&\\&\ddots&\\&&\lim _ {s \rightarrow \infty} s ^ {d _ {p} + 1} \bar {g} _ {p p} (s)\end{array}\right] \tag {5.103}
$$

这表明 $\vec{E}$ 为对角线非奇异常阵。再知 $\vec{E}=EL$ ，且 L 为非奇异，从而即知 $E=\vec{E}L^{-1}$ 为非奇异。必要性得证。

充分性：采用构造性证明，取 $\{L, K\}$ 为：

$$L = E ^ {- 1}, \quad K = E ^ {- 1} F \tag {5.104}$$

其中，由已知 $E$ 为非奇异故 $E^{-1}$ 存在，而 $p \times n$ 常阵 $F$ 定义为：
