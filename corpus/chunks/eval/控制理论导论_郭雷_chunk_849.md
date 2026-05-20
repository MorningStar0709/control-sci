$$\widehat {\boldsymbol {X}} (k) = \widehat {\boldsymbol {X}} (k - 1) \widehat {\boldsymbol {A}} \oplus \widehat {\boldsymbol {U}} (k) \widehat {\boldsymbol {B}},\widehat {Y} (k) = \widehat {X} (k) \widehat {C},$$

其中 $\hat{A} = P_1^{-1}AP_1, \hat{B} = P_2^{-1}BP_1, \hat{C} = P_1^{-1}CP_3$ ，且 $G(\hat{A})$ 与 $G(A)$ 是同一有向图，仅点的编号次序不同。

本节中除定理 11.5.8, 11.5.3, 其他定理与引理的证明都较容易，限于篇幅略去这些较易的证明，详见文献 [5], [10].

下面讨论能达性与能观测性。能控性与能观测性是现代控制理论中两个基本的重要概念。对于 DEDS, Cohen 首先提出了基于结构连通性的能控性与能观测性的概念，文献 [27], [29] 提出了分别能控与上限能观测的概念及其判据，笔者等改进了这些判据，得到了用 $A, B, C$ 直接表示的判据，并证明了：对线性 DEDS，分别能控与上限能观测就是 Cohen 的能控与能观测，是同一个概念的两个不同侧面的表现。

1985年，文献[5]提出了准域这一代数结构，与域相比，它可以没有减法，并研究和给出了准域上动态系统完全能达与能观测的概念与判据。由于极大代数 $D$ 含负实数，因此 $D$ 显然是一种特殊的准域，上述文献的结果完全适用于DEDS。由于传统的能控性是指施加控制后把状态控制到零的能力，而在DEDS中，用运算 $\oplus$ 施加控制只会降低把状态控制到零的能力，所以把国内外文献中的有关的能控性称为能达性也许更妥当。下面先介绍Cohen等人提出的能达性与能观测性概念。

定义 11.5.2 (Cohen 等) 当系统 (11.5.1) 的 Petri 网中每个中间变迁 $x_{i}$ 与某输入变迁 $u_{r_{i}}$ 相连通时，我们称系统 (11.5.1) 结构能达 (也可称为能控); 当每个中间变迁 $x_{i}$ 与某输出变迁 $y_{s_{i}}$ 连通时，称系统 (11.5.1) 结构能观测.

定义11.5.3 能与某输入变迁 $u_{r_i}$ 连通的状态分量 $x_i$ 称为结构能达的，否则称为不结构能达的。能与某输出变迁 $y_{s_i}$ 连通的状态分量 $x_i$ 称为结构能观测的，否则称为不结构能观测的。

以后，在不易混淆的地方，我们省去结构这二个字，而简称能达或能观测.

由于 $X_{i}$ 内各点之间强连通，所以 $X_{i}$ 内各状态分量有相同的能达或能观测性，可称凝网内点 $X_{i}$ 为能达的或能观测的.

定理 11.5.1 $^{[10]}$ 考察强凝网中全部不同的 $X_{i}$ 之间的弧，把无进弧的 $X_{i}$ 记为 $X_{r}$ ，无出弧的 $X_{i}$ 记为 $X_{s}$ ；则当且仅当系统 (11.5.1) 的强凝网中，对所有 r 有弧 $UX_{r}$ 时系统 (11.5.1) 能达。当且仅当对所有 s 有弧 $X_{s}Y$ 时系统 (11.5.1) 能观测。

具有标准序的强凝网对应的系统 (11.5.1) 中的各阵可写为如下分块阵：

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1} & \boldsymbol {A} _ {1 2} & \dots & \boldsymbol {A} _ {1 \omega} \\ \phi & \boldsymbol {A} _ {2} & \dots & \boldsymbol {A} _ {2 \omega} \\ \vdots & \vdots & & \vdots \\ \phi & \phi & \dots & \boldsymbol {A} _ {\omega} \end{array} \right], \quad \boldsymbol {B} = [ B _ {1} B _ {2} \dots B _ {\omega} ], \quad \boldsymbol {C} = \left[ \begin{array}{c} \boldsymbol {C} _ {1} \\ \boldsymbol {C} _ {2} \\ \vdots \\ \boldsymbol {C} _ {\omega} \end{array} \right]. \tag {11.5.2}
$$

因此，不失一般性，以后总设系统(11.5.1)的 $A, B, C$ 为上式所示，而

$$\boldsymbol {X} (k) = \left[ \boldsymbol {X} _ {1} (k), \boldsymbol {X} _ {2} (k), \dots , \boldsymbol {X} _ {\omega} (k) \right]. \tag {11.5.3}$$

从图论语言描述的定理11.5.1易证得 $\pmb{D}$ 上矩阵语言描述的以下定理.
