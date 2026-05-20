这里 $\tilde{x}_1(t),\tilde{x}_2(t)$ 分别为 $\nu$ 维和 $n - \nu$ 维状态变量， $\tilde{A}_1,\tilde{A}_2,\tilde{A}_4,\tilde{B}_1,\tilde{B}_2$ 和 $\tilde{C}_1$ 分别为 $\nu \times \nu ,(n - \nu)\times (n - \nu),(n - \nu)\times \nu ,\nu \times (n - \nu),(n - \nu)\times (n - \nu)$ 和 $m\times \nu$ 常值矩阵，并且

$$
\tilde {\boldsymbol {A}} = \left[ \begin{array}{c c} \tilde {\boldsymbol {A}} _ {1} & 0 \\ \tilde {\boldsymbol {A}} _ {4} & \tilde {\boldsymbol {A}} _ {2} \end{array} \right] = \boldsymbol {T} \boldsymbol {A} \boldsymbol {T} ^ {- 1}, \quad \tilde {\boldsymbol {B}} = \left[ \begin{array}{c} \tilde {\boldsymbol {B}} _ {1} \\ \tilde {\boldsymbol {B}} _ {2} \end{array} \right] = \boldsymbol {T} \boldsymbol {B},

\tilde {\boldsymbol {C}} = \left[ \begin{array}{l l} \tilde {\boldsymbol {C}} _ {1} & 0 \end{array} \right] = \boldsymbol {C T} ^ {- 1}.
$$

同时， $(\widetilde{A}_{1},\widetilde{C}_{1})$ 是能观测的.

对系统 $(A, B, C)$ , 称代数等价系统 (1.3.16) 为它的能控标准分解, 而系统 (1.3.17) 为它的能观测标准分解.

设系统 (1.3.17) 的传递函数矩阵为 $\widetilde{W}(s)$ , 显然 $\widetilde{W}(s) = \widetilde{C}_1(sI_{n - \nu} - \widetilde{A}_1)^{-1}\widetilde{B}_1$ . 由于坐标变换不改变系统的传递函数矩阵, 所以有 $W(s) = \widetilde{C}_1(sI_{n - \nu} - \widetilde{A}_1)^{-1}\widetilde{B}_1$ . 这表明定常线性系统的传递函数矩阵不包含系统的不能观测子系统的特征.

从以上两个定理并注意到系统的传递函数矩阵的性质可以看出，一个不完全能控和不完全能观测的定常线性系统的传递函数矩阵，只能刻画它的既能控又能观测子系统的特性.

定理1.3.10 已知定常线性系统 $(A, B, C)$ , 它的能控性矩阵 $Q_{c}$ 的秩为 $\mu$ , 能观测矩阵 $Q_{o}$ 的秩为 $\nu$ , 那么存在一个坐标变换 $\overline{x} = T^{-1}x$ , $T$ 是一个 $n \times n$ 阶非奇异矩阵, 使得系统 $(A, B, C)$ 在这个坐标变换下变成如下代数等价的标准结构形式:
