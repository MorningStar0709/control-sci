$$Q _ {c} = [ B, A B, \dots , A ^ {n - 1} B ],\overline {{{Q}}} _ {c} = [ B G, (A + B K) B G, \dots , (A + B K) ^ {n - 1} B G ],$$

那么可以证明 $\operatorname{Image}(\mathbf{Q}_c) = \operatorname{Image}(\overline{\mathbf{Q}}_c)$ .

要想说明 $\operatorname{Image}(\mathbf{Q}_c) = \operatorname{Image}(\overline{\mathbf{Q}}_c)$ , 只需证明 $\mathcal{N}(\mathbf{Q}_c^{\mathrm{T}}) = \mathcal{N}(\overline{\mathbf{Q}}_c^{\mathrm{T}})$ 便可. 任取 $x_0 \in \mathcal{N}(\mathbf{Q}_c^{\mathrm{T}})$ , 则有 $\mathbf{Q}_c^{\mathrm{T}} x_0 = 0$ . 于是对每个 $i (i = 0,1,\dots,n - 1)$ 有

$$\boldsymbol {B} ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}}) ^ {i} x _ {0} = 0. \tag {1.6.6}$$

由此容易验证

$$\boldsymbol {G} ^ {\mathrm{T}} \boldsymbol {B} ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {B} ^ {\mathrm{T}}) ^ {i} x _ {0} = 0, \quad i = 0, 1, \dots , n - 1. \tag {1.6.7}$$

因此有 $\overline{\pmb{Q}}_c^{\mathrm{T}}x_0 = 0$ ，即 $x_0\in \mathcal{N}(\overline{\pmb{Q}}_c^{\mathrm{T}})$ ，于是由 $x_0$ 任意性可知， $\mathcal{N}(\pmb {Q}_c^{\mathrm{T}})\subset \mathcal{N}(\overline{\pmb{Q}}_c^{\mathrm{T}})$

反之，若 $x_0 \in \mathcal{N}(\overline{\boldsymbol{Q}}_c^{\mathrm{T}})$ ，那么对每个 $i(i = 0,1,\dots ,n - 1)$ 等式 (1.6.7) 皆成立。由于 $\pmb{G}$ 是非奇异矩阵，从而有

$$\boldsymbol {B} ^ {\mathrm{T}} \left(\boldsymbol {A} ^ {\mathrm{T}} + \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {B} ^ {\mathrm{T}}\right) ^ {i} x _ {0} = 0, \quad i = 0, 1, \dots , n - 1,$$

由此不难得出式 (1.6.6) 成立，从而 $x_0 \in \mathcal{N}(\mathbf{Q}_c^{\mathrm{T}})$ ，这就是 $\mathcal{N}(\overline{\mathbf{Q}}_c^{\mathrm{T}}) \subset \mathcal{N}(\mathbf{Q}_c^{\mathrm{T}})$ .

综上所述， $\mathcal{N}(\boldsymbol{Q}_{c}^{\mathrm{T}})=\mathcal{N}(\overline{\boldsymbol{Q}}_{c}^{\mathrm{T}})$ 。这就是所要求的结论。

状态反馈最重要的性质是它能够移动系统的极点。如果结合它保持系统能控性不变的性质，可以说，状态反馈能够移动能控子系统的极点。但状态反馈是否能够移动能控子系统的全部极点呢？这是下面要讨论的问题。

定义 1.6.1 已知定常线性系统 (1.6.1). 如果对任意给定的由 n 个复数组成的对称集合 $\Lambda$ （即若 $\lambda_{0} \in \Lambda$ ，则它的共轭复数 $\overline{\lambda}_{0} \in \Lambda$ ），总存在 $r \times n$ 常值矩阵 K，使得 $A + BK$ 的特征值集合为 $\Lambda$ ，那么就说系统 (1.6.1) 能任意极点配置，或者说 $(A, B)$ 能任意极点配置.

在定义1.6.1中所说的任意极点配置，实际上是说通过状态反馈把系统(1.6.1)的极点移动到预先指定的位置上。由于状态反馈移动极点的能力受系统能控性的限制，故若系统能任意极点配置的话，一定要求这个系统完全能控。

定理1.6.1 定常线性系统(1.6.1)能任意极点配置的充分必要条件是，它为完全能控系统.

证明 充分性. 假设系统 (1.6.1) 是完全能控的, 证明它能任意极点配置. 为此分两步进行, 第一步讨论单输入情况, 第二步讨论多输入情况.
