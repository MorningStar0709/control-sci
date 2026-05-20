# 11.6 周期（“极点”）配置

传统线性系统的极点就是阵 A 的特征值，DEDS 中 A 的 $\omega$ 个不可约阵 $A_{i}$ 的特征值可称为周期，因而极点配置在这里对应为周期配置.

Cohen 首先探讨了“极点”配置理论，他给出了用输出反馈把系统 (11.5.1) 合并成仅含一个强连通分量的闭环系统 (即闭环的 $A$ 不可约) 的充分条件：系统 (11.5.1) 能达能观测，并指出在这条件下，闭环系统的唯一特征值 $\lambda$ 可在 $[\lambda_m, +\infty]$ 中任意配置，这里 $\lambda_m$ 为开环 $A$ 的最大特征值。我们将用凝网的方法证明上述条件是充要的。本节的中心内容是介绍关于不合并成一个强连通分量的一般配置问题，不合并的 $\omega$ 个不可约阵 $A_i$ 的特征值 $\lambda_i$ 的配置问题与传统线性控制理论中著名而重要的极点配置问题完全对应。由于特征值 $\lambda_i$ 表示了自治系统平均周期这一重要的性能指标，所以我们有理由称 $\lambda_i$ 为 $A$ 的或系统的周期，并称 $\lambda_i$ 配置为周期配置。当 $A$ 的 $\omega$ 个不可约阵 $A_i$ 的特征值 $\lambda_i$ 不全相同时，系统 (11.5.1) 称为多周期系统，若 $A$ 的 $\lambda_i$ 全相同或 $A$ 不可约时，称为单周期系统。由于各台机器加工周期可以不同，机器资源对应的 $A$ 构成的系统经常是多周期的。因此，多周期系统在实际中是常见的。应用中有时也需要闭环系统有多个周期，如柔性制造系统 (FMS) 有时需要按零件配套装配的比例或市场销售的比例生产，又如用 Petri 网描述的计算机网中要求信息以不同的周期输出等。至于理论上，多周期系统的周期配置及一系列有关问题的重要性是显然的。本节的讨论也显示出其理论比单周期系统理论更为丰富。我们将依次讨论：不合并配置，部分配置，合并配置，配置与能达能观测性的关系。

用状态反馈 $U(k) = X(k - 1)K$ 或输出反馈 $U(k) = Y(k - 1)K$ 可把系统(11.5.1)分别变为以下系统：

$$\boldsymbol {X} (k) = \boldsymbol {X} (k - 1) (\boldsymbol {A} \oplus \boldsymbol {K B}), \quad \boldsymbol {Y} (k) = \boldsymbol {X} (k) \boldsymbol {C}, \tag {11.6.1}\boldsymbol {X} (k) = \boldsymbol {X} (k - 1) (\boldsymbol {A} \oplus \boldsymbol {C K B}), \quad \boldsymbol {Y} (k) = \boldsymbol {X} (k) \boldsymbol {C}. \tag {11.6.2}$$

引理11.6.1 设系统(11.6.1)中的 $A \oplus KB$ 记为 $\tilde{A}, \tilde{A}$ 的右上三角块标准形的不可约子阵为 $\tilde{A}_i, 1 \leqslant i \leqslant \tilde{\omega}$ , 则图 $G(A)$ 变到 $G(\tilde{A})$ 时, 强连通子图 $G(A_i)$ 或变为 $G(\tilde{A}_j)$ , 或者几个子图 $G(A_i)$ 合并成一个 $G(\tilde{A}_j)$ , 且都有 $\tilde{\lambda}_j \geqslant \lambda_i, \tilde{\omega} \leqslant \omega, \tilde{\lambda}_j$ 为 $\tilde{A}_j$ 特征值.

证明 因为 $A \to A \oplus KB$ 只能使 $G(A)$ 增加新弧, 不能切断原弧, 所以 $G(A_i)$ 只保持或合并成强连通的 $G(\tilde{A}_j)$ , $\tilde{\omega} \leqslant \omega$ ; 又因 $\oplus KB$ 不能减少 $G(A)$ 中每条弧的权重, 而 $\lambda_i$ 是 $G(A_i)$ 中临界回路的平均权重, 所以, $\tilde{\lambda}_j \geqslant \lambda_i$ .

定义11.6.1 若对任意 $\tilde{\lambda}_i\in [\lambda_i, + \infty),1\leqslant i\leqslant \omega ,$ 都能找到 $K$ ，使 $\pmb {A}\oplus \pmb{KB}$ 或 $\pmb {A}\oplus \pmb{CKB}$ 的周期为 $\tilde{\lambda}_i,1\leqslant i\leqslant \omega$ ，则分别称系统(11.5.1)能用状态反馈或输出反馈配置周期.

定理 11.6.1 $^{[11]}$ A 不可约时，系统 (11.5.1) 的周期能用状态反馈配置的充要条件是 $B \neq \phi$ .
