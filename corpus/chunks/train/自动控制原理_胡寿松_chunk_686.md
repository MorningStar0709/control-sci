$$\boldsymbol {c} _ {i} (\boldsymbol {A} - \boldsymbol {B F C}) = \boldsymbol {c} _ {i} \boldsymbol {A} - (\alpha_ {1} \boldsymbol {c} _ {1} + \alpha_ {2} \boldsymbol {c} _ {2} + \dots + \alpha_ {q} \boldsymbol {c} _ {q})$$

该式表明 $C(A - BFC)$ 的行是 $[C^T A^T C^T]^T$ 的行的线性组合。同理有 $C(A - BFC)^2$ 的行是 $[C^T A^T C^T (A^T)^2 C^T]^T$ 的行的线性组合，如此等等。故 $V_{oF}$ 的每一行均可表为 $V_o$ 的行的线性组合，由此可得

$$\operatorname{rank} \mathbf {V} _ {o F} \leqslant \operatorname{rank} \mathbf {V} _ {o} \tag {9-222}$$

由于 $\Sigma_0$ 又可看成为 $\Sigma_F$ 的输出反馈系统，因而有

$$\operatorname{rank} \mathbf {V} _ {o} \leqslant \operatorname{rank} \mathbf {V} _ {a F} \tag {9-223}$$

由式(9-222)和式(9-223)可得

$$\operatorname{rank} \mathbf {V} _ {o} = \operatorname{rank} \mathbf {V} _ {a F} \tag {9-224}$$

这表明输出至参考输入的反馈可保持系统的可观测性。证毕。

2）对系统稳定性的影响。状态反馈和输出反馈都能影响系统的稳定性。加入反馈，使得通过反馈构成的闭环系统成为稳定系统，称之为镇定。由于状态反馈具有许多优越性，且输出反馈系统总可以找到与之性能等同的状态反馈系统，故在此只讨论状态反馈的镇定问题。对于线性定常被控系统

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u}$$

如果可以找到状态反馈控制律

$$\boldsymbol {u} = - \boldsymbol {K x} + \nu$$

其中， $\pmb{v}$ 为参考输入，使得通过反馈构成的闭环系统

$$\dot {\boldsymbol {x}} = (\boldsymbol {A} - \boldsymbol {B K}) \boldsymbol {x} + \boldsymbol {B v}$$

是渐近稳定的，即 $(\mathbf{A} - \mathbf{BK})$ 的特征值均具有负实部，则称系统实现了状态反馈镇定。

定理 9-4 当且仅当线性定常系统的不可控部分渐近稳定时,系统是状态反馈可镇定的。

证明 由于 $\{\mathbf{A},\mathbf{B}\}$ 不完全可控，则一定可引入非奇异线性变换进行可控性结构分解，使得

$$
\overline {{{\boldsymbol {A}}}} = \boldsymbol {P} \boldsymbol {A} \boldsymbol {P} ^ {- 1} = \left[ \begin{array}{l l} \overline {{{\boldsymbol {A}}}} _ {c c} & \overline {{{\boldsymbol {A}}}} _ {1 2} \\ 0 & \overline {{{\boldsymbol {A}}}} _ {c c} \end{array} \right], \quad \overline {{{\boldsymbol {B}}}} = \boldsymbol {P} \boldsymbol {B} = \left[ \begin{array}{l} \overline {{{\boldsymbol {B}}}} _ {c c} \\ \boldsymbol {0} \end{array} \right] \tag {9-255}
$$

式中， $\bar{A}_c$ 为可控状态子矩阵； $\bar{A}_c$ 为不可控状态子矩阵； $\bar{B}_c$ 为可控输入子矩阵。并且对任意 $\bar{K} = [\bar{K}_1, \bar{K}_2]$ 可导出
