# 1）对系统可控性和可观测性的影响。

定理 9-1 对于系统(9-208)，状态反馈的引入不改变系统的可控性，但可能改变系统的可观测性。

证明 设被控系统 $\Sigma_0$ 的动态方程为

$$\dot {x} = A x + B u, \quad y = C x$$

加入状态反馈后系统 $\Sigma_{K}$ 的动态方程为

$$\dot {x} = (A - B K) x + B v, \quad y = C x$$

首先证明状态反馈系统 $\Sigma_{K}$ 可控的充分必要条件是被控系统 $\Sigma_{0}$ 可控。

系统 $\Sigma_{0}$ 的可控性矩阵为

$$
\boldsymbol {S} _ {c} = \left[ \begin{array}{l l l l} \boldsymbol {B} & \boldsymbol {A B} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {B} \end{array} \right]
$$

系统 $\Sigma_{K}$ 的可控性矩阵为

$$
\boldsymbol {S} _ {c K} = \left[ \begin{array}{l l l l} \boldsymbol {B} & (\boldsymbol {A} - \boldsymbol {B K}) \boldsymbol {B} & \dots & (\boldsymbol {A} - \boldsymbol {B K}) ^ {n - 1} \boldsymbol {B} \end{array} \right]
$$

由于 $B = [b_{1} \quad b_{2} \quad \cdots \quad b_{p}]$ ， $AB = [Ab_{1} \quad Ab_{2} \quad \cdots \quad Ab_{p}]$

$$(\mathbf {A} - \mathbf {B K}) \mathbf {B} = \left[ (\mathbf {A} - \mathbf {B K}) \mathbf {b} _ {1} \quad (\mathbf {A} - \mathbf {B K}) \mathbf {b} _ {2} \quad \dots \quad (\mathbf {A} - \mathbf {B K}) \mathbf {b} _ {p} \right]$$

式中， $b_{i}(i=1,2,\cdots,p)$ 为列向量。将 K 表示为行向量组

$$
\boldsymbol {K} = \left[ \begin{array}{c} \boldsymbol {k} _ {1} \\ \boldsymbol {k} _ {2} \\ \vdots \\ \boldsymbol {k} _ {p} \end{array} \right]
$$

则 $(\mathbf{A} - \mathbf{B}\mathbf{K})\mathbf{b}_i = \mathbf{A}\mathbf{b}_i - [\mathbf{b}_1\quad \mathbf{b}_2\quad \dots \quad \mathbf{b}_p]\left[ \begin{array}{c}\pmb {k}_1\pmb {b}_i\\ \pmb{k}_2\pmb {b}_i\\ \vdots \\ \pmb {k}_p\pmb {b}_i \end{array} \right]$

令 $c_{1i}=k_{1}b_{i},\quad c_{2i}=k_{2}b_{i},\quad\cdots,\quad c_{pi}=k_{p}b_{i}$

式中， $c_{ji}(j=1,2,\cdots,p)$ 均为标量。故

$$(\mathbf {A} - \mathbf {B K}) \mathbf {b} _ {i} = \mathbf {A b} _ {i} - (c _ {1 i} \mathbf {b} _ {1} + c _ {2 i} \mathbf {b} _ {2} + \dots + c _ {p i} \mathbf {b} _ {p})$$

这说明 $(\mathbf{A} - \mathbf{B}\mathbf{K})\mathbf{B}$ 的列是 $[\mathbf{B} - \mathbf{AB}]$ 列的线性组合。同理有 $(\mathbf{A} - \mathbf{B}\mathbf{K})^2\mathbf{B}$ 的列是 $[\mathbf{B} - \mathbf{AB} - \mathbf{A}^2\mathbf{B}]$ 列的线性组合，如此等等，故 $S_{cK}$ 的每一列均可表为 $S_c$ 的列的线性组合。由此可得

$$\operatorname{rank} \mathbf {S} _ {c K} \leqslant \operatorname{rank} \mathbf {S} _ {c} \tag {9-217}$$

另一方面， $\Sigma_0$ 又可看成为 $\Sigma_K$ 的状态反馈系统，即
